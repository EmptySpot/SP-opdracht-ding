from Mastermind.Feedback import simplestrategyfeedback

def bestegok(mogelijk):
    if len(mogelijk) > 1000:
        return '1122'
    else:
        max_feedback = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]       #Dit is zeker niet de netste manier om dit te maken, hier heb ik niet al te veel naar clean coding standards gewerkt.
        mogelijklist = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        for i in reversed(mogelijk):
            item_feedback = simplestrategyfeedback('1122', i)
            if item_feedback == [4, 0]:
                max_feedback[0] += 1
                mogelijklist[0].append(i)
            if item_feedback == [3, 0]:
                max_feedback[1] += 1
                mogelijklist[1].append(i)
            if item_feedback == [2, 2]:
                max_feedback[2] += 1
                mogelijklist[2].append(i)
            if item_feedback == [2, 1]:
                max_feedback[3] += 1
                mogelijklist[3].append(i)
            if item_feedback == [2, 0]:
                max_feedback[4] += 1
                mogelijklist[4].append(i)
            if item_feedback == [1, 3]:
                max_feedback[5] += 1
                mogelijklist[5].append(i)
            if item_feedback == [1, 2]:
                max_feedback[6] += 1
                mogelijklist[6].append(i)
            if item_feedback == [1, 1]:
                max_feedback[7] += 1
                mogelijklist[7].append(i)
            if item_feedback == [1, 0]:
                max_feedback[8] += 1
                mogelijklist[8].append(i)
            if item_feedback == [0, 4]:
                max_feedback[9] += 1
                mogelijklist[9].append(i)
            if item_feedback == [0, 3]:
                max_feedback[10] += 1
                mogelijklist[10].append(i)
            if item_feedback == [0, 2]:
                max_feedback[11] += 1
                mogelijklist[11].append(i)
            if item_feedback == [0, 1]:
                max_feedback[12] += 1
                mogelijklist[12].append(i)
            if item_feedback == [0, 0]:
                max_feedback[13] += 1
                mogelijklist[13].append(i)
            max_feedback_index = max_feedback.index(max(max_feedback))
            antwoord = mogelijklist[max_feedback_index][0]
            return antwoord