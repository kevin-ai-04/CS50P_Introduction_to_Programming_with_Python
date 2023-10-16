text=input("Greeting: ")
text=text.strip().lower()


if text.startswith("hello"):
    money=0
elif text.startswith("h"):
    money=20
else:
    money=100

print ("$",money,sep='')