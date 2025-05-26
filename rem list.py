# Write your code here :-)
test_list = [1, 3, 4, 6, 7]

# Initializing remove list
remove_list = [3, 6]


# Removing elements present in other list
# using list comprehension
res = [i for i in test_list if i not in remove_list]

# Printing the result
print("The list after performing remove operation is : " + str(res))
