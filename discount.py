def calculate_discounted_bill(prices, threshold, discount_rate):
    """
    Calculates total cost of items in order.
    Every time total spending hits 'threshold',
    the NEXT item receives a discount equal to 'discount_rate'.
    """
    if not prices:
        return 0.0

    total_spent = 0.0
    spent_since_last_discount = 0.0
    apply_discount = False

    for i in range(len(prices)):
        price = prices[i]

        # Apply discount if flagged from previous threshold breach
        if apply_discount:
            discounted_price = price * (1 - discount_rate)
            total_spent += discounted_price
            spent_since_last_discount = 0.0
            apply_discount = False  # Reset flag after applying discount
        else:
            total_spent += price
            spent_since_last_discount += price

        # Check if we hit threshold to discount NEXT item
        if spent_since_last_discount >= threshold:
            apply_discount = True

    return round(total_spent, 2)

print(calculate_discounted_bill([10,20,10,10], 10, .5))