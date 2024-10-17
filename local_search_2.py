import numpy as np
import csv

MAX_BITS = 16
N_1 = 2
N_2 = 5
N_3 = 10
MIN_VALUE = -10
MAX_VALUE = 10
MAX_ITER = 10000
MAX_ITER_EXPERIMENT = 100

def gray_to_binary(gray):
    binary = gray
    while gray > 0:
        gray >>= 1
        binary ^= gray
    return binary

def gray_to_decimal(gray):
    binary = gray_to_binary(gray)
    return binary

def mapping_value(decimal, bits_per_dimension):
    max_decimal = 2**bits_per_dimension - 1
    return MIN_VALUE + (MAX_VALUE - MIN_VALUE) * decimal / max_decimal

def neighborhood_operator(m, solution, bits_per_dimension, dimensions):
    neighbor = solution
    for _ in range(dimensions):
        for j in range(bits_per_dimension):
            if np.random.uniform(0, 1) < m / MAX_BITS:
                neighbor ^= (1 << j)
    return neighbor

def evaluation_function(dimensions, solution, bits_per_dimension):
    total_sum = 0
    for i in range(dimensions):
        gray_segment = (solution >> (bits_per_dimension * (dimensions - 1 - i))) & ((1 << bits_per_dimension) - 1)
        decimal_value = gray_to_decimal(gray_segment)
        mapped_value = mapping_value(decimal_value, bits_per_dimension)
        total_sum += mapped_value ** 2
    return total_sum

def first_improvement_local_search(x, m, dimensions):
    iteration = 0
    bits_per_dimension = MAX_BITS // dimensions
    best_value = evaluation_function(dimensions, x, bits_per_dimension)
    values = [best_value]
    while iteration < MAX_ITER:
        iteration += 1
        improved = False
        for _ in range(MAX_BITS):
            x_prime = neighborhood_operator(m, x, bits_per_dimension, dimensions)
            new_value = evaluation_function(dimensions, x_prime, bits_per_dimension)
            if new_value < best_value:
                x = x_prime
                best_value = new_value
                improved = True
                break
        values.append(best_value)
        if not improved:
            break
    return x, values

def run_experiments(dimensions, filename):
    starting_point = (1 << MAX_BITS) - 1  # 0b1111111111111111
    m = 4
    all_values = []
    for _ in range(MAX_ITER_EXPERIMENT):
        _, values = first_improvement_local_search(starting_point, m, dimensions)
        all_values.append(values)
    max_length = max(len(values) for values in all_values)
    for values in all_values:
        while len(values) < max_length:
            values.append(values[-1])
    averaged_values = np.mean(all_values, axis=0)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Iteration", "Average Value"])
        for i, value in enumerate(averaged_values):
            writer.writerow([i, value])

def main():
    run_experiments(N_1, 'results_n2.csv')
    run_experiments(N_2, 'results_n5.csv')
    run_experiments(N_3, 'results_n10.csv')

if __name__ == '__main__':
    main()