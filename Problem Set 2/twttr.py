text=input("Input: ")
vowels=['a','e','i','o','u']
print("Output: ",end='')
for i in text:
    if i.lower() not in vowels:
        print(i,end='')