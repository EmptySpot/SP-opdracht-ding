import random
from Feedback import botstart
from Mogelijk import createans

def start():
    wie = input("Wil je zelf gokken of de pc laten gokken? Hiernaast is mogelijk om een zelf bedachte algoritme als al: ").lower()
    if wie == ("pc"):
        menscode()
    else:
        if wie == ("zelf"):
            randomcode()
        else:
            if wie == ("al"):
                alcode()
            else:
                start()

def randomcode():
    code = []
    while len(code) != 4:
        randomkleur = random.randint(1, 6)
        kleurdict = {1 : "wit", 2 : "zwart", 3 : "rood", 4 : "blauw", 5 : "geel", 6 : "groen"}
        code.append(kleurdict[randomkleur])
    print(code)
    gok(code)

def gok(code):
    mode = input("Easy of normal?").lower()
    poging = 1
    while poging != 11:
        print("Je hebt hiervoor nog " + str(11 - poging) + " pogingen")
        if poging == 10:
            print("Laatste kans")
        hint = []
        gok = []
        b = len(gok)
        zwartepin = 0
        wittepin = 0
        aanpascode = code
        while b != 3:
            b = len(gok)
            gok.append(input("Gok kleur "+ str(b+1) + ": "))
        if gok == code:
            print("Gefeliciteerd")
            break
        else:
            while zwartepin != 3:
                if aanpascode[zwartepin] == gok[zwartepin].lower():
                    aanpascode[zwartepin] = 'gebruikt'
                    hint.append('zwarte pin')
                zwartepin += 1
            while wittepin != 3:
                if gok[wittepin] in aanpascode:
                    aanpas = int(aanpascode.index(gok[wittepin]))
                    aanpascode[aanpas] = 'gebruikt'
                    hint.append('witte pin')
                wittepin += 1
            if len(hint) < 4:
                aantalleeg = 4 - len(hint)
                while aantalleeg > 0:
                    hint.append('geen pin')
                    aantalleeg -= 1


            if mode == ('easy'):
                print(hint)
            else:
                random.shuffle(hint)
                print(hint)
            poging += 1
    start()

def menscode():
    botcode = []
    b = 0
    while b != 4:
        kleur = (input("Wat is code kleur " + str(b + 1) + "?: "))
        kleurdict = {'wit' : 1, 'zwart' : 2, "rood" : 3, "blauw" : 4, "geel" : 5, "groen" : 6}
        try:
            botcode.append(kleurdict[kleur])
            b += 1
        except KeyError:
            print("Deze kleur zit niet in de game")
        print(botcode)
    mogelijk = createans()
    code = ''.join(map(str, botcode))
    feedbacktester(mogelijk, code)

def feedbacktester(mogelijk, code):
    lives = 10
    attempts = 0

    while lives > 0:
        print(mogelijk)
        gok = mogelijk[0]
        print(gok)
        feedback = botstart(code, gok)

        for i in reversed(mogelijk):
            item_feedback = botstart(gok, i)

            if feedback != item_feedback:
                mogelijk.remove(i)

        lives -= 1
        attempts += 1

        if code == gok:
            print('gevonden')
            print(attempts)
            break
        else:
            if lives == 0:
                print('game over')
    start()

def alcode():
    mogelijk = createans()
    b = 0
    code = []
    while b != 4:
        b = len(code)
        kleur = (input("Wat is code nummer" + str(b+1)))
        if kleur < '7':
            code.append(kleur)
            b += 1
        else:
            print("Dit getal werkt niet")
    code = ''.join(map(str, code))
    j = '1'
    while int(j) != 7:
        hint = botstart(code, j+j+j+j)
        if sum(hint) == 0:
            for i in reversed(mogelijk):
                if j in i:
                    mogelijk.remove(i)
        j = str(int(j)+1)
    attempts = 6
    for i in reversed(mogelijk):
        if i != code:
            attempts += 1
            mogelijk.remove(i)
        else:
            print('Klaar')
            print(i)
            print(attempts)
            break
    start()






start()