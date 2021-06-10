"""
Room

Rooms are simple containers that has no location of their own.

"""
from collections import defaultdict

from evennia.utils.utils import list_to_string
from utils.utils import exit_stacker


from evennia import DefaultRoom


class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """

    def at_object_creation(self):
        """
        Called only at initial creation.
        """
        #set persistent attributes

        if not self.attributes.has('cname'):
            self.db.cname = self.name
        self.db.nightdesc = ''
        self.db.flags = []

    def get_display_name(self, looker, **kwargs):
        """
        Displays the name of the object in a viewer-aware manner.

        Args:
            looker (TypedObject): The object or account that is looking
                at/getting inforamtion for this object.

        Returns:
            name (str): A string containing the name of the object,
                including the DBREF if this user is privileged to control
                said object.

        Notes:
            This function could be extended to change how object names
            appear to users in character, but be wary. This function
            does not change an object's keys or aliases when
            searching, and is expected to produce something useful for
            builders.

        """
        if self.locks.check_lockstring(looker, "perm(Builder)"):
            return "{} ({}) ({})".format(self.db.cname, self.name, self.id)
        return self.db.cname

    def return_appearance(self, looker, **kwargs):
        """
        This formats a description. It is the hook a 'look' command
        should call.

        Args:
            looker (Object): Object doing the looking.
            **kwargs (dict): Arbitrary, optional arguments for users
                overriding the call (unused by default).
        """
        if not looker:
            return ""
        # get and identify all objects
        visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
        exits, users, things = [], [], defaultdict(list)
        for con in visible:
            key = con.get_display_name(looker)
            if con.destination:
                exits.append(con)
            elif con.has_account:
                users.append("|c%s|n" % key)
            else:
                # things can be pluralized
                things[key].append(con)
        # get description, build string
        string = "|c%s|n\n" % self.get_display_name(looker)
        desc = self.db.desc
        if desc:
            string += "%s" % desc
        if exits:
            string += "\n|wObvious Exits:|n\n" + exit_stacker(looker, exits)
        if users or things:
            # handle pluralization of things (never pluralize users)
            thing_strings = []
            for key, itemlist in sorted(things.items()):
                nitem = len(itemlist)
                if nitem == 1:
                    key, _ = itemlist[0].get_numbered_name(nitem, looker, key=key)
                else:
                    key = [item.get_numbered_name(nitem, looker, key=key)[1] for item in itemlist][
                        0
                    ]
                thing_strings.append(key)

            string += "\n|wYou see:|n " + list_to_string(users + thing_strings)

        return string
