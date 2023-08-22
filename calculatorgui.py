import easygui

num1 = int(easygui.enterbox("First number"))
operand = easygui.enterbox("Enter operator \n" + "+, -, /, *\n")
num2 = int(easygui.enterbox("Second number"))

answerplus = num1 + num2
answerplus = str(answerplus)
answerminus = num1 - num2
answerminus = str(answerminus)
answertimes = num1 * num2
answertimes = str(answertimes)
answerdivide = num1 / num2
answerdivide = str(answerdivide)
if operand == "+":
    easygui.msgbox("The answer is" + answerplus)
elif operand == "-":
    easygui.msgbox("The answer is" + answerminus)
elif operand == "/":
    easygui.msgbox("The answer is " + answerdivide)
elif operand == "*":
    easygui.msgbox("The answer is " + answertimes)
