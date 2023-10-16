Months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

while True:
    try:
        date=input("Date: ")
        if "/" in date:
            month,day,year=date.split("/")
        else:
            temp, year=date.split(", ")
            month_name,day=temp.split(" ")
            month=Months.index(month_name)+1
        if int(month)>12 or int(month)<0 or int(day)>31:
            raise ValueError
        print(f"{int(year)}-{int(month):02}-{int(day):02}")
        break
    except ValueError:
        pass
    except EOFError:
        break