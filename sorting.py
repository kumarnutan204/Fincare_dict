my_dict={1:4,4:2,5:7,9:6,3:9}
print("Sorting dictionary by values: ")
sorted_dict= sorted(my_dict.items(), key= lambda kv: kv[1])

rev_sorted= sorted(my_dict.items(), key= lambda kv: kv[1],reverse=True)
print(sorted_dict)
print(rev_sorted)

print("Sorting by keys now:")
sorted_dict2= dict(sorted(my_dict.items()))
sorted_dict3= dict(sorted(my_dict.items()),reverse=True)
print(sorted_dict2)
print(sorted_dict3)
