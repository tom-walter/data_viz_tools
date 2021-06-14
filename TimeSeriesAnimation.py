import matplotlib.pyplot as plt
import numpy as np

seed = 3.14
time = np.arange(40)
lagged = np.empty_like(time, dtype='float')

for t in time:
    plt.clf()
    lagged[t] = seed + np.random.normal(loc=0, scale=2.0, size=1)
    seed = lagged[t]

    plt.xlim(0, 40)
    plt.ylim(-5, 16, 1)

    plt.title('Stock Gains/Loss')
    plt.plot(time[:t+1], lagged[:t+1], color='k')
    plt.plot(time[t], lagged[t], color='k', marker='o')
    plt.grid(alpha=.5)
    plt.text(t, lagged[t], "{:.2f}$".format(lagged[t]), ha='center')
    plt.savefig('ts' + str(t) + '.jpg', facecolor='white', format='jpg')
    plt.pause(0.001)

plt.show()
