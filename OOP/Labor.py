import random
from Blume import *

class Labor():
    flower=[]
    namelist = ["Flo","Winnie","Kevin","Sven","Johanna","Schmid","Ramsi","Keya"]
    colourlist=["grün","gelb","rot","blau","violett","rosa","weiss","orange","schwarz"]
    typelist=["Fleischfresser","Herbivore","Karnivore","Topfpflanze","Vegi","Wasserpflanze","Kommunist"]

    def __init__(self):
        anzahl=int(input("Wie viele Blumen ziehst du? "))
        for i in range (anzahl):
            self.flower.append(Blume(self.namelist[(random.randint(0,(len(self.namelist)-1)))],self.colourlist[(random.randint(0,(len(self.colourlist)-1)))],random.randint(1,99),random.randint(2,50),self.typelist[(random.randint(0,(len(self.typelist)-1)))]))
            print(str(self.flower[i]))

z = Labor()
