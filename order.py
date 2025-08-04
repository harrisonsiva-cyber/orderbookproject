from datetime import datetime
from itertools import count

class Order:
    # Class-level constants for valid order types and sides
    VALID_TYPES = {"FOK", "LIMIT", "MARKET"}
    VALID_SIDES = {"BUY", "SELL"}

    def __init__(self, order_type, side, price, rounded_PRICE, quantity, timestamp=None):
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

        # Validating timestamp
        if timestamp is None:
            timestamp = datetime.now()
        elif not isinstance(timestamp, datetime):
            raise ValueError("Timestamp must be a datetime object")

        # Set instance attributes
        self.order_type = order_type
        self.side = side
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp

    def __str__(self):
        return f"Order({self.order_type}, {self.side}, {self.price}, {self.quantity}, {self.timestamp})"

class orderBook:
    # Creating a list for buying and selling
    BUY_QUEUE = {}
    SELL_QUEUE = {}
    order_number = 1

    for i in count(0):
        side = str(input("Enter whether the order is a buy or sell: ")).upper()
        order_type = str(input("Enter whether the order is a FOK, LIMIT OR MARKET: ")).upper()
        price = float(input("Enter the total price of the order: £ "))
        rounded_PRICE = round(price, 2)
        quantity = int(input("Enter the number of shares: "))
        timestamp = datetime.now()
        x = input("Type Yes if you would like to carry on or Stop if you want to stop: ").upper()

        if side == 'BUY':
            BUY_QUEUE = {order_number, order_type, rounded_PRICE, quantity, timestamp}
            order_number += 1
        elif side == 'SELL':
            SELL_QUEUE = {order_number, order_type, rounded_PRICE, quantity, timestamp}
            order_number += 1
        if x == 'STOP':
            print(BUY_QUEUE)
            print(SELL_QUEUE)
            break
        else:
            order_number += 1

