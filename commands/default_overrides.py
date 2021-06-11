from evennia.commands.default.system import CmdObjects

class CmdObjects(CmdObjects):
    """
    statistics on objects in the database

    Usage:
      objects [<nr>]

    Gives statictics on objects in database as well as
    a list of <nr> latest objects in database. If not
    given, <nr> defaults to 10.
    """

    key = "objects"
    aliases = ["listobjects", "listobjs", "db"]
    locks = "cmd:perm(listobjects) or perm(Admin)"
    help_category = "System"