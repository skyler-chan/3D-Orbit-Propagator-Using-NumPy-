# Faulty version of RK2


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

# Initialize values

# radius is 6378, orbit say at 6878
x[0] = 6878  # km
y[0] = 0
vx[0] = 0
vy[0] = 7.7  # km/s

# vy is the instantaneous velocity at the start

h = 1  # sec


for n in range(0, N - 1):

    # RK 1 Step

    # In order to get accel from the init point, we need the
    # radius of the spacecraft from the earth at init point
    r = sqrt(x[n]**2 + y[n]**2)

# Slopes from starting point
    kx1 = vx[n]
    ky1 = vy[n]
    kvx1 = - GM / r**3 * x[n]
    kvy1 = - GM / r**3 * y[n]

    # Euler step to the next point, for purposes of estimating slope.
    x1 = x[n] + kx1 * h
    y1 = y[n] + ky1 * h
    vx1 = vx[n] + kvx1 * h
    vy1 = vy[n] + kvy1 * h

    r1 = sqrt(x1**2 + y1**2)

    # Slopes frmo the next point
    kx2 = vx1
    ky2 = vy1
    kvx2 = - GM / r1**3 * x1
    kvy2 = - GM / r1**3 * y1

    # Put it all together
    x[n+1] = x[n] + h * 1/2 * (kx1 + kx2)
    y[n+1] = y[n] + h * 1/2 * (ky1 + ky2)
    vx[n+1] = vx[n] + h * 1/2 * (kvx1 + kvx2)
    vy[n+1] = vy[n] + h * 1/2 * (kvy1 + kvy2)

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
