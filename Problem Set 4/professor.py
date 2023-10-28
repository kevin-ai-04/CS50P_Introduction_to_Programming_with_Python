import random


def main():
    level = get_level()
    count = 0
    score = 0

    while count < 10:
        try_count = 1
        x = generate_integer(level)
        y = generate_integer(level)
        ans = x + y
        while try_count <= 3:
            print(x, "+", y, "= ", end="")
            try:
                user_input = int(input(""))
                if user_input == ans:
                    score += 1
                    break
                else:
                    print("EEE")
                    try_count += 1
            except:
                print("EEE")
                try_count += 1
                pass
        if try_count == 4:
            print(x, "+", y, "=", ans)
        count += 1

    print("Score:", score)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n < 1 or n > 3:
                raise ValueError
            else:
                break
        except:
            pass
    return n


def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(10, 99)
    else:
        n = random.randint(100, 999)
    return n


if __name__ == "__main__":
    main()
