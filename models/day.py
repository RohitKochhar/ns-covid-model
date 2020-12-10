from models.case import Case

class Day():
    def __init__(self, i_DayNumber, i_NewCases, a_ActiveCases):
        # This is data from our input array, i_DayNumber is the idx 
        #                                and i_NewCases is the value
        self.i_DayNumber            = i_DayNumber
        self.i_NewCases             = i_NewCases

        # Constructions

        # We need to create as many new cases objects as we are told to
        self.a_NewCases  = []
        self.setNewCases()

        # Now we compile a new list of total active cases
        self.a_ActiveCases  = []
        self.constructActiveCases(a_ActiveCases)

        # We need to check how many of our cases have recovered
        self.a_Recoveries = []
        self.setRecoveries()

        self.f_Transmission    = 0
        self.setZone()

        self.updateActiveCases()

    def setZone(self):
        if len(self.a_ActiveCases) >= 100:
            self.s_Zone             = "RED"
            self.f_Transmission     = 0.05
            return
        elif len(self.a_ActiveCases) >= 50 and len(self.a_ActiveCases) < 100:
            self.s_Zone             = "ORANGE"
            self.f_Transmission     = 0.10
            return
        else:
            self.s_Zone             = "YELLOW"
            self.f_Transmission     = 0.15
            return        

    def setNewCases(self):
        # Repeat as many times as specified in self.i_NewCase
        for i_CaseNum in range(0, self.i_NewCases):
            o_Case      =   Case(
                s_CaseId        = f"{self.i_DayNumber}-{i_CaseNum}",
                i_DiagnosedOn   = self.i_DayNumber
            )
            self.a_NewCases.append(o_Case)

    def constructActiveCases(self, a_PrevActiveCases):
        for o_Case in a_PrevActiveCases:
            self.a_ActiveCases.append(o_Case)
        for o_Case in self.a_NewCases:
            self.a_ActiveCases.append(o_Case)

    def updateActiveCases(self):
        for o_Case in self.a_Recoveries:
            self.a_ActiveCases.remove(o_Case)

    def setRecoveries(self):
        self.i_NumRecoveries    = 0
        for o_Case in self.a_ActiveCases:
            if o_Case.getsRemovedToday(self.i_DayNumber) == True:
                self.a_Recoveries.append(o_Case)


    def __str__(self):
        return f"Day #{self.i_DayNumber} |\t{self.i_NewCases} reported \t\t Active Cases: {len(self.a_ActiveCases)} \t\t Operating in {self.s_Zone} zone"
