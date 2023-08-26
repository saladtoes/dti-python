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
import bisect


def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str
 
file = open("answers.py", 'w')
file.close()
print(" This is the maker for the custom quiz.\n to run the quiz that you make via this script please run 'playgame.py'\n In this script you are only able to make upto 5 questions in a quiz.\n\n")



numberofq = int(input("How many questions do you want to make?"))



def questions1():
    global quest1Final
    q1asnwercount = int(input("Q1. How many answers do you want this question to have?\n Maximum of 5: "))
    
    questions = []
    q1Answers = []

    if q1asnwercount == 1:
        q1 = input("enter question 1: ")
        questions.append(q1)
        q1Answers1 = input(" Enter Answer 1: ")
        q1Answers.append(q1Answers1 + '\n')
        correctAnswer1 = int(input("Enter the correct answer, 1:  "))
        quest1 = [q1, q1Answers[0], correctAnswer1]
        quest1 = str(quest1)
        quest1 = ("q1AndAnswer1 = ", quest1)
        quest1Final = convertTuple(quest1)
    elif q1asnwercount == 2:
        q1 = input("enter question 1: ")
        questions.append(q1)
        q1Answers1 = input(" Enter Answer 1: ")
        q1Answers.append(q1Answers1 + '\n')
        q1Answers1 = input(" Enter Answer 2: ")
        q1Answers.append(q1Answers1 + '\n')
        correctAnswer1 = int(input("Enter the correct answer, 1, 2:  "))
        quest1 = [q1, q1Answers[0], q1Answers[1], correctAnswer1]
        quest1 = str(quest1)
        quest1 = ("q1AndAnswer1 = ", quest1)
        quest1Final = convertTuple(quest1)
    elif q1asnwercount == 3:
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
    elif q1asnwercount == 4:
        q1 = input("enter question 1: ")
        questions.append(q1)
        q1Answers1 = input(" Enter Answer 1: ")
        q1Answers.append(q1Answers1 + '\n')
        q1Answers1 = input(" Enter Answer 2: ")
        q1Answers.append(q1Answers1 + '\n')
        q1Answers1 = input(" Enter Answer 3: ")
        q1Answers.append(q1Answers1 + '\n')
        q1Answers1 = input(" Enter Answer 4: ")
        q1Answers.append(q1Answers1 + '\n')
        correctAnswer1 = int(input("Enter the correct answer, 1, 2, 3, 4: "))
        quest1 = [q1, q1Answers[0], q1Answers[1], q1Answers[2], q1Answers[3], correctAnswer1]
        quest1 = str(quest1)
        quest1 = ("q1AndAnswer1 = ", quest1)
        quest1Final = convertTuple(quest1)
    elif q1asnwercount == 5:
        q1 = input("enter question 5: ")
        questions.append(q1)
        q1Answers1 = input(" Enter Answer 1: ")
        q1Answers.append(q1Answers1 + '\n')
        q1Answers1 = input(" Enter Answer 2: ")
        q1Answers.append(q1Answers1 + '\n')
        q1Answers1 = input(" Enter Answer 3: ")
        q1Answers.append(q1Answers1 + '\n')
        q1Answers1 = input(" Enter Answer 4: ")
        q1Answers.append(q1Answers1 + '\n')
        q1Answers1 = input(" Enter Answer 5: ")
        q1Answers.append(q1Answers1 + '\n')
        correctAnswer1 = int(input("Enter the correct answer, 1, 2, 3, 4, 5: "))
        quest1 = [q1, q1Answers[0], q1Answers[1], q1Answers[2], q1Answers[3], q1Answers[4], correctAnswer1]
        quest1 = str(quest1)
        quest1 = ("q1AndAnswer1 = ", quest1)
        quest1Final = convertTuple(quest1)

def questions2():
    questions = []
    q2Answers = []
    global quest2Final
    q2asnwercount = int(input("Q2. How many answers do you want this question to have?\n Maximum of 5: "))
    if q2asnwercount == 1:
        q2 = input("enter question 1: ")
        questions.append(q2)
        q2Answers2 = input(" Enter Answer 1: ")
        q2Answers.append(q2Answers2 + '\n')
        correctAnswer2 = int(input("Enter the correct answer, 1:  "))
        quest2 = [q2, q2Answers[0], correctAnswer2]
        quest2 = str(quest2)
        quest2 = ("q2AndAnswer2 = ", quest2)
        quest2Final = convertTuple(quest2)
    elif q2asnwercount == 2:
        q2 = input("enter question 1: ")
        questions.append(q2)
        q2Answers2 = input(" Enter Answer 1: ")
        q2Answers.append(q2Answers2 + '\n')
        q2Answers2 = input(" Enter Answer 2: ")
        q2Answers.append(q2Answers2 + '\n')
        correctAnswer2 = int(input("Enter the correct answer, 1, 2:  "))
        quest2 = [q2, q2Answers[0], q2Answers[1], correctAnswer2]
        quest2 = str(quest2)
        quest2 = ("q2AndAnswer2 = ", quest2)
        quest2Final = convertTuple(quest2)
    elif q2asnwercount == 3:
        q2 = input("enter question 1: ")
        questions.append(q2)
        q2Answers2 = input(" Enter Answer 1: ")
        q2Answers.append(q2Answers2 + '\n')
        q2Answers2 = input(" Enter Answer 2: ")
        q2Answers.append(q2Answers2 + '\n')
        q2Answers2 = input(" Enter Answer 3: ")
        q2Answers.append(q2Answers2 + '\n')
        correctAnswer2 = int(input("Enter the correct answer, 1, 2, 3: "))
        quest2 = [q2, q2Answers[0], q2Answers[1], q2Answers[2], correctAnswer2]
        quest2 = str(quest2)
        quest2 = ("q2AndAnswer2 = ", quest2)
        quest2Final = convertTuple(quest2)
    elif q2asnwercount == 4:
        q2 = input("enter question 1: ")
        questions.append(q2)
        q2Answers2 = input(" Enter Answer 1: ")
        q2Answers.append(q2Answers2 + '\n')
        q2Answers2 = input(" Enter Answer 2: ")
        q2Answers.append(q2Answers2 + '\n')
        q2Answers2 = input(" Enter Answer 3: ")
        q2Answers.append(q2Answers2 + '\n')
        q2Answers2 = input(" Enter Answer 4: ")
        q2Answers.append(q2Answers2 + '\n')
        correctAnswer2 = int(input("Enter the correct answer, 1, 2, 3, 4: "))
        quest2 = [q2, q2Answers[0], q2Answers[1], q2Answers[2], q2Answers[3], correctAnswer2]
        quest2 = str(quest2)
        quest2 = ("q2AndAnswer2 = ", quest2)
        quest2Final = convertTuple(quest2)
    elif q2asnwercount == 5:
        q2 = input("enter question 5: ")
        questions.append(q2)
        q2Answers2 = input(" Enter Answer 1: ")
        q2Answers.append(q2Answers2 + '\n')
        q2Answers2 = input(" Enter Answer 2: ")
        q2Answers.append(q2Answers2 + '\n')
        q2Answers2 = input(" Enter Answer 3: ")
        q2Answers.append(q2Answers2 + '\n')
        q2Answers2 = input(" Enter Answer 4: ")
        q2Answers.append(q2Answers2 + '\n')
        q2Answers2 = input(" Enter Answer 5: ")
        q2Answers.append(q2Answers2 + '\n')
        correctAnswer2 = int(input("Enter the correct answer, 1, 2, 3, 4, 5: "))
        quest2 = [q2, q2Answers[0], q2Answers[1], q2Answers[2], q2Answers[3], q2Answers[4], correctAnswer2]
        quest2 = str(quest2)
        quest2 = ("q2AndAnswer2 = ", quest2)
        quest2Final = convertTuple(quest2)
def questions3():
    questions = []
    q3Answers = []
    global quest3Final
    q3asnwercount = int(input("Q3. How many answers do you want this question to have?\n Maximum of 5: "))
    if q3asnwercount == 1:
        q3 = input("enter question 1: ")
        questions.append(q3)
        q3Answers3 = input(" Enter Answer 1: ")
        q3Answers.append(q3Answers3 + '\n')
        correctAnswer3 = int(input("Enter the correct answer, 1:  "))
        quest3 = [q3, q3Answers[0], correctAnswer3]
        quest3 = str(quest3)
        quest3 = ("q3AndAnswer3 = ", quest3)
        quest3Final = convertTuple(quest3)
    elif q3asnwercount == 2:
        q3 = input("enter question 1: ")
        questions.append(q3)
        q3Answers3 = input(" Enter Answer 1: ")
        q3Answers.append(q3Answers3 + '\n')
        q3Answers3 = input(" Enter Answer 2: ")
        q3Answers.append(q3Answers3 + '\n')
        correctAnswer3 = int(input("Enter the correct answer, 1, 2:  "))
        quest3 = [q3, q3Answers[0], q3Answers[1], correctAnswer3]
        quest3 = str(quest3)
        quest3 = ("q3AndAnswer3 = ", quest3)
        quest3Final = convertTuple(quest3)
    elif q3asnwercount == 3:
        q3 = input("enter question 1: ")
        questions.append(q3)
        q3Answers3 = input(" Enter Answer 1: ")
        q3Answers.append(q3Answers3 + '\n')
        q3Answers3 = input(" Enter Answer 2: ")
        q3Answers.append(q3Answers3 + '\n')
        q3Answers3 = input(" Enter Answer 3: ")
        q3Answers.append(q3Answers3 + '\n')
        correctAnswer3 = int(input("Enter the correct answer, 1, 2, 3: "))
        quest3 = [q3, q3Answers[0], q3Answers[1], q3Answers[2], correctAnswer3]
        quest3 = str(quest3)
        quest3 = ("q3AndAnswer3 = ", quest3)
        quest3Final = convertTuple(quest3)
    elif q3asnwercount == 4:
        q3 = input("enter question 1: ")
        questions.append(q3)
        q3Answers3 = input(" Enter Answer 1: ")
        q3Answers.append(q3Answers3 + '\n')
        q3Answers3 = input(" Enter Answer 2: ")
        q3Answers.append(q3Answers3 + '\n')
        q3Answers3 = input(" Enter Answer 3: ")
        q3Answers.append(q3Answers3 + '\n')
        q3Answers3 = input(" Enter Answer 4: ")
        q3Answers.append(q3Answers3 + '\n')
        correctAnswer3 = int(input("Enter the correct answer, 1, 2, 3, 4: "))
        quest3 = [q3, q3Answers[0], q3Answers[1], q3Answers[2], q3Answers[3], correctAnswer3]
        quest3 = str(quest3)
        quest3 = ("q3AndAnswer3 = ", quest3)
        quest3Final = convertTuple(quest3)
    elif q3asnwercount == 5:
        q3 = input("enter question 5: ")
        questions.append(q3)
        q3Answers3 = input(" Enter Answer 1: ")
        q3Answers.append(q3Answers3 + '\n')
        q3Answers3 = input(" Enter Answer 2: ")
        q3Answers.append(q3Answers3 + '\n')
        q3Answers3 = input(" Enter Answer 3: ")
        q3Answers.append(q3Answers3 + '\n')
        q3Answers3 = input(" Enter Answer 4: ")
        q3Answers.append(q3Answers3 + '\n')
        q3Answers3 = input(" Enter Answer 5: ")
        q3Answers.append(q3Answers3 + '\n')
        correctAnswer3 = int(input("Enter the correct answer, 1, 2, 3, 4, 5: "))
        quest3 = [q3, q3Answers[0], q3Answers[1], q3Answers[2], q3Answers[3], q3Answers[4], correctAnswer3]
        quest3 = str(quest3)
        quest3 = ("q3AndAnswer3 = ", quest3)
        quest3Final = convertTuple(quest3)
def questions4():

    questions = []
    q4Answers = []
    global quest4Final
    q4asnwercount = int(input("Q4. How many answers do you want this question to have?\n Maximum of 5: "))
    if q4asnwercount == 1:
        q4 = input("enter question 1: ")
        questions.append(q4)
        q4Answers4 = input(" Enter Answer 1: ")
        q4Answers.append(q4Answers4 + '\n')
        correctAnswer4 = int(input("Enter the correct answer, 1:  "))
        quest4 = [q4, q4Answers[0], correctAnswer4]
        quest4 = str(quest4)
        quest4 = ("q4AndAnswer4 = ", quest4)
        quest4Final = convertTuple(quest4)
    elif q4asnwercount == 2:
        q4 = input("enter question 1: ")
        questions.append(q4)
        q4Answers4 = input(" Enter Answer 1: ")
        q4Answers.append(q4Answers4 + '\n')
        q4Answers4 = input(" Enter Answer 2: ")
        q4Answers.append(q4Answers4 + '\n')
        correctAnswer4 = int(input("Enter the correct answer, 1, 2:  "))
        quest4 = [q4, q4Answers[0], q4Answers[1], correctAnswer4]
        quest4 = str(quest4)
        quest4 = ("q4AndAnswer4 = ", quest4)
        quest4Final = convertTuple(quest4)
    elif q4asnwercount == 3:
        q4 = input("enter question 1: ")
        questions.append(q4)
        q4Answers4 = input(" Enter Answer 1: ")
        q4Answers.append(q4Answers4 + '\n')
        q4Answers4 = input(" Enter Answer 2: ")
        q4Answers.append(q4Answers4 + '\n')
        q4Answers4 = input(" Enter Answer 3: ")
        q4Answers.append(q4Answers4 + '\n')
        correctAnswer4 = int(input("Enter the correct answer, 1, 2, 3: "))
        quest4 = [q4, q4Answers[0], q4Answers[1], q4Answers[2], correctAnswer4]
        quest4 = str(quest4)
        quest4 = ("q4AndAnswer4 = ", quest4)
        quest4Final = convertTuple(quest4)
    elif q4asnwercount == 4:
        q4 = input("enter question 1: ")
        questions.append(q4)
        q4Answers4 = input(" Enter Answer 1: ")
        q4Answers.append(q4Answers4 + '\n')
        q4Answers4 = input(" Enter Answer 2: ")
        q4Answers.append(q4Answers4 + '\n')
        q4Answers4 = input(" Enter Answer 3: ")
        q4Answers.append(q4Answers4 + '\n')
        q4Answers4 = input(" Enter Answer 4: ")
        q4Answers.append(q4Answers4 + '\n')
        correctAnswer4 = int(input("Enter the correct answer, 1, 2, 3, 4: "))
        quest4 = [q4, q4Answers[0], q4Answers[1], q4Answers[2], q4Answers[3], correctAnswer4]
        quest4 = str(quest4)
        quest4 = ("q4AndAnswer4 = ", quest4)
        quest4Final = convertTuple(quest4)
    elif q4asnwercount == 5:
        q4 = input("enter question 5: ")
        questions.append(q4)
        q4Answers4 = input(" Enter Answer 1: ")
        q4Answers.append(q4Answers4 + '\n')
        q4Answers4 = input(" Enter Answer 2: ")
        q4Answers.append(q4Answers4 + '\n')
        q4Answers4 = input(" Enter Answer 3: ")
        q4Answers.append(q4Answers4 + '\n')
        q4Answers4 = input(" Enter Answer 4: ")
        q4Answers.append(q4Answers4 + '\n')
        q4Answers4 = input(" Enter Answer 5: ")
        q4Answers.append(q4Answers4 + '\n')
        correctAnswer4 = int(input("Enter the correct answer, 1, 2, 3, 4, 5: "))
        quest4 = [q4, q4Answers[0], q4Answers[1], q4Answers[2], q4Answers[3], q4Answers[4], correctAnswer4]
        quest4 = str(quest4)
        quest4 = ("q5AndAnswer5 = ", quest4)
        quest4Final = convertTuple(quest4)
def questions5():
    questions = []
    q5Answers = []
    global quest5Final
    q5asnwercount = int(input("Q5. How many answers do you want this question to have?\n Maximum of 5: "))
    if q5asnwercount == 1:
        q5 = input("enter question 1: ")
        questions.append(q5)
        q5Answers5 = input(" Enter Answer 1: ")
        q5Answers.append(q5Answers5 + '\n')
        correctAnswer5 = int(input("Enter the correct answer, 1:  "))
        quest5 = [q5, q5Answers[0], correctAnswer5]
        quest5 = str(quest5)
        quest5 = ("q5AndAnswer5 = ", quest5)
        quest5Final = convertTuple(quest5)
    elif q5asnwercount == 2:
        q4 = input("enter question 1: ")
        questions.append(q5)
        q5Answers5 = input(" Enter Answer 1: ")
        q5Answers.append(q5Answers5 + '\n')
        q5Answers5 = input(" Enter Answer 2: ")
        q5Answers.append(q5Answers5 + '\n')
        correctAnswer5 = int(input("Enter the correct answer, 1, 2:  "))
        quest5 = [q5, q5Answers[0], q5Answers[1], correctAnswer5]
        quest5 = str(quest5)
        quest5 = ("q5AndAnswer5 = ", quest5)
        quest5Final = convertTuple(quest5)
    elif q5asnwercount == 3:
        q5 = input("enter question 1: ")
        questions.append(q5)
        q5Answers5 = input(" Enter Answer 1: ")
        q5Answers.append(q5Answers5 + '\n')
        q5Answers5 = input(" Enter Answer 2: ")
        q5Answers.append(q5Answers5 + '\n')
        q5Answers5 = input(" Enter Answer 3: ")
        q5Answers.append(q5Answers5 + '\n')
        correctAnswer5 = int(input("Enter the correct answer, 1, 2, 3: "))
        quest5 = [q5, q5Answers[0], q5Answers[1], q5Answers[2], correctAnswer5]
        quest5 = str(quest5)
        quest5 = ("q5AndAnswer5 = ", quest5)
        quest5Final = convertTuple(quest5)
    elif q5asnwercount == 4:
        q5 = input("enter question 1: ")
        questions.append(q5)
        q5Answers5 = input(" Enter Answer 1: ")
        q5Answers.append(q5Answers5 + '\n')
        q5Answers5 = input(" Enter Answer 2: ")
        q5Answers.append(q5Answers5 + '\n')
        q5Answers5 = input(" Enter Answer 3: ")
        q5Answers.append(q5Answers5 + '\n')
        q5Answers5 = input(" Enter Answer 4: ")
        q5Answers.append(q5Answers5 + '\n')
        correctAnswer5 = int(input("Enter the correct answer, 1, 2, 3, 4: "))
        quest5 = [q5, q5Answers[0], q5Answers[1], q5Answers[2], q5Answers[3], correctAnswer5]
        quest5 = str(quest5)
        quest5 = ("q5AndAnswer5 = ", quest5)
        quest5Final = convertTuple(quest5)
    elif q5asnwercount == 5:
        q5 = input("enter question 5: ")
        questions.append(q5)
        q5Answers5 = input(" Enter Answer 1: ")
        q5Answers.append(q5Answers5 + '\n')
        q5Answers5 = input(" Enter Answer 2: ")
        q5Answers.append(q5Answers5 + '\n')
        q5Answers5 = input(" Enter Answer 3: ")
        q5Answers.append(q5Answers5 + '\n')
        q5Answers5 = input(" Enter Answer 4: ")
        q5Answers.append(q5Answers5 + '\n')
        q5Answers5 = input(" Enter Answer 5: ")
        q5Answers.append(q5Answers5 + '\n')
        correctAnswer5 = int(input("Enter the correct answer, 1, 2, 3, 4, 5: "))
        quest5 = [q5, q5Answers[0], q5Answers[1], q5Answers[2], q5Answers[3], q5Answers[4], correctAnswer5]
        quest5 = str(quest5)
        quest5 = ("q5AndAnswer5 = ", quest5)
        quest5Final = convertTuple(quest5)

    
if numberofq == 1:
    questions1()
    file = open("answers.py", 'a')
    file.write(quest1Final + '\n')
    file.close()
elif numberofq == 2:
    questions1()
    questions2()
    file = open("answers.py", 'a')
    file.write(quest1Final + '\n')
    file.write(quest2Final + '\n')
    file.close()
elif numberofq == 3:
    questions1()
    questions2()
    questions3()
    file = open("answers.py", 'a')
    file.write(quest1Final + '\n')
    file.write(quest2Final + '\n')
    file.write(quest3Final + '\n')
    file.close()
elif numberofq == 4:
    questions1()
    questions2()
    questions3()
    questions4()
    file = open("answers.py", 'a')
    file.write(quest1Final + '\n')
    file.write(quest2Final + '\n')
    file.write(quest3Final + '\n')
    file.write(quest4Final + '\n')
    file.close()

elif numberofq == 5:
    questions1()
    questions2()
    questions3()
    questions4()
    questions5()
    file = open("answers.py", 'a')
    file.write(quest1Final + '\n')
    file.write(quest2Final + '\n')
    file.write(quest3Final + '\n')
    file.write(quest4Final + '\n')
    file.write(quest5Final + '\n')
    file.close()

numberofq = str(numberofq)
numberofq = ("numberofq = ", numberofq)
numberofq = convertTuple(numberofq)
file = open("answers.py", 'a')
file.write(numberofq + '\n')
file.close()


# file = open("answers.py", 'a')
# file.write(quest1Final + '\n')
# file.write(quest2Final + '\n')
# file.write(quest3Final + '\n')
# file.write(quest4Final + '\n')
# file.write(quest5Final + '\n')
# file.close()
