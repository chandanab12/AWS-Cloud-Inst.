# # # # farm_animals = {"cow", "chicken", "sheep", "pig"}
# # # # print(farm_animals)

# # # # new_set = { }

# # # # print(new_set)

# # # # converted_set = set([1,2,3,4])

# # # # print(converted_set)


# # # list = [1,2,4,4,6,7,8,8,4]

# # # new_set = set(list)

# # # print(new_set)

# # ratings = {1, 2, 3, 4, 5}

# # print (5 in ratings)

# wild_animals = {"pig", "lion", "koala", "kangaroo"}
# farm_animals = {"cow", "chicken", "sheep", "pig"}
# australian_animals = {"koala", "kangaroo"}

# print (farm_animals.isdisjoint(australian_animals))
# print (wild_animals.isdisjoint(australian_animals))

# print(australian_animals.isdisjoint(farm_animals))


wild_animals = {"pig", "lion", "koala", "kangaroo"}
farm_animals = {"cow", "chicken", "sheep", "pig"}
australian_animals = {"koala", "kangaroo"}

print (australian_animals.issuperset(wild_animals))
print (wild_animals.issuperset(australian_animals))
