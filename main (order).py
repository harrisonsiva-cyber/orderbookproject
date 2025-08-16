from itertools import count


class order_book:

    # Class-level constants for valid order types and sides
    VALID_TYPES = {"FOK", "LIMIT", "MARKET"}
    VALID_SIDES = {"BUY", "SELL"}

    BUY_ORDERS = {}
    SELL_ORDERS = {}

    order_number = 0
    print_format = "{:<10}\t{:<10}\t{:>10}\t{:>10}\t{:>10}"

    def __init__(self, order_type, side, price, quantity, timestamp=None):
        self.order_type = order_type
        self.side = side
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp if timestamp else datetime.now()

    def __str__(self):
        return self.print_format.format(
          self.order_type.name, self.side.name, self.quantity, self.price)

    def print(self):
        print(f"Order Type: {self.order_type}")
        print(f"Order Side: {self.side}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Timestamp: {self.timestamp}")


    for i in count(0):
        side = str(input("Enter whether the order is a buy or sell: ")).upper()
        if side not in self.VALID_SIDES:  # Validating side
            raise ValueError(f"Invalid side: {side}. Must be one of {self.VALID_SIDES}")

        order_type = str(input("Enter whether the order is a FOK, LIMIT OR MARKET: ")).upper()
        if order_type not in self.VALID_TYPES:  # Validating order type
            raise ValueError(f"Invalid order type: {order_type}. Must be one of {self.VALID_TYPES}")

        intial_price = float(input("Enter the total price of the order: £ "))
        price = round(intial_price, 2)
        if not isinstance(price, (int, float)) or price <= 0:  # Validating price
            raise ValueError("Price must be a positive integer or positive decimal")

        quantity = int(input("Enter the number of shares: "))
        if not isinstance(quantity, (int, float)) or quantity <= 0:  # Validating quantity
            raise ValueError("Quantity must be a positive number")

        x = input("Type Yes if you would like to carry on or Stop if you want to stop: ").upper()

        if side == 'BUY':
            BUY_ORDERS[order_number] = {
                'order_type': order_type,
                'side': side,
                'quantity': quantity,
                'price': price,

             }
            order_number += 1
        elif side == 'SELL':
            SELL_ORDERS[order_number] = {
                'order_type': order_type,
                'side': side,
                'quantity': quantity,
                'price': price,

            }
        order_number += 1
        if x == 'STOP':
            break


print("\nBUY ORDERS: ")
for order_number, order in BUY_ORDERS.items():
    print(f'{order_number}: {order}')
print("\nSELL ORDERS: ")
for order_number, order in SELL_ORDERS.items():
    print(f'{order_number}: {order}')
