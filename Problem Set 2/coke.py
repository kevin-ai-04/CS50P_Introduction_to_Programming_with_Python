amount_due=50
amount_in=0
while True:
    print("Amount Due:",amount_due)
    coin=int(input("Insert coin: "))
    if coin==25 or coin==10 or coin==5:
        amount_due-=coin
        amount_in+=coin
    if amount_due<=0:
        change=0-amount_due
        break
print("Change Owed:",change)


