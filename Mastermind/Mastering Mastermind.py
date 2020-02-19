import random
from termcolor import colored
from Mastermind.Feedback import simplestrategyfeedback
from Mastermind.Feedback import AlgoritmeFeedback
from Mastermind.Feedback import SnelFeedback
from Mastermind.Mogelijk import createans
from Mastermind.lookingonestepahead import bestegok

def start():
    print(colored("\rWelcome by Mastermind\n", 'red'))
    print(colored("For this Mastermind are a couple options\nSuch as the pc making a code, which you try to guess. This is option: ", 'blue') + (colored("me", 'red')))
    print(colored("Furturmore there is the option make a code and let the pc guess, which the pc can do from 3 different forms, one of them is by simple strategy. This is option: ", 'blue') + (colored("simple", 'red')))
    print(colored("Another option is to let the pc guess by a heuristic code written by an amateur. This is option: ", 'blue') + (colored("hu", 'red')))
    print(colored("The last option is to let the pc guess looking one step ahead. This is option: ", 'blue') + (colored("one", 'red')))
    print(colored("So the options are: ", 'blue') + (colored("me, simple, hu, one", 'red')))
    wie = input(colored("\nDo you want to guess yourself? Or would you rather let the pc handle the guesswork? Choose one of the options announced above: ", 'yellow')).lower()


    if wie == ("simple"):
        simplestrategy()
    else:
        if wie == ("me"):
            randomcode()
        else:
            if wie == ("hu"):
                heuristiekcode()
            else:
                if wie == ('one'):
                    lookingonestep()
                else:
                    start()

def randomcode():
    code = []
    while len(code) != 4:
        randomkleur = random.randint(1, 6)
        kleurdict = {1 : "white", 2 : "black", 3 : "red", 4 : "blue", 5 : "yellow", 6 : "green"}
        code.append(kleurdict[randomkleur])
    gok(code)

def gok(code):
    mode = input("Easy of normal? ").lower()
    poging = 1
    while poging != 11:
        print("You got " + str(11 - poging) + " tries")
        if poging == 10:
            print("Last chance")
        hint = []
        gok = []
        b = len(gok)
        zwartepin = 0
        wittepin = 0
        aanpascode = []
        aanpascode.append(code)
        while b != 3:
            b = len(gok)
            gok.append(input("Guess colour "+ str(b+1) + ": "))
        if gok == code:
            print("Congrats")
            break
        else:
            while zwartepin != 3:
                if aanpascode[0][zwartepin] == gok[zwartepin].lower():
                    aanpascode[0][zwartepin] = 'gebruikt'
                    hint.append('black pin')
                zwartepin += 1
            while wittepin != 3:
                if gok[wittepin] in aanpascode:
                    aanpas = int(aanpascode.index(gok[wittepin]))
                    aanpascode[0][aanpas] = 'gebruikt'
                    hint.append('white pin')
                wittepin += 1
            if len(hint) < 4:
                aantalleeg = 4 - len(hint)
                while aantalleeg > 0:
                    hint.append('no pin')
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
    print("This code works with the colours: white, black, red, blue, yellow and green.")
    while b != 4:
        kleur = (input("What is the colour code of nummer " + str(b + 1) + "?: "))
        kleurdict = {'white' : 1, 'black' : 2, "red" : 3, "blue" : 4, "yellow" : 5, "green" : 6}
        try:
            botcode.append(kleurdict[kleur])
            b += 1
        except KeyError:
            print("This colour ain`t in the game")
    mogelijk = createans()
    code = ''.join(map(str, botcode))
    return mogelijk, code

def simplestrategy():
    mogelijk, code = menscode()
    attempts = 0
    while True:
        gok = mogelijk[0]
        feedback = simplestrategyfeedback(code, gok)
        for i in reversed(mogelijk):
            item_feedback = simplestrategyfeedback(gok, i)
            if feedback != item_feedback:
                mogelijk.remove(i)
        print(gok)
        attempts += 1
        if code == gok:
            print("The code replies in numbers, which represents the colours as follows: white = 1, black = 2, red = 3, blue = 4, yellow = 5 and green = 6.")
            print(colored('The code has been found as ', 'red') + str(gok))
            print('This has been done in ' + str(attempts) + ' attempts\n' )
            break
        else:
            if attempts == 10:
                print('Game over')
    start()

def heuristiekcode():
    mogelijk = createans()
    b = 0
    code = []
    print("This code works with numbers instead of colours")
    while b != 4:
        b = len(code)
        kleur = (input("What is the code number " + str(b+1) +"? "))
        if kleur < '7':
            code.append(kleur)
            b += 1
        else:
            print("Dit getal werkt niet")
    code = ''.join(map(str, code))
    mogelijk, attempts = AlgoritmeFeedback(code, mogelijk)
    i, attempts = SnelFeedback(code, mogelijk, attempts)
    print(colored('The code has been found as ', 'red') + str(i))
    print('This has been done in ' + str(attempts) + ' attempts\n')
    start()

def lookingonestep():
    mogelijk, code = menscode()
    attempts = 0
    while True:
        gok = bestegok(mogelijk)
        print("Het algoritme gokt " + str(gok))
        feedback = simplestrategyfeedback(code, gok)
        for i in reversed(mogelijk):
            item_feedback = simplestrategyfeedback(gok, i)
            if feedback != item_feedback:
                mogelijk.remove(i)
        attempts += 1
        if code == gok:
            print("The code replies in numbers, which represents the colours as follows: white = 1, black = 2, red = 3, blue = 4, yellow = 5 and green = 6.")
            print(colored('The code has been found as ', 'red') + str(gok))
            print('This has been done in ' + str(attempts) + ' attempts\n' )
            break
        else:
            if attempts == 10:
                print(colored('Game over', 'gray'))
    start()




start()