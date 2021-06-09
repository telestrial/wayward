from evennia.contrib.building_menu import BuildingMenu
from commands.command import Command

class EditCmd(Command):

    """
    Editing command.

    Usage:
      edit [object]

    Open a building menu to edit the specified object.  This menu allows to
    specific information about this object.

    Examples:
      edit here
      edit self
      edit #142

    """

    key = "edit"
    locks = "perm(Builders)"
    help_category = "Building"

    def func(self):
        if not self.args.strip():
            self.msg("|rYou should provide an argument to this function: the object to edit.|n")
            return

        obj = self.caller.search(self.args.strip(), global_search=True)
        if not obj:
            return

        if obj.typename == "Room":
            Menu = RoomBuildingMenu
        else:
            self.msg("|rThe object {} cannot be edited.|n".format(obj.get_display_name(self.caller)))
            return

        menu = Menu(self.caller, obj)
        menu.open()



# Our building menus
class RoomBuildingMenu(BuildingMenu):

    """
    Building menu to edit a room.
    """

    def init(self, room):
        self.add_choice("name", key="n", attr="key", glance="{obj.key}", text="""
                -------------------------------------------------------------------------------
                Editing the name of {{obj.key}}(#{{obj.id}})

                You can change the name simply by entering it.
                Use |y{back}|n to go back to the main menu.

                Current name: |c{{obj.key}}|n
        """.format(back="|n or |y".join(self.keys_go_back)))
        self.add_choice("Colored Name", key="c", attr="db.cname")
        self.add_choice_edit("description", "d")
        self.add_choice("exits", "e", glance=glance_exits, text=text_exits, on_nomatch=nomatch_exits)


# Menu functions
def glance_exits(room):
    """Show the room exits."""
    if room.exits:
        glance = ""
        for exit in room.exits:
            glance += "\n  |y{exit}|n".format(exit=exit.key)

        return glance

    return "\n  |gNo exit yet|n"

def text_exits(caller, room):
    """Show the room exits in the choice itself."""
    text = "-" * 79
    text += "\n\nRoom exits:"
    text += "\n Use |y@c|n to create a new exit."
    text += "\n\nExisting exits:"
    if room.exits:
        for exit in room.exits:
            text += "\n  |y@e {exit}|n".format(exit=exit.key)
            if exit.aliases.all():
                text += " (|y{aliases}|n)".format(aliases="|n, |y".join(
                        alias for alias in exit.aliases.all()))
            if exit.destination:
                text += " toward {destination}".format(destination=exit.get_display_name(caller))
    else:
        text += "\n\n |gNo exit has yet been defined.|n"

    return text

def nomatch_exits(menu, caller, room, string):
    """
    The user typed something in the list of exits.  Maybe an exit name?
    """
    string = string[3:]
    exit = caller.search(string, candidates=room.exits)
    if exit is None:
        return

    # Open a sub-menu, using nested keys
    caller.msg("Editing: {}".format(exit.key))
    menu.open_submenu("commands.building.ExitBuildingMenu", exit, parent_keys=["e"])
    return False

class ExitBuildingMenu(BuildingMenu):

    """
    Building menu to edit an exit.

    """

    def init(self, exit):
        self.add_choice("key", key="k", attr="key", glance="{obj.key}")
        self.add_choice_edit("description", "d")