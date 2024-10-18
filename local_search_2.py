import numpy as np
import time
import pandas as pd

BITS_PER_DIMENSION = 16
MIN_VALUE = -10
MAX_VALUE = 10
MAX_ITER = 10000
MAX_ITER_EXPERIMENT = 100
N_1 = 2
N_2 = 5
N_3 = 10

def mapping_value(decimal, bits_per_dimension):
    max_decimal = 2**bits_per_dimension - 1
    return MIN_VALUE + (MAX_VALUE - MIN_VALUE) * decimal / max_decimal

def neighborhood_operator(m, solution, dimensions):
    neighbor = solution
    total_bits = BITS_PER_DIMENSION * dimensions
    for _ in range(total_bits):
        bit_to_flip = np.random.randint(0, total_bits)
        if np.random.uniform(0, 1) < m / total_bits:
            neighbor ^= (1 << bit_to_flip)
    return neighbor

def evaluation_function(dimensions, solution):
    total_sum = 0
    for i in range(dimensions):
        binary_segment = (solution >> (BITS_PER_DIMENSION * (dimensions - 1 - i))) & ((1 << BITS_PER_DIMENSION) - 1)
        mapped_value = mapping_value(binary_segment, BITS_PER_DIMENSION)
        total_sum += mapped_value ** 2
    return total_sum

def first_improvement_local_search(x, m, dimensions):
    # Local search to find a first better solution by exploring neighbors
    iteration = 0
    evaluation_values = []
    while iteration < MAX_ITER:
        iteration += 1
        improved = False

        total_bits = BITS_PER_DIMENSION * dimensions  # Total bits for all dimensions
        for _ in range(total_bits):
            # Generate a neighboring solution
            x_prime = neighborhood_operator(m, x, dimensions)
            # If the neighbor has a better (lower) evaluation, update the current solution
            evaluation_value_x = evaluation_function(dimensions, x)
            evaluation_value_x_prime = evaluation_function(dimensions, x_prime)
            if evaluation_value_x_prime < evaluation_value_x:
                evaluation_values.append(evaluation_value_x_prime)
                x = x_prime
                improved = True
                break
            else:
                evaluation_values.append(evaluation_value_x)

        if not improved:
            break

    return x, evaluation_values

def excercise_2(dimensions):
    starting_point = (1 << (BITS_PER_DIMENSION * dimensions)) - 1
    m = 4
    all_evaluation_series = []
    for _ in range(MAX_ITER_EXPERIMENT):
        _, evaluation_values = first_improvement_local_search(starting_point, m, dimensions)
        all_evaluation_series.append(evaluation_values)
    return all_evaluation_series

def pad_evaluation_series(all_evaluation_series):
    max_length = max(len(series) for series in all_evaluation_series)
    padded_series = [series + [series[-1]] * (max_length - len(series)) for series in all_evaluation_series]
    return padded_series

def average_evaluation_series(all_evaluation_series):
    padded_series = pad_evaluation_series(all_evaluation_series)
    avg_series = np.mean(padded_series, axis=0)
    return avg_series

def save_to_excel(n1_data, n2_data, n3_data):
    with pd.ExcelWriter('lab2_files/results.xlsx') as writer:
        for data, n in zip([n1_data, n2_data, n3_data], [N_1, N_2, N_3]):
            df = pd.DataFrame(data)
            df.to_excel(writer, sheet_name=f'n={n}', index=False)
            avg_series = average_evaluation_series(data)
            avg_df = pd.DataFrame(avg_series, columns=['Average Evaluation'])
            avg_df.to_excel(writer, sheet_name=f'n={n}_avg', index=False)

def main():
    n1_data = excercise_2(N_1)
    print("N1 done")
    n2_data = excercise_2(N_2)
    print("N2 done")
    n3_data = excercise_2(N_3)
    print("N3 done")
    save_to_excel(n1_data, n2_data, n3_data)

if __name__ == '__main__':
    main()