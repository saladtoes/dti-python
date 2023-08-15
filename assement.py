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
    answers = ["a", "b", "c"]
    questions = ["Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?", "You find out that someone has posted an embarrassing picture of you online. What should you do?", "You want to join an online gaming site. Which of the following information is okay for you to post on the site.", "Someone in your class has posted their first video on YouTube and has asked you to comment on it. You don’t think the video is good because the editing is very choppy. What could you comment?", "Someone in your class is a real bully. Some of the other people in your class say: “Let’s get them back, and spam them with random texts.” What do you reply?"]
    score = 0
    q1 = input(questions[2])
    if q1 == answers[1]:
        print("that is correct")
        score += 1
        pass
    q2 = input("question1")
    if q2 == answers[2]:
        print("that is correct")
        score += 1
        pass    
    q3 = input(questions[2])
    if q3 == answers[0]:
        print("that is correct")
        score += 1
        pass    
    q4 = input("question1")
    if q4 == answers[2]:
        print("that is correct")
        score += 1
        pass    
    q5 = input("question1")
    if q5 == answers[0]:
        print("that is correct")
        score += 1
        pass    
    
    if score == 5:
        print("it worked")