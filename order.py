from itertools import count
class Order:
    order_id = 0
    print_format = "{:<10}\t{:<10}\t{:>10}\t{:>10}\t{:>10}"

    def __init__(self, order_type, side, price, quantity, timestamp=None):
        # Set instance attributes
        self.order_type = order_type
        self.side = side
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp

    def __str__(self):
        return f"{self.order_number}\t\t{self.order_type}\t\t{self.side}\t\t{self.quantity}\t\t{self.price}"
        return self.print_format.format(
            self.order_number, self.order_type, self.side, self.quantity, self.price)


class orderBook:

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


