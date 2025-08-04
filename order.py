from datetime import datetime

from enum import Enum

class OrderType(Enum):
    FOK = "FOK"
    LIMIT = "LIMIT"
    MARKET = "MARKET"

class OrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"

class Order:
    order_id = 0
    print_format = "{:<10}\t\t{:<10}\t\t{:>10}\t\t{:>10}"

    def __init__(self, order_type, side, price, quantity, timestamp=None):
        self.order_type = order_type
        self.side = side
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp if timestamp else datetime.now()

        # increment order_id and assign it to the instance
        Order.order_id += 1
        self.order_id = Order.order_id



    def __str__(self):
        return self.print_format.format(
            self.order_id, self.order_type.name, self.side.name, self.quantity, self.price)

    def print(self):
        print(f"Order ID: {self.order_id}")
        print(f"Order Type: {self.order_type}")
        print(f"Order Side: {self.side}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Timestamp: {self.timestamp}")

