import random

while True:
    try:
        n = int(input("Level: "))
        if n < 1:
            raise EOFError
        elif n > 100:
            raise EOFError
        else:
            break
    except:
        pass

ans = random.randrange(0, n)
while True:
    try:
        num = int(input("Guess: "))
        if num <= 0 or num > 100:
            raise EOFError
        elif num > ans:
            print("Too large!")
        elif num < ans:
            print("Too small!")
        else:
            print("Just right!")
            break
    except:
        pass
