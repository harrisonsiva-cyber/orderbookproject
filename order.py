class Order:
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


