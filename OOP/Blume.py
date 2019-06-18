
class Blume():
    name = ""
    farbe = ""
    groesse = 0
    anzBlaetter = 0
    typ = ""

    def __init__(self, namelist, colourlist, groesse, anzBlaetter, typelist):
        self.namelist = namelist
        self.colourlist = colourlist
        self.groesse = groesse
        self.anzBlaetter = anzBlaetter
        self.typelist = typelist

    def __str__(self):
        return "Gewächs "+self.namelist+" ist "+self.colourlist+", "+str(self.groesse)+"cm gross, hat "+str(self.anzBlaetter)+" Blätter und ist vom Typ "+self.typelist+"."
