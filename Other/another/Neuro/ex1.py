import numpy as np


def act(x):
    return 0 if x < 0.5 else 1


def go(house, rock, attr):
    x = np.array([house, rock, attr])
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]
    weight1 = np.array([w11, w12])  # matrix 2x3
    weight2 = np.array([-1, 1])  # vector 1x2

    sum_hidden = np.dot(weight1, x)  # calculate the sum at the inputs of the hidden layer
    print("Значения сумм на нейронах скрытого слоя: "+str(sum_hidden))

    out_hidden = np.array([act(x) for x in sum_hidden])
    print("Значения на выходах нейронов скрытого слоя "+str(out_hidden))

    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)
    print("Выходное значение нейронной сети: "+str(y))

    return y


house = 1
rock = 0
attr = 1

result = go(house, rock, attr)

if result == 1:
    print("I love you")
else:
    print("Goodbye...")
