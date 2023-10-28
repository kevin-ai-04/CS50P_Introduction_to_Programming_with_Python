import requests
import sys


def main():
    if len(sys.argv) == 2:
        try:
            num = float(sys.argv[1])
            amount = convert_to_Bitcoin(num)
            print(f"${amount:,.4f}")
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Invalid format")


def convert_to_Bitcoin(num):
    while True:
        try:
            response = requests.get(
                f"https://api.coindesk.com/v1/bpi/currentprice.json"
            )
            result = response.json()
            price = result["bpi"]["USD"]["rate_float"]
            amount = price * num
            break
        except requests.RequestException:
            pass
    return amount


if __name__ == "__main__":
    main()
