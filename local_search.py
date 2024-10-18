import numpy as np
import time

BITS_PER_DIMENSION = 16  # 16 bits for each dimension
MIN_VALUE = -10
MAX_VALUE = 10
MAX_ITER = 10000
MAX_ITER_EXPERIMENT = 100
N_1 = 2  # 2 dimensions
N_2 = 5  # 5 dimensions
N_3 = 10  # 10 dimensions


def mapping_value(decimal, bits_per_dimension):
    # Maps the binary decimal value to the range [MIN_VALUE, MAX_VALUE]
    max_decimal = 2**bits_per_dimension - 1
    return MIN_VALUE + (MAX_VALUE - MIN_VALUE) * decimal / max_decimal

def neighborhood_operator(m, solution, dimensions):
    # Generate a neighbor by flipping bits in the binary solution
    neighbor = solution
    total_bits = BITS_PER_DIMENSION * dimensions  # Total number of bits for all dimensions

    for _ in range(total_bits):
        bit_to_flip = np.random.randint(0, total_bits)  # Select a random bit to flip
        if np.random.uniform(0, 1) < m / total_bits:
            neighbor ^= (1 << bit_to_flip)  # Flip the selected bit

    return neighbor

def evaluation_function(dimensions, solution):
    # Evaluate the binary solution as a sum of squares function
    total_sum = 0

    for i in range(dimensions):
        # Get the 16 bits for the current dimension
        binary_segment = (solution >> (BITS_PER_DIMENSION * (dimensions - 1 - i))) & ((1 << BITS_PER_DIMENSION) - 1)

        # Map the value to the correct range
        mapped_value = mapping_value(binary_segment, BITS_PER_DIMENSION)

        # Sum the square of the mapped value
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

    show_results(x, dimensions)
    return x, evaluation_values

def show_results(best_solution, dimensions):
    print(f"Best Binary code: {bin(best_solution)}")
    bits_per_dimension = BITS_PER_DIMENSION  # 16 bits per dimension
    for i in range(dimensions):
        binary_segment = (best_solution >> (bits_per_dimension * (dimensions - 1 - i))) & ((1 << bits_per_dimension) - 1)
        mapped_value = mapping_value(binary_segment, bits_per_dimension)
        print(f"Dimension {i + 1}:")
        print(f"  Binary segment: {bin(binary_segment)}")
        print(f"  Decimal value: {binary_segment}")
        print(f"  Mapped value: {mapped_value}")

def save_results(eval_values, dimensions, execution_time, iteration):
    with open(f"results_{dimensions}_dimensions.txt", "a") as file:
        file.write(f"Evaluation values for experiment number {iteration}:\n")
        counter = 0
        for value in eval_values:
            counter += 1
            file.write(f"{counter};{value}\n")
    with open(f"time_results_{dimensions}_dimensions.txt", "a") as file:
        file.write(f"Experiment number: {iteration};")
        file.write(f"Execution time: {execution_time:.6f} seconds\n")

def excercise_2():
    dimensions = N_3
    starting_point = (1 << (BITS_PER_DIMENSION * dimensions)) - 1  # Initial solution (all bits set to 1 for N_1 dimensions)
    m = 4  # Perturbation factor

    for _ in range(MAX_ITER_EXPERIMENT):
        print(f"\n\nExperiment number: {_ + 1}\n")
        start_time = time.time()
        # Execute the local search
        __ , evaluation_values = first_improvement_local_search(starting_point, m, dimensions)
        end_time = time.time()
        execution_time = end_time - start_time
        save_results(evaluation_values, dimensions, execution_time, _)
        print(f"Execution time for experiment {_ + 1}: {execution_time:.6f} seconds")


def main():
    # Runs the experiment
    excercise_2()

if __name__ == '__main__':
    main()
