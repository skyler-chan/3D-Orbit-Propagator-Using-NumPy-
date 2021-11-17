# Euler's method, RK1 (RK4 is best, stands for Runge-Kutta)
# Next goal, to get RK4, then using smt diff not for loops, for loops are slow
# Matplotlib is used to graph stuff
from matplotlib import pyplot as plt
from math import sqrt  # math gives a sqrt function
import numpy as np

N = 800
GM = 3.986e5


# Creating the arrays (basically to let values sit somewhere - point of arrays, kinda like spreadsheet)

u = np.zeros((N, 6))
t = [0]*N

# Initialize init positions
u[0] = np.array([6800, 0, 0, 0, 7.7, 2.5])

h = 10  # sec

for n in range(0, N-1):

    # RK 1 Step

    # In order to get acceleration at the initial point, we need
    # the radius of the spacecraft from the earth at the initial point
    r = sqrt(u[n][0]**2 + u[n][1]**2 + u[n][2]**2)

    # Slopes from the starting point
    k1 = np.array([u[n][3],
                   u[n][4],
                   u[n][5],
                   - GM / r**3 * u[n][0],
                   - GM / r**3 * u[n][1],
                   - GM / r**3 * u[n][2]])

    # Euler step to the next point, for purposes of estimating slope.
    u1 = u[n] + k1*h

    # In order to get acceleration at the next point, we need
    # the radius of the spacecraft from the earth at the next point
    r1 = sqrt(u1[0]**2 + u1[1]**2 + u1[2]**2)

    # Slopes from the next point
    k2 = np.array([u1[3],
                  u1[4],
                  u1[5],
                  - GM / r**3 * u1[0],
                  - GM / r**3 * u1[1],
                  - GM / r**3 * u1[2]])

    # Put it all together
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


# notice when run, takes a sec to plot, solver is slow
# error bc of euler's method is accumulating in the overlap of orbit
