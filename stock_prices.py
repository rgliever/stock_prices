# Ryan Gliever, 2015

# finds the optimal buy/sell points by iterating prices.
# keeps a min value and a max difference value, updating each appropriately
# as it iterates the list
def max_profit(prices):
    # return if tomfoolery
    if len(prices)<2: return [0, 0]
    minimum = prices[0]
    min_index = 0
    max_difference = prices[1] - prices[0]
    max_prof_pts = [0, 1]
    for i, p in enumerate(prices):
        if p - minimum > max_difference:
            max_difference = p - minimum
            max_prof_pts = [min_index, i]
        if p < minimum:
            minimum = p
            min_index = i
    return max_prof_pts

def main():
    prices = [9, 8, 4, 7, 11, 1, 24]
    print("Stock Prices: ", end="")
    print(prices)
    # give the option of user input :)
    user_price_input = input("Enter a list of integers separated by\n" +
        "spaces or press enter to use the default list:\n")
    user_prices = user_price_input.split()
    for i, p in enumerate(user_prices):
        user_prices[i] = int(p)
    if user_prices:
        print("Using Stock Prices ", end="")
        print(user_prices)
        print("Optimal buy and sell days: ", end="")
        print(max_profit(user_prices))
    else:
        print(max_profit(prices))

main()
