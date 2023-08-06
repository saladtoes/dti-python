import easygui

number1 = easygui.enterbox("What is your first number? ")
operand = easygui.buttonbox(choices=["+","-","/","*"])
number2 = easygui.enterbox("What is your second number? ")

easygui.msgbox("answer = ", number1, operand, number2)
