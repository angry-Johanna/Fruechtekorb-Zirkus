from Figur import *
import random

class Zirkus:
    zirkustruppe=[]
    kunststuecke=["den Handstand *macht Handstand*","das Rad schlagen *schlägt ein Rad*","den Rückwärtssalto *macht einen Rückwärtssalto*","den Affen machen *Ugha Ugha","Feuer spucken *spuckt Feuer*","Schwerter schlucken *schluckt ein Riesenschwert"]
    namelist = ["Flo","Winnie","Kevin","Sven","Johanna","Schmid","Ramsi","Keya"]
    dedoraliv2=False

    def __init__(self):
        while True:
            try:
                anzahl=int(input("Wie viele Artisten willst du sehen? "))
            except ValueError:
                self.dedoraliv2 = False
                break
            else:
                self.dedoraliv2 = True
                break
        if self.dedoraliv2:
            for i in range (anzahl):
                self.zirkustruppe.append(Figur(self.namelist[random.randint(0,(len(self.namelist)-1))],self.kunststuecke[random.randint(0,(len(self.kunststuecke)-1))]))
                print(str(self.zirkustruppe[i]))
                                         




