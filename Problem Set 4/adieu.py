Names = []

while True:
    try:
        name = input("Name: ")
    except EOFError:
        print()
        break
    Names.append(name)

count = len(Names)
print("Adieu, adieu, to", end=" ")
for i in range(0, count):
    print(Names[i], end="")
    if i != count - 2 and count > 1:
        print(", ", end="")
    elif i == count - 2 and count > 1:
        if count == 2:
            print(" and ", end="")
        else:
            print(", and ", end="")
        print(Names[i + 1])
        break
    else:
        break
