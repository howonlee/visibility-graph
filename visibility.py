import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr

def brownian(length, loc=0, scale=1):
    #1d brownian
    arr = npr.normal(loc, scale, size=length)
    return np.cumsum(arr, axis=-1)

if __name__ == "__main__":
    plt.plot(brownian(1000))
    plt.show()

