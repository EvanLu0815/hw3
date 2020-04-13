import matplotlib.pyplot as plt
import numpy as np
import serial
import time

x = np.arange(0, 100, 1)
y = np.arange(0, 100, 1)
z = np.arange(0, 100, 1)
tilt = np.arange(0, 100, 1)
i = np.arange(0, 100, 1)

serdev = 'dev/ttyACM0'
s = serial.Serial(serdev);
for a in range(0, 100):
    line = s.readline()
    x[i] = float(line)
    line = s.readline()
    y[i] = float(line)
    line = s.readline()
    z[i] = float(line)
    line = s.readline()
    tilt[i] = int(line)

fig, ax = plt.subplots(2, 1)
ax[0].plot(i, x)
ax[0].plot(i, y)
ax[0].plot(i, z)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[0].legend('x', 'y', 'z')
ax[1].plot(i, tilt)
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')