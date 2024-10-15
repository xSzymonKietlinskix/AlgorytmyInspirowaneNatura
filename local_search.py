import numpy as np

MAX_BITS = 16
N_1 = 2
N_2 = 5
N_3 = 10
MIN_VALUE = -10
MAX_VALUE = 10
MAX_ITER = 10000
MAX_ITER_EXPERIMENT = 100
# punkt x0 to zawsze prawy gorny punkt ekranu

def gray_to_binary(gray):
    binary = gray
    while gray > 0:
        gray >>= 1
        binary ^= gray
    return binary

def gray_to_decimal(gray):
    binary = gray_to_binary(gray)
    return binary

def mapping_value(decimal):
    return ((MAX_VALUE - MIN_VALUE) / (2**MAX_BITS)) * decimal + MIN_VALUE


def neighborhood_operator(m, solution): # m controlls the strength of perturbation
    neighbor = solution
    for j in range(MAX_BITS):
        if np.random.uniform(0, 1) < m / MAX_BITS:
            neighbor ^= (1 << j)
    return neighbor


# # Example usage
# gray_code = 0b1101  # Example Gray code in binary (up to 16 bits)
# decimal_number = gray_to_decimal(gray_code)
# print(f"Gray code: {bin(gray_code)}")
# print(f"Decimal number: {decimal_number}")