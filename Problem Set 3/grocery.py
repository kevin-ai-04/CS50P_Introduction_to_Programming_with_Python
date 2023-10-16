items={}

while True:
    try:
        key=input("").upper()
        if key in items:
            items[key]+=1
        else:
            items[key]=1
    except EOFError:
        break

keys=sorted(list(items.keys()))
for i in keys:
    print(items[i],i)