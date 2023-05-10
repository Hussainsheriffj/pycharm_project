my_list = ["jan", "feb", "mar"]
print(my_list[-1])
my_list.append("apr")
print(my_list)
print(my_list[-1])
my_list.remove("apr")
print(my_list)


# if the same item in two times, remove will remove the first item in the list
my_list.append("jan")
print(my_list)
my_list.remove("jan")
print(my_list)