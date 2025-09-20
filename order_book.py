import order

# Class-level constants for valid order types and sides
VALID_TYPES = ["FOK", "LIMIT", "MARKET"]
VALID_SIDES = ["BUY", "SELL"]

class order_book:

    BUY_ORDERS = []
    SELL_ORDERS = []
    order_number = 0

    def add_order(self, side, order_type, quantity, price):
        order_instance = order.Order(self.order_number, order_type, side, price, quantity)
        if side == order.OrderSide.BUY:
            self.order_number += 1
            self.BUY_ORDERS.append(order_instance)
            self.BUY_ORDERS.sort(key=lambda x: x.price)
        else:
            self.order_number += 1
            self.SELL_ORDERS.append(order_instance)
            self.SELL_ORDERS.sort(key=lambda x: x.price, reverse=True)

    def print(self):
        for x in self.BUY_ORDERS:
            print(x)
        for x in self.SELL_ORDERS:
            print(x)

    def match(self):
        while self.BUY_ORDERS and self.SELL_ORDERS:
            if order_type == order.OrderType.FOK:
                BUY_ORDER = self.BUY_ORDERS[0]
                SELL_ORDER = self.SELL_ORDERS[0]
                #Filling the order
                if BUY_ORDER.price >= SELL_ORDER.price and BUY_ORDER.quantity <= SELL_ORDER.quantity:
                    SELL_ORDER.quantity -= BUY_ORDER.quantity
                    self.BUY_ORDERS.pop(0)
                    if SELL_ORDER.quantity == 0:
                        self.SELL_ORDERS.pop(0)

                else:
                    self.BUY_ORDERS.pop(0)

            elif order_type == order.OrderType.LIMIT:
                BUY_ORDER = self.BUY_ORDERS[0]
                SELL_ORDER = self.SELL_ORDERS[0]

                if BUY_ORDER.price >= SELL_ORDER.price:
                    traded_quantity = min(BUY_ORDER.quantity, SELL_ORDER.quantity)
                    BUY_ORDER.quantity -= traded_quantity
                    SELL_ORDER.quantity -= traded_quantity

                    if BUY_ORDER.quantity == 0:
                        self.BUY_ORDERS.pop(0)
                    if SELL_ORDER.quantity == 0:
                        self.SELL_ORDERS.pop(0)
                else:
                    break

            elif order_type == order.OrderType.MARKET:
                BUY_ORDER = self.BUY_ORDERS[0]
                SELL_ORDER = self.SELL_ORDERS[0]

                traded_quantity = min(BUY_ORDER.quantity, SELL_ORDER.quantity)
                BUY_ORDER.quantity -= traded_quantity
                SELL_ORDER.quantity -= traded_quantity

                if BUY_ORDER.quantity == 0:
                    self.BUY_ORDERS.pop(0)
                if SELL_ORDER.quantity == 0:
                    self.SELL_ORDERS.pop(0)
                else:
                     break
