using Brownian
using NPZ

p = FBM(0:1.0:100000, 0.000001)
npzwrite("quick_fbm.npy", rand(p))
