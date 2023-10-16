def main():
    x=getfuel()
    if x<=1:
        print("E")
    elif x>=99:
        print("F")
    else:
        print(x,"%",sep='')

def getfuel():
    while True:
        try:
            fraction=input("Fraction: ")
            a,b=fraction.split("/")
            if int(a)>int(b):
                continue
            else:
                percentage=(( int(a) / int(b) )*100)
                break
        except (ValueError,ZeroDivisionError):
            pass
    return round(percentage)

main()
