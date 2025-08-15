class Order:
    order_id = 0
    print_format = "{:<10}\t{:<10}\t{:>10}\t{:>10}\t{:>10}"

    def __init__(self, order_type, side, rounded_price, quantity, timestamp=None):
        # Set instance attributes
        self.order_type = order_type
        self.side = side
        self.price = price
        self.rounded_price = rounded_price
        self.quantity = quantity
        self.timestamp = timestamp

    def __str__(self):
        return f"{self.order_number}\t\t{self.order_type}\t\t{self.side}\t\t{self.quantity}\t\t{self.rounded_price}"
        return self.print_format.format(
            self.order_number, self.order_type, self.side, self.quantity, self.rounded_price)

    def print(self):
        print(f"Order Number: {self.order_number}")
        print(f"Order Type: {self.order_type}")
        print(f"Order Side: {self.side}")
        print(f"Price: {self.rounded_price}")
        print(f"Quantity: {self.quantity}")
        print(f"Timestamp: {self.timestamp}")


