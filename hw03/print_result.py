import matplotlib.pyplot as plt
import numpy as np
import serial
import time

x = np.arange(0, 100, 1, dtype=float)
y = np.arange(0, 100, 1, dtype=float)
z = np.arange(0, 100, 1, dtype=float)
tilt = np.arange(0, 100, 1, dtype=int)
i = np.arange(0, 100, 1, dtype=int)

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 115200)
for a in range(100):
    line = s.readline()
    x[a] = float(line)
    line = s.readline()
    y[a] = float(line)
    line = s.readline()
    z[a] = float(line)
    line = s.readline()
    tilt[a] = int(line)

fig, ax = plt.subplots(2, 1)
ax[0].plot(i, x, color='blue', linewidth = 1, label = 'x')
ax[0].plot(i, y, color='red', linewidth = 1, label = 'y')
ax[0].plot(i, z, color='green', linewidth = 1, label = 'z')
ax[0].legend(loc='lower left')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[1].stem(i, tilt)
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')
plt.show()
s.close()