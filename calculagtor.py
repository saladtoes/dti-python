import easygui

testtype = easygui.enterbox("What type of test is this?: ")
outOf = easygui.integerbox("How many marks was the " + testtype + " out of?: ")
marksgotten = easygui.integerbox("How mant marks did you get?: ")
percent = (marksgotten/outOf)*100
easygui.integerbox("Your percentage for the " + testtype + "test is" + percent )

