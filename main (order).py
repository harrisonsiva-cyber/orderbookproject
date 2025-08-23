from itertools import count
import order as ord
import beautifultable as BeautifulTable


class order_book:

    # Class-level constants for valid order types and sides
    VALID_TYPES = ["FOK", "LIMIT", "MARKET"]
    VALID_SIDES = ["BUY", "SELL"]

    BUY_ORDERS = []
    SELL_ORDERS = []

    order_number = 0

    for i in count(0):
        str_side = str(input("Enter whether the order is a buy or sell: ")).upper()
        if str_side not in VALID_SIDES:  # Validating side
            raise ValueError(f"Invalid side: {str_side}. Must be one of {VALID_SIDES}")
        side = ord.OrderSide[str_side]

        str_order_type = str(input("Enter whether the order is a FOK, LIMIT OR MARKET: ")).upper()
        if str_order_type not in VALID_TYPES:  # Validating order type
            raise ValueError(f"Invalid order type: {str_order_type}. Must be one of {VALID_TYPES}")
        order_type = ord.OrderType[str_order_type]

        quantity = int(input("Enter the number of shares: "))
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("Quantity must be a positive number")

        initial_price = float(input("Enter the total price of the order: £ "))
        price = round(initial_price, 2)
        if not isinstance(price, (int, float)) or price <= 0:  # Validating price
            raise ValueError("Price must be a positive integer or positive decimal")

        order_instance = ord.Order(order_number, order_type, side, price, quantity)
        if side == ord.OrderSide.BUY:
            BUY_ORDERS.append(order_instance)
        else:
            SELL_ORDERS.append(order_instance)

        x = input("Type Yes if you would like to carry on or Stop if you want to stop: ").upper()

        if x == 'STOP':
            break

    BUY_ORDERS.sort(key=lambda x: x['price'])
    SELL_ORDERS.sort(key=lambda x: x['price'], reverse=True)

    if side == ord.OrderSide.BUY:
        buy_table = BeautifulTable()
        buy_table.column_headers = ["Order Number", "Price", "Quantity"]
        buy_table.append_row([order_number, price, quantity])
        print(buy_table)

    elif side == ord.OrderSide.SELL:
        sell_table = BeautifulTable()
        sell_table.column_headers = ["Order Number", "Price", "Quantity"]
        sell_table.append_row([order_number, price, quantity])
        print(sell_table)

# Matching the fok orders
# Matching the limit orders
# Matching the market orders
