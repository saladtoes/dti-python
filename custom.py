# q1 = []
# q1answers = []
# q2 = []
# q2answers = []
# q3 = []
# q3answers = []
# q4 = []
# q4answers = []
# q5 = []
# q5answers = []
import playgame
import os
def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str
 

# q1Input = input("enter question 1")
# q1.append(q1Input)
# q1answers1 = input("enter answer 1")
# q1answers.append(q1answers1)
# q1answers2 = input("enter answer 2")
# q1answers.append(q1answers2)
# q1answers3 = input("enter answer 3")
# q1answers.append(q1answers3)
# q1correct = int(input("what answer is correct? 1, 2, 3"))

# q1correct = q1correct - 1

# answer1 = q1correct

# text = [q1[0], q1answers[0], q1answers[1], q1answers[2]]

# text = str(text)
# texty = ("q1AndAnswer1 = ", text)

# textFinal = convertTuple(texty)




print("This is the creator for the custom quiz.\n to run the quiz that you make via this script please run 'playgane.py'\n In this script you are only able to make upto 5 questions in a quiz.\n each question MUST have 3 answers")


def makeNewVar():
    questionnum = int(input("enter question number: "))
    if questionnum == 1:
            global quest1Final
            questions = []
            q1Answers = []
            q1 = input("enter question 1: ")
            questions.append(q1)
            q1Answers1 = input(" Enter Answer 1: ")
            q1Answers.append(q1Answers1 + '\n')
            q1Answers1 = input(" Enter Answer 2: ")
            q1Answers.append(q1Answers1 + '\n')
            q1Answers1 = input(" Enter Answer 3: ")
            q1Answers.append(q1Answers1 + '\n')
            correctAnswer1 = int(input("Enter the correct answer, 1, 2, 3: "))
            quest1 = [q1, q1Answers[0], q1Answers[1], q1Answers[2], correctAnswer1]
            quest1 = str(quest1)
            quest1 = ("q1AndAnswer1 = ", quest1)
            quest1Final = convertTuple(quest1)
            makeNewVar()
    elif questionnum == 2:
            global quest2Final
            questions = []
            q2Answers = []
            q2 = input("enter question 2: ")
            questions.append(q2)
            q2Answers2 = input(" Enter Answer 1: ")
            q2Answers.append(q2Answers2 + '\n')
            q2Answers2 = input(" Enter Answer 2: ")
            q2Answers.append(q2Answers2 + '\n')
            q2Answers2 = input(" Enter Answer 3: ")
            q2Answers.append(q2Answers2 + '\n')
            correctAnswer2 = int(input("Enter the correct answer, 1, 2, 3: "))
            quest2 = [q2, q2Answers[0], q2Answers[1], q2Answers[2], correctAnswer2 ]
            quest2 = str(quest2)
            quest2 = ("q2AndAnswer2 = ", quest2)
            quest2Final = convertTuple(quest2)
            makeNewVar()
    elif questionnum == 3:
            global quest3Final
            questions = []
            q3Answers = []
            q3 = input("enter question 3: ")
            questions.append(q3)
            q3Answers3 = input(" Enter Answer 1: ")
            q3Answers.append(q3Answers3 + '\n')
            q3Answers3 = input(" Enter Answer 2: ")
            q3Answers.append(q3Answers3 + '\n')
            q3Answers3 = input(" Enter Answer 3: ")
            q3Answers.append(q3Answers3 + '\n')
            correctAnswer3 = int(input("Enter the correct answer, 1, 2, 3: "))
            quest3 = [q3, q3Answers[0], q3Answers[1], q3Answers[2], correctAnswer3 ]
            quest3 = str(quest3)
            quest3 = ("q3AndAnswer3 = ", quest3)
            quest3Final = convertTuple(quest3)
            makeNewVar()
    elif questionnum == 4:
            global quest4Final
            questions = []
            q4Answers = []
            q4 = input("enter question 4: ")
            questions.append(q4)
            q4Answers4 = input(" Enter Answer 1: ")
            q4Answers.append(q4Answers4 + '\n')
            q4Answers4 = input(" Enter Answer 2: ")
            q4Answers.append(q4Answers4 + '\n')
            q4Answers4 = input(" Enter Answer 3: ")
            q4Answers.append(q4Answers4 + '\n')
            correctAnswer4 = int(input("Enter the correct answer, 1, 2, 3: "))
            quest4 = [q4, q4Answers[0], q4Answers[1], q4Answers[2], correctAnswer4 ]
            quest4 = str(quest4)
            quest4 = ("q4AndAnswer4 = ", quest4)
            quest4Final = convertTuple(quest4)
            makeNewVar()
    elif questionnum == 5:
            global quest5Final
            questions = []
            q5Answers = []
            q5 = input("enter question 2: ")
            questions.append(q5)
            q5Answers5 = input(" Enter Answer 1: ")
            q5Answers.append(q5Answers5 + '\n')
            q5Answers5 = input(" Enter Answer 2: ")
            q5Answers.append(q5Answers5 + '\n')
            q5Answers5 = input(" Enter Answer 3: ")
            q5Answers.append(q5Answers5 + '\n')
            correctAnswer5 = int(input("Enter the correct answer, 1, 2, 3: "))
            quest5 = [q5, q5Answers[0], q5Answers[1], q5Answers[2], correctAnswer5 ]
            quest5 = str(quest5)
            quest5 = ("q5AndAnswer5 = ", quest5)
            quest5Final = convertTuple(quest5)

         


makeNewVar()

# print(textFinal)
file = open("answers.py", 'w')
file.close()


file = open("answers.py", 'a')
file.write(quest1Final + '\n')
file.write(quest2Final + '\n')
file.write(quest3Final + '\n')
file.write(quest4Final + '\n')
file.write(quest5Final + '\n')

file.close()

def play():
    again = input("would you like to play the game right now?")
    if again.lower() == 'y':
        playgame.play()
        exit()
    else:
        exit()

play()