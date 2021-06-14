import matplotlib.pyplot as plt
import random

values = [0] * 30

for i in range(30):
    values[i] = random.randint(0, 100)

    plt.xlim(0, 30)
    plt.ylim(0, 100)
    plt.bar(list(range(30)), values,
            # color="tab:blue" # use for stable color
            )
    plt.text(i, values[i], "{}".format(values[i]), ha='center')
    plt.savefig('bar'+str(i)+'.jpg', facecolor='white', format='jpg')
    plt.pause(0.001)

plt.show()