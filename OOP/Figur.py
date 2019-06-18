

class Figur:
    namelist=""
    kunststuecke=""

    def __init__(self,namelist,kunststuecke):
        self.namelist=namelist
        self.kunststuecke=kunststuecke

    def __str__(self):
        return "Ich bin "+self.namelist+" und ich kann "+self.kunststuecke
        





