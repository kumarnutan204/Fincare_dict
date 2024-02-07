my_dict={'Hello': 'World', 'a': 10, 'name':'Rahul', 'class': 'B'}
print(my_dict)
delKey=input("Enter a valid key to delete")

del my_dict[delKey]
print(f"New updated dict is : {my_dict} ")
