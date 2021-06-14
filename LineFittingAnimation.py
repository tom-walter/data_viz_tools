import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import random
import numpy as np

plt.style.use('ggplot')

reg = LinearRegression()

x_vals = list()
y_vals = list()

for i in range(1000):
    plt.clf()
    x_vals.append(random.randint(0, 100))
    y_vals.append(random.randint(0, 100))

    x = np.array(x_vals).reshape(-1, 1)
    y = np.array(y_vals).reshape(-1, 1)

    if i % 20 == 0:
        reg.fit(x, y)
        plt.xlim(0, 100)
        plt.ylim(0, 100)
        plt.scatter(x_vals, y_vals, s=5)
        plt.plot(list(range(100)), reg.predict(np.array([x for x in range(100)]).reshape(-1, 1)), ls='--', color='b')
        plt.savefig('line' + str(i) + '.jpg', facecolor='white', format='jpg')
        plt.pause(0.001)

plt.show()
