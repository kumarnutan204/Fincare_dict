stud = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

count=0
for item in stud:
    if (item['success'])==True:
       count+=1 

print(f"The number true success are: {count}")
