import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')


for i in range(100):
    plt.clf()

    x = np.linspace(0, 3, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))

    plt.xlim(0, 3, 0.5)
    plt.ylim(-1.5, 1.5, 0.5)
    plt.plot(x, y, c='lime', lw=3)
    plt.grid(b=True, lw=.5)
    # plt.savefig('sinus' + str(i) + '.jpg', facecolor='black', format='jpg')
    plt.pause(0.001)

plt.show()