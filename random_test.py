import random
import numpy as np

class TestObj:

    def __init__(self):
        self.a = True
        self.b = True

def random_selection_generation(size):
    selection = []
    for i in range(size):
        num = random.gammavariate(alpha=0.5, beta=0.5) + 1
        selection.append(num)

    # selection = np.random.gamma(size=size, scale=0.1, shape=[1]) + 1

    fine_count = 0
    less_count = 0
    more_count = 0

    for num in selection:
        if num > 1.015 and num < 1.45:
            fine_count += 1
        elif num < 1.015:
            less_count += 1
        else:
            more_count += 1

    print('fine_count: ' + str(fine_count))
    print('less_count: ' + str(less_count))
    print('more_count: ' + str(more_count))

    print(min(selection))
    print(max(selection))

# random_selection_generation(1000)
a = TestObj()
print(a.__dict__)