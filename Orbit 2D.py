

# Euler's method, RK1 (RK4 is best, stands for Runge-Kutta)
# Next goal, to get RK4, then using smt diff not for loops, for loops are slow


# Matplotlib is used to graph stuff

from matplotlib import pyplot as plt
from math import sqrt  # math gives a sqrt function

N = 7000
GM = 3.986e5


# Creating the arrays (basically to let values set somewhere - point of arrays, kinda like spreadsheet)

vx = [0] * N
vy = [0] * N
x = [0] * N
y = [0] * N
t = [0] * N

# Initialioze values

# radius is 6378, orbit say at 6878
x[0] = 6878  # km
y[0] = 0
vx[0] = 0
vy[0] = 11.2  # km/s

# vy is the instantaneous velocity at the start

h = 1  # sec


for n in range(0, N - 1):
    r = sqrt(x[n]**2 + y[n]**2)

    vx[n+1] = vx[n] - ((GM * x[n])/(r**3)) * h
    x[n+1] = x[n] + vx[n] * h

    vy[n+1] = vy[n] - ((GM * y[n])/(r**3)) * h
    y[n+1] = y[n] + vy[n] * h

    t[n+1] = t[n] + h


plt.plot(x, y)

earth = plt.Circle((0, 0), 6378)
plt.plot(x, y, "k")
plt.gca().add_artist(earth)
plt.gca().set_aspect(1)
# get current access = gca


plt.show()


# notice when run, takes a sec to plot, solver is slow
# error bc of euler's method is accumulating in the overlap of orbit
