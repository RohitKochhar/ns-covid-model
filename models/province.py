from models.day import Day

class Province():
    def __init__(self, a_CasesPerDay):
        # We need to create a day object for every
        #   entry in our a_CasesPerDay
        self.d_CaseHistory      = {}

        # We also need to closely monitor the active cases
        self.a_ActiveCases      = []

        # We will store these cases in the dictionary above
        #   This way we can access a day's historys by Province.d_CaseHistory[day-1]
        for idx in range(0, len(a_CasesPerDay)):
            # The day will inherit a lot from the province
            o_Day   = Day(i_DayNumber=idx, i_NewCases=a_CasesPerDay[idx], a_ActiveCases=self.a_ActiveCases)

            # For each day, update our active cases
            self.UpdateActiveCases(o_Day.a_ActiveCases)

            self.d_CaseHistory[f"day-{idx}"]   = o_Day

    def UpdateActiveCases(self, a_DailyNewCases):
        self.a_ActiveCases = a_DailyNewCases


