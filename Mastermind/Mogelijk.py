def createans():
    possibleans = []
    for i in range(1111, 6667):
        answer = str(i)
        if '7' in answer or '8' in answer or '9' in answer or '0' in answer:            #Deze regel heb ik van Brandon Betz, ik had origineel een functie die ook 8 9 en 0 erbij deed.
            continue
        else:
            possibleans.append(answer)
    return possibleans
