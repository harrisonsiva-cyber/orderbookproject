from datetime import datetime
from collections import namedtuple
from itertools import count

class Order:
    # Class-level constants for valid order types and sides
    VALID_TYPES = {"FOK", "LIMIT", "MARKET"}
    VALID_SIDES = {"BUY", "SELL"}

    def __init__(self, order_type, side, price, quantity, timestamp=None):
        # Validating order type
        if order_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid order type: {order_type}. Must be one of {self.VALID_TYPES}")

        # Validating side
        if side not in self.VALID_SIDES:
            raise ValueError(f"Invalid side: {side}. Must be one of {self.VALID_SIDES}")

        # Validating price
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")

        # Validating quantity
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("Quantity must be a positive number")

        # Validating timestamp
        if timestamp == False:
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

BUY = namedtuple('Order', ['order_number' ,'order_type', 'rounded_price', 'quantity', 'timestamp'])
SELL = namedtuple('Order',['order_number','order_type', 'rounded_price', 'quantity', 'timestamp'])
order_number = 0
for i in count(0):
    price = float(input("Enter the total price of the order: £ "))
    quantity = int(input("Enter the number of shares: "))
    timestamp = datetime.now()
    side = str(input("Enter whether the order is a buy or sell: ")).upper()
    order_type = str(input("Enter whether the order is a FOK, LIMIT OR MARKET: ")).upper()
    rounded_PRICE = round(price, 2)
    x = input("Type Yes if you would like to carry on or Stop if you want to stop: ").upper()
    if x == 'STOP':
        break
    else:
        order_number += 1
    if side == 'BUY':
        list_1 = list(BUY)
        list_1.append('order_number','order_type', 'rounded_price', 'quantity', 'timestamp')
        BUY = tuple(list_1)
        print(BUY)
    elif side == 'SELL':
        list_2 = list(SELL)
        list_2.append('order_number','order_type', 'rounded_price', 'quantity', 'timestamp')
        SELL = tuple(list_2)
        print(SELL)
    print(f'Your order number is {order_number}')
    print(timestamp)
 # Create a order book class
 # Use dictionaries
