def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean(b % a, a)
        return gcd, y - (b // a) * x, x

def multiplicative_inverse(a, b):
    gcd, x, _ = extended_euclidean(a, b)
    if gcd == 1:
        return x % b  # Ensure the result is positive
    else:
        raise Exception(f'{a} has no multiplicative inverse modulo {b}')

# a.x + b.y = c
def ext_euc(a, b, c):
    x_inv = multiplicative_inverse(a, b)
    y = (c - a * x_inv) // b
    print(x_inv, y)

# Test the function with example inputs (a.x + b.y = c)
ext_euc(3, 5, 1)
# 2 -1 

ext_euc(10, 17, 1)
# 12 -7
