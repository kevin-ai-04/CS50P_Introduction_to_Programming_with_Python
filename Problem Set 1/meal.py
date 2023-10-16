def main():
    time=input("What time is it? : ")
    time=convert(time)
    if 7<=time<=8:
        print("breakfast time")
    elif 12<=time<=13:
        print("lunch time")
    elif 18<=time<=19:
        print("dinner time")


def convert(time):
    time.strip()
    x,y=time.split(":")
    hour=float(x)
    min=float(y)
    min=min*(1/60)
    return (hour+min)


if __name__ == "__main__":
    main()