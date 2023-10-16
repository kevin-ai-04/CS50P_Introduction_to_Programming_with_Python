def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    check=True
    count=len(s)

    if count<2 or count>6: #LengthCheck
        check=False
    else:
        for i in s:
            if i.isalpha()==False and i.isdigit()==False: #Symbol/Space Check
                check=False
                break
        if s[0].isalpha()==False or s[1].isalpha()==False: #First two characters check
            check=False
        else:
            if s.isalpha()==False: #If Plate isn't entirely alphabets (for NRVOUS)
                if s[count-1].isdigit()==False: #Ending with digit check
                    check=False
                else:
                    for i in range (0,count): #Checking if an alphabet is in between numbers
                        if s[i].isdigit()==True:
                            start=i
                            break
                    for i in range (start,count):
                        if s[i].isdigit()==False:
                            check=False

                    for i in s: #If First Digit is 0 check
                        if i.isdigit()==True:
                            break
                    if i=='0':
                        check=False

    return check

main()