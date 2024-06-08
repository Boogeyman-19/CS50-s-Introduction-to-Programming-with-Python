import sys
import requests

def main():



    try:
        if len(sys.argv) != 2:
            sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Argument must be a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        print(data)
        rate = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error: Unable to fetch Bitcoin price")

    cost = bitcoins * rate
    print(f"${cost:,.4f}")

if __name__ == "__main__":
    main()
