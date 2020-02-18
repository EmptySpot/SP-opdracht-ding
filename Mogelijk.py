def createans():
    possibleans = []
    for i in range(1111, 6667):
        answer = str(i)
        if '7' in answer or '8' in answer or '9' in answer or '0' in answer:
            continue
        else:
            possibleans.append(answer)
    print(possibleans)
    return possibleans