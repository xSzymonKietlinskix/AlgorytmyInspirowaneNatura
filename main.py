import numpy as np
from numpy.random import normal


def normal_distribution(mean, std_dev, size):
    return np.random.normal(mean, std_dev, size)

def uniform_distribution(low, high, size):
    return np.random.uniform(low, high, size)

def show_circle_shots(amount_of_shots, radius, x):
    # losowanie współrzędnych punktów
    x = uniform_distribution(-x, x, amount_of_shots)
    y = uniform_distribution(-x, x, amount_of_shots)
    shots = np.array([x, y]).T

    inside_circle = []
    counter = 0
    for shot in shots:
        counter += 1
        if np.linalg.norm(shot) <= radius:
            inside_circle.append(shot)
        if counter == 100 or counter == 1000:
            print(f"Proporcja trafień do strzałów: {len(inside_circle)} : {counter}\n")
            print(f"Pole koła liczone z proporcji:: {4 * x**2 * len(inside_circle) / counter}\n\n")
            print(f"Rzeczywiste pole kola: {np.pi * radius**2}")

    print(f"Proporcja trafień do strzałów: {len(inside_circle)} : {counter}\n")
    print(f"Pole koła liczone z proporcji:: {4 * x ** 2 * len(inside_circle) / counter}\n\n")
    print(f"Rzeczywiste pole kola: {np.pi * radius ** 2}")



def exercise_1():
    # rozkład równomierny
    uniform_dist_numbers = uniform_distribution(-100, 100, 1000)
    print(f"Wygenerowne liczby z rozkładem równomiernym: {uniform_dist_numbers}\n\n")
    np.savetxt("uniform_dist_numbers.txt", uniform_dist_numbers, fmt=".6f")

    # rozkład normalny
    normal_dist_numbers = normal_distribution(0,50,1000)
    print(f"Wygenerowne liczby z rozkładem normalnym: {normal_dist_numbers}\n\n")
    np.savetxt("normal_dist_numbers.txt", normal_dist_numbers)

def main():
    exercise_1()

if __name__ == '__main__':
    main()