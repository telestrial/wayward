def exit_stacker(looker, exits):
    stacked_exits = ''

    if looker.locks.check_lockstring(looker, "perm(Builder)"):
        for x in exits:
            stacked_exits += f"{x.key.capitalize()} - {x.destination.db.cname} ({x.destination.name}) ({x.destination.id})\n"
        return stacked_exits
    else:
        for x in exits:
            stacked_exits += f"{x.key.capitalize()} - {x.destination.db.cname}\n"
        return stacked_exits


def stat_render(self, obj):
    exit_view = exit_stacker(self.caller, obj.exits)

    rstat_view = """
|xName: |c{}       |xId: |c{}
|xCname:|x {}
|xFlags:|W {}
|xDescription:|W
{}
|xNight Description:|W
{}
|xExits:|W
{}""".format(obj.name, obj.id, obj.db.cname, obj.db.flags, obj.db.desc, obj.db.nightdesc, exit_view)
    return rstat_view
