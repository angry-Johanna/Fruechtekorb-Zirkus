import random
from Blume import *

class Labor():
    flower=[]
    namelist = ["Flo","Winnie","Kevin","Sven","Johanna","Schmid","Ramsi","Keya"]
    colourlist=["grün","gelb","rot","blau","violett","rosa","weiss","orange","schwarz"]
    typelist=["Fleischfresser","Herbivore","Karnivore","Topfpflanze","Vegi","Wasserpflanze","Kommunist"]

#Abfrage nach Werten des Gewächses
    def __init__(self):

#Abfrage nach Farbe
        while True:
            try:
                farbzahl=int(input("Was für eine Farbe hättest du gerne?\n1: "
                                   +"Grün\n2: Gelb\n3: Rot\n4: Blau\n5: Violett\n"
                                   +"6: Rosa\n7: Weiss\n8: Orange\n9: Schwarz\n"))
                if farbzahl >=1 and farbzahl <=9:
                    break
                else:
                    print("Bitte gib eine Zahl zwischen 1 bis 9 ein für eine Farbe.")
            except ValueError:
                print("Bitte gib eine Zahl ein für eine Farbe.")
        farbzahl=farbzahl-1

#Abfrage nach groesse
        while True:
            try:
                groessezahl=int(input("Wie gross soll deine Pflanze sein?\n"))
                if groessezahl >=5 and groessezahl <=20:
                    break
                else:
                    print("Bitte gib eine Zahl zwischen 5 bis 20 ein.")
            except ValueError:
                print("Bitte gib eine Zahl ein.")

#Abfrage nach anzahl Bluetenblaetter
        while True:
            try:
                blaetterzahl=int(input("Wie viele Blätter hat dein Gewächs?\n"))
                if blaetterzahl >=4 and blaetterzahl <=15:
                    break
                else:
                    print("Bitte gib eine Zahl zwischen 4 bis 15 ein.")
            except ValueError:
                print("Bitte gib eine Zahl ein.")

#Abfrage nach typ
        while True:
            try:
                typzahl=int(input("Was für einen Typ Gewächs hättest du gerne?\n1: "
                                   +"Fleischfresser\n2: Herbivore\n3: Karnivore\n4: Topfpflanze\n5: Vegi\n"
                                   +"6: Wasserpflanze\n7: Kommunist\n"))
                if typzahl >=1 and typzahl <=7:
                    break
                else:
                    print("Bitte gib für den Typ eine Zahl zwischen 1 bis 7 ein.")
            except ValueError:
                print("Bitte gib für den Typ eine Zahl ein.")
        typzahl=typzahl-1      
                            
                
        self.flower.append(Blume(self.namelist[(random.randint(0,(len(self.namelist)-1)))],self.colourlist[farbzahl],groessezahl,blaetterzahl,self.typelist[typzahl]))
        print(str(self.flower[0]))

z = Labor()
