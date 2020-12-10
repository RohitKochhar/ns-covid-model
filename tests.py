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
    
def SimulateDistribution():
    print("Creating Province object...")
    o_Province = Province(a_InputData)

    print(f"Day # \t\tNew Cases\t\tActive Cases\t\tOperation Zone")
    
    i_AverageFinalVaue  =   0
    for i in range(0, 1000):
        for i in range(0, len(a_InputData)):
            print(o_Province.d_CaseHistory[f"day-{i}"])
            i_FinalActiveCases = len(o_Province.d_CaseHistory[f"day-{i}"].a_ActiveCases)        
        i_AverageFinalVaue += i_FinalActiveCases
    print(i_AverageFinalVaue/1000)


SimulateDistribution()