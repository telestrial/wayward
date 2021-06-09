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