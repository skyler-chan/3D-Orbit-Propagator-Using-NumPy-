
# From meeting with Mingde, Sep 27 2021
# Matplotlib is used to graph stuff

from matplotlib import pyplot as plt

N = 200


# Creating the arrays

v = [0] * N
z = [0] * N
z_an = [0] * N
t = [0] * N
# Initialize these to zero because we dont know them


# Except z. since its 10 since we know that

z[0] = 10

h = 0.01
g = 10
for n in range(0, N - 1):
    z_an[n] = -1/2 * g * t[n]**2 + 10  # z = -1/2 gt^2 +10

    z[n+1] = z[n] + v[n] * h
    v[n+1] = v[n] - g * h
    t[n+1] = t[n] + h

plt.plot(t, z)
plt.plot(t, z_an)
plt.show()
