import collections

#Ik heb alle feedback functies in 1 bestand bij elkaar gezet

def simplestrategyfeedback(strcode, gok):
    hint = [0, 0]
    geteldecode = collections.Counter(strcode)          #Deze heb ik als tip van Menno Oud gekregen vanwege mijn trage en bar werkende orginele feedback,
    geteldegok = collections.Counter(gok)
    wit = sum(min(geteldecode[k], geteldegok[k]) for k in geteldecode)
    zwart = sum(a==b for a,b in zip(strcode, gok))      #De tip van Menno is tot en met deze regel.
    wit -= zwart
    hint[0] = zwart
    hint[1] = wit
    return hint


def AlgoritmeFeedback(code, mogelijk):
    j = '1'                                             #Ik gebruik j als teller in while loops, ook gebruik ik het om bijvoorbeeld locaties in een list te bepalen in die while loop.
    attemptsvermindering = 4
    attemps = 0
    while int(j) != 6:
        attemps += 1
        hint = simplestrategyfeedback(code, j+j+j+j)
        print("Het algoritme gokt " + str(j+j+j+j))
        if sum(hint) == 0:
            for i in reversed(mogelijk):
                if j in i:
                    mogelijk.remove(i)
        else:
                for i in reversed(mogelijk):
                    hoeveelheid = collections.Counter(i)
                    if sum(hint) != hoeveelheid[j]:
                        mogelijk.remove(i)
        attemptsvermindering -= sum(hint)
        if attemptsvermindering == 0:
            break
        j = str(int(j)+1)
    return mogelijk, attemps

def SnelFeedback(code, mogelijk, attempts):
    for i in reversed(mogelijk):
        attempts += 1
        print('Het algoritme gokt ' +str(i))
        if i != code:
            attempts += 1
            mogelijk.remove(i)
        else:
            break
    return i, attempts

