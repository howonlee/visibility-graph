import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr
import networkx as nx

def brownian(length, loc=0, scale=1):
    #1d brownian
    arr = npr.normal(loc, scale, size=length)
    return np.cumsum(arr, axis=-1)

def calc_vizmat(arr):
    num_points = arr.shape[0]
    vis_mat = np.zeros((num_points, num_points)) #duplicate
    for a in xrange(num_points):
        max_yc = 0
        max_tc = 0
        for b in xrange(a+1, num_points):
            yc_pred = arr[b] + ((arr[a] - arr[b]) * ((b - max_tc) / (b - a)))
            if yc_pred > max_yc:
                vis_mat[a,b] = 1
                max_yc = arr[b]
                max_tc = b
    return vis_mat

def vizmat_to_net(mat):
    return nx.from_numpy_matrix(mat)

def plot_vizmat(vizmat, sample):
    plt.matshow(vizmat)
    plt.savefig("vizmat.png")
    plt.close()
    plt.plot(sample)
    plt.savefig("sample.png")

def plot_degree_dist(net):
    degs = sorted(nx.degree(net).values(), reverse=True)
    plt.loglog(degs)
    plt.show()

if __name__ == "__main__":
    sample = brownian(4000)
    vizmat = calc_vizmat(sample)
    net = vizmat_to_net(vizmat)
    #plot_vizmat(vizmat, sample)
    plot_degree_dist(net)
