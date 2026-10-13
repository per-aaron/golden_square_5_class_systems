def make_change(price, paid):
    """
    This function works out which coins a vending machine should give back
    as change, using as few coins as possible. Prices are in pounds.
    It returns a dictionary of {coin value in pence: number of that coin}.
    For example, make_change(1.10, 2.00) should return {50: 1, 20: 2}.
    """
    if paid < price:
        return "not enough money paid"
    if paid > 10:
        return "machine only accepts up to £10 for this exercise"
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    remaining = int(round(paid - price, 2) * 100) #float rounding error, added round to 2 dp
    change = {}
    i = -1 #start at end of list
    while remaining > 0:
        coin = coins[i]
        while coin <= remaining: #force loop to check each coin until remaining is smaller, allows for multiple of one coin
            change[coin] = change.get(coin, 0) + 1
            remaining -= coin
        i -= 1 #decrement to go backwards through list
    return change

print(make_change(1.10, 2.00))