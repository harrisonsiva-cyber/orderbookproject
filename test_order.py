import unittest
import order


class MyTestCase(unittest.TestCase):
    def test_orders(self):
        buy_orders = []
        sell_orders = []
        order1 = order.Order(order.OrderType.FOK, order.OrderSide.BUY, 100.0, 10)
        order2 = order.Order(order.OrderType.LIMIT, order.OrderSide.SELL, 150.0, 5)
        order3 = order.Order(order.OrderType.MARKET, order.OrderSide.BUY, 200.0, 20)
        order4 = order.Order(order.OrderType.FOK, order.OrderSide.SELL, 250.0, 15)
        order5 = order.Order(order.OrderType.LIMIT, order.OrderSide.BUY, 300.0, 25)
        order6 = order.Order(order.OrderType.MARKET, order.OrderSide.SELL, 350.0, 30)
        order7 = order.Order(order.OrderType.FOK, order.OrderSide.BUY, 400.0, 35)

        buy_orders.append(order1)
        buy_orders.append(order3)
        buy_orders.append(order5)
        sell_orders.append(order2)
        sell_orders.append(order4)
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
