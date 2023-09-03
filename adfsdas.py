def contains_number(asdgsdfg):
    return any(char.isdigit() for char in asdgsdfg)
# running funtion to see if name has answers if there are it asks again
name = str(input("What is your name?: "))





while contains_number(name):
    print("Your name can not contain a number")
    name = str(input("What is your name?: "))
    