#!/usr/bin/env python

from Frucht import *
import random
import time
from Zirkus import *
from Asciipicture import *

easteregg=""
a=Asciipicture('mi')

while easteregg !="jupi":

    a.asciigametitel()
    a.asciifruits()



    namen=input("Gib hier deinen Namen ein: ")
    if namen == "micycle" or namen =="Micycle" or namen =="minycle" or namen =="Minycle" or namen =="minicycle" or namen =="Minicycle" or namen =="mikeybikey" or namen =="Mikeybikey" or namen =="dinimueter":
        time.sleep(1)
        print("\nGratuliere!\nDu hast das unloesbare Game geknackt!")
        time.sleep(1)
        print("Hier kommt ein Zirkus!")
        time.sleep(1)
        a.asciitruppe()
        easteregg ="jupi"
        X=Zirkus()
        if not X.dedoraliv2:
            print("Macht nix!")
            print("Der Zirkus lebt trotzdem!")
            a.asciiaffe()

    else:
        class Fruechtekorb:
            fruchtekorb=[]
            frucht=["Mario","Melanie","MikeDerCoach","Micycle","Dani","Sevi"]
            zustand=["frisch","verrottet","schimmelig","unreif","perfekt","genau richtig"]
            herkunft=["der Schweiz","dem Ausland","dem Atlantis","dem Mars","der Erdatmosphaere","Spanien"]
            dedoraliv=False

            def __init__(self):
                while True:
                    try:
                        anzahl=int(input("\nWie viele Fruechte sollen in den Fruechtekorb? "))
                    except ValueError:
                        self.dedoraliv = False
                        break
                    else:
                        self.dedoraliv = True
                        break
                if self.dedoraliv:
                    for i in range (anzahl):
                        self.fruchtekorb.append(Frucht(self.frucht[random.randint(0,(len(self.frucht)-1))],self.zustand[random.randint(0,(len(self.zustand)-1))],self.herkunft[random.randint(0,(len(self.herkunft)-1))]))
                        print(str(self.fruchtekorb[i]))



        z=Fruechtekorb()

        if z.dedoraliv:
            time.sleep(3)
            print("\nÜberraschung! Es kommt ein Zirkus vorbei!\n")
            time.sleep(1)

            damokles=random.randint(0,1)

            if (damokles%2)==0:
                a.asciitruppe()
                x=Zirkus()
                time.sleep(1)
                if x.dedoraliv2:
                    time.sleep(3)
                    print("\nNach diesem tollen Zirkusauftritt gibst du den Artisten Fruechte von deinem Fruechtekorb.")
                    time.sleep(2)
                    print("\nDie Fruechte waren aber alle schon schimmelig.")
                    time.sleep(1)
                    print("\nDer Zirkus hat nicht ueberlebt.")
                    a.asciiskullded()
                if not x.dedoraliv2:
                        print("\nWegen deiner Unbedachten falschen Eingabe gab es eine Invasion der Ostschweizer.")
                        time.sleep(1)
                        a.asciikommunist()
                        time.sleep(1)
                        print("Der Zirkus hat nicht ueberlebt.")
                        time.sleep(1)
                        a.asciimuchskullded()

            else:
                print("Leider hat es ein Gasleck gegeben und der ganze Zirkus ist gestorben.")
                a.asciiskull()

        else:
            time.sleep(2)
            print("\nWegen deiner Unbedachten falschen Eingabe musste ein Zirkus sterben.")
            a.asciitruppeded()

    if easteregg=="jupi":
        time.sleep(2)
        a.asciicredits()

    else:
        time.sleep(2)
        a.asciigameover()
        time.sleep(2)
        restart=input("Druecke Enter um ein neues Spiel zu starten...")

