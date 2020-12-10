from models.case import Case

class Day():
    def __init__(self, i_DayNumber, i_NewCases, d_ActiveCases, d_PreviousData):
        # This is data from our input array, i_DayNumber is the idx 
        #                                and i_NewCases is the value
        self.i_DayNumber            = i_DayNumber
        self.i_NewCases             = i_NewCases

        self.d_PreviousData         = d_PreviousData

        # It takes 10 days the the restrictions to propogate
        self.i_RestrictionDelay     = 10

        # Constructions

        # We need to create as many new cases objects as we are told to
        self.d_NewCases  = {}
        self.setNewCases()

        # Now we compile a new list of total active cases
        self.d_ActiveCases  = d_ActiveCases
        self.constructActiveCases()

        self.setZone()
        self.setTransmission()


    def setZone(self):
        if len(self.d_ActiveCases) >= 100:
            self.s_Zone             = "RED"
            return
        elif len(self.d_ActiveCases) >= 50 and len(self.d_ActiveCases) < 100:
            self.s_Zone             = "ORANGE"
            return
        else:
            self.s_Zone             = "YELLOW"
            return        

    def setTransmission(self):
        i_RelevantDay   =   self.i_DayNumber - self.i_RestrictionDelay
        if i_RelevantDay <= 0:
            # We don't have data here, set transmission to 10%
            self.f_Transmission     = 0.10
        else:
            # Get the zone from the relevant day
            o_Day = self.d_PreviousData[f'day-{self.i_DayNumber - self.i_RestrictionDelay}']
            if o_Day.s_Zone == "RED":
                self.f_Transmission     = 0.05
            elif o_Day.s_Zone == "ORANGE":
                self.f_Transmission     = 0.075
            else:
                self.f_Transmission     = 0.15

    def setNewCases(self):
        # Repeat as many times as specified in self.i_NewCase
        for i_CaseNum in range(0, self.i_NewCases):
            self.d_NewCases[f"{self.i_DayNumber}-{i_CaseNum}"] = Case(
                s_CaseId        = f"{self.i_DayNumber}-{i_CaseNum}",
                i_DiagnosedOn   = self.i_DayNumber
            )

    def constructActiveCases(self):
        # Before this function is called, self.d_ActiveCases has all of yesterdays data
        for s_CaseId in self.d_NewCases:
            self.d_ActiveCases[s_CaseId] = self.d_NewCases[s_CaseId]

        a_Recoveries    = []

        for s_CaseId in self.d_ActiveCases:
            if self.d_ActiveCases[s_CaseId].getsRemovedToday(self.i_DayNumber) == True:
                a_Recoveries.append(s_CaseId)
        
        for s_RecoveredId in a_Recoveries:
            del self.d_ActiveCases[s_RecoveredId]

    def getNumberOfActiveCases(self):
        return len(self.d_ActiveCases)
        
    def __str__(self):
        return f"Day #{self.i_DayNumber} |\t{self.i_NewCases} reported \t\t Active Cases: {self.getNumberOfActiveCases()} \t\t Operating in {self.s_Zone} zone"
