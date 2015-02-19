using Brownian
using NPZ

p = FBM(0:1.0:1000000, 0.000000001)
npzwrite("quick_fbm.npy", rand(p))
