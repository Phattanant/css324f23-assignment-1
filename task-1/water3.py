def initial_state():
    return (8, 0, 0)


def is_goal(s):
    return s[0] == 4 and s[1] == 4


def successors(s):
    x, y, z = s

    # pour
    if x > 0 and y < 5:
        space = 5 - y
        amount = min(x, space)
        yield ((x - amount, y + amount, z), amount)
    if x > 0 and z < 3:
        space = 3 - z
        amount = min(x, space)
        yield ((x - amount, y, z + amount), amount)
    if y > 0 and x < 8:
        space = 8 - x
        amount = min(y, space)
        yield ((x + amount, y - amount, z), amount)
    if y > 0 and z < 3:
        space = 3 - z
        amount = min(y, space)
        yield ((x, y - amount, z + amount), amount)
    if z > 0 and x < 8:
        space = 8 - x
        amount = min(z, space)
        yield ((x + amount, y, z - amount), amount)
    if z > 0 and y < 5:
        space = 5 - y
        amount = min(z, space)
        yield ((x, y + amount, z - amount), amount)
        
    return []
