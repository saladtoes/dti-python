def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str

questions = []
q2Answers = []
q2 = input("enter question 2")
questions.append(q2)
q2Answers2 = input(" Enter Answer 1.")
q2Answers.append(q2Answers2)
q2Answers2 = input(" Enter Answer 2.")
q2Answers.append(q2Answers2)
q2Answers2 = input(" Enter Answer 3.")
q2Answers.append(q2Answers2 + '\n')
correctAnswer2 = int(input("Enter the correct answer, 1, 2, 3"))
correctAnswer2 = correctAnswer2 - 1
quest2 = [q2, q2Answers[0], q2Answers[1], q2Answers[2], correctAnswer2 , "\n"]
quest2 = str(quest2)
quest2 = ("q2AndAnswer2 = ", quest2)
quest2Final = convertTuple(quest2)

print(quest2Final)
