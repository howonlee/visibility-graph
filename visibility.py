import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr
import networkx as nx

def brownian(length, loc=0, scale=1):
    #1d brownian
    arr = npr.normal(loc, scale, size=length)
    return np.cumsum(arr, axis=-1)

def calc_vis_matrix(arr):
    vis_mat = np.zeros(arr.shape[0], arr.shape[0]) #duplicate
    for x in the array:
        for y also in the array:
            vis_mat[x,y] = whether we can see
    return vis_mat

def vis_mat_to_nx(mat):
    net = nx.from_numpy_matrix(mat)

if __name__ == "__main__":
    sample = brownian(1000)

