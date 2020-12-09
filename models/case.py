import random

class Case():
    def __init__(self, s_CaseId, i_DiagnosedOn):
        # Initializations
        self.s_CaseId           = s_CaseId
        self.i_DiagnosedOn      = i_DiagnosedOn
        self.i_RemovedOn        = 0
        self.i_ActiveFor        = 0
        self.b_Survived         = True

        # Constructions
        self.setRemovedOn()
        self.setSurvived()
        self.setActiveFor()

    def setRemovedOn(self):
        # We need to generate a random number between 0 and 100
        i_Random = random.randint(0,100)
        if i_Random <= 1:
            self.i_RemovedOn = self.i_DiagnosedOn+1
        elif i_Random > 1 and i_Random <= 3:
            self.i_RemovedOn = self.i_DiagnosedOn+2
        elif i_Random > 3 and i_Random <= 6:
            self.i_RemovedOn = self.i_DiagnosedOn+3
        elif i_Random > 6 and i_Random <= 12:
            self.i_RemovedOn = self.i_DiagnosedOn+4
        elif i_Random > 12 and i_Random <= 24:
            self.i_RemovedOn = self.i_DiagnosedOn+5
        elif i_Random > 24 and i_Random <= 48:
            self.i_RemovedOn = self.i_DiagnosedOn+6
        elif i_Random > 48 and i_Random <= 72:
            self.i_RemovedOn = self.i_DiagnosedOn+7
        elif i_Random > 72 and i_Random <= 78:
            self.i_RemovedOn = self.i_DiagnosedOn+8
        elif i_Random > 78 and i_Random <= 90:
            self.i_RemovedOn = self.i_DiagnosedOn+9
        elif i_Random > 90 and i_Random <= 100:
            self.i_RemovedOn = self.i_DiagnosedOn+10

    def setSurvived(self):
        i_Random = random.randint(0,101)
        if i_Random < 95:
            return True
        else:
            return False

    def setActiveFor(self):
        self.i_ActiveFor = self.i_RemovedOn - self.i_DiagnosedOn

    def getsRemovedToday(self, i_CurrentDayNum):
        print(f"{self.i_RemovedOn} -> {i_CurrentDayNum}")
        if self.i_RemovedOn == i_CurrentDayNum:
            self.b_GetsRemovedToday = True
        else:
            self.b_GetsRemovedToday = False
        return self.b_GetsRemovedToday

    def __str__(self):
        return f"Diagnosed on: {self.i_DiagnosedOn}, Removed on: {self.i_RemovedOn}, Active for: {self.i_ActiveFor}"
        