# -*- coding: utf-8 -*-
import easygui
name = str(easygui.enterbox("What is your name?: "))
def contains_number(string):
    return any(char.isdigit() for char in string)
while contains_number(name):
    easygui.msgbox("Your name can not contain a number")
    name = str(easygui.enterbox("What is your name?: "))
global age
def agecheck():
    global age
    try:
        age = int(easygui.enterbox("Hello " + name + " how old are you?: "))
    except:
        agecheck()
    else:
        pass
agecheck()
if age <= 7:
    easygui.msgbox("youre too young to do this quiz")
    quit()
elif age >= 14:
    easygui.msgbox("Your above the recommended age for this quiz.\nPlease try the CyberSmart Youth quiz instead")
    quit()
else:
    easygui.msgbox("Hello " + name + " Welcome to the Cybersmart start quiz")
global questionrightcount, questionwrongcount, questionnum, questions, question5Answers, question4Answers, question3Answers, question2Answers, question1Answers, answers, score, questionnumquestionsprint, questionAnswers, answer
answers = ["a", "b", "c"]
question1Answers = [" A: Delete the message and try to forget about it\n", "B: Keep the text and show an adult you trust\n", "C: Text the person back and say something mean to them"]
question2Answers = [" A: Tweet that they are an idiot and a loser\n", "B: Ask your friends to grive the person a hard time\n", "C: Tell and adult you trust\n"]
question3Answers = [" A: Nickname\n", "B: Your name\n", "C: Your email address\n"]
question4Answers = [" A: Your video is rubbish\n", "B: Man, this is awful! Stick to playing spport or something.\n", "C: Congrats on your first video! Let me know if you'd like any help editing for your next video\n"]
question5Answers = [' A: “We shouldn’t be mean to them just because they’re mean to us."\n', 'B: “Yeah, totally. They’re evil and deserve it!”\n', 'C: “Yes, I think that is a great idea. Maybe they will understand what it feels like, and stop bullying us!”\n']
questions = ["Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?\n", "You find out that someone has posted an embarrassing picture of you online. What should you do?\n", "You want to join an online gaming site. Which of the following information is okay for you to post on the site.\n", "Someone in your class has posted their first video on YouTube and has asked you to comment on it. You don’t think the video is good because the editing is very choppy. What could you comment?\n", "Someone in your class is a real bully. Some of the other people in your class say: “Let’s get them back, and spam them with random texts.” What do you reply?\n"]
questionnum = 0
score = 0
questionsprint, questionAnswers, answer = "", "", ""
def questionsask():
    global score, questionrightcount, questionwrongcount, questionnum, questions, question5Answers, question4Answers, question3Answers, question2Answers, question1Answers, answers, questionsprint, questionAnswers, answer
    questionrightcount, questionwrongcount = 0, 0

    if questionnum == 0:
        questionsprint = questions[0]
        questionAnswers = question1Answers[0] + question1Answers[1] + question1Answers[2]
        answer = answers[1]
    elif questionnum == 1:
        questionsprint = questions[1]
        questionAnswers = question2Answers[0] + question2Answers[1] + question2Answers[2]
        answer = answers[2]
    elif questionnum == 2:
        questionsprint = questions[2]
        questionAnswers = question3Answers[0] + question3Answers[1] + question3Answers[2]
        answer = answers[0]
    elif questionnum == 3:
        questionsprint = questions[3]
        questionAnswers = question4Answers[0] + question4Answers[1] + question4Answers[2]
        answer = answers[2]
    elif questionnum == 4:
        questionsprint = questions[4]
        questionAnswers = question5Answers[0] + question5Answers[1] + question5Answers[2]
        answer = answers[2]
    else:
        return
    while questionwrongcount != 3 or questionrightcount >= 1:
        question = easygui.enterbox(questionsprint + questionAnswers + "\nAnswer now: ")
        if question == answer:
            if questionwrongcount == 0:
                score = int(score)
                score += 1
                pass
            score = str(score)
            easygui.msgbox("That is correct\n" + "Your score is now" + str(score) + "out of 5")
            questionrightcount += 1
            questionnum += 1
        elif contains_number(question) or question not in answers:
            easygui.msgbox("Invalid Input\n Please input only a, b or c")
            questionwrongcount += 1
        elif question != answers[1]:
            easygui.msgbox("That was wrong")
            questionwrongcount += 1
        if questionwrongcount == 3:
            questionnum += 1
        else:
            pass

        questionrightcount, questionwrongcount, = 0, 0
        questionsprint, questionAnswers, answer = "", "", ""
        questionsask()
        if questionnum == 5:
            break

questionsask()
score = str(score)
easygui.msgbox(name + " Your score is " + score + " out of 5")


