import matplotlib.pyplot as plt
import numpy as np

def superelipsa(a, b, m, n, nPoints=1000):
    t = np.linspace(0, 2 * np.pi, nPoints)
    x = a * np.sign(np.cos(t)) * np.abs(np.cos(t))**(2/m)
    y = b * np.sign(np.sin(t)) * np.abs(np.sin(t))**(2/n)
    return x, y

def plot_superelipsa(a, b, m, n):
    x, y = superelipsa(a, b, m, n)
    plt.plot(x, y)
    plt.title('Superelipsa')
    plt.xlabel('Oś x')
    plt.ylabel('Oś y')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

plot_superelipsa(1, 1, 2, 0.5)
