import numpy as np

def normal_distribution(mean, std_dev, size):
    return np.random.normal(mean, std_dev, size)

def uniform_distribution(low, high, size):
    return np.random.uniform(low, high, size)

def show_circle_shots(amount_of_shots, radius):
    x = uniform_distribution(-radius, radius, amount_of_shots)
    y = uniform_distribution(-radius, radius, amount_of_shots)
    shots = np.array([x, y]).T

    inside_circle = []
    counter = 0
    for shot in shots:
        if np.linalg.norm(shot) <= radius:
            inside_circle.append(shot)
        if counter % 1000 == 0 and counter != 0:
            print(f"Shot {len(inside_circle)} : {counter}")
            print(f"Pole kola: {np.pi * radius**2}")
            print(f"Procent trafien: {4 * radius * radius * len(inside_circle) / counter}\n\n")
        counter += 1

    print(f"Amount of shots inside the circle: {len(inside_circle)} / {len(shots)}")

    return shots


def main():
    show_circle_shots(10000, 2)

if __name__ == '__main__':
    main()