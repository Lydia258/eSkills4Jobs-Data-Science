## ask for two numbers. If the first one is larger than the second, 
## display the second number
## first and then the first number
## otherwise show first number first and then the second
## asking for two inputs and converting them to interger

# number1 = int(input("Enter first number:"))
# number2 = int(input("Enter second number:"))

# if(number1 > number2):
#     print(number2, number1)

# else: 
#     print(number1, number2)

## ask the user to enter a number that is under 20.
## if they enter a number that is 20 or more
## display the the message "Too High" otherwise "Thank you"

#number = int(input("Enter number < 20"))
#if(number < 20):
 #   print("Thank you")
#else:
 #   print( "Too High")

 #Ask the user to enter an number between 10 and 20 (inclusive)
 #If they enter a within
 #Display the message "Thank you"
 #Otherwise display the message "Incorrect Answer"

 #user_input = int(input("Enter a number b/n 10 and 20"))
#if((user_input >= 10)) and (user_input <= 20):
    #print("Thank you")
#else:
    #print("Incorrect Answer")

# user_input= input("Enter your favourite colour")
# if((user_input == "red") or (user_input == "RED") or (user_input == "Red")):
#     print("I like red too")
# else:
#     print("I don't like the color")

 #Question 19
# print("Enter 1 or 2 or 3")
# user_input = int(input("Enter the number of your choice:"))
# if(user_input == 1):
#     print("Thank you")
# elif(user_input == 2):
#     print("Well done")
# elif(user_input == 3):
#     print("Correct")
# else: 
#     print("Error messgae")

#Day 3 python

# ## generate seq of numbers b/n 1 and 11
# for each_number in range(1, 11):
#     print("Each Number: <= ", each_number)

# ## generate seq of numbers b/n 1 and 10 (inclusive)
# for each_number in range(2, 11, 2):
#     print("Each Number: <= ", each_number)

#     ## generate seq of numbers b/n 1 and 11
# for each_number in range(10, 1, -1):
#     print("Each Number: <= ", each_number)

# #groups_of items
# class_reg = ['lydia' ,'Mick', 'Teiwe', 'Sarah']
# for each_item in class_reg:
#     print(each_item)

# user_name = input("Enter your name: ")
# for each_name in range(1, 5):
#     print("Your name is:", user_name)

# user_name = input("Enter your name:")
# number = int (input("Enter number:"))
# for each_name  in range(number):
#     print(user_name)


# user_name = input("Enter your name:")
# number = int (input("Enter number:"))
# for each_name  in range(1, number, +1):
#     print(user_name)


user_name = input("Enter your name")
number = int(input("Enter number:" ))
if(number < 10):
    for each_name in range(1, number, +1):
    print(user_name)
else:
    for each_message in range(1, 4)
    print("Too High")
