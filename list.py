my_list = []
#Append the following elements to my_list
my_list.extend([10,20,30,40])
#Insert the value 15 at the second position in the list
my_list.insert(1,15)
my_list.extend([50,60,70])
print("The extended array is: ", my_list)
my_list.pop()
my_list.sort()
print("The final array:", my_list)
index = my_list.index(30)
print("The index of value 30 is:", index)

