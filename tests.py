a_InputData = [1,5,8,11,11,37,16,14,9,14,10,15,10,17,11,15,6,4,8,7,6]
import random
import matplotlib.pyplot as plt

from models import Province, Case



def GetRecoveryDistribution():
    a_LengthOfSickness = []
    d_Results   =   {
                        "1": 0, "2": 0, "3": 0, 
                        "4": 0, "5": 0, "6": 0,
                        "7": 0, "8": 0, "9": 0, "10": 0
                     }
    for i in range(0, 100):
        o_Case = Case(1)
        a_LengthOfSickness.append(o_Case.i_ActiveFor)
        d_Results[f"{o_Case.i_ActiveFor}"]  += 1

    a_XValues = []
    a_YValues = []

    for i in range(0, len(d_Results)):
        a_XValues.append(1 + i)
        a_YValues.append(d_Results[f"{1+i}"])
    
    plt.bar(a_XValues, a_YValues)
    
GetRecoveryDistribution()