import sys
import requests

coindesk_api = "https://api.coindesk.com/v1/bpi/currentprice.json"


def main():
    """Let the user ask the price of Bitcoin using sys.argv"""
    print(f"${coindesk(input_logic()):,.4f}")


def input_logic():
    """Check  that the user respects our rules for argv input"""
    try:

        if len(sys.argv) < 2:
            print("Missing command-line argument")
            sys.exit(1)
        elif not float(sys.argv[1]):
            print("Command-line argument is not a number")
            sys.exit(1)
        else:
            return float(sys.argv[1])

    # If the argument is anything but a floatable number, let the user know
    except (TypeError, ValueError):
        print("Command-line argument is not a number")
        sys.exit(1)


def coindesk(amount):
    """Sends a get requests to the Coindesk API and return
    the value for the requested amount of Bitcoin"""
    try:
        response = requests.get(coindesk_api)
        data = response.json()
        value = data["bpi"]["USD"]["rate_float"]
        amountvalue = amount * value

    # Let the user know when a request to the API cannot be made
    except requests.RequestException:
        print("Coinbase not available. Please try again in a few minutes.")
        sys.exit()

    return amountvalue


if __name__ == "__main__":
    main()
