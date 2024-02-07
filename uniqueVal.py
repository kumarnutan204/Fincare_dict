my_dict=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

#here creating a set to get all unique values from the dictionary 
u= set()

for i in my_dict: #for each key value pair i
    for val in i.values(): #for each
        u.add(val)

print(u)
