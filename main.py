# IN THE NAME OF GOD

# Binary Game
# help source -> https://www.geeksforgeeks.org/binary-decimal-vice-versa-python


def decimal_to_binary(n):
    x = []

    def dec_bin(m):
        if m > 1:
            # divide with integral result (discard remainder)
            dec_bin(m // 2)

        # Put at the end of list x
        # (Due to the recursive function last run do this first)
        x.insert(len(x), str(m % 2))

    dec_bin(n)
    return "".join(x)
