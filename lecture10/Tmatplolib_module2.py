import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
fig, ax = plt.subplote()

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

line, = ax.plot(x, y)

def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))

ani = animation.funcAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()