a_InputData         = [1, 5, 8, 11, 11, 37, 16, 14, 9, 14, 10, 15, 10, 17, 11, 15, 6, 4, 8, 7,  6,  4,  9,  7,  6,  5]
a_ActualActiveCases = [0, 0, 0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0, 0, 71, 64, 65, 61, 59, 57]

import random
import matplotlib.pyplot as plt

from models import Province, Case

print("Creating Province object...")
o_Province = Province(a_InputData)

