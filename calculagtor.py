import easygui
testtype = easygui.enterbox("What type of test is this?: ")
outOf = easygui.integerbox("How many marks was the " + testtype + " test out of?: ")
marksgotten = easygui.integerbox("How mant marks did you get?: ")
percent = str(round((marksgotten/outOf)*100))
easygui.msgbox("Your percentage for the " + testtype + "test is " + percent + "%" )