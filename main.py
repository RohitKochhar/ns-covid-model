a_InputData = [1,5,8,11,11,37,16,14,9,14,10,15,10,17,11,15,6,4,8,7,6]
import random
import matplotlib.pyplot as plt

from models import Province, Case

# We need to contain all our data within a Province object
#   This object takes in our input array by default
print("Creating Province object...")
o_Province = Province(a_InputData)

print(f"Day # \t\tNew Cases\t\tActive Cases\t\tOperation Zone")
for i in range(0, len(a_InputData)):
    print(o_Province.d_CaseHistory[f"day-{i}"])


print("--------------------- Extrapolating Next Weeks Data ------------------")

print(f"Day # \t\tNew Cases\t\tActive Cases\t\tOperation Zone")
for i in range(len(a_InputData), len(a_InputData)+9):
    print(o_Province.d_CaseHistory[f"day-{i}"])