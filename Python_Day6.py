# ## Creatin empty list
# empty_list = list()
# print(empty_list)

# ## Creating another with2, 3, 4
# list_nums = list([2, 3, 4])
# print(list_nums)

## alternative
# list_num_2 = [5, 6, 7]
# print(list_num_2)

# user_name = "Moro"

# access the element within a list
#[] = index operator
# print(list_num_2[0])
# print(list_num_2[1])
# print(list_num_2[2])

#to easily get all elements in the list
# for each_item in list_nums:
#     print(each_item)

##accessing all items within a list
# for seq in range (0, 3):
#     print(list_nums[seq])

# for seq in range (0,len(list_nums)):
#     print(list_nums[seq])

# ##let's return the size
# print("...........")
# print(len(list_nums))

# ##create a new list
# house_items = ["car", 3, "dog", 2, "TV", "boys"]

# ##List slicing
# print(house_items[0:1])
# print(house_items[2:6])

# ##adding a new element to the list
# house_items.append("girls")
# print(house_items)

# ##extending a list
# house_items.extend(list_nums)
# print(house_items)

# ##Insert an item a specific index
# house_items.insert(0, "Pen")
# print(house_items)

# ##Removing an item
# house_items.remove("dog")
# print(house_items)

# ##Returning the index of an element within a list
# print(house_items.index("girls"))

# ## Creating an empty list
# fav_sports =[]

# ##ask the user their fav ports
# user_input =input("What is your favorite sports:")

# ##add that to the original list
# fav_sports.append(user_input)
# print(fav_sports)

# ##ask the user their favorite sports
# user_input =input("What team do you support in that sport:")
# fav_sports.append(user_input)
# print(fav_sports)


## Ways of creating a dic(), {} : Value
# dic(), {}
# My_dic = {    
#     "name": "John", "Age":25, "City": "New York"}

# class_records =  {
#                    1: {"Lydia Khris", "Class 6"},
#                    2: {"Blessing Khris", "Class 6"},
#                    3: {"Godwin Khris", "Class 6"}
#                    }
    

# print(My_dic["City"])

# ##Return all the keys in a dictionary
# print(class_records.keys())
# ##Return all the values in a dictionary
# print(class_records.values())

# print(class_records)

# ##Insert a new record in the dictionary
# class_records[1] = {"Shadrack", "Class 6"}
# print(class_records)

# var = class_records.keys()
# for each_item in var:
#     print(each_item)

#     var = class_records.keys()
# for each_item in var:
#     print(class_records[each_item])


    ##Create and empty class
class_reg =[]
reg_count = int(input("Enter the number of students to register:"))
## 25 participants
## Ask for the users fullname
for each_user in range(1,reg_count + 1):
    user_input = input("Enter your fullname:")
##Store the users name in the class register  
    class_reg.append(user_input)

  #Dislay thr class register
print(user_input)