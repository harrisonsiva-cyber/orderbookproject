from enum import Enum

class OrderType(Enum):
    FOK = "FOK"
    LIMIT = "LIMIT"
    MARKET = "MARKET"

class OrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"

class Order:
    print_format = "{:<5}\t{:<5}\t{:>10}\t{:>10}\t{:>10}"

    def __init__(self, order_number, order_type, side, price, quantity):
        self.order_number = order_number
        self.order_type = order_type
        self.side = side
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return self.print_format.format(
         self.order_number, self.order_type.name, self.side.name, self.price, self.quantity)

    def print(self):
        print(f"Order Number: {self.order_number}")
        print(f"Order Type: {self.order_type}")
        print(f"Order Side: {self.side}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")


