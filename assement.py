from tkinter import scrolledtext


name = input("What is your name?: ")
age = int(input("Hello " + name + " how old are you?: "))
    
if age <= 7:
    print("youre too young to do this quiz")
    
elif age >= 14:
    print("Your above the recommended age for this quiz.\nPlease try the Cybersmarth Youth quiz instead")
    pass
else:
    print("Hello", name, "Welcome to the Cybersmart start quiz")
    answers = ["a", "b", "c", "A", "B", "C"]
    question1Answers = [" A: Delete the message and try to forget about it\n", "B: Keep the text and show an adult you trust\n", "C: Text the person back and say something mean to them"]
    question2Answers = [" A: Tweet that they are an idiot and a loser\n", "B: Ask your friends to grive the person a hard time\n", "C: Tell and adult you trust\n"]
    question3Answers = [" A: Nickname\n", "B: Your name\n", "C: Your email address\n"]
    question4Answers = [" A: Your video is rubbish\n", "B: Man, this is awful! Stick to playing spport or something.\n", "C: Congrats on your first video! Let me know if you'd like any help editing for your next video\n"]
    question5Answers = [' A: “We shouldn’t be mean to them just because they’re mean to us."\n', 'B: “Yeah, totally. They’re evil and deserve it!”\n', 'C: “Yes, I think that is a great idea. Maybe they will understand what it feels like, and stop bullying us!”\n']
    questions = ["Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?\n", "You find out that someone has posted an embarrassing picture of you online. What should you do?", "You want to join an online gaming site. Which of the following information is okay for you to post on the site.", "Someone in your class has posted their first video on YouTube and has asked you to comment on it. You don’t think the video is good because the editing is very choppy. What could you comment?", "Someone in your class is a real bully. Some of the other people in your class say: “Let’s get them back, and spam them with random texts.” What do you reply?"]
    score = 0
    print(questions[0])
    print(question1Answers[0], question1Answers[1], question1Answers[2])
    q1 = input("Answer Now: ")
    if q1 == answers[1] or answers[3]:
        print("that is correct\n")
        score += 1
        pass
    else:
        score -+ 1
        pass
    print(questions[1])
    print(question2Answers[0], question2Answers[1], question2Answers[2])
    q2 = input("Answer now:")
    if q2 == answers[2] or answers[4]:
        print("that is correct\n")
        score += 1
        pass    
    print(questions[2])
    print(question3Answers[0], question3Answers[1], question3Answers[2])
    q3 = input("Answer now:")
    if q3 == answers[0] or answers[3]:
        print("that is correct\n")
        score += 1
        pass    
    print(questions[3])
    print(question4Answers[0], question4Answers[1], question4Answers[2])
    q4 = input("Answer now:")
    if q4 == answers[2] or answers[4]:
        print("that is correct\n")
        score += 1
        pass    
    print(questions[4])
    print(question5Answers[0], question5Answers[1], question5Answers[2])
    q5 = input("Answer now:")
    if q5 == answers[0] or answers[3]:
        print("that is correct\n")
        score += 1
        pass    
    
    print("your got", score, "out of 5")