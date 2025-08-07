from itertools import count

class Order:
    # Class-level constants for valid order types and sides
    VALID_TYPES = {"FOK", "LIMIT", "MARKET"}
    VALID_SIDES = {"BUY", "SELL"}

    def __init__(self, order_type, side, price, rounded_PRICE, quantity):
        # Validating order type
        if order_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid order type: {order_type}. Must be one of {self.VALID_TYPES}")

        # Validating side
        if side not in self.VALID_SIDES:
            raise ValueError(f"Invalid side: {side}. Must be one of {self.VALID_SIDES}")

        # Validating price
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive integer or positive decimal")

        if not isinstance(rounded_PRICE, (int, float)) or rounded_PRICE <= 0:
            raise ValueError("Rounded Price must be a positive integer or positive decimal")

        # Validating quantity
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("Quantity must be a positive number")

        # Set instance attributes
        self.order_type = order_type
        self.side = side
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Order({self.order_type}, {self.side}, {self.price}, {self.quantity})"

class orderBook:
    # Creating a list for buying and selling
    BUY_ORDERS = {}
    SELL_ORDERS = {}
    order_number = 1

    for i in count(0):
        side = str(input("Enter whether the order is a buy or sell: ")).upper()
        order_type = str(input("Enter whether the order is a FOK, LIMIT OR MARKET: ")).upper()
        price = float(input("Enter the total price of the order: £ "))
        rounded_PRICE = round(price, 2)
        quantity = int(input("Enter the number of shares: "))
        x = input("Type Yes if you would like to carry on or Stop if you want to stop: ").upper()

        if side == 'BUY':
            BUY_ORDERS[order_number] = {
                'order_type': order_type,
                'side': side,
                'quantity': quantity,
                'price': rounded_PRICE,

            }
            order_number += 1
        elif side == 'SELL':
            SELL_ORDERS[order_number] = {
                'order_type': order_type,
                'side': side,
                'quantity': quantity,
                'price': rounded_PRICE,

            }
        order_number += 1
        if x == 'STOP':
            print(BUY_ORDERS)
            print(SELL_ORDERS)
            break

