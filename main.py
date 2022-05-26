# IN THE NAME OF GOD

# Binary Game
# help source -> https://www.geeksforgeeks.org/binary-decimal-vice-versa-python


def decimal_to_binary(n):
    x = []

    def dec_bin(m):
        if m > 1:
            # divide with integral result (discard remainder)
            dec_bin(m // 2)

        x.insert(0, str(m % 2))

    dec_bin(n)
    return "".join(x)
