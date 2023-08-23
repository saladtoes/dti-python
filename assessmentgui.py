import easygui
name = str(easygui.enterbox("What is your name?: "))
def contains_number(string):
    return any(char.isdigit() for char in string)
while contains_number(name):
    easygui.msgbox("Your name can not contain a number")
    name = str(easygui.enterbox("What is your name?: "))
    

age = int(easygui.integerbox("Hello " + name + " how old are you?: "))
    
if age <= 7:
    easygui.msgbox("youre too young to do this quiz")
    quit()
elif age >= 14:
    easygui.msgbox("Your above the recommended age for this quiz.\nPlease try the Cybersmath Youth quiz instead")
    quit()
else:
    easygui.msgbox("Hello " + name + " Welcome to the Cybersmart start quiz")
global answers
answers = ["a", "b", "c"]
question1Answers = [" A: Delete the message and try to forget about it\n", "B: Keep the text and show an adult you trust\n", "C: Text the person back and say something mean to them"]
question2Answers = [" A: Tweet that they are an idiot and a loser\n", "B: Ask your friends to grive the person a hard time\n", "C: Tell and adult you trust\n"]
question3Answers = [" A: Nickname\n", "B: Your name\n", "C: Your email address\n"]
question4Answers = [" A: Your video is rubbish\n", "B: Man, this is awful! Stick to playing spport or something.\n", "C: Congrats on your first video! Let me know if you'd like any help editing for your next video\n"]
question5Answers = [' A: “We shouldn’t be mean to them just because they’re mean to us."\n', 'B: “Yeah, totally. They’re evil and deserve it!”\n', 'C: “Yes, I think that is a great idea. Maybe they will understand what it feels like, and stop bullying us!”\n']
questions = ["Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?\n", "You find out that someone has posted an embarrassing picture of you online. What should you do?\n", "You want to join an online gaming site. Which of the following information is okay for you to post on the site.\n", "Someone in your class has posted their first video on YouTube and has asked you to comment on it. You don’t think the video is good because the editing is very choppy. What could you comment?\n", "Someone in your class is a real bully. Some of the other people in your class say: “Let’s get them back, and spam them with random texts.” What do you reply?\n"]
global score
score = 0 
question1count, question2count, question3count, question4count, question5count = 0, 0, 0, 0, 0
question1countright, question2countright, question3countright, question4countright, question5countright = 0, 0, 0, 0, 0

def question1():
    global score, question1count, question1countright
    question1countright = 0
    question1count = 0
while question1count != 3 or question1countright >= 1:
    q1 = easygui.enterbox(questions[0] + question1Answers[0] + question1Answers[1] + question1Answers[2] + "\nAnswer now: ")
    q1 = q1.lower()
    if q1 == answers[1]:
        if question1count == 0:
            score += 1
            pass
        score = str(score)
        easygui.msgbox("that is correct\n" + "Your score is now" + score + "out of 5")
        question1countright += 1
        score = int(score)

        break
    elif contains_number(q1):
        easygui.msgbox("Invalid Input\n please enter only a, b, c")
        question1count += 1
        pass
    elif q1 != answers[1]:
        easygui.msgbox("That was wrong")
        question1count += 1
        pass
    

def question2():
    global score, question2count, question2countright
    question2countright = 0    
    question2count = 0
while question2count != 3 or question2countright >= 1:
    q2 = easygui.enterbox(questions[1] + question2Answers[0] + question2Answers[1] + question2Answers[2] + "\nAnswer now: ")
    q2 = q2.lower()
    if q2 == answers[2]:
        if question2count == 0:
            score += 1
            pass
        score = str(score)
        easygui.msgbox("that is correct\n" + "Your score is now " + score + " out of 5")
        question2countright += 1
        score = int(score)

        break
    elif contains_number(q2):
        easygui.msgbox("Invalid Input\n please enter only a, b, c")
        question2count += 1
        pass
    elif q2 != answers[2]:
        easygui.msgbox("That was wrong")
        question2count += 1
        pass

def question3():
    global score, question3count, question3countright
    question3countright = 0
    question3count = 0
while question3count != 3 or question3countright >= 1:
    q3 = easygui.enterbox(questions[2] + question3Answers[0] + question3Answers[1] + question3Answers[2] + "\nAnswer now: ")
    q3 = q3.lower()
    if q3 == answers[0]:
        if question3count == 0:
            score += 1
        score = str(score)
        easygui.msgbox("that is correct\n" + "Your score is now " + score + " out of 5")
        score = int(score)
        question3countright += 1
        break
    elif contains_number(q3):
        easygui.msgbox("Invalid Input\n please enter only a, b, c")
        question3count += 1
        pass
    elif q3 != answers[0]:
        easygui.msgbox("That was wrong")
        question3count += 1
        pass

def question4():
    global score, question4count, question4countright
    question4countright = 0
    question4count = 0
while question4count != 3 or question4countright >= 1:
    q4 = easygui.enterbox(questions[3] + question4Answers[0] + question4Answers[1] + question4Answers[2])
    q4 = q4.lower()
    if q4 == answers[2]:
        if question4count == 0:
            score += 1
        score = str(score)
        easygui.msgbox("That was correct\n" + "Your score is now " + score + " out of 5")
        score = int(score)
        question4countright += 1

        break
    elif contains_number(q4):
        easygui.msgbox("Invalid Input\n please enter only a, b, c")
        question4count += 1
        pass
    elif q4 != answers[2]:
        easygui.msgbox("That was wrong\n")
        question4count += 1
        pass

def question5():
    global score, question5count, question5countright
    question5countright = 0
    question5count = 0
while question4count != 3 or question5countright >= 1:
    q5 = easygui.enterbox(questions[4] + question5Answers[0] + question5Answers[1] + question5Answers[2])
    q5 = q5.lower()
    if q5 == answers[0]:
        if question5count == 0:
            score += 1
        score = str(score)
        easygui.msgbox("That was correct\n" + "Your score is now " + score + " out of 5")
        question5countright += 1
        score = int(score)

        break
    elif contains_number(q5):
        easygui.msgbox("Invalid Input\n please enter only a, b, c")
        question5count += 1
        pass
    elif q5 != answers[0]:
        easygui.msgbox("That was wrong\n")
        question5count += 1
        pass

question1()
question2()
question3()
question4()
question5()
score = str(score)
easygui.msgbox(name + " Your score is " + score + " out of 5")


