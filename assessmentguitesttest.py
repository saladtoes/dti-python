import easygui
name = str(easygui.enterbox("What is your name?:"))
def contains_number(string): return any(char.isdigit() for char in string)
while contains_number(name): name = str(easygui.enterbox("Your name cannot contain a number \nWhat is your name?: "))
def agecheck():
    global age
    try: age = int(easygui.enterbox("Hello " + name + " how old are you?: "))
    except: agecheck()
    else: pass
agecheck()
if age > 14 or age < 8: easygui.msgbox("Youre either too old or too young to do this quiz\n You must be ages 8-13"); quit()
else: easygui.msgbox("Hello " + name + " Welcome to the Cybersmart start quiz")
info, questionnum, score, done, questionsprint, questionAnswers, answer, answers = [" A: Delete the message and try to forget about it\n", "B: Keep the text and show an adult you trust\n", "C: Text the person back and say something mean to them", " A: Tweet that they are an idiot and a loser\n", "B: Ask your friends to grive the person a hard time\n", "C: Tell and adult you trust\n", " A: Nickname\n", "B: Your name\n", "C: Your email address\n", " A: Your video is rubbish\n", "B: Man, this is awful! Stick to playing spport or something.\n", "C: Congrats on your first video! Let me know if you'd like any help editing for your next video\n", ' A: “We shouldn’t be mean to them just because they’re mean to us."\n', 'B: “Yeah, totally. They’re evil and deserve it!”\n', 'C: “Yes, I think that is a great idea. Maybe they will understand what it feels like, and stop bullying us!”\n', "Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?\n", "You find out that someone has posted an embarrassing picture of you online. What should you do?\n", "You want to join an online gaming site. Which of the following information is okay for you to post on the site.\n", "Someone in your class has posted their first video on YouTube and has asked you to comment on it. You don’t think the video is good because the editing is very choppy. What could you comment?\n", "Someone in your class is a real bully. Some of the other people in your class say: “Let’s get them back, and spam them with random texts.” What do you reply?\n", "a", "b", "c"], 0, 0, 0, "", "", 0, "a" + "b" + "c"
def questionsask():
    global score, questionrightcount, questionwrongcount, questionnum, questions, question5Answers, question4Answers, question3Answers, question2Answers, question1Answers, answers, questionsprint, questionAnswers, answer, done
    questionsprint, questionAnswers, answer, questionrightcount, questionwrongcount = "", "", 0, 0, 0
    if questionnum == 0: questionsprint, questionAnswers, answer = info[15], info[0] + info[1] + info[2], info[21]
    elif questionnum == 1: questionsprint, questionAnswers, answer = info[16], info[3] + info[4] + info[5], info[22]
    elif questionnum == 2: questionsprint, questionAnswers, answer = info[17], info[6] + info[7] + info[8], info[20]
    elif questionnum == 3: questionsprint, questionAnswers, answer = info[18], info[9] + info[10] + info[11], info[22]
    elif questionnum == 4: questionsprint, questionAnswers, answer = info[19], info[12] + info[13] + info[14], info[20]
    elif questionnum == 5: return
    def askquestion():
        global score, questionrightcount, questionwrongcount, questionnum, questions, question5Answers, question4Answers, question3Answers, question2Answers, question1Answers, answers, questionsprint, questionAnswers, answer, done
        while questionwrongcount != 3 or questionrightcount != 1:
            question = easygui.enterbox(questionsprint + questionAnswers + "\nAnswer now: ")
            if question.lower() == answer:
                if questionwrongcount == 0:
                    score += 1; pass
                easygui.msgbox("that is correct\n" + "Your score is now" + str(score) + "out of 5")
                questionrightcount += 1; pass
            elif contains_number(question) or question not in answers:
                easygui.msgbox("Invalid Input\n please enter only a, b, c")
                questionwrongcount += 1; pass
            elif question != answer: 
                easygui.msgbox("That was wrong") 
                questionwrongcount += 1; pass
            if questionwrongcount == 3 or questionrightcount == 1:
                questionnum += 1
                if questionnum == 5: easygui.msgbox(name + " Your Final score is " + str(score) + " out of 5"); quit()
                questionsask()
            else: askquestion()
    if questionnum != 5: askquestion()
    else: return
if done == 0: questionsask()
