
def max_profit(prices):
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
    print(max_profit(prices))

main()
