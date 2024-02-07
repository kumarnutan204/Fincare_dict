st= input("Enter the string to count characters")

d= dict()
for ch in st:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
print(d)
