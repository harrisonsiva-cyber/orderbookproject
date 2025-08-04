import order
from itertools import count

from order import OrderType


def main():

    buy_orders = []
    sell_orders = []

    order_number = 0
    for i in count(0):
        # read order details from the user
        entered_price = float(input("Enter the total price of the order: £ "))
        price = round(entered_price, 2)
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")

        quantity = int(input("Enter the number of shares: "))
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("Quantity must be a positive number")

        strside = input("Enter whether the order is a buy or sell: ").upper()
#        if strside not in order.OrderSide:
#            raise ValueError(f"Invalid side: {strside}.")
        side = order.OrderSide[strside]

        str_order_type = str(input("Enter whether the order is a FOK, LIMIT OR MARKET: ")).upper()
#        if order_type not in order.OrderType:
#            raise ValueError(f"Invalid order type: {order_type}.")
        order_type = order.OrderType[str_order_type]

        # Create an order instance
        order_instance = order.Order(order_type, side, price, quantity)
        if side == order.OrderSide.BUY:
            buy_orders.append(order_instance)
        else:
            sell_orders.append(order_instance)

        print(order_instance)

        x = input("Type Yes if you would like to carry on or Stop if you want to stop: ").upper()
        if x == 'STOP':
            break

    print("\nBuy Orders:")
    for myorder in buy_orders:
        print(myorder)

    print("\nSell Orders:")
    for myorder in sell_orders:
        print(myorder)


# Only run the main function when the script is executed correctly.
if __name__ == "__main__":
    main()

