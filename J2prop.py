# Appended J2 Perturbation (causes Nodal Precession)
from matplotlib import pyplot as plt
from math import sqrt  # math gives a sqrt function
import numpy as np

N = 8000
GM = 3.986e5  # Gravitational parameter of Earth
J2 = 0.00108263  # J2 dimensionless constant
RE = 6378  # Radius of earth in km

# Creating the arrays (basically to let values set somewhere - point of arrays, kinda like spreadsheet)

u = np.zeros((N, 6))
t = [0]*N

# Initialize init positions
u[0] = np.array([6800, 0, 0, 0, 7.7, 2.5])

h = 100  # sec

for n in range(0, N-1):

    # RK 1 Step

    # In order to get acceleration at the initial point, we need
    # the radius of the spacecraft from the earth at the initial point
    r = sqrt(u[n][0]**2 + u[n][1]**2 + u[n][2]**2)

    # Slopes from the starting point
    k1 = np.array([u[n][3],
                   u[n][4],
                   u[n][5],
                  - GM / r**3 *
                   u[n][0] + (3/2 * J2 * GM * RE**2 / r**5) *
                   u[n][0]*(5*u[n][2]**2/r**2 - 1),
                  - GM / r**3 * u[n][1] + (3/2 * J2 * GM * RE**2 / r**5) *
                   u[n][1]*(5*u[n][2]**2/r**2 - 1),
                  - GM / r**3 * u[n][2] + (3/2 * J2 * GM * RE**2 / r**5) *
                  u[n][2]*(5*u[n][2]**2/r**2 - 3)])

    # Euler step to the next point, for purposes of estimating slope.
    u1 = u[n] + k1*h

    # In order to get acceleration at the next point, we need the radius of the spacecraft from the earth at the next point
    r1 = sqrt(u1[0]**2 + u1[1]**2 + u1[2]**2)

    # Slopes from the next point
    k2 = np.array([u1[3],
                  u1[4],
                  u1[5],
                  - GM / r**3 *
                   u1[0] + (3/2 * J2 * GM * RE**2 / r**5) *
                   u1[0]*(5*u1[2]**2/r**2 - 1),
                  - GM / r**3 * u1[1] + (3/2 * J2 * GM * RE**2 / r**5) *
                   u1[1]*(5*u1[2]**2/r**2 - 1),
                  - GM / r**3 * u1[2] + (3/2 * J2 * GM * RE**2 / r**5) *
                  u1[2]*(5*u1[2]**2/r**2 - 3)])
    u[n+1] = u[n] + h * 1/2 * (k1 + k2)
    t[n+1] = t[n] + h

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

U, V = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = 6378 * np.cos(U)*np.sin(V)
y = 6378 * np.sin(U)*np.sin(V)
z = 6378 * np.cos(V)
ax.plot_wireframe(x, y, z, color="b")  # plot the sphere
ax.plot(u[:, 0], u[:, 1], u[:, 2], "k")

# get current access = gca


plt.show()
