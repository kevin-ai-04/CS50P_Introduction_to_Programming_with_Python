exp=input("Enter an Expression: ")

x,y,z=exp.split(" ")
x=float(x)
z=float(z)

if y == "+":
    result=x+z
elif y=="-":
    result=x-z
elif y=="*" or y.lower()=="x":
    result=x*z
elif y=="/":
    result=x/z
else:
    print("Invalid Input")

print(result)