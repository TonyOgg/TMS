# 1

import random

def some_fn(a, b):
    c = a + b
    x = random.randint(1, 100)
    return c / x

def some_fn2(a):
    c = a ** 3
    z = c / random.randint(1, 100)
    return z

m = random.randint(1, 100)
k = random.randint(1, 100)
y = some_fn(m, k)
d = some_fn2(y)
y = y + 1
print("y ravno " + str(y))

# 2

"""def fucktorial(x):
    if x == 0:
        return 1
    else:
        y = fucktorial(x - 1)
        z = x * y
        return z

print(fucktorial(3))"""


# 3



"""def reduce(fn, ls, acc):
    if len(ls) == 0:
        return acc
    else:
        new_acc = fn(ls[0], acc)
        ls_without_first_element = ls[1:]
        result = reduce(fn, ls_without_first_element, new_acc)
        return result


def pluserED(a, b):
    return a + b


print(reduce(pluserED, [1, 3, 5], 0))"""

