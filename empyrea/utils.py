from random import choice


def LoadInit(filename):
    initdict = {}
    initfile = open(filename, 'r')
    init = initfile.readlines()
    initfile.close()
    for line in init:
        line = line.strip('\n')
        if line.startswith('===') or line.startswith('*'):
            continue
        if not line.strip(' '):
            continue
        else:
            sname = line.split(': ')[0]
            setting = line.split(': ')[1]
            initdict[sname] = setting
    return initdict


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


def dchoice(choicelist,capitalize = 0,possessive = 0):
    global paraswitch, ctitles, curchoice
    if not possessive:
        poss = ''
    else:
        if not paraswitch or not choicelist == ctitles:
            poss = '\'s'
        else:
            poss = 's'
    if not paraswitch or not choicelist == ctitles:
        dchoice = choice(choicelist)
        curchoice = dchoice
        if capitalize:
            return dchoice[0].upper() + dchoice[1:] + poss
        else:
            return dchoice + poss
    else:
        if capitalize:
            return 'It' + poss
        else:
            return 'it' + poss


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


def throwSwitches(subject,switches):
    for switch in switches:
        case = getattr(subject,switch)
        setattr(subject,switch,not case)
