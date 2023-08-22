import easygui

num1 = int(input("First number"))
operand = input("Enter operator \n" + "+, -, /, *\n")
num2 = int(input("Second number"))

answerplus = num1 + num2
answerplus = str(answerplus)
answerminus = num1 - num2
answerminus = str(answerminus)
answertimes = num1 * num2
answertimes = str(answertimes)
answerdivide = num1 / num2
answerdivide = str(answerdivide)
if operand == "+":
    print("The answer is" + answerplus)
elif operand == "-":
    print("The answer is" + answerminus)
elif operand == "/":
    print("The answer is " + answerdivide)
elif operand == "*":
    print("The answer is " + answertimes)
