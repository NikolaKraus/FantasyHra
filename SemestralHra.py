#!/usr/bin/python3
import time
import re
import pickle
import os.path
import os
import random

class Postava: #trida pro vytvoreni postavy a ulozeni postupu ve hre
#oblast pro ulozeni informaci o postave
    sila = 0
    obratnost = 0
    odolnost = 0
    inteligence =0
    zivotyMax= 0#maximalni mnozstvi zivotu
    zivotyAkt= 0#aktualni stav zivotu
    zkusenosti = 0#zkusenosti ziskane za souboje
    zkBody = 0#zkusenostni body ziskane za dosazeni urovne
    uroven = 0#uroven postavy vypocitana z mnozstvi dosazenych zkusenosti
    rasa = ""#vybrana rasa
    typRasa = ["Hobit ", "Kudún ", "Trpaslík ","Elf ","Člověk ", "Barbar", "Kroll"]# rasy postav za ktere je mozno hrat
    prace = ""#vybrana prace
    typPrace  = ["válečník", "hraničář", "alchymista", "kouzelník", "zloděj"]#moznosti prace
    misto0 = "" #pro posun ve hre
    misto1 = "" #pro posun ve hre
    misto2 = "" #pro posun ve hre
    misto3 = "" #pro posun ve hre
    misto4 = "" #pro posun ve hre
    misto5 = "" #pro posun ve hre
    misto6 = "" #pro posun ve hre
    misto7 = "" #pro posun ve hre
    mince = 0
    protivnik0 = True #seznam zneskodnenych protivniku
    protivnik1 = True
    protivnik2 = True
    protivnik3 = True
    protivnik4 = True
    protivnik5 = True
    protivnik6 = True
    protivnik7 = True
    protivnik8 = True
    protivnik9 = True
    protivnik10 = True
    protivnik11 = True
#oblast pro ulozeni informaci o postave konec

    def nactiProt(self):#oziveni protivniku
        protivnik0 = True
        protivnik1 = True
        protivnik2 = True
        protivnik3 = True
        protivnik4 = True
        protivnik5 = True
        protivnik6 = True
        protivnik7 = True
        protivnik8 = True
        protivnik9 = True
        protivnik10 = True
        protivnik11 = True

    def vlastnosti(self, sila, obratnost, odolnost, inteligence, zivoty, uroven): #pro prirazeni vlastnosti
        self.sila = sila
        self.obratnost = obratnost
        self.odolnost = odolnost
        self.inteligence = inteligence
        self.zivotyMax = zivoty
        self.zivotyAkt = zivoty
        self.uroven = uroven
    
    def pricVlast(self, sila, obratnost, odolnost, inteligence, zivoty, uroven): #navyseni hodnoty vlastnosti
        self.sila += sila
        self.obratnost += obratnost
        self.odolnost += odolnost
        self.inteligence += inteligence
        self.zivotyMax += zivoty
        self.zivotyAkt += zivoty
        self.uroven += uroven
    
    def vypisVlast(self): #vypise vlastnosti pri vybrani rasy a povolani
        self.vypocUroven()
        print("Vaše vlastnosti jsou:")
        print("Úroveň "+str(self.uroven))
        print("Životy "+str(self.zivotyAkt))
        print("Síla = "+str(self.sila)+"-"+str(self.sila+5))
        print("Obratnost = "+str(self.obratnost)+"-"+str(self.obratnost+5))
        print("Odolnost = "+str(self.odolnost)+"-"+str(self.odolnost+5))
        print("Inteligence = "+str(self.inteligence)+"-"+str(self.inteligence+5))
    
    def vypisPreh(self): #vypise prehled v menu
        self.vypocUroven()
        print("Vaše vlastnosti jsou:")
        print("Postava - "+self.typRasa[int(self.rasa)-1]+" "+self.typPrace[int(self.prace)-1])
        print("Úroveň "+str(self.uroven))
        print("Životy "+str(self.zivotyAkt)+"/"+str(self.zivotyMax))
        print("Síla = "+str(self.sila)+"-"+str(self.sila+5))
        print("Obratnost = "+str(self.obratnost)+"-"+str(self.obratnost+5))
        print("Odolnost = "+str(self.odolnost)+"-"+str(self.odolnost+5))
        print("Inteligence = "+str(self.inteligence)+"-"+str(self.inteligence+5))
        print("Majetek : "+str(self.mince)+" mincí")
    
    def vyberRasy(self): #Vybere se rasa
        self.rasa = ""
        while not ((self.rasa == "1")|(self.rasa == "2")|(self.rasa == "3")|(self.rasa == "4")|(self.rasa == "5")|(self.rasa == "6")|(self.rasa == "7")):
            print ("Vyberte si rasu za kterou budete hrát :") #Nazev menu
            for i in range(0,len(self.typRasa)):
                print(" "+str(i+1)+". "+self.typRasa[i]+"")#vypis volby ras
            self.rasa = input("  Zadejte číslo : ")
            if self.rasa == "1":
                self.vlastnosti(3,11,8,10,1,1)
            else:
                if self.rasa == "2":
                    self.vlastnosti(5,10,10,9,1,1)
                else:
                    if self.rasa == "3":
                        self.vlastnosti(7,7,12,8,1,1)
                    else:
                        if self.rasa == "4":
                            self.vlastnosti(6,10,6,12,1,1)
                        else:
                            if self.rasa == "5":
                                self.vlastnosti(6,9,9,10,1,1)
                            else:
                                if self.rasa == "6":
                                    self.vlastnosti(10,8,11,6,1,1)
                                else:
                                    if self.rasa == "7":
                                        self.vlastnosti(11,5,13,2,1,1)
                                    else:
                                        print("Zadal jste špatné číslo, zkuste to znovu")# nahlaseni chyby
                                        self.pockej(4)
        #konec while rasa
        print("\n")
        self.vypisVlast() #vypise vlastnosti vybrane rasy

    def vyberPovolani(self): #vybere se povolani
        self.prace = ""
        while not ((self.prace == "1")|(self.prace == "2")|(self.prace == "3")|(self.prace == "4")|(self.prace == "5")):
            print("Vyberte povolání za které budete hrát :") #Nazev menu
            for i in range(0,len(self.typPrace)):
                print(" "+str(i+1)+". "+self.typPrace[i]+"")#vypis volby prace
            self.prace = input("  Zadejte číslo : ") # Zadani hodnoty
            if self.prace == "1":
                    if self.rasa == "1":
                        self.vlastnosti(8,11,13,10,20,1)
                    else:
                        if self.rasa == "2":
                            self.vlastnosti(10,10,14,9,20,1)
                        else:
                            if self.rasa == "3":
                                self.vlastnosti(14,7,16,8,20,1)
                            else:
                                if self.rasa == "4":
                                    self.vlastnosti(13,10,9,12,20,1)
                                else:
                                    if self.rasa == "5":
                                        self.vlastnosti(13,9,13,10,20,1)
                                    else:
                                        if self.rasa == "6":
                                            self.vlastnosti(14,8,14,6,20,1)
                                        else:
                                            if self.rasa == "7":
                                                self.vlastnosti(16,5,16,2,20,1)
            else:
                if self.prace == "2":
                    if self.rasa == "1":
                        self.vlastnosti(6,11,8,11,16,1)
                    else:
                        if self.rasa == "2":
                            self.vlastnosti(8,10,10,10,16,1)
                        else:
                            if self.rasa == "3":
                                self.vlastnosti(12,7,12,9,16,1)
                            else:
                                if self.rasa == "4":
                                    self.vlastnosti(11,10,6,14,16,1)
                                else:
                                    if self.rasa == "5":
                                        self.vlastnosti(11,9,9,12,16,1)
                                    else:
                                        if self.rasa == "6":
                                            self.vlastnosti(12,8,11,12,16,1)
                                        else:
                                            if self.rasa == "7":
                                                self.vlastnosti(14,5,13,6,16,1)
                else:
                    if self.prace == "3":
                        if self.rasa == "1":
                            self.vlastnosti(3,15,12,10,14,1)
                        else:
                            if self.rasa == "2":
                                self.vlastnosti(5,14,13,9,14,1)
                            else:
                                if self.rasa == "3":
                                    self.vlastnosti(7,11,15,8,14,1)
                                else:
                                    if self.rasa == "4":
                                        self.vlastnosti(6,14,8,12,14,1)
                                    else:
                                        if self.rasa == "5":
                                            self.vlastnosti(6,13,12,10,14,1)
                                        else:
                                            if self.rasa == "6":
                                                self.vlastnosti(10,12,13,6,14,1)
                                            else:
                                                if self.rasa == "7":
                                                    self.vlastnosti(11,8,15,2,14,1)
                    else:
                        if self.prace == "4":
                            if self.rasa == "1":
                                self.vlastnosti(3,11,8,12,12,1)
                            else:
                                if self.rasa == "2":
                                    self.vlastnosti(5,10,10,12,12,1)
                                else:
                                    if self.rasa == "3":
                                        self.vlastnosti(7,7,12,11,12,1)
                                    else:
                                        if self.rasa == "4":
                                            self.vlastnosti(6,10,6,16,12,1)
                                        else:
                                            if self.rasa == "5":
                                                self.vlastnosti(6,9,9,14,12,1)
                                            else:
                                                if self.rasa == "6":
                                                    self.vlastnosti(10,8,11,6,12,1)
                                                else:
                                                    if self.rasa == "7":
                                                        self.vlastnosti(11,5,13,8,12,1)
                        else:
                            if self.prace == "5":
                                if self.rasa == "1":
                                    self.vlastnosti(3,16,8,10,12,1)
                                else:
                                    if self.rasa == "2":
                                        self.vlastnosti(5,15,10,9,12,1)
                                    else:
                                        if self.rasa == "3":
                                            self.vlastnosti(7,12,12,8,12,1)
                                        else:
                                            if self.rasa == "4":
                                                self.vlastnosti(6,15,6,12,12,1)
                                            else:
                                                if self.rasa == "5":
                                                    self.vlastnosti(6,14,9,10,12,1)
                                                else:
                                                    if self.rasa == "6":
                                                        self.vlastnosti(10,13,11,6,12,1)
                                                    else:
                                                        if self.rasa == "7":
                                                            self.vlastnosti(11,9,13,2,12,1)
                            else:
                                print("Zadal jste špatné číslo, zkuste to znovu")#hlaska o chybe
                                self.pockej(4)
        #konec while prace
        print("")
        self.vypisVlast()#vypise vlastnosti vybrane rasy

    def vypocUroven(self): #vypocitani urovne ze ziskanych zkusenosti
        if self.zkusenosti > (500+(75*self.uroven)): #pro ziskani dalsi urovne potrebuje hrac vice zkusenosti nez predtim
            self.zkusenosti = self.zkusenosti-(500+(75*self.uroven)) #odecteni zkusenosti
            self.pricVlast(0,0,0,0,self.nahoda(6)+1,1) #Zvisi se zdravi i úroveň
            self.zkBody = self.zkBody+5 #zkusenostni body pro uceni

    def nahoda(self,n):#vraceni nahodneho cisla v rozsahu 0-n
        return random.randrange(n)

    def pockej(self,x): #Pocka nejaky cas a pote algoritmus pokracuje dal
        time.sleep(x) #Ceka x sec

#konec tridy postava

#Deklarace hlavni program
#promenne
Ja = Postava() #vytvoreni objektu hlavni postavy
volba = ""#promenna vyuzita u zadani uzivatelem
prolog = True#promena boolean 
#promenne konec

#pomocne metody
def pockej(x): #Pocka nejaky cas a pote algoritmus pokracuje dal
    time.sleep(x) #Ceka x sec 

def tvorbaSloz(nazevSlozky):#vytvori slozku pokud neexistuje
    slozka = os.path.isdir(nazevSlozky)
    if not slozka:
        os.mkdir(nazevSlozky)

def nahoda(n):#vraci nahodnou hodnotu v rozsahu 0-n
    return random.randrange(n)

def posun(n): #Posun o n radku kvuli prehlednosti
    for i in range(0,n):
        print("")

def cistiObrazovku():#vycisti obrazovku v terminalu (win cmd)
    os.system('cls' if os.name == 'nt' else 'clear')

def stisk(): #Pokracovani po stisknuti klavesy
    print("")
    cil = input("pro pokračování stiskni : Enter") #pouze pro vyckani nez uzivatel bude chtit pokracovat

def vyprazdPol(): #vynulovani mista
    global Ja
    Ja.misto0 = ""
    Ja.misto1 = ""
    Ja.misto2 = ""
    Ja.misto3 = ""
    Ja.misto4 = ""
    Ja.misto5 = ""
    Ja.misto6 = ""
    Ja.misto7 = ""

def rovnostNehledeNaVelikost(slovo1,slovo2): #equalsIgnoreCase nerozlisovat velka a mala pismena
    return slovo1.upper() == slovo2.upper()

#pomocne metody konec

#Sekced prace se soubory

def nazvySoub(slozka): #vypsani drive ulozenych her
    print("Uložené hry :")
    list = os.listdir(slozka) #nacteni seznamu nazvu souboru do pole
    for i in range(len(list)):
        print(list[i][:-4])#vypise nazev bez pripony

#Sekce ukladani souboru
def autoUlozit(): #automaticke ulozeni hry
    pisDoSoub("save","autoSave.dat")

def tvorbaSoub( slozka, soubor):
    tvorbaSloz("save")#overeni existence slozky
    if os.path.exists(slozka+"/"+soubor): #test existence souboru
        prubeh = True
        while prubeh:
            cistiObrazovku()
            print("Přeješ si přepsat již uloženou pozici Ano(A)/Ne(N)?")
            znak = input("Zadej písmeno : ")
            if rovnostNehledeNaVelikost(znak,("A")): #potvrzeni prepsani existujici pozice
                pisDoSoub (slozka,soubor) #tvorba pozice(ulozeni)
                prubeh = False
            else: #v pripade odmitnuti ulozeni
                if rovnostNehledeNaVelikost(znak,("N")):
                    print("")
                    print("Ukládání neproběhlo")
                    prubeh = False
                else:#v pripade spatne zadaneho znaku vypis o chybe
                    print("Zadal jsi nesprávný znak! Zkus to znovu.")
                pockej(3)
    else:
        pisDoSoub(slozka,soubor) #tvorba pozice(ulozeni)

def ulozit(): #ulozeni rozehrane hry
    tvorbaSloz("save")#overeni existence slozky
    nazvySoub("save") #vypise jiz ulozene hry aby uzivatel mel prehled pouzitych nazvu
    nazev = input("Zadej název pozice : ") #nazev ukladane pozice
    if (nazev.strip()==""):#pokud jsou zadany pouze bile znaky neprijmout nazev
        print("Pozice se musí nějak jmenovat -> ukládání neproběhlo.")
        pockej(4)
    else:
        tvorbaSoub("save",nazev+".dat") #vytvori novou ulozenou pozici
                


def pisDoSoub ( slozka, soubor): #zapis objektu do souboru
    with open(slozka+"/"+soubor, 'wb') as output:#ulozeni objektu
        global Ja
        pickle.dump(Ja, output, pickle.HIGHEST_PROTOCOL)

#Konec ukladani souboru

#Sekce nacteni ze souboru
def nacist():
    tvorbaSloz("save")#overeni existence slozky
    nazvySoub("save")
    ctiZeSoub("save", input("Zadej název souboru : ")+".dat")

def ctiZeSoub( slozka, soubor):
    if os.path.exists(slozka+"/"+soubor): #test existence souboru
        with open(slozka+"/"+soubor, 'rb') as input:
            global Ja
            Ja = pickle.load(input)
    else:
        print("Tato pozice nexistuje!")
        pockej(3)
 
#Konec nacteni ze souboru
#Sekce mazani souboru
def smazat(): #mazani souboru
    nazvySoub("save")
    smazatSoub("save", input("Zadej název souboru : ")+".dat") #nacteni nazvu mazaneho souboru

def smazatSoub( slozka, soubor): #smazani souboru
    if os.path.exists(slozka+"/"+soubor):
        print("Opravdu si přeješ smazat tuto pozici? - "+soubor[:-4])
        if rovnostNehledeNaVelikost(input("Ano(A)/Ne(N) : "),"A"): #potvrzeni smazani
            os.remove(slozka+"/"+soubor) #smazani souboru
            print("Pozice "+soubor+" byla smazána") #vzpis o provedeni 
        else:
            print("Pozice "+soubor+" nebyla smazána") #vypis o provedeni
    else:
        print("Pozice: "+soubor[:-4]+" neexistuje!")
    pockej(3)

#Konec mazani souboru

#Konec prace se soubory

#vypisy
def zacVypis():#pouze strucny uvodni vypis
    cistiObrazovku()
    print("Semestrální práce")
    print("Fantasy slovní hra")
    print("")
    print("Zpracoval: Nikola Kraus")
    time.sleep(4)#Ceka 4 sec

def chybaZnak():
    print("Zadal jsi špatné číslo, zkus to znovu!!!") #varovani v pripade spatneho zadani znaku
    pockej(4) #cekani pro precteni varovani

def prehled(): #prehled o postave
    global Ja
    Ja.vypisPreh()
    stisk()

#def pomocR(): #pomaha k vypsani kodu mista
#    aktMisto = Ja.misto0+Ja.misto1+Ja.misto2+Ja.misto3+Ja.misto4+Ja.misto5+Ja.misto6+Ja.misto7
#    print(aktMisto)

def retezMapa(misto): #urceni mista vzskytu v Jeskyni
    global Ja
    #zjisteni kodu aktualniho mista postavy
    aktMisto = Ja.misto0+Ja.misto1+Ja.misto2+Ja.misto3+Ja.misto4+Ja.misto5+Ja.misto6+Ja.misto7
    if(misto == aktMisto):
        return "X" #postava se vyskytuje
    else:
        return " " #postava se nevyskytuje

def mapa(): #vykresleni mapy s pozici postavy
    print(" Mapa jeskyně")
    print("    Postava (X)")
    print("")
    print("")
    print("    .| |.")
    print("    .."+retezMapa("511122")+"..")
    print("    .| |   .| |.")
    print("    .."+retezMapa("51112")+"|   .."+retezMapa("513")+"..")
    print("    .| |....| |..")
    print("    .."+retezMapa("5111")+".."+retezMapa("511")+"..."+retezMapa("51")+"..  <--vchod do jeskyně")
    print("     ...| | | |")
    print("     ."+retezMapa("51121")+".."+retezMapa("5112")+"|")
    print("        | |")
    print("")
    stisk()

#vypisy konec
#tvorba postavy
def ZmenRozhod(): #dotaz na zmenu rozhodnuti
    print("Přeješ si změnit volbu?\n")  
    return input("pokud Ne(N) jinak \"Enter\" : ")

def tvorbaPost(): #vytvoreni nove postavy v Nove hre
    global Ja
    global prolog
    prolog = True #zapnuti prologu
    Ja.vlastnosti(0, 0, 0, 0, 0, 0) #Vynulovani vlastnosti
    vyprazdPol() #vyprazdni pameti s misty
    Ja.nactiProt() #Ozivy protivniky
    Ja.mince = 100+nahoda(50) #da postave mince (100-150)
    rozhodnuti = ""
    while not rovnostNehledeNaVelikost("N",rozhodnuti): #dokud uzivatel nezada N/n opakuje se cykl vyberu postavy
        cistiObrazovku()
        Ja.vyberRasy() #vybirani rasy
        rozhodnuti = ZmenRozhod()
    #konec vyberu rasy
    rozhodnuti = ""
    while not rovnostNehledeNaVelikost("N",rozhodnuti): #dokud uzivatel nezada N/n opakuje se cykl vyberu povolani
        cistiObrazovku()
        Ja.vyberPovolani() #vybirani povolani
        rozhodnuti = ZmenRozhod()
    #konec vyberu povolani

#tvorba postavy konec

#Sekce Menu
#Hl. Menu
def menu1(): #prvni menu ochraneno pred ulozenim mrtve postavy
    global volba
    cistiObrazovku()
    print("Menu:\n") #vypsani menu1
    print("  1. Nová hra\n")
    print("  2. Načíst pozici\n")
    print("  3. Smazat pozici\n")
    print("  4. Konec\n")
    volba = input("  Zadej číslo : ") #nacte volbu od uzivatele
    #provede volbu uzivatele
    if volba == "1": #posle do sekce vytvoreni postavy se zakladnimy schopnostmi
        cistiObrazovku()
        tvorbaPost()
        volba = "pribeh"
    else:
        if volba == "2": #sekce nacteni ulozene pozice
            cistiObrazovku()
            nacist()
        else:
            if volba == "3": #sekce pro mazani ulozenych pozic
                cistiObrazovku()
                smazat()
            else:
                if volba == "4": #ukonceni programu
                    cistiObrazovku()
                    volba = "konec"
                else:
                    chybaZnak() #varovny vypis

def menu2(): #menu 2 pro rezim hrani s yivou postavou
    global volba
    cistiObrazovku()
    print("Menu:\n") #vypsani menu
    print("  1. Nová hra\n")
    print("  2. Načíst pozici\n")
    print("  3. Uložit pozici\n")
    print("  4. Smazat pozici\n")
    print("  5. Přehled\n")
    print("  6. Mapa\n")
    print("  7. Pokračovat\n")
    print("  8. Konec\n")
    volba = input("  Zadej číslo : ") #nacteni volby uzivatele
    if volba == "1": #zacne novou hru sekce tvorba postavy
        cistiObrazovku()
        tvorbaPost()
        volba = "pribeh"
    else:
        if volba == "2": #nacteni ulozene pozice postavy
            cistiObrazovku()
            nacist()
        else:
            if volba == "3": #ulozeni momentalne rozehrane postavy
                cistiObrazovku()
                ulozit()
            else:
                if volba == "4": #smazani drive ulozenych postav
                    cistiObrazovku()
                    smazat()
                else:
                    if volba == "5": #vypise aktualni prehled o postave
                        cistiObrazovku()
                        prehled()
                    else:
                        if volba == "6": #vypise aktualni prehled o postave
                            cistiObrazovku()
                            mapa()
                        else:
                            if volba == "7": #posle postavu zpet do pribehove linky
                                cistiObrazovku()
                                volba = "pribeh"
                            else:
                                if volba == "8": #ukonci program
                                    cistiObrazovku()
                                    volba = "konec"
                                else:
                                    chybaZnak() #varovny vypis
#Konec Menu


#Sekce souboje
def boj( s, ob, od, i, z, u): #soubojovy rezim
    global Ja
    souper = Postava() #vznik soupere
    souper.vlastnosti(s, ob, od, i, z, u) #nacteni vlastnosti soupere
    utek = True #moznost uniku z boje s moznosti straty nekterych zivotu
    while not ((Ja.zivotyAkt<1) | (souper.zivotyAkt<1) | (utek==False)): #smrt hrace, smrt protivnika, utek
        posun(1)
        pocet = 1 #pocet provedeni souboju
        obratS = souper.obratnost+nahoda(6) #priradi souperi nahodnou obratnost
        odolS = souper.odolnost+nahoda(6) #priradi souperi nahodnou odolnost
        silS = souper.sila+nahoda(6) #priradi souperi nahodnou silu
        intelS = souper.inteligence+nahoda(6) #priradi souperi nahodnou inteligenci
        obratJ = Ja.obratnost+nahoda(6) #priradi hraci nahodnou obratnost
        odolJ = Ja.odolnost+nahoda(6) #priradi hraci nahodnou odolnost
        silJ = Ja.sila+nahoda(6) #priradi hraci nahodnou silu
        intelJ = Ja.inteligence+nahoda(6) #priradi hraci nahodnou inteligenci          
        cistiObrazovku()
        print("_Boj_") #vypsani soubojoveho menu
        print("  1. Úder")
        print("  2. Kouzlo")
        print("  3. Útěk")
        volbaUtoku = input("  Zadej číslo : ")
        if volbaUtoku == "1":
            if silJ-(((obratS*2)+odolS)/3)<1: #overeni zda souper ma mensi odolnost vuci uderu nez je hracova sila
                print("Protivník tvůj úder vykryl") #vypis neucinosti utoku
            else:
                souper.zivotyAkt=souper.zivotyAkt-(silJ-(((obratS*4)+odolS)/5))
                print("Uštědřil jsi protivníkovy zranení nyní má "+str(souper.zivotyAkt)+" životů") #vypis ztraty zivotu protivnika
        else:
            if volbaUtoku == "2":
                if intelJ-(((odolS*2)+obratS)/3)<1: #overeni zda souper ma mensi odolnost vuci kouzlu nez je hracova inteligence
                    print("a protivník se tvému kouzlu vyhnul") #vypis neucinosti utoku
                else:
                    souper.zivotyAkt = souper.zivotyAkt-(intelJ-(((odolS*4)+obratS)/5))
                    print("Uštědřil jsi protivníkovy zranení nyní má "+str(souper.zivotyAkt)+" životů") #vypis ztraty zivotu protivnika
            else:
                if volbaUtoku == "3":
                    #v pripade uteku
                    pocet = nahoda(3) #protivnik jeste 0-2x zautoci
                    utek = False #vyskoceni z cyklu
                    print("Než jsi stihl utéci Protivník na tebe ještě stihl zaútočit "+str(pocet)+"-krát.") #vypise kolikrat protivnik zautoci
                else:
                    pocet=0 #souboj se neprovede
                    chybaZnak() #varovny vypis
        while pocet>0: #pocet utoku od protivnika
            pocet -= 1
            posun(5)
            print("Protivník na tebe zaútočil ")
            if nahoda(2)==0: #nahodne rozodnuti zda protivnik zautoci uderem nebo kouzlem
                if silS-(((obratJ*2)+odolJ)/3)<1: #overeni zda hrac ma mensi odolnost vuci uderu nez je souperova sila
                    print("avšak ty jsi se jeho úderu vyhnul") #vypis neucinosti utoku
                else:
                    Ja.zivotyAkt=Ja.zivotyAkt-(silS-(((obratJ*4)+odolJ)/5))
                    print("a uštědžil ti zranění úderem - zbývá ti "+str(Ja.zivotyAkt)+" životů") #vypis ztraty zivotu hrace
            else:
                if intelS-(((odolJ*2)+obratJ)/3)<1: #overen zda hrac ma mensi odolnost vuci kouzlu nez je souperova inteligence
                    print("avšak ty jsi se jeho kouzlu vyhnul") #vypis neucinku utoku
                else:
                    Ja.zivotyAkt = Ja.zivotyAkt-(intelS-(((odolJ*4)+obratJ)/5))
                    print("a uštědžil ti zranění kouzlem - zbývá ti "+str(Ja.zivotyAkt)+" životů") #vypis ztraty zivotu hrace
            stisk()

    if Ja.zivotyAkt<1: #v pripade hracovi smrti
        print("Zemřel jsi KONEC HRY")
        Ja.misto0 = "menu"
    else:
        if (souper.zivotyAkt<1):
            print("Vyhrál jsi podařilo se ti zneškodnit nepřítele") #v pripade souperovi smrti
        else:
            print("Podařilo se ti utéci") #v pripade zdareneho uteku
    pockej(3)
    return souper.zivotyAkt #vraci protivnikovi zivoty ohledne udaje zda je protivnik mrtvy, kvuli plneni ukolu a vycisteni jeskyne
#Konec souboje

#Sekce pribeh
def hra(): #prvni cast rozcesti
    global Ja
    global prolog
    global volba
    while not Ja.misto0 == "menu": #cykl s moznosti vystupu do menu
        autoUlozit() #automaticke ulozeni hry
        if Ja.misto1 == "1":
            mesto()
        else:
            if Ja.misto1 == "2":
                baziny()
            else:
                if Ja.misto1 == "3":
                    hory()
                else:
                    if Ja.misto1 == "4":
                        hrbitov()
                    else:
                        if Ja.misto1 == "5":
                            jeskyne()
                        else:
                            if Ja.misto1 == "6": #moznost navratu do menu
                                Ja.misto0 = "menu"
                                Ja.misto1 = "" 
                            else: #pokud nebyla zatim zadana volba ci je volba nespravna provede se vypis vloby
                                cistiObrazovku()
                                if(prolog): #pri spusteni nove hry
                                    print("Probral ses uprostřed mýtiny. Slunce žhne ptáci zpívají") #vypis prologu
                                    print("a ty si vůbec nepamatuješ, kdo jsi ani co tu děláš, prostě")
                                    print("nic. Jediné co víš je, že tě hrozně bolí hlava. Rozhlížíš")
                                    print("se kolem sebe, voláš na všechny strany, ale jediný efekt této")
                                    print("snahy je, jen vyplašení všech ptáků a zvěře v tvém okolí.")
                                    print("Tak se vydáváš nají nějakou tu cestu z lesa. Po chvíli")
                                    print("konečně nalézáš konec lesa a při vylézání z keře tě ještě")
                                    print("na rozloučenou švíkne větev přes obličej. Vylezl jsi přímo")
                                    print("na rozcestí.")
                                    posun(2)
                                    stisk()
                                    prolog = False #vypnuti prologu
                                print("_Rozcestí_")
                                print("  1. Město")
                                print("  2. Smrtící bažiny")
                                print("  3. Nebeské hory")
                                print("  4. Hřbitov věčného úplňku")
                                print("  5. Jeskyně")
                                print("  6. Menu")
                                Ja.misto1 = input("  Zadej číslo : ") #nacteni volby
    volba = "" #pred vstupem do menu zajisteni prazdne promenne volba

#Sekce mesto
def mesto(): #lokace mesto
    global Ja
    while not ((Ja.misto0 == "menu") | (Ja.misto1 == "")): #vystup z cyklu v pripade nahledu do menu nebo vraceni se do puvodni lokace
        if Ja.misto2 == "1":
            hospoda()
        else:
            if Ja.misto2 == "2":
                cviciste()
            else:
                if Ja.misto2 == "3":
                    arena()
                else:
                    if Ja.misto2 == "4":
                        lekar()
                    else:
                        if Ja.misto2 == "5": #navrat do predchozi oblasti
                            Ja.misto1 = ""
                            Ja.misto2 = ""
                        else:
                            if Ja.misto2 == "6": #moznost navratu do menu
                                Ja.misto0 = "menu"
                                Ja.misto2 = ""
                            else: #pokud nebyla zatim zadana volba ci je volba nespravna provede se vypis vloby
                                cistiObrazovku()
                                print("Když přiješ na náměstí, nemůžeš skoro spustit oči")
                                print("z těch malebných domů a krásné kašny uprostřed.")
                                posun(2)
                                print("_Město_")
                                print("  1. Hospoda u kdákající kočky")
                                print("  2. Cvičiště")
                                print("  3. Arena")
                                print("  4. Lékař")
                                print("  5. Opustit město")
                                print("  6. Menu")
                                Ja.misto2 = input("  Zadej číslo : ")

def hospoda():
    global Ja
    while not((Ja.misto0 == "menu") | (Ja.misto2 == "")): #vystup z cyklu v pripade nahledu do menu nebo vraceni se do puvodni lokace
        if Ja.misto3 == "1":
            ukol()
            Ja.misto3 = ""
        else:
            if Ja.misto3 == "2":
                Ja.misto2 = ""
                Ja.misto3 = ""
            else:
                if Ja.misto3 == "3": #moznost navratu do menu
                    Ja.misto0 = "menu"
                    Ja.misto3 = ""
                else: #pokud nebyla zatim zadana volba ci je volba nespravna provede se vypis vloby
                    cistiObrazovku()
                    print("Chvíli ti trvá než se v šeru rozkoukáš. Náhle cítíš")
                    print("lahodnou vůni nějakého pokrmu co se připravuje v kuchyni.")
                    print("Pak se ale rozpomeneš, že máš svou práci, a tak se rozhlédneš")
                    print("po hospodě - a hele ona tu na okně opravdu nějaká kočka sedí.")
                    print("Ale za celou dobu co jsi uvnitř ta potvora nevidá ani hlásku.")
                    posun(2)
                    print("_Hospoda u kdákající kočky_")
                    print("  1. Poptat se na úkol")
                    print("  2. Jít na náměstí")
                    print("  3. Menu")
                    Ja.misto3 = input("  Zadej číslo : ")
        
def ukol(): #vypis aktualniho ukolu v hospode navazuji po sobe podle obtiznosti
    cistiObrazovku()
    global Ja
    print("Rozhlédneš se po místnosti a zamíříš si to přímo ke stolu")
    print("v rohu místnosti u kterého sedí nějaký tajemný hrbatý stařík.")
    posun(2)
    print("Jen co se přiblížíš ke stolu hned stařík spustí :")
    print("\"Zdravím tě cizinče.")
    if Ja.protivnik0:
        print("Vypadáš jako veliký hrdina. A já bych pro tebe měl ")
        print("nějakou tu práci. Už jsi byl v aréně?")
        print("Je tam jeden padouch, který mi dluží již mnoho")
        print("peněz a pořád se nemá ke splácení. Nedal bys mu místo")
        print("mne za vyučenou? Dříve bych se o to postaral sám,")
        print("ale teď již nemám tolik sil.")
    else:
        if Ja.protivnik1:
            print("Ještě že jdeš, za městem v bažinách se usídlila")
            print("hydra, mysliš že bys jí dokázal porazit?")
            print("Ale dej si pozor myslím že to nebude tak snadné,")
            print("jako zápasit s nějakým lapkou v aréně.")
        else:
            if Ja.protivnik2:
                print("No konečně, kde ses flakal? Z hor na náše")
                print("město útočí každou chvílí hypogrif. Honem")
                print("běž a usmrť ho.")
            else:
                if Ja.protivnik3:
                    print("Promiň že jsem byl s tou záležitostí")
                    print("ohledně hypogrifa tak nezdvořilý. Prosím")
                    print("přijmi mou omluvu. Znáš to, když se člověk bojí.")
                    print("Vlastně ty to asi moc neznáš. A mimochodem,")
                    print("blíží se uplněk, což znamená, že na našem")
                    print("hřbitově se budou probouzet mrtvý. Jo a kdyby")
                    print("tě to zajímalo, tak tam máme zakopané docela velké")
                    print("zbohatlíky, co si vzali své zlato s sebou do hrobu.")
                else:
                    print("Bohužel již pro tebe nemám žádné úkoly, ale slyšel jsem,")
                    print("že v té jeskyni co hlídá ten obr, se skrývá strašlivý drak")
                    print("a střeží si tam své ukradené zlato, ale což to ale prý tam")
                    print("je i mezi tím vším pokladem i nějaká sožka, která prý zodpoví všechny")
                    print("otázky. Možná by tě to mohlo zajímat.")
    stisk()
    
def cviciste():
    global Ja
    while not((Ja.misto0 == "menu") | (Ja.misto2 == "")): #vystup z cyklu v pripade nahledu do menu nebo vraceni se do puvodni lokace
        if Ja.misto3 == "1":
            if (Ja.zkBody>0)&(Ja.mince>9):
                Ja.sila=Ja.sila+1
                Ja.zkBody=Ja.zkBody-1
                Ja.mince=Ja.mince-10
            Ja.misto3 = ""
        else:
            if Ja.misto3 == "2":
                if (Ja.zkBody>0)&(Ja.mince>9):
                    Ja.obratnost=Ja.obratnost+1
                    Ja.zkBody=Ja.zkBody-1
                    Ja.mince=Ja.mince-10
                Ja.misto3 = ""
            else:
                if Ja.misto3 == "3":
                    if (Ja.zkBody>0)&(Ja.mince>9):
                        Ja.odolnost=Ja.odolnost+1
                        Ja.zkBody=Ja.zkBody-1
                        Ja.mince=Ja.mince-10
                    Ja.misto3 = ""
                else:
                    if Ja.misto3 == "4":
                        if (Ja.zkBody>0)&(Ja.mince>9):
                            Ja.inteligence=Ja.inteligence+1
                            Ja.zkBody=Ja.zkBody-1
                            Ja.mince=Ja.mince-10
                        Ja.misto3 = ""
                    else:
                        if Ja.misto3 == "5":
                            Ja.misto2 = ""
                            Ja.misto3 = ""
                        else:
                            if Ja.misto3 == "6":
                                Ja.misto0 = "menu"
                                Ja.misto3 = ""
                            else:
                                cistiObrazovku()
                                print("Už před branou cvičiště jsi slyšel strašlivý ryk zbraní")
                                print("a řevu. A teď, když jsi uvnitř, je to téměř k nesnesení.")
                                posun(2)
                                print("_Cvičiště_")
                                print("Máš "+str(Ja.zkBody)+" zkušenostních bodů a "+str(Ja.mince)+" mincí.")
                                print("")
                                print("Jen co k tobě trenér přijde hned jen tak bez okolků")
                                print("a bez pozdravu ti zdělí : ")
                                print("\"Každý trénink libovolné chopnosti stojí 10 zlatých Zelenáči.\"")
                                print("")
                                print(" Trénovat :")
                                print("  1. Sílu")
                                print("  2. obratnost")
                                print("  3. odolnost")
                                print("  4. inteligenci")
                                print("  5. Jít na náměstí")
                                print("  6. Menu")
                                Ja.misto3 = input("  Zadej číslo : ")

def arena(): #lokace arena placeny souboj a sazky
    global Ja
    while not((Ja.misto0 == "menu") | (Ja.misto2 == "")): #vystup z cyklu v pripade nahledu do menu nebo vraceni se do puvodni lokace
        if Ja.misto3 == "1":
            gladiator = boj(5,13,8,9,15,1) #vytvori se novy protivnik
            if (gladiator<1)&(Ja.zivotyAkt>0): #kdyz hrac vyhraje
                Ja.zkusenosti=Ja.zkusenosti+80+nahoda(11) #prictou se zkusenosti
                Ja.mince=Ja.mince+5+nahoda(6) #prictou se penize
                Ja.vypocUroven() #vypocte se uroven
                Ja.protivnik0=False #kvuli splneni ukolu
            Ja.misto3 = ""
        else:
            if Ja.misto3 == "2":
                sazka()
                Ja.misto3 = ""
            else:
                if Ja.misto3 == "3":
                    Ja.misto2 = ""
                    Ja.misto3 = ""
                else:
                    if Ja.misto3 == "4":
                        Ja.misto0 = "menu"
                        Ja.misto3 = ""
                    else:
                        cistiObrazovku()
                        print("Když vejdeš do té malé arény okamžitě")
                        print("ucítí nepříjemně nasládlý pach krve.")
                        print("Ale co každej si musí nějak vydělat.")
                        posun(2)
                        print("_Aréna_")
                        print("  1. Souboj")
                        print("  2. Sázka")
                        print("  3. Jít na náměstí")
                        print("  4. Menu")
                        Ja.misto3 = input("  Zadej číslo : ")

def sazka(): #Sazeni moznost vyhry temer 50/50
    global Ja
    print("_Sázení_")
    print("Máš "+str(Ja.mince)+" mincí")
    print("")
    print("Po nějakém čase hledání jsi konečně našel diváka,")
    print("který by si proti tvému gladiatorovi chtěl vsadit.")
    castka = input("Zadej částku, kterou chceš vsadit : ") #nacte se vsazena castka
    if int(castka)>Ja.mince: #pokud nema hrac dostatek penez vypise se hlaska
        print("Nemůžeš vsadit něco co nemaš!!!")
    else:
        if nahoda(30)>13: #sance na vyhru
            Ja.mince = Ja.mince+int(castka)
            print("Vyhrál jsi sázku niní máš "+str(Ja.mince)+" mincí.")
            Ja.zkusenosti=Ja.zkusenosti+40
        else:
            Ja.mince = Ja.mince - int(castka)
            print("Prohrál jsi sázku niní máš "+str(Ja.mince)+" mincí.")
            Ja.zkusenosti = Ja.zkusenosti+20
    stisk()
    Ja.vypocUroven()

            
def lekar(): #pro vyleceni zraneni
    global Ja
    while not((Ja.misto0 == "menu") | (Ja.misto2 == "")): #vystup z cyklu v pripade nahledu do menu nebo vraceni se do puvodni lokace
        cistiObrazovku()
        if Ja.misto3 == "1":
            if (Ja.mince>1):
                if Ja.zivotyMax>Ja.zivotyAkt:
                    Ja.zivotyAkt=Ja.zivotyAkt+1
                    Ja.mince = Ja.mince-2
                else:
                    print("A c-c-c-co mám l-l-l-léčit. Fy-Fyzicky jsi zd-zd-ráv a psychické cho-choroby já neléčim! I k-dyž bys t-t-to po-po-po-potřeboval")
                    pockej(4)
            else:
                print("Léčitel: \"Žádné p-p-peníze žadná l-léčba\"")
                pockej(4)
            Ja.misto3 = ""
        else:
            if Ja.misto3 == "2":
                Ja.misto2 = ""
                Ja.misto3 = ""
            else:
                if Ja.misto3 == "3":
                    Ja.misto0 = "menu"
                    Ja.misto3 = ""
                else:
                    print("Jen co vejdeš do dveří lékařského domu hned se zhrozíš kolyk")
                    print("je všude nacákáno krve. Jak na nějakých jatkách.")
                    posun(2)
                    print("_Lékař_")
                    print("Máš "+str(Ja.zivotyAkt)+"/"+str(Ja.zivotyMax)+" životů a "+str(Ja.mince)+" mincí")
                    print("")
                    print("Najednou se u tebe objevý nějaký chlápek vypadající")
                    print("jako řezník a podivně očichávaje tě ti povídá : \"Dva z-z-zlatý\"")
                    print("")
                    print("  1. Léčit(1 život za 2 mince)")
                    print("  2. Jít na náměstí")                            
                    print("  3. Menu")
                    Ja.misto3 = input("  Zadej číslo : ")

#Sekce baziny
def baziny():
    global Ja
    cistiObrazovku()
    print("Po vstupu do mokřad máš hned zasiflené boty.")
    print("Jdeš asi tak půl kilometru bažinou, což ti")
    print("připadá jako věčnost a náhle se z vod a bahna")
    print("vynoří velká hydra. Jak ses lek zakopl jsi")
    print("a zabořil se obličejem do bahna. Když se zvedneš")
    print("a promneš si oči hydra na tebe pobaveně kouká,")
    print("ale ne dlouho po chvíli se pouštíte do boje.")
    stisk()
    hydra=boj(14,11,10,13,25,1) #vytvori protivnika
    if (hydra<1)&(Ja.zivotyAkt>0): #kdyz hrac vyhraje
        Ja.zkusenosti = Ja.zkusenosti+250+nahoda(50)
        Ja.mince = Ja.mince+50+nahoda(11)
        Ja.vypocUroven()
        Ja.protivnik1 = False
        print("Tak a teď už se ti ta mnoha hlavá hadice smát nebude.")
        pockej(5)
        Ja.misto1 = ""

#Sekce hory
def hory():
    global Ja
    cistiObrazovku()
    print("Po dlouhé cestě na vrchol hory se rozhlédneš kolem")
    print("sebe po krajině a všechno ti připadá opravdu malé.")
    print("A náhle se z nebe spustí hned vedle tebe hipogryf.")
    print("Pořádně se nadechuješ z plných plic čerstvého vzduchu")
    print("a pouštíš se do boje.")
    stisk()
    hipogryf=boj(16,14,11,16,35,1) #vytvori protivnika
    if (hipogryf<1)&(Ja.zivotyAkt>0): #kdyz hrac vyhraje
        Ja.zkusenosti=Ja.zkusenosti+500+nahoda(80)
        Ja.mince=Ja.mince+70+nahoda(21)
        Ja.vypocUroven()
        Ja.protivnik2=False
        print("Hahá teď ten polokůň, polopták vypadá, jak oškubanej koňskej salám.")
        pockej(5)
    Ja.misto1 = ""

def hrbitov():
    global Ja
    cistiObrazovku()
    print("Hned jakmile ses přiblížil ke hřbitovu ucítil jsi závan mrtvol.")
    print("Přeskakuješ hřbitovní zeď jako by pět metru od tebe nebyli vrátka.")
    print("Po ladném skoku přez dvoumetrovou zeď dopadáš do náruče")
    print("jednomu z nemrtvých. Odstrkuješ ho od sebe.")
    stisk()
    nemrtvy = boj(18,15,13,14,50,1) #vytvori protivnika
    if (nemrtvy<1)&(Ja.zivotyAkt>0): #kdyz hrac vyhraje
        Ja.zkusenosti=Ja.zkusenosti+700+nahoda(90)
        Ja.mince=Ja.mince+100+nahoda(51)
        Ja.vypocUroven()
        Ja.protivnik3=False
        print("Tak a z macatýho zombíka zbyla jen malá")
        print("hromádka kostiček a zkaženýho masa.")
    Ja.misto1 = ""

#Vypisi podsveti
def X(txt1, txt2, txt3, txt4):
    print("_Křižovatka_")
    print("  1. "+txt1)
    print("  2. "+txt2)
    print("  3. "+txt3)
    print("  4. "+txt4)
    print("  5. Menu")
    return input("Zadej číslo:")
    
    
def T( txt1, txt2, txt3):
    print("_Křižovatka_")
    print("  1. "+txt1)
    print("  2. "+txt2)
    print("  3. "+txt3)
    print("  4. Menu")
    return input("Zadej číslo:")

def prazdMist():
    cistiObrazovku()
    print("Vešel jsi do prázdné místnosti, která")
    print("nikam dál nevede. Po chvíl tupého zírání")
    print("na holé zdi se otáčíš na patě a jdeš zpět.")
    stisk()


def minotMist(protivnik): #Mistnost s minotaurem
    global Ja
    cistiObrazovku()
    if protivnik:
        print("Vstoupil jsi do místnosti. Náhle se za tebou zabouchnou")
        print("dveře a ucítíš zuřivé funění na zátylku. Otočís se a spatříš")
        print("velké rohy a rudě žhnousi oči, jak se proti tobě ženou.")
        stisk()
        minotaur=boj(17,14,13,13,40,1) #vytvori protivnika
        if (minotaur<1)&(Ja.zivotyAkt>0): #kdyz hrac vyhraje
            Ja.zkusenosti=Ja.zkusenosti+500+nahoda(50)
            Ja.mince=Ja.mince+45+nahoda(16)
            Ja.vypocUroven()
            protivnik=False
            cistiObrazovku()
            print("Tak to by mělo té velké bíčí bestyji stačit.")
            print("Teď už si s nikým na \"toró\" hrát nebude")
    else:
        print("Jen co jsi vstoupil, tak jsi podle bíčího zápachu poznal, že jsi")
        print("zde už byl a ležící mrtvola minotaura tě o tom jen utvrzuje.")
    stisk()
    return protivnik

def bandMist(protivnik): #Mistnost s minotaurem
    global Ja
    cistiObrazovku()
    if protivnik:
        print("Po vstupu do místnosti se jen tak procházíš, protože jsi zahlédl")
        print("ve stínu v rohu jednoho banditu, ktrerý si zjevně myslí, že o něm")
        print("vůbec nevíš bohužel pro něj. Kdyby ten hlupák aspoň nenechal")
        print("uprostřed místnosti tu lucernu.")
        stisk()
        bandita=boj(12,15,13,8,21,1) #vytvori protivnika
        if (bandita<1)&(Ja.zivotyAkt>0): #kdyz hrac vyhraje
            Ja.zkusenosti=Ja.zkusenosti+300+nahoda(50)
            Ja.mince=Ja.mince+30+nahoda(11)
            Ja.vypocUroven()
            protivnik=False
            cistiObrazovku()
            print("No a je po všem. Chudák asi si měl najít lepší schovku.")
    else:
        print("Ááá nazazil jsi na místnost s tim hlupákem, co se")
        print("schovával ve stínu. Teď tu leží jako nějaká vzdechlina.")
    stisk()
    return protivnik


def kostraMist(protivnik): #Mistnost s koslivcem
    global Ja
    cistiObrazovku()
    if (protivnik):
        print("Hned jak jsi vstoupil do místnosti se proti tobě rozběhne")
        print("kostra co stála uprotřed místnosti.")
        stisk()
        kostlivec=boj(12,15,13,8,21,1) #vytvori protivnika
        if (kostlivec<1)&(Ja.zivotyAkt>0): #kdyz hrac vyhraje
            Ja.zkusenosti=Ja.zkusenosti+300+nahoda(50)
            Ja.mince=Ja.mince+30+nahoda(11)
            Ja.vypocUroven()
            protivnik=False
            cistiObrazovku()
            print("A je konec. Po kostlivci tu zbyla jen hromádka kostí.")
    else:
        print("Tahle hromádka kostí je ti povědomá. To bude asi po tom kostlivci.")
    stisk()
    return protivnik

def drak(): #Mistnost s minotaurem
    global Ja
    cistiObrazovku()
    print("Vešel jsi do obrovského sálu. Všude jsou hory a hory zlata")
    print("a drahých kamenů. Tu si všimneš na nejvyšším kopci jak stojí")
    print("soška na oltáři, kolem kterého je stočený drak. Beze ostychu")
    print("začneš šplkat po strmém kopci zlata přímo k sošce. Když se")
    print("dostaneš do půlky kopce náhle se drak probudí a kouká na tebe")
    print("jak se namáháš. Mezitim co k němu šplháš, k tobě začne promlouvat:")
    print("\"Slišel jsem o tobě cizinče. Vše jsem se o tobě dozvěděl od")
    print("sošky dokonce o tobě prý vím více než ty sám. Avšak prý nepociťuješ")
    print("strach ,ale tomu tak nebylo vždy to mi věř. Také jsem se od ní")
    print("dozvěděl, že osud nás dvou ještě nebyl napsán a dnes se o nem rozhodne,")
    print("jelikož přežije jen jeden z nás.\"")
    print("Zrovna ses vyškrábal na samý vrcholek.")
    stisk()
    Drak=boj(20,18,18,20,99,10) #vytvori protivnika
    if (Drak<1)&(Ja.zivotyAkt>0): #kdyz hrac vyhraje
        cistiObrazovku()
        print("Drak padl a veškerý poklad je tvůj, ale ještě více než všechen")
        print("ten poklad tě zajímá ta soška. Konečně ti budou zodpovězeny")
        print("všechny otázky jako odkud jsi, kdo vůbec jsi a co se ti stalo.")
        print("Ale hlavně jako první otázku pokládáš, zda ta kočka v hospodě")
        print("opravdu kdáká.")
        print("")
        print("   KONEC HRY")
        stisk()
        Ja.zivotyAkt=0 #vynuluje zivot, aby se ukoncila hra
        Ja.misto0="menu" #posle uzivatele do menu

#Vypisi podsveti konec


#Sekce jeskyne
def jeskyne():
    global Ja
    autoUlozit() #automaticke ulozeni hry
    while not((Ja.misto0 == "menu") | (Ja.misto1 == "")): #vystup z cyklu v pripade nahledu do menu nebo vraceni se do puvodni lokace
        #posun do dalsi lokace
        if Ja.misto2 == "1": 
            vstup()
        else:
            if Ja.misto2 == "2":
                Ja.misto1 = ""
                Ja.misto2 = ""
            else:
                if Ja.misto2 == "3": #moznost navratu do menu
                    Ja.misto0 = "menu"
                    Ja.misto2 = ""
                else: #pokud nebyla zatim zadana volba ci je volba nespravna provede se vypis vloby
                    cistiObrazovku()
                    if (Ja.protivnik4):
                        print("Přišel jsi ke vchodu do jeskyně rozhlížeje se neustále")
                        print("kolem sebe jestli nespatříš nějaký pohyb, ale kde nic tu nic.")
                        print("Až najednou na tebe z boku vyběhne obrovitý obr a vůbec nechápeš")
                        print("jak sis ho mohl nevšimnout.")
                        stisk()
                        obr = boj(17,14,13,13,40,1) #vytvori protivnika
                        if (obr<1)&(Ja.zivotyAkt>0): #kdyz hrac vyhraje
                            Ja.zkusenosti=Ja.zkusenosti+500+nahoda(50)
                            Ja.mince=Ja.mince+45+nahoda(16)
                            Ja.vypocUroven()
                            Ja.protivnik4=False
                            print("Konečně, obr padl a ty máš volný vstup do jeskyně.")
                            stisk()
                        else:                     
                            Ja.misto1 = ""
                    else:
                        print("Závan tlející mrtvoly obra je cítit široko daleko.")
                        stisk()
                        cistiObrazovku()
                        print("Fuj ten obr ale smrdí")
                        posun(2)
                        print("_Jeskyně_")
                        print("  1. Vstoupit do jeskyně")
                        print("  2. Jít na rozcestí")
                        print("  3. Menu")
                        Ja.misto2 = input("  Zadej číslo : ") 

def vstup():
    global Ja
    while not((Ja.misto0 == "menu") | (Ja.misto2 == "")): #vystup z cyklu v pripade nahledu do menu nebo vraceni se do puvodni lokace
        #posun do dalsi lokace
        if Ja.misto3 == "1":
            chodZ() 
        else:
            if Ja.misto3 == "2":
                prazdMist()
                Ja.misto3 = ""
            else:
                if Ja.misto3 == "3":
                    chodS()
                else:
                    if Ja.misto3 == "4":
                        Ja.misto2 = ""
                        Ja.misto3 = ""
                    else:
                        if Ja.misto3 == "5": #moznost navratu do menu
                            Ja.misto0 = "menu"
                            Ja.misto3 = ""
                        else: #pokud nebyla zatim zadana volba ci je volba nespravna provede se vypis vloby
                            cistiObrazovku()
                            print("V jeskyni cítíš strašlivý zápach plísně.")
                            print("Honem pryč snad to bude jinde lepší.")
                            posun(2)
                            Ja.misto3 = X("Jít na západ", "Jít na jih", "Jít na sever", "Vrátit se před jeskyni")  
    
def chodZ():
    global Ja
    while not((Ja.misto0 == "menu") | (Ja.misto3 == "")): #vystup z cyklu v pripade nahledu do menu nebo vraceni se do puvodni lokace
        if Ja.misto4 == "1":
            chodZZ()
        else:
            if Ja.misto4 == "2":
                chodZJ()
            else:
                if Ja.misto4 == "3":
                    Ja.misto3 = ""
                    Ja.misto4 = ""
                else:
                    if Ja.misto4 == "4":#moznost navratu do menu
                        Ja.misto0 = "menu"
                        Ja.misto4 = ""
                    else: #pokud nebyla zatim zadana volba ci je volba nespravna provede se vypis vloby
                        Ja.protivnik7 = bandMist(Ja.protivnik7)
                        if Ja.protivnik7:
                            Ja.misto3 = ""
                        else:
                            cistiObrazovku()
                            print("Ta lucerna tak pěkně svítí O.o")
                            posun(2)
                            Ja.misto4 = T("Jít na západ", "Jít na jih", "Jít na východ")          

def chodZJ():
    global Ja
    while not((Ja.misto0 == "menu") | (Ja.misto4 == "")): #vystup z cyklu v pripade nahledu do menu nebo vraceni se do puvodni lokace
        if Ja.misto5 == "1":
            chodZJZ()
        else:
            if Ja.misto5 == "2":
                prazdMist()
                Ja.misto5 = ""
            else:
                if Ja.misto5 == "3":
                    Ja.misto4 = ""
                    Ja.misto5 = ""
                else:
                    if Ja.misto5 == "4": #moznost navratu do menu
                        Ja.misto0 = "menu"
                        Ja.misto5 = ""
                    else: #pokud nebyla zatim zadana volba ci je volba nespravna provede se vypis vloby
                        cistiObrazovku()
                        print("Náhle se něco pohne uprostřed místnosti a ty strachy")
                        print("vykřikneš jako malá holka. Naštěstí to je jenom myš.")
                        posun(2)
                        T("Jít západnímy dveřmi", "Jít jižnímy dveřmi", "Jít severními dveřmi")
                        Ja.misto5 = cti.nextLine()            

def chodZJZ():
    global Ja
    while not((Ja.misto0 == "menu") | (Ja.misto5 == "")): #vystup z cyklu v pripade nahledu do menu nebo vraceni se do puvodni lokace
        if Ja.misto6 == "1":
            Ja.protivnik8 = bandMist(Ja.protivnik8)
            Ja.misto6 = ""
        else:
            if Ja.misto6 == "2":
                Ja.misto5 = ""
                Ja.misto6 = ""
            else:
                if Ja.misto6 == "3": #moznost navratu do menu
                    Ja.misto0 = "menu"
                    Ja.misto6 = ""
                else: #pokud nebyla zatim zadana volba ci je volba nespravna provede se vypis vloby
                    cistiObrazovku()
                    print("Tak tohle za to stálo, přišel jsi do chodby v níž na stěnách")
                    print("je nějaký luminiscentní povlak který vytváří nádherné obrazce.")
                    print("Jen si říkáš \"Škoda, že nemám nějaké kouzlo, kterým bych zachytil")
                    print("ten nádherný výjev.")
                    posun(2)
                    print("_Chodba_")
                    print("  1. Jít na západ")
                    print("  2. Jít na východ")
                    print("  3. Menu")
                    Ja.misto6 = input("  Zadej číslo : ")
    
def chodZZ():
    global Ja
    while not((Ja.misto0 == "menu") | (Ja.misto4 == "")): #vystup z cyklu v pripade nahledu do menu nebo vraceni se do puvodni lokace
        if Ja.misto5 == "1":
            Ja.protivnik9 = minotMist(Ja.protivnik9)
            Ja.misto5 = ""
        else:
            if Ja.misto5 == "2":
                chodZZS()
            else:
                if Ja.misto5 == "3":
                    Ja.misto4 = ""
                    Ja.misto5 = ""
                else:
                    if Ja.misto5 == "4": #moznost navratu do menu
                        Ja.misto0 = "menu"
                        Ja.misto5 = ""
                    else: #pokud nebyla zatim zadana volba ci je volba nespravna provede se vypis vloby
                        cistiObrazovku()
                        print("Přišel jsi do zvláštní místnosti kde máš zvláštní pocit")
                        print("jako by se s tebou celá otáčela, až se ti z toho dělá nevolno.")
                        posun(2)
                        Ja.misto5 = T("Jít na západ", "Jít na sever", "Jít na východ")

def chodZZS():
    global Ja
    while not((Ja.misto0 == "menu") | (Ja.misto5 == "")): #vystup z cyklu v pripade nahledu do menu nebo vraceni se do puvodni lokace
        if Ja.misto6 == "1":
            prazdMist()
            Ja.misto6 = ""
        else:
            if Ja.misto6 == "2":
                chodZZSS()
            else:
                if Ja.misto6 == "3":
                    Ja.misto5 = ""
                    Ja.misto6 = ""
                else:
                    if Ja.misto6 == "4": #moznost navratu do menu
                        Ja.misto0 = "menu"
                        Ja.misto6 = ""
                    else: #pokud nebyla zatim zadana volba ci je volba nespravna provede se vypis vloby
                        Ja.protivnik10 = kostraMist(Ja.protivnik10)
                        if Ja.protivnik10:
                            Ja.misto5 = ""
                        else:
                            cistiObrazovku()
                            print("Hmm kosti.")
                            posun(2)
                            Ja.misto6 = T("Jít na západ", "Jít na sever", "Jít na Jih")

def chodZZSS():
    global Ja
    while not((Ja.misto0 == "menu") | (Ja.misto6 == "")): #vystup z cyklu v pripade nahledu do menu nebo vraceni se do puvodni lokace
        if Ja.misto7 == "1":
            prazdMist()
            Ja.misto7 = ""
        else:
            if Ja.misto7 == "2":
                Ja.protivnik11 = kostraMist(Ja.protivnik11)
                Ja.misto7 = ""
            else:
                if Ja.misto7 == "3":
                    drak()
                    Ja.misto7 = ""
                else:
                    if Ja.misto7 == "4":
                        Ja.misto6 = ""
                        Ja.misto7 = ""
                    else:
                        if Ja.misto7 == "5": #moznost navratu do menu
                            Ja.misto0 = "menu"
                            Ja.misto7 = ""
                        else: #pokud nebyla zatim zadana volba ci je volba nespravna provede se vypis vloby
                            cistiObrazovku()
                            print("Tak tady na té křižovatce je pěkný dusno a horko,")
                            print("asi už budeš blízko dračího kutlochu.")
                            posun(2)
                            Ja.misto7 = X("Jít na východ", "Jít na sever", "Jít na západ", "Jít na jih")

def chodS():
    global Ja
    while not((Ja.misto0 == "menu") | (Ja.misto3 == "")): #vystup z cyklu v pripade nahledu do menu nebo vraceni se do puvodni lokace
        if Ja.misto4 == "1":
            prazdMist()
            Ja.misto4 = ""
        else:
            if Ja.misto4 == "2":
                Ja.protivnik5 = minotMist(Ja.protivnik5)
                Ja.misto4 = ""
            else:
                if Ja.misto4 == "3":
                    Ja.protivnik6 = bandMist(Ja.protivnik6)
                    Ja.misto4 = ""
                else:
                    if Ja.misto4 == "4":
                        Ja.misto3 = ""
                        Ja.misto4 = ""
                    else:
                        if Ja.misto4 == "5": #moznost navratu do menu
                            Ja.misto0 = "menu"
                            Ja.misto4 = ""
                        else: #pokud nebyla zatim zadana volba ci je volba nespravna provede se vypis vloby
                            cistiObrazovku()
                            print("Teď si říkáš, kam si to vlez, tady na té křižovatce je")
                            print("ještě větší smrad než na na té u vchodu do jeskyně.")
                            posun(2)
                            Ja.misto4 = X("Jít na západ", "Jít na sever", "Jít na východ", "Jít na jih")
#sekce jeskyne konec
#konec deklarace hlavni program

#Sekce Hl. Metoda


tvorbaSloz("save")#overeni existence slozky
zacVypis()#Pouze pocatecni vypis
zacykleni = 0
#Tvorba postavy
while not volba == "konec": #hlavni cykl programu
    Ja = Postava()
    prolog = False#Zamitnuti prolog
    Ja.vlastnosti(0, 0, 0, 0, 0, 0) #Vynulovani vlastnosti
    vyprazdPol() #vyprazdni pole s misty
    Ja.nactiProt() #Ozivy protivniky
    Ja.mince = 100+nahoda(50) #da postave mince (100-150)
    prubeh = True
    while prubeh: #cykl hry
        volba = "" #smaze retezec volby
        Ja.misto0 = "" #vyprazdni policko pro menu
        if Ja.zivotyAkt < 1: #menu pro start hry ci po smrti postavy (osetreni ryzika ulozeni mrtve postavy)
            menu1()
        else:
            menu2()
        while volba == "pribeh": #Cykl hrani
            hra()
        prubeh = not((Ja.zivotyAkt < 1) | (volba == "konec"))
        #konec cyklu hrani
    prubeh = True
    #Cykl hry se ukonci po smrti nebo volbe konce hry
#konec hlavniho cyklu programu
print("  Konec\n") #vypise konec
pockej(4)
cistiObrazovku()
#Konec Hl. Metoda
