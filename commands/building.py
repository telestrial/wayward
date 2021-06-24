from evennia.utils import eveditor

from commands.command import Command

from utils.utils import stat_render

BUILD_FLAGS_ROOMS = ['indoors', 'outdoors', 'dark']

# Setting up the Eveditor for long text input.


def _desc_load(caller):
    "get the current description"
    return caller.ndb.evmenu_target.db.desc or ""


def _desc_save(caller, buf):
    "save the buffer to that object's description"
    caller.ndb.evmenu_target.db.desc = buf
    caller.msg('Saved.')
    return True


def _desc_quit(caller):
    "Since we define it, we must handle messages"
    caller.msg("Exited editor.")


def _nightdesc_load(caller):
    "get the current value"
    return caller.ndb.evmenu_target.db.nightdesc or ""


def _nightdesc_save(caller, buf):
    "save the buffer"
    caller.ndb.evmenu_target.db.nightdesc = buf
    caller.msg('Saved.')
    return True


def _nightdesc_quit(caller):
    "Since we define it, we must handle messages"
    caller.msg("Editor exited")

# def _desc_load(caller):
#     return caller.db.evmenu_target.db.desc or ""


# def _desc_save(caller, buf):
#     """
#     Save line buffer to the desc prop. This should
#     return True if successful and also report its status to the user.
#     """
#     caller.db.evmenu_target.db.desc = buf
#     caller.msg("Saved.")
#     return True


# def _desc_quit(caller):
#     caller.attributes.remove("evmenu_target")
#     caller.msg("Exited editor.")
# ----------------------------------------------


class StatCmd(Command):
    """
    An implementation of Xstat/edit system.

    Usage:
      stat [room name/id]

    Will return the targetted thing's modifiable values. Less verbose than
    examine. Will return the view for the invoker's current room if one is
    not specified.

    Examples:
      stat
      stat 71
      stat bgs_canteen
    """

    key = "stat"
    locks = "perm(Builders)"
    help_category = "Building"

    def func(self):
        args = self.args.strip()
        if not args:
            obj = self.caller.search('here')
        elif args.isdigit():
            obj = self.caller.search(f"#{args}")
        else:
            obj = self.caller.search(args, global_search=True)

        if not obj:
            return

        if obj.typename == "Room":
            self.msg(stat_render(self, obj))
        else:
            self.msg("|r{} cannot be edited.|n".format(
                obj.get_display_name(self.caller)))
            return


class EditCmd(Command):
    """
    Edit command for rooms, objects, mobs, and more! The power is in your hands.

    Usage
      edit [thing] [attribute] [value]

    If no arguments are supplied, stats the current room. If only [thing] is supplied,
    performs a stat command on that [thing]. With [thing] and [attribute], will attempt
    to help you understand what values you can supply. The command should not let you set
    things you shouldn't set....mostly.
    """
    key = "edit"
    locks = "perm(Builders)"
    help_category = "Building"

    def func(self):
        if not self.args.strip():
            self.msg(stat_render(self, self.caller.location))
            return

        self.args = self.args.strip().split(" ", 2)
        obj = self.caller.search(self.args[0], global_search=True)

        if not obj:
            return

        if 'room' in obj.typeclass_path:

            # If there is no argument, stat command the room.
            if len(self.args) == 1:
                self.msg(stat_render(self, obj))
                return

            if len(self.args) == 2:

                # if the field is invalid, tell them.
                if not obj.attributes.has(self.args[1]):
                    self.msg('{} has no atrribute: {}'.format(
                        obj, self.args[1]))

                # if it's a description, load the editor
                if self.args[1] == 'desc':
                    self.caller.ndb.evmenu_target = obj
                    # launch the editor
                    key = 'Description of %s' % (obj)
                    eveditor.EvEditor(self.caller,
                                      loadfunc=_desc_load, savefunc=_desc_save, quitfunc=_desc_quit,
                                      key=key)
                    return

                # if it's a night description, load the editor
                if self.args[1] == 'nightdesc':
                    self.caller.ndb.evmenu_target = obj
                    # launch the editor
                    key = 'Night Description of %s' % (obj)
                    eveditor.EvEditor(self.caller,
                                      loadfunc=_nightdesc_load, savefunc=_nightdesc_save, quitfunc=_nightdesc_quit,
                                      key=key)
                    return

            # If it's the colored name, set it.
            if self.args[1] == 'cname':
                obj.attributes.add('cname', self.args[2])

            if self.args[1] == 'flags':

                # if it's not a valid flag, do not allow them to set
                if self.args[2] not in BUILD_FLAGS_ROOMS:
                    self.msg('That is not a valid build flag for rooms.')
                    return

                # if it's in the flag array, remove it.
                if self.args[2] in obj.attributes.get('flags'):
                    obj.db.flags.remove(self.args[2])
                    self.msg('{} flag removed from {}.'.format(
                        self.args[2], obj.name))
                    return

                # if it's not in the flag array, add it.
                if self.args[2] not in obj.attributes.get('flags'):
                    obj.db.flags.append(self.args[2])
                    self.msg('{} flag added to {}.'. format(
                        self.args[2], obj.name))
                    return

# pos    0    1    2
# len()  1    2    3
# edit here desc the only way
