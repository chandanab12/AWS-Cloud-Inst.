# # # # # # # # # # test_scores = [45,53,62,73,45]
# # # # # # # # # # print(len(test_scores))

# # # # # # # # # my_list = ["first", "second", "third", "fourth"]

# # # # # # # # # # print single element using the positive index
# # # # # # # # # print(my_list[0])

# # # # # # # # # # print single element using the negative index
# # # # # # # # # print(my_list[-1])

# # # # # # # # # # print range of values using the slice operator
# # # # # # # # # print(my_list[1:3])

# # # # # # # # """
# # # # # # # # Challenge
# # # # # # # # """ 

# # # # # # # # num_list = [68, 64, 88, 54, 17, 28, 35, 76, 68, 8, 27, 
# # # # # # # #     50, 53, 39, 5, 43, 58, 33, 38, 30, 76, 38, 22, 60,
# # # # # # # #     79, 23, 39, 5, 22, 66, 37, 49, 5, 66, 32, 89, 46, 
# # # # # # # #     82, 80, 84, 14, 22, 46, 100, 72, 22, 51, 83, 47]

# # # # # # # # ## Use the len() function to find the positive index 
# # # # # # # # ## associated with the last number on this list. 

# # # # # # # # print(len(num_list))
# # # # # # # # print(num_list[48])


# # # # # # # # initializes colors list
# # # # # # # colors = ["orange", "yellow", "green", "blue"]

# # # # # # # # adds purple to the end of the colors list
# # # # # # # colors.append("purple")

# # # # # # # # inserts red at the beginning of the colors list
# # # # # # # colors.insert(0, "red")

# # # # # # # more_colors = ["indigo", "pink"]

# # # # # # # #colors.extend(more_colors) # adds list to an existing list 

# # # # # # # colors += more_colors

# # # # # # # print(colors)


# # # # # # pets = ["dog", "cat", "hamster", "iguana", "goldfish"]

# # # # # # # pop last element
# # # # # # lost_pet = pets.pop()
# # # # # # print ("pets after pop() is:", pets)
# # # # # # print ("lost_pet is:", lost_pet)

# # # # # # # pop specific element
# # # # # # lost_pet = pets.pop(3)
# # # # # # print ("pets after pop(0) is:", pets)
# # # # # # print ("lost_pet is:", lost_pet)

# # # # # pets = ["dog", "cat", "hamster", "iguana", "goldfish"]

# # # # # # remove
# # # # # pets.remove("hamster")
# # # # # print ("pets after remove('hamster') is", pets)

# # # # # pets.remove(pets[3])
# # # # # print ("pets after remove(pets[3]) is", pets)

# # # # # # clear
# # # # # pets.clear()
# # # # # print("pets after clear() is", pets)


# # # # orig_list = [1, 2, 3, 4, 5]

# # # # copied_list = orig_list.copy()

# # # # orig_list.append(12)

# # # # print(orig_list)
# # # # print(copied_list)

# # # # new_list = orig_list[:]
# # # # print(new_list)

# # # # new_name = orig_list # assignment operator

# # # # print(new_name)


# # # new_list = list((1, 2, 3))  # converts a tuple to a list

# # # empty_list = list() # creates a new  empty list

# # # orig_list = [1, 2, 3]  
# # # copied_list = list(orig_list)  # creates a copy of the existing list

# # # print(new_list, empty_list, copied_list)


# # # sort alphanumeric string
# # my_list = ["car", "boat", "truck", "fish", "far"]
# # my_list.sort()
# # print("Mixed case alphanumeric sort:", my_list)

# # # sort with optional reverse argument
# # # my_list.sort(reverse=True)
# # # print("Sort with optional reverse argument:", my_list)


# # # # sort using reverse method
# # # groceries = ["apples", "berries", "cabbage"]
# # # groceries.reverse()
# # # print("groceries after reverse()", groceries)


# rainfall = [2, 3, 5, 4, 4, 3, 1, 1, 2, 4, 3]
# print (rainfall.count(6))  # returns the number of times 4 occurs on this list. 

# rainfall = [2, 3, 5, 4, 4, 3, 1, 1, 2, 4, 3]

# print (2 in rainfall)
# print (2 not in rainfall)


grocery_list = [  ]

add_items = True
    
while add_items:   

    item = input("Enter an item to add to the grocery list:")


    grocery_list.append(item)
    
    end_list = input("Do you wanna add any more items? (y/n):")

    if end_list.lower() == 'n':
        add_items = False
        
grocery_list.sort()

print(grocery_list)

