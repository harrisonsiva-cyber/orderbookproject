import order
from itertools import count

from order import orderType

def main():

    VALID_TYPES = {'FOK', 'LIMIT', 'MARKET'}
    VALID_SIDES = ['BUY', 'SELLl']

    BUY_ORDERS = {}
    SELL_ORDERS = []

    order_number = 1

    for i in count(0):
        side = str(input("Enter whether the order is a buy or sell: ")).upper()
        if side not in self.VALID_SIDES:  # Validating side
            raise ValueError(f"Invalid side: {side}. Must be one of {self.VALID_SIDES}")

        order_type = str(input("Enter whether the order is a FOK, LIMIT OR MARKET: ")).upper()
        if order_type not in self.VALID_TYPES:  # Validating order type
            raise ValueError(f"Invalid order type: {order_type}. Must be one of {self.VALID_TYPES}")

        price = float(input("Enter the total price of the order: £ "))
        if not isinstance(price, (int, float)) or price <= 0:  # Validating price
            raise ValueError("Price must be a positive integer or positive decimal")

        rounded_PRICE = round(price, 2)
        if not isinstance(rounded_PRICE, (int, float)) or rounded_PRICE <= 0:  # Validating rounded PRICE
            raise ValueError("Rounded Price must be a positive integer or positive decimal")

        quantity = int(input("Enter the number of shares: "))
        if not isinstance(quantity, (int, float)) or quantity <= 0: # Validating quantity
            raise ValueError("Quantity must be a positive number")

        x = input("Type Yes if you would like to carry on or Stop if you want to stop: ").upper()

        if x == 'STOP':
            print("BUY ORDERS: ")
            for order_number, order in BUY_ORDERS.items():
                print(f'{order_number}: {order}')
            print("\nSELL ORDERS: ")
            for order_number, order in SELL_ORDERS.items():
                print(f'{order_number}: {order}')
            break


# Only run the main function its is executed correctly.
if __name__ == "__main__":
    main()
