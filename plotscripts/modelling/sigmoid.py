import numpy as np

def a(x, a, b, c):
     y = c / (1 + np.exp(-b*(x-a)))
     return y
