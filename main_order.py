import order
import order_book

while True:
    str_side = str(input("Enter whether the order is a buy or sell: ")).upper()
    if str_side not in order_book.VALID_SIDES:  # Validating side
        raise ValueError(f"Invalid side: {str_side}. Must be one of {order_book.VALID_SIDES}")
    side = order.OrderSide[str_side]

    str_order_type = str(input("Enter whether the order is a FOK, LIMIT OR MARKET: ")).upper()
    if str_order_type not in order_book.VALID_TYPES:  # Validating order type
        raise ValueError(f"Invalid order type: {str_order_type}. Must be one of {order_book.VALID_TYPES}")
    order_type = order.OrderType[str_order_type]

    quantity = int(input("Enter the number of shares: "))
    if not isinstance(quantity, (int, float)) or quantity <= 0:
        raise ValueError("Quantity must be a positive number")

    initial_price = float(input("Enter the total price of the order: £ "))
    price = round(initial_price, 2)
    if not isinstance(price, (int, float)) or price <= 0:  # Validating price
        raise ValueError("Price must be a positive integer or positive decimal")

    x = input("Type Yes if you would like to carry on or Stop if you want to stop: ").upper()

    if x == 'STOP':
        break
