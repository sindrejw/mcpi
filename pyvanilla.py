from random import random

def estimate_pi(iterations=100):
    """Estimate pi using MC-simulation.

    Keyword arguments:
    interations -- number of iterations used (default 100)
    """

    circle_points = 0

    for i in range(iterations):
        x, y = random(), random()

        if x*x + y*y <= 1:
            circle_points += 1

    return 4*circle_points/iterations

if (__name__ == '__main__'):
    estimate_pi()