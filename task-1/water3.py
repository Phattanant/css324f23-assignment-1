def initial_state():
    return (8, 0, 0)


def is_goal(s):
    return s[0] == 4 and s[1] == 4


def successors(s):
    x, y, z = s

    # empty
    if x > 0:
        yield ((0, y, z), x)
    if y > 0:
        yield ((x, 0, z), y)
    if z > 0:
        yield ((x, y, 0), z)

    # fill
    if x < 8:
        yield ((8, y, z), 8 - x)
    if y < 5:
        yield ((x, 5, z), 5 - y)
    if z < 3:
        yield ((x, y, 3), 3 - z)

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
