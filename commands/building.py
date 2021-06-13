from evennia.utils import eveditor

from commands.command import Command

from utils.utils import stat_render

BUILD_FLAGS_ROOMS = ['indoors', 'outdoors', 'dark']


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

        if len(self.args) == 1:
            self.msg(stat_render(self, obj))
            return

        if len(self.args) == 2:
            if not obj.attributes.has(self.args[1]):
                self.msg('{} has no atrribute: {}'.format(obj, self.args[1]))

            if self.args[1] == 'desc':
                def load(obj):
                    "get the current value"
                    return obj.attributes.get("desc")

                def save(obj, buffer):
                    "save the buffer"
                    obj.attributes.set("desc", buffer)

                def quit(caller):
                    "Since we define it, we must handle messages"
                    caller.msg("Editor exited")

                key = "%s/desc" % obj
                # launch the editor
                eveditor.EvEditor(self.caller,
                                  loadfunc=load, savefunc=save, quitfunc=quit,
                                  key=key)

#        0    1    2
#        1    2    3
# edit here desc the only way
