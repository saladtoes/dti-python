import easygui
testtype = easygui.enterbox("What type of test is this?: ")
totalmarks = easygui.integerbox("How many marks was the " + testtype + " test out of?: ")
marksgotten = easygui.integerbox("How many marks did you get?: ")
percentage = str(round((marksgotten/totalmarks)*100))
easygui.msgbox("Your percentage for the " + testtype + " test is " + percentage + "%" )
