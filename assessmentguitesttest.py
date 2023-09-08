# -*- coding: utf-8 -*-
import easygui
name = str(easygui.enterbox("What is your name?: "))
def contains_number(string):
    return any(char.isdigit() for char in string)
while contains_number(name):
    name = str(easygui.enterbox("Your name cannot contain a number \nWhat is your name?: "))
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
global questionrightcount, questionwrongcount, questionnum, questions, question5Answers, question4Answers, question3Answers, question2Answers, question1Answers, answers, score, questionnumquestionsprint, questionAnswers, answer, done
answers = ["a", "b", "c"]
info = [" A: Delete the message and try to forget about it\n", "B: Keep the text and show an adult you trust\n", "C: Text the person back and say something mean to them", " A: Tweet that they are an idiot and a loser\n", "B: Ask your friends to grive the person a hard time\n", "C: Tell and adult you trust\n", " A: Nickname\n", "B: Your name\n", "C: Your email address\n", " A: Your video is rubbish\n", "B: Man, this is awful! Stick to playing spport or something.\n", "C: Congrats on your first video! Let me know if you'd like any help editing for your next video\n", ' A: “We shouldn’t be mean to them just because they’re mean to us."\n', 'B: “Yeah, totally. They’re evil and deserve it!”\n', 'C: “Yes, I think that is a great idea. Maybe they will understand what it feels like, and stop bullying us!”\n', "Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?\n", "You find out that someone has posted an embarrassing picture of you online. What should you do?\n", "You want to join an online gaming site. Which of the following information is okay for you to post on the site.\n", "Someone in your class has posted their first video on YouTube and has asked you to comment on it. You don’t think the video is good because the editing is very choppy. What could you comment?\n", "Someone in your class is a real bully. Some of the other people in your class say: “Let’s get them back, and spam them with random texts.” What do you reply?\n", "a", "b", "c"]
questionnum, score, done, questionsprint, questionAnswers, answer = 0, 0, 0, "", "", 0
def questionsask():
    global score, questionrightcount, questionwrongcount, questionnum, questions, question5Answers, question4Answers, question3Answers, question2Answers, question1Answers, answers, questionsprint, questionAnswers, answer, done
    questionsprint, questionAnswers, answer, questionrightcount, questionwrongcount = "", "", 0, 0, 0
    if questionnum == 0:
        questionsprint = info[15]
        questionAnswers = info[0] + info[1] + info[2]
        answer = info[21]
    elif questionnum == 1:
        questionsprint = info[16]
        questionAnswers = info[3] + info[4] + info[5]
        answer = info[22]
    elif questionnum == 2:
        questionsprint = info[17]
        questionAnswers = info[6] + info[7] + info[8]
        answer = info[20]
    elif questionnum == 3:
        questionsprint = info[18]
        questionAnswers = info[9] + info[10] + info[11]
        answer = info[22]
    elif questionnum == 4:
        questionsprint = info[19]
        questionAnswers = info[12] + info[13] + info[14]
        answer = info[20]
    elif questionnum == 5:
        return
    def askquestion():
        global score, questionrightcount, questionwrongcount, questionnum, questions, question5Answers, question4Answers, question3Answers, question2Answers, question1Answers, answers, questionsprint, questionAnswers, answer, done
        while questionwrongcount != 3 or questionrightcount != 1:
            question = easygui.enterbox(questionsprint + questionAnswers + "\nAnswer now: ")
            if question.lower() == answer:
                if questionwrongcount == 0:
                    score = int(score)
                    score += 1
                    pass
                easygui.msgbox("that is correct\n" + "Your score is now" + str(score) + "out of 5")
                questionrightcount += 1
                score = int(score)
                pass
            elif contains_number(question) or question not in answers:
                easygui.msgbox("Invalid Input\n please enter only a, b, c")
                questionwrongcount += 1
                pass
            elif question != answer:
                easygui.msgbox("That was wrong")
                questionwrongcount += 1
                pass
            if questionwrongcount == 3 or questionrightcount == 1:
                questionnum += 1
                pass
            if questionnum == 5:
                easygui.msgbox(name + " Your Final score is " + str(score) + " out of 5")
                quit()
            if questionwrongcount == 3 or questionrightcount == 1:
                questionsask()
            else:
                askquestion()
    if questionnum != 5:
        askquestion()
    else:
        return
if done == 0:
    questionsask()
