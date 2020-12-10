from models.day import Day
import random

class Province():
    def __init__(self, a_CasesPerDay):
        # We need to create a day object for every
        #   entry in our a_CasesPerDay
        self.d_CaseHistory      = {}

        # We also need to closely monitor the active cases, individually
        self.d_ActiveCases      = {}

        # We will store these cases in the dictionary above
        #   This way we can access a day's historys by Province.d_CaseHistory[day-1]

        print(f"Day # \t\tNew Cases\t\tActive Cases\t\tOperation Zone")
        print("--------------------- Confirmed Govt Data          -------------------")
        for self.i_Cursor in range(0, len(a_CasesPerDay)):
            # The day will inherit a lot from the province
            o_Day   = Day(i_DayNumber=self.i_Cursor, i_NewCases=a_CasesPerDay[self.i_Cursor], d_ActiveCases=self.d_ActiveCases, d_PreviousData=self.d_CaseHistory)
            
            self.d_ActiveCases = o_Day.d_ActiveCases

            self.d_CaseHistory[f"day-{self.i_Cursor}"]   = o_Day
            print(self.d_CaseHistory[f"day-{self.i_Cursor}"])
    
        # End of interpolation ----------------------------------------------------------
        # Mark when our confirmed data ends ---------------------------------------------
        self.i_InputSignalEndIdx    = self.i_Cursor+1
        print("--------------------- Extrapolated Data          -------------------")
        for self.i_Cursor in range(self.i_InputSignalEndIdx, self.i_InputSignalEndIdx + 10):
            # Here we are predicting 10 days ahead
            o_Day = self.ProjectNextDay()
            self.d_CaseHistory[f"day-{self.i_Cursor}"]   = o_Day
            print(self.d_CaseHistory[f"day-{self.i_Cursor}"])

    def ProjectNextDay(self):
        i_ProjectedNewCases     =   self.ProjectNewCases()
        o_Day = Day(i_DayNumber=self.i_Cursor, i_NewCases=i_ProjectedNewCases, d_ActiveCases=self.d_ActiveCases, d_PreviousData=self.d_CaseHistory)
        return o_Day

    def ProjectNewCases(self):
        # We get yesterdays object
        o_Day               = self.d_CaseHistory[f"day-{self.i_Cursor-1}"]

        # Simulated total
        i_ProjectedCaseSum  = 0

        # For each active case...
        for i_Case in range(0, len(o_Day.d_ActiveCases)):
            # Generate a random number between 0 and 100
            i_Random = random.randint(0,100)
            if i_Random < 100*o_Day.f_Transmission:
                i_ProjectedCaseSum += 1

        return i_ProjectedCaseSum


