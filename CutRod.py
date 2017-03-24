
def _main_():
    list_price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(cut_rode(list_price, 10))


def cut_rode(list_price, n_length):
    """
    Return the maximum revenue based on the list of price and the given length of the rod.
    """
    if n_length == 0:
        return 0
    revenue = -1
    for i in range(1, n_length + 1): # Be careful. Range(1, n) ::= 1..n-1
        revenue = max([revenue, list_price[i] + cut_rode(list_price, n_length - i)])
    return revenue

_main_()

