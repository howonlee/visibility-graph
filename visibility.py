import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr
import networkx as nx

def brownian(length, loc=0, scale=1):
    #1d brownian
    arr = npr.normal(loc, scale, size=length)
    return np.cumsum(arr, axis=-1)

def calc_vis_matrix(arr):
    vis_mat = np.zeros((arr.shape[0], arr.shape[0])) #duplicate
    for x in np.nditer(arr, order="C"):
        #iterate through twice
        curr_val = 0
        #figure out how to calculate this in O(n^2)
        #slope = (t_b - t_c) / (t_b - t_a)
        #y_c < y_b + (y_a - y_b) * slope
        for y in np.nditer(arr, order="C"):
            if y > curr_val:
                vis_mat[x,y] = 1
                curr_val = y
    return vis_mat

def vis_mat_to_nx(mat):
    net = nx.from_numpy_matrix(mat)

if __name__ == "__main__":
    sample = brownian(1000)
    vizmat = calc_vis_matrix(sample)
    plt.matshow(vizmat)
    plt.show()
