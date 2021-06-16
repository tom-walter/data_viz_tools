import matplotlib.pyplot as plt
import numpy as np

seed = 3.14
time = np.arange(40)
auto_correlated = np.empty_like(time, dtype='float')

for t in time:
    plt.clf()
    auto_correlated[t] = seed + np.random.normal(loc=0, scale=2.0, size=1)
    seed = auto_correlated[t]

    plt.xlim(0, 40)
    plt.ylim(-5, 15, 1)

    plt.title('Portfolio Gains/Losses')
    if auto_correlated[t] >= 0:
        plt.plot(time[:t+1], auto_correlated[:t + 1], color='g')
    else:
        plt.plot(time[:t + 1], auto_correlated[:t + 1], color='r')
    if auto_correlated[t] >= auto_correlated[t-1]:
        plt.plot(time[t], auto_correlated[t], color='g', marker='^')
    else:
        plt.plot(time[t], auto_correlated[t], color='r', marker='v')

    plt.hlines(0, 0, 40, ls='--', colors='k')
    plt.grid(alpha=.5)
    plt.text(t, auto_correlated[t]*1.1, "${:.2f}".format(auto_correlated[t]), ha='center')
    plt.savefig('ts' + str(t) + '.jpg', facecolor='white', format='jpg')
    plt.pause(0.1)

plt.show()
