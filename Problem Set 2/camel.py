text=input("Enter Variable Name in camelCase: ")
for i in text:
    if i.islower():
        print(i,end='')
    else:
        print("_",i.lower(),sep='',end='')