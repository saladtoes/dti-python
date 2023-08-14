# name = input("What is your name? ")
# print("Hello, " + name)

# age = int(input("How old are you?"))

# def main():
#     while True:
#         again = input("Would you like to play? Enter y/n: ")

#         if again == "n":
#             print ("Thanks for Playing!")
#             return
#         elif again == "y":
#             print ("Lets play!")
#         else:
#             print ("You should enter either \"y\" or \"n\".")
#         return



# if age <= 7 and age >= 5:
#     score = 0
#     main()  
#     q1 = input("What is the capital of New Zealand? \n A. Auckland \n B. Wellington \n C. Christchurch \n D. Hamilton \n Answer in CAPS: ")
#     if q1 == "B":
#         print("Correct")
#         score +=1
#         pass
#     else: 
#         print("that is incorrect")
#         if score <= 0:
#             pass
#         else:
#             score -=1 
#         pass
#     q2 = input('Which city is known as "The Garden City"? \n A. Wellington \n B. Christchurch \n C. Paeroa \n D. Auckland \n Answer in CAPS: ')
#     if q2 == "B":
#         print("Correct")
#         score +=1
#         pass
#     else:
#         print("that is incorrect")
#         if score <= 0:
#             pass
#         else:
#             score -=1
#         pass
#     q3 = input("Where did L&P soda originally come from? \n A. Putaruru \n B. Waihi \n C. Paeroa \n D. Auckland \n Answer in CAPS: ")
#     if q3 == "C":
#         print("Correct")
#         score +=1
#         pass
#     else: 
#         print("that is incorrect")
#         if score <= 0:
#             pass
#         else:
#             score -=1
#         pass
#     q4 = input("In what month is Matariki celebrated? \n A. April \n B. May \n C. June \n D. July \n Answer in CAPS: ")
#     if q4 == "C":
#         print("Correct")
#         score +=1
#         pass
#     else: 
#         print("that is incorrect")
#         if score <= 0:
#             pass
#         else:
#             score -=1
#         pass
#     q5 = input("Final question \n What colour is Kakariki? \n A. Green \n B. Blue \n C. Black \n D. Grey \n Answer in CAPS: ")
#     if q5 == "A":
#         print("Correct")
#         score +=1
#         pass
#     else:
#         print("That is incorrect")
#         if score <= 0:
#             pass
#         else: 
#             score -=1
#         pass
#     print("You have finished this quiz with a score of", score, "out of 5")
    


# else: 
#     if age >= 7 and age <= 11:
#         score = 0
#         main()
#         q1 = input("What is the name of the stretch of water that separates the North and South Islands? \n A. Wellington Strait \n B. Tasman Channel \n C. Cook Strait \n D. Kaikoura Strait \n Answer in CAPS: ")
#         if q1 == "C":
#             print("Correct")
#             score +=1
#             pass
#         else:
#             print("that is incorrect")
#             if score <= 0:
#                 pass
#             else:
#                 score -=1
#             pass
#         q2 = input("Which New Zealand city houses the Beehive? \n A. Wellington  \n B. Christchurch \n C. Paeroa \n D. Auckland \n Answer in CAPS:")
#         if q2 == "A":
#             print("Correct")
#             score +=1 
#             pass
#         else:
#             print("That is incorrect")
#             if score <= 0:
#                 pass
#             else:
#                 score -=1
#             pass
#         q3 = input("Which town has a giant carrot as a landmark? \n A. Taihape \n B. Waihi \n C. Paeroa \n D. Ohakune \n Answer in CAPS:" )
#         if q3 == "D":
#             print("Correct")
#             score +=1
#             pass
#         else:
#             print("That is incorrect")
#             if score <= 0:
#                 pass
#             else:
#                 score -=1
#             pass
#         q4 = input("Where is 90 mile beach? \n A. Top of the North Island \n B. Bottom of the south island \n C. Bottom of the North Island \n D. Top of the South Island \n Answer in caps: ")
#         if q4 == "A":
#             print("Correct")
#             score +=1
#             pass
#         else:
#             print("That is incorrect")
#             if score <= 0:
#                 pass
#             else:
#                 score -=1
#             pass
#         q5 = input("When was the Treaty of Waitangi signed? \n A. 1815 \n B. 1840 \n C. 1855 \n D. 1875 \n Answer in CAPS: ")
#         if q5 == "B":
#             print("Correct")
#             score +=1
#             pass
#         else:
#             print("That is incorrect")
#             if score <= 0:
#                 pass
#             else:
#                 score -=1
#             pass
#         print("You have finished the quiz with a score of", score, "out of 5")

import easygui

ages = ["7 or Younger", "8 or older"]
easygui.buttonbox(title="age", msg="How old are you?", choices=ages)
