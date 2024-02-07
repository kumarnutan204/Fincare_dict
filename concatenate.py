
def Concatenate(dict1,dict2):
    return (dict2.update(dict1))
    

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

Concatenate(dict1,dict2)
print(dict2)

#Another way to do it 
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
     
dict3 = {'x': 11, 'y': 89}
dict4 = {'z': 90, 'k': 5}
dict5 = Merge(dict3, dict4)
print(dict5)


#Another way to do this 
#using union operation 
def Merge2(dict1, dict2):
    # union operator (|)
    merged_dict = dict(dict1.items() | dict2.items())
    return merged_dict
dict7 = {'a': 10, 'b': 8}
dict8 = {'d': 6, 'c': 4}
merged_dict = Merge2(dict7, dict8)
print(merged_dict)
