import unittest
import order


class MyTestCase(unittest.TestCase):
    def test_orders(self):
        buy_orders = []
        sell_orders = []
        order1 = order.Order(1, order.OrderType.LIMIT, order.OrderSide.BUY, 500.0, 1)
        order2 = order.Order(2, order.OrderType.MARKET, order.OrderSide.BUY, 550.0, 5)
        order3 = order.Order(3, order.OrderType.FOK, order.OrderSide.BUY, 560.0, 10)
        order4 = order.Order(4, order.OrderType.FOK, order.OrderSide.SELL, 570.0, 15)
        order5 = order.Order(5, order.OrderType.LIMIT, order.OrderSide.SELL, 580.0, 20)
        order6 = order.Order(6, order.OrderType.MARKET, order.OrderSide.SELL, 590.0, 35)
        order7 = order.Order(7, order.OrderType.LIMIT, order.OrderSide.SELL, 600.0, 30)

        buy_orders.append(order1)
        buy_orders.append(order2)
        buy_orders.append(order3)
        sell_orders.append(order4)
        sell_orders.append(order5)
        sell_orders.append(order6)
        sell_orders.append(order7)

        print("\nBuy Orders:")
        for ord in buy_orders:
            print(ord)

        print("\nSell Orders:")
        for ord in sell_orders:
            print(ord)


if __name__ == '__main__':
    unittest.main()

