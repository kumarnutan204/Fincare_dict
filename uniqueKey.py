my_dict={'a':1,'b':45,'a':54,'c':34,'d':84,'g':33,'a':23}

s= set()

for item in my_dict:
    s.add(item)

print(s)
if(len(my_dict)!=len(s)):
    print("Multiple keys exists")

    
