import numpy as np
from numpy.random import normal


def normal_distribution(mean, std_dev, size):
    return np.random.normal(mean, std_dev, size)

def uniform_distribution(low, high, size):
    return np.random.uniform(low, high, size)

def show_circle_shots(amount_of_shots, radius, half_side):
    # losowanie współrzędnych punktów
    x = uniform_distribution(-half_side, half_side, amount_of_shots)
    y = uniform_distribution(-half_side, half_side, amount_of_shots)
    shots = np.array([x, y]).T

    inside_circle = []
    outside_circle = []
    counter = 0
    for shot in shots:
        counter += 1
        if np.linalg.norm(shot) <= radius:
            inside_circle.append(shot)
        else:
            outside_circle.append(shot)
        if counter == 100 or counter == 1000:
            res = 4 * half_side**2 * len(inside_circle) / counter
            print(f"Proporcja trafień do strzałów: {len(inside_circle)} : {counter}")
            print(f"Pole koła liczone z proporcji:: {res}")
            print(f"Rzeczywiste pole kola: {np.pi * radius**2}\n")

    print(f"Proporcja trafień do strzałów: {len(inside_circle)} : {counter}")
    print(f"Pole koła liczone z proporcji:: {4 * half_side**2 * len(inside_circle) / counter}")
    print(f"Rzeczywiste pole kola: {np.pi * radius ** 2}\n")

    np.savetxt("inside_circle.txt", inside_circle)
    np.savetxt("outside_circle.txt", outside_circle)


def exercise_1():
    # rozkład równomierny
    uniform_dist_numbers = uniform_distribution(-100, 100, 1000)
    np.savetxt("uniform_dist_numbers.txt", uniform_dist_numbers)

    # rozkład normalny
    normal_dist_numbers = normal_distribution(0,50,1000)
    np.savetxt("normal_dist_numbers.txt", normal_dist_numbers)

    # koło
    show_circle_shots(10000, 3, 4)

def main():
    exercise_1()

if __name__ == '__main__':
    main()