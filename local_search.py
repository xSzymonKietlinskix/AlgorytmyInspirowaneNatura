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

def mapping_value(decimal, bits_per_dimension):
    # poprawiłem żeby działało w różnych wymirach
    max_decimal = 2**bits_per_dimension - 1
    return MIN_VALUE + (MAX_VALUE - MIN_VALUE) * decimal / max_decimal


def neighborhood_operator(m, solution, bits_per_dimension, dimensions):
    # szczerze nie wiem co tu się dzieje w tej funkcji ale buja
    neighbor = solution
    for _ in range(dimensions):
        for j in range(bits_per_dimension):
            if np.random.uniform(0, 1) < m / MAX_BITS:
                neighbor ^= (1 << j)
    return neighbor

def evaluation_function(dimensions, solution, bits_per_dimension):
    # funkcja oceny
    total_sum = 0

    # Dla każdego wymiaru, bierze odpowiednią liczbę bitów z rozwiązania,
    # przelicza na wartość dziesiętną i mapuje na odpowiedni zakres
    # sumuje kwadraty tych wartości (funkcja oceny/celu to parabola)
    for i in range(dimensions):
        # get bits from the gray code for the current dimension
        gray_segment = (solution >> (bits_per_dimension * (dimensions - 1 - i))) & ((1 << bits_per_dimension) - 1)

        decimal_value = gray_to_decimal(gray_segment)

        # Map the value to the correct range
        mapped_value = mapping_value(decimal_value, bits_per_dimension)

        # Sum the square of the mapped value
        total_sum += mapped_value ** 2

    return total_sum


def first_improvement_local_search(x, m, dimensions):
    # x - punkt startowy, m - perturbacja, dimensions - wymiary
    iteration = 0
    # obliczamy ile bitów przypada na jeden wymiar
    bits_per_dimension = MAX_BITS // dimensions
    while iteration < MAX_ITER:
        iteration += 1
        improved = False

        # nie jestem przekoany czy tutaj ma być MAX_BITS czy bits_per_dimension
        for _ in range(MAX_BITS):
            # somsiad
            x_prime = neighborhood_operator(m, x, bits_per_dimension, dimensions)
            # jak wartość paraboli mniejsza dla somsiada to zamieniamy
            if evaluation_function(dimensions, x_prime, bits_per_dimension) < evaluation_function(dimensions, x, bits_per_dimension):
                x = x_prime
                improved = True
                break

        if not improved:
            break

    show_results(x, bits_per_dimension, dimensions)
    return x

def show_results(best_solution, bits_per_dimension, dimensions):
    print(f"Best Gray code: {bin(best_solution)}")
    for i in range(dimensions):
        gray_segment = (best_solution >> (bits_per_dimension * (dimensions - 1 - i))) & ((1 << bits_per_dimension) - 1)
        decimal_value = gray_to_decimal(gray_segment)
        mapped_value = mapping_value(decimal_value, bits_per_dimension)
        print(f"Dimension {i + 1}:")
        print(f"  Gray segment: {bin(gray_segment)}")
        print(f"  Decimal value: {decimal_value}")
        print(f"  Mapped value: {mapped_value}")


def excercise_2():
    starting_point = 0b1111111111111111
    # perturbacja
    m = 4

    for _ in range(MAX_ITER_EXPERIMENT):
        print(f"\n\nExperiment number: {_ + 1}\n")
        best_solution = first_improvement_local_search(starting_point, m, N_1)

def main():
    # # Example usage
    # gray_code = 0b1101  # Example Gray code in binary (up to 16 bits)
    # decimal_number = gray_to_decimal(gray_code)
    # print(f"Gray code: {bin(gray_code)}")
    # print(f"Decimal number: {decimal_number}")
    # Inicjalizujemy punkt startowy - x0

    excercise_2()
#     TO DO:
# zweryfikować wyniki dla dwóch wymiarów, to co wypluwa wygląda ok ale nie jestem pewien czy aby na pewno xD
# jak są git to zrobić dla 5 i 10 wymiarów
# wygenerować jakieś dane do wykresów (jescze nie czaje co to ma być)
# usunąć moje polskie komenatrze, dodać ewntualnie jakieś sensowne po angielsku
#  przejrzeć to jeszcze raz xD


if __name__ == '__main__':
    main()
