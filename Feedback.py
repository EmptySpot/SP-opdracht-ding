import collections
def botstart(strcode, gok):
    hint = [0, 0]
    geteldecode = collections.Counter(strcode)
    geteldegok = collections.Counter(gok)
    wit = sum(min(geteldecode[k], geteldegok[k]) for k in geteldecode) #Thanks
    zwart = sum(a==b for a,b in zip(strcode, gok))
    wit -= zwart
    hint[0] = zwart
    hint[1] = wit
    return hint