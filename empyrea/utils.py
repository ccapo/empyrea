from random import choice


def wchoice(lst):
    total = 0
    for pair in lst:
        total += pair[1]
    if str(total) != '1.0':
        raise ValueError
    randlist = []
    for pair in lst:
        randlist += [pair[0]] * int(pair[1] * 1000)
    return choice(randlist)


def DictCmp(x, y):
    if x[1] > y[1]:
        return -1
    elif x[1] == y[1]:
        return 0
    else:
        return 1


def ListCmp(x, y):
    if x[0] > y[0]:
        return -1
    elif x[0] == y[0]:
        return 0
    else:
        return 1


def ListCmp2(x, y):
    if x[1] > y[1]:
        return -1
    elif x[1] == y[1]:
        return 0
    else:
        return 1


def LenCmp(x, y):
    if len(x) > len(y):
        return -1
    elif len(x) == len(y):
        return 0
    else:
        return 1


def doNothing():
    pass


def throwSwitches(subject, switches):
    for switch in switches:
        case = getattr(subject, switch)
        setattr(subject, switch, not case)
