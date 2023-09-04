import answers as a

global score
score = 0 
question1count, question2count,question3count,question4count, question5count = 0, 0, 0, 0, 0
question1countright, question2countright, question3countright, question4countright, question5countright = 0, 0, 0, 0, 0

def question1():
    global score, question1count, question1countright
    question1countright = 0
    question1count = 0
    if isinstance(a.q1AndAnswer1[2], int):
        while question1count != 3 or question1countright >= 1:
            print("Q1 - " + a.q1AndAnswer1[0])
            print(" 1.", a.q1AndAnswer1[1])
            q1 = input("Answer Now: ")
            if q1 == a.q1AndAnswer1[2]:
                print("that is correct\n")
                question1countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q1 != a.q1AndAnswer1[2]:
                print("That was wrong")
                question1count += 1
                print("attempt", question1count, "of 3")
                pass
    elif isinstance(a.q1AndAnswer1[3], int):
        while question1count != 3 or question1countright >= 1:
            print("Q1 - " + a.q1AndAnswer1[0])
            print(" 1.", a.q1AndAnswer1[1], "2.", a.q1AndAnswer1[2])
            q1 = int(input("Answer Now: "))
            if q1 == a.q1AndAnswer1[3]:
                print("that is correct\n")
                question1countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q1 != a.q1AndAnswer1[3]:
                print("That was wrong")
                question1count += 1
                print("attempt", question1count, "of 3")
                pass
    elif isinstance(a.q1AndAnswer1[4], int):
        while question1count != 3 or question1countright >= 1:
            print("Q1 - " + a.q1AndAnswer1[0])
            print(" 1.", a.q1AndAnswer1[1], "2.", a.q1AndAnswer1[2], "3.", a.q1AndAnswer1[3])
            q1 = input("Answer Now: ")
            q1 = int(q1)
            if q1 == a.q1AndAnswer1[4]:
                print("that is correct\n")
                question1countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q1 != a.q1AndAnswer1[4]:
                print("That was wrong")
                question1count += 1
                print("attempt", question1count, "of 3")
                pass
    elif isinstance(a.q1AndAnswer1[5], int):
        while question1count != 3 or question1countright >= 1:
            print("Q1 - " + a.q1AndAnswer1[0])
            print(" 1.", a.q1AndAnswer1[1], "2.", a.q1AndAnswer1[2], "3.", a.q1AndAnswer1[3], "4.", a.q1AndAnswer1[4])
            q1 = int(input("Answer Now: "))
            if q1 == a.q1AndAnswer1[5]:
                print("that is correct\n")
                question1countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q1 != a.q1AndAnswer1[5]:
                print("That was wrong")
                question1count += 1
                print("attempt", question1count, "of 3")
                pass
    elif isinstance(a.q1AndAnswer1[6], int):
        while question1count != 3 or question1countright >= 1:
            print("Q1 - " + a.q1AndAnswer1[0])
            print(" 1.", a.q1AndAnswer1[1], "2.", a.q1AndAnswer1[2], "3.", a.q1AndAnswer1[3], "4.", a.q1AndAnswer1[4], "5.", a.q1AndAnswer1[5])
            q1 = int(input("Answer Now: "))
            if q1 == a.q1AndAnswer1[6]:
                print("that is correct\n")
                question1countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q1 != a.q1AndAnswer1[6]:
                print("That was wrong")
                question1count += 1
                print("attempt", question1count, "of 3")
                pass

def question2():
    global score, question2count, question2countright
    question2countright = 0    
    question2count = 0
    if isinstance(a.q2AndAnswer2[2], int):
        while question2count != 3 or question2countright >= 1:
            print(a.q2AndAnswer2[0])
            print(" 1.", a.q2AndAnswer2[1])
            q2 = int(input("Answer Now: "))
            if q2 == a.q2AndAnswer2[2]:
                print("that is correct\n")
                question2countright += 1
                if question2count == 0:
                    score += 1
                break
            elif q2 != a.q2AndAnswer2[2]:
                print("That was wrong")
                question2count += 1
                print("attempt", question2count, "of 3")
                pass
    elif isinstance(a.q2AndAnswer2[3], int):
        while question2count != 3 or question2countright >= 1:
            print(a.q2AndAnswer2[0])
            print(" 1.", a.q2AndAnswer2[1], "2.", a.q2AndAnswer2[2])
            q2 = int(input("Answer Now: "))
            if q2 == a.q2AndAnswer2[3]:
                print("that is correct\n")
                question2countright += 1
                if question2count == 0:
                    score += 1
                break
            elif q2 != a.q2AndAnswer2[3]:
                print("That was wrong")
                question2count += 1
                print("attempt", question2count, "of 3")
                pass
    elif isinstance(a.q2AndAnswer2[4], int):
        while question2count != 3 or question2countright >= 1:
            print(a.q2AndAnswer2[0])
            print(" 1.", a.q2AndAnswer2[1], "2.", a.q2AndAnswer2[2], "3.", a.q2AndAnswer2[3])
            q2 = int(input("Answer Now: "))
            if q2 == a.q2AndAnswer2[4]:
                print("that is correct\n")
                question2countright += 1
                if question2count == 0:
                    score += 1
                break
            elif q2 != a.q2AndAnswer2[4]:
                print("That was wrong")
                question2count += 1
                print("attempt", question2count, "of 3")
                pass
    elif isinstance(a.q2AndAnswer2[5], int):
        while question2count != 3 or question2countright >= 1:
            print(a.q2AndAnswer2[0])
            print(" 1.", a.q2AndAnswer2[1], "2.", a.q2AndAnswer2[2], "3.", a.q2AndAnswer2[3], "4.", a.q2AndAnswer2[4])
            q2 = int(input("Answer Now: "))
            if q2 == a.q2AndAnswer2[5]:
                print("that is correct\n")
                question2countright += 1
                if question2count == 0:
                    score += 1
                break
            elif q2 != a.q2AndAnswer2[5]:
                print("That was wrong")
                question2count += 1
                print("attempt", question2count, "of 3")
                pass
    elif isinstance(a.q2AndAnswer2[6], int):
        while question2count != 3 or question2countright >= 1:
            print(a.q2AndAnswer2[0])
            print(" 1.", a.q2AndAnswer2[1], "2.", a.q2AndAnswer2[2], "3.", a.q2AndAnswer2[3], "4.", a.q2AndAnswer2[4], "5.", a.q2AndAnswer2[5])
            q2 = int(input("Answer Now: "))
            if q2 == a.q2AndAnswer2[6]:
                print("that is correct\n")
                question2countright += 1
                if question2count == 0:
                    score += 1
                break
            elif q2 != a.q2AndAnswer2[6]:
                print("That was wrong")
                question2count += 1
                print("attempt", question2count, "of 3")
                pass

def question3():
    global score, question3count, question3countright
    question3countright = 0
    question3count = 0
    if isinstance(a.q3AndAnswer3[2], int):
        while question3count != 3 or question3countright >= 1:
            print(a.q3AndAnswer3[0])
            print(" 1.", a.q3AndAnswer3[1])
            q3 = int(input("Answer Now: "))
            if q3 == a.q3AndAnswer3[2]:
                print("that is correct\n")
                question3countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q3 != a.q3AndAnswer3[2]:
                print("That was wrong")
                question3count += 1
                print("attempt", question3count, "of 3")
                pass
    elif isinstance(a.q3AndAnswer3[3], int):
        while question3count != 3 or question3countright >= 1:
            print(a.q3AndAnswer3[0])
            print(" 1.", a.q3AndAnswer3[1], "2.", a.q3AndAnswer3[2])
            q3 = int(input("Answer Now: "))
            if q3 == a.q3AndAnswer3[3]:
                print("that is correct\n")
                question3countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q3 != a.q3AndAnswer3[3]:
                print("That was wrong")
                question3count += 1
                print("attempt", question3count, "of 3")
                pass
    elif isinstance(a.q3AndAnswer3[4], int):
        while question3count != 3 or question3countright >= 1:
            print(a.q3AndAnswer3[0])
            print(" 1.", a.q3AndAnswer3[1], "2.", a.q3AndAnswer3[2], "3.", a.q3AndAnswer3[3])
            q3 = int(input("Answer Now: "))
            if q3 == a.q3AndAnswer3[4]:
                print("that is correct\n")
                question3countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q3 != a.q3AndAnswer3[4]:
                print("That was wrong")
                question3count += 1
                print("attempt", question3count, "of 3")
                pass
    elif isinstance(a.q3AndAnswer3[5], int):
        while question3count != 3 or question3countright >= 1:
            print(a.q3AndAnswer3[0])
            print(" 1.", a.q3AndAnswer3[1], "2.", a.q3AndAnswer3[2], "3.", a.q3AndAnswer3[3], "4.", a.q3AndAnswer3[4])
            q3 = int(input("Answer Now: "))
            if q3 == a.q3AndAnswer3[5]:
                print("that is correct\n")
                question3countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q3 != a.q3AndAnswer3[5]:
                print("That was wrong")
                question3count += 1
                print("attempt", question3count, "of 3")
                pass
    elif isinstance(a.q3AndAnswer3[6], int):
        while question3count != 3 or question3countright >= 1:
            print(a.q3AndAnswer3[0])
            print(" 1.", a.q3AndAnswer3[1], "2.", a.q3AndAnswer3[2], "3.", a.q3AndAnswer3[3], "4.", a.q3AndAnswer3[4], "5.", a.q3AndAnswer3[5])
            q3 = int(input("Answer Now: "))
            if q3 == a.q3AndAnswer3[6]:
                print("that is correct\n")
                question3countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q3 != a.q3AndAnswer3[6]:
                print("That was wrong")
                question3count += 1
                print("attempt", question3count, "of 3")
                pass

def question4():
    global score, question4count, question4countright
    question4countright = 0
    question4count = 0
    if isinstance(a.q4AndAnswer4[2], int):
        while question4count != 3 or question4countright >= 1:
            print(a.q4AndAnswer4[0])
            print(" 1.", a.q4AndAnswer4[1])
            q4 = int(input("Answer now: "))
            if q4 == a.q4AndAnswer4[2]:
                print("That was correct\n")
                question4countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q4 != a.q4AndAnswer4[2]:
                print("That was wrong\n")
                question4count += 1
                print("attempt", question4count, "of 3")
                pass
    elif isinstance(a.q4AndAnswer4[3], int):
        while question4count != 3 or question4countright >= 1:
            print(a.q4AndAnswer4[0])
            print(" 1.", a.q4AndAnswer4[1], "2.", a.q4AndAnswer4[2])
            q4 = int(input("Answer now: "))
            if q4 == a.q4AndAnswer4[3]:
                print("That was correct\n")
                question4countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q4 != a.q4AndAnswer4[3]:
                print("That was wrong\n")
                question4count += 1
                print("attempt", question4count, "of 3")
                pass
    elif isinstance(a.q4AndAnswer4[4], int):
        while question4count != 3 or question4countright >= 1:
            print(a.q4AndAnswer4[0])
            print("1.", a.q4AndAnswer4[1], "2.", a.q4AndAnswer4[2], "3.", a.q4AndAnswer4[3])
            q4 = int(input("Answer now: "))
            if q4 == a.q4AndAnswer4[4]:
                print("That was correct\n")
                question4countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q4 != a.q4AndAnswer4[4]:
                print("That was wrong\n")
                question4count += 1
                print("attempt", question4count, "of 3")
                pass
    elif isinstance(a.q4AndAnswer4[5], int):
        while question4count != 3 or question4countright >= 1:
            print(a.q4AndAnswer4[0])
            print(" 1.", a.q4AndAnswer4[1], "2.", a.q4AndAnswer4[2], "3.", a.q4AndAnswer4[3], "4.", a.q4AndAnswers4[4])
            q4 = int(input("Answer now: "))
            if q4 == a.q4AndAnswer4[5]:
                print("That was correct\n")
                question4countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q4 != a.q4AndAnswer4[5]:
                print("That was wrong\n")
                question4count += 1
                print("attempt", question4count, "of 3")
                pass
    elif isinstance(a.q4AndAnswer4[6], int):
        while question4count != 3 or question4countright >= 1:
            print(a.q4AndAnswer4[0])
            print(" 1.", a.q4AndAnswer4[1], "2.", a.q4AndAnswer4[2], "3.", a.q4AndAnswer4[3], "4.", a.q4AndAnswers4[4], "5.", a.q5AndAnswer5[5])
            q4 = int(input("Answer now: "))
            if q4 == a.q4AndAnswer4[6]:
                print("That was correct\n")
                question4countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q4 != a.q4AndAnswer4[6]:
                print("That was wrong\n")
                question4count += 1
                print("attempt", question4count, "of 3")
                pass

def question5():
    global score, question5count, question5countright
    question5countright = 0
    question5count = 0
    if isinstance(a.q5AndAnswer5[2], int):
        while question4count != 3 or question5countright >= 1:
            print(a.q5AndAnswer5[0])  
            print(" 1.", a.q5AndAnswer5[1])
            q5 = int(input("Answer now: "))
            if q5 == a.q5AndAnswer5[2]:
                print("That was correct\n")
                question5countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q5 != a.q5AndAnswer5[2]:
                print("That was wrong\n")
                question5count += 1
                print("attempt", question5count, "of 3")
                pass  
    elif isinstance(a.q5AndAnswer5[3], int):
        while question4count != 3 or question5countright >= 1:
            print(a.q5AndAnswer5[0])  
            print(" 1.", a.q5AndAnswer5[1], "2.", a.q5AndAnswer5[2])
            q5 = int(input("Answer now: "))
            if q5 == a.q5AndAnswer5[3]:
                print("That was correct\n")
                question5countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q5 != a.q5AndAnswer5[3]:
                print("That was wrong\n")
                question5count += 1
                print("attempt", question5count, "of 3")
                pass
    elif isinstance(a.q5AndAnswer5[4], int):
        while question4count != 3 or question5countright >= 1:
            print(a.q5AndAnswer5[0])  
            print(" 1.", a.q5AndAnswer5[1], "2.", a.q5AndAnswer5[2], "3.", a.q5AndAnswer5[3])
            q5 = int(input("Answer now: "))
            if q5 == a.q5AndAnswer5[4]:
                print("That was correct\n")
                question5countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q5 != a.q5AndAnswer5[4]:
                print("That was wrong\n")
                question5count += 1
                print("attempt", question5count, "of 3")
                pass
    elif isinstance(a.q5AndAnswer5[5], int):
        while question4count != 3 or question5countright >= 1:
            print(a.q5AndAnswer5[0])  
            print(" 1.", a.q5AndAnswer5[1], "2.", a.q5AndAnswer5[2], "3.", a.q5AndAnswer5[3], "4.", a.q5AndAnswer5[4])
            q5 = int(input("Answer now: "))
            if q5 == a.q5AndAnswer5[5]:
                print("That was correct\n")
                question5countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q5 != a.q5AndAnswer5[5]:
                print("That was wrong\n")
                question5count += 1
                print("attempt", question5count, "of 3")
                pass
    elif isinstance(a.q5AndAnswer5[6], int):
        while question4count != 3 or question5countright >= 1:
            print(a.q5AndAnswer5[0])  
            print(" 1.", a.q5AndAnswer5[1], "2.", a.q5AndAnswer5[2], "3.", a.q5AndAnswer5[3], "4.", a.q5AndAnswer5[4], "5.", a.q5AndAnswer5[5])
            q5 = int(input("Answer now: "))
            if q5 == a.q5AndAnswer5[6]:
                print("That was correct\n")
                question5countright += 1
                if question1count == 0:
                    score += 1
                break
            elif q5 != a.q5AndAnswer5[6]:
                print("That was wrong\n")
                question5count += 1
                print("attempt", question5count, "of 3")
                pass


if a.numberofq == 1:
    question1()
elif a.numberofq == 2:
    question1()
    question2()
elif a.numberofq == 3:
    question1()
    question2()
    question3()
elif a.numberofq == 4:
    question1()
    question2()
    question3()
    question4()
elif a.numberofq == 5:
    question1()
    question2()
    question3()
    question4()
    question5()

print("Your score is", score, "out of ", a.numberofq)
