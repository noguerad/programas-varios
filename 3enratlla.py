#!/usr/bin/python
# -*- coding: utf-8 -*-

### Joc de 3 en ratlla.
### Creat per David Noguera contacta@noguerad.es
### Sou lliures de copiar o modificar el codi,
### però siusplau citeu a l'autor.

import os
import random
import time
#-----Variables


#-----Constants
tirs = ['5']                # Començem amb la casella central ja ocupada.
moviments = ["x"]           # Guardem les tirades.
    ## Linees del tauler.
L1 = [" ", " ", " "]
L2 = [" ", "x", " "]
L3 = [" ", " ", " "]


#-----Funcions
def explica():
    os.system("clear")
    print (" ")
    print (" 1 | 2 | 3 ")
    print ("---+---+---")
    print (" 4 | 5 | 6 ")
    print ("---+---+---")
    print (" 7 | 8 | 9 \n")
    print ("El jugador ha de triar una casella segons aquesta numeració.")
    print ("Començen les x al centre. ")
    raw_input("Esteu preparats? ")
    comenca()


def comenca():              # Funció principal del programa.
    #moviments = 1
    print ("Començen les x: ")
    while len(moviments)<9 :
        tauler()
        print (" ")
        #print tirs             # Tests de trencament del programa.
        #print moviments
        #print len(moviments)        
        if len(moviments)%2==0 :
            #tira = raw_input("Torn de les x, casella?: ")
            print ("Torn de les x. ")
            time.sleep(1)
            tira = auto()           
            jug = "x"
            tirast = str(tira)
            casella(tirast, jug)
            tirs.append(tira)
            moviments.append(jug)
            if guanyador()==1:
                break
        else:
            tira = raw_input("Torn de les o, casella?: ")            
            jug = "o"
            casella(tira, jug)
            tirs.append(tira)
            moviments.append(jug)
            if guanyador()==1:
                break
    felicitats(len(moviments))     

def casella(x,jug):         # Comprovem si la casella està plena
    xa = int(x)             # i la omplim si no ho està.
    if x in tirs:
        y = raw_input("Ocupada, tria de nou: ")
        casella(y, jug)
    elif xa==1 :
        L1[0] = jug
    elif xa==2 :
        L1[1] = jug
    elif xa==3 :
        L1[2] = jug
    elif xa==4 :
        L2[0] = jug
    elif xa==6 :
        L2[2] = jug
    elif xa==7 :
        L3[0] = jug
    elif xa==8 :
        L3[1] = jug
    elif xa==9 :
        L3[2] = jug
    else:
        z = raw_input("Incorrecte, tria de nou: ")
        casella(z, jug)

def auto():              # L'ordinador tira com a jugador x.
    if (L1[0]=="x" and L1[1]=="x" and L1[2]==" ") :
        return "3"
    elif (L1[0]==" " and L1[1]=="x" and L1[2]=="x") :
        return "1"
    elif (L1[0]=="x" and L1[1]==" " and L1[2]=="x") :
        return "2"
    elif (L2[0]==" " and L2[1]=="x" and L2[2]=="x") :
        return "4"
    elif (L2[0]=="x" and L2[1]=="x" and L2[2]==" ") :
        return "6"
    elif (L1[0]=="x" and L2[0]=="x" and L3[0]==" ") :
        return "7"
    elif (L1[0]==" " and L2[0]=="x" and L3[0]=="x") :
        return "1"
    elif (L1[0]=="x" and L2[0]==" " and L3[0]=="x") :
        return "4"
    elif (L1[1]=="x" and L2[1]=="x" and L3[1]==" ") :
        return "8"
    elif (L1[1]==" " and L2[1]=="x" and L3[1]=="x") :
        return "2"
    elif (L1[0]=="x" and L2[1]=="x" and L3[2]==" ") :
        return "9"
    elif (L1[0]==" " and L2[1]=="x" and L3[2]=="x") :
        return "1"
    elif (L1[2]==" " and L2[1]=="x" and L3[0]=="x") :
        return "3"
    elif (L1[2]=="x" and L2[1]=="x" and L3[0]==" ") :
        return "7"
    elif (L1[2]=="x" and L2[2]=="x" and L3[2]==" ") :
        return "9"
    elif (L1[2]==" " and L2[2]=="x" and L3[2]=="x") :
        return "3"
    elif (L1[2]=="x" and L2[2]==" " and L3[2]=="x") :
        return "6"
    elif (L3[0]=="x" and L3[1]=="x" and L3[2]==" ") :
        return "9"
    elif (L3[0]==" " and L3[1]=="x" and L3[2]=="x") :
        return "7"
    elif (L3[0]=="x" and L3[1]==" " and L3[2]=="x") :
        return "8"        
    elif (L1[0]=="o" and L1[1]=="o" and L1[2]==" ") :
        return "3"
    elif (L1[0]==" " and L1[1]=="o" and L1[2]=="o") :
        return "1"
    elif (L1[0]=="o" and L1[1]==" " and L1[2]=="o") :
        return "2"
    elif (L1[0]=="o" and L2[0]=="o" and L3[0]==" ") :
        return "7"
    elif (L1[0]==" " and L2[0]=="o" and L3[0]=="o") :
        return "1"
    elif (L1[0]=="o" and L2[0]==" " and L3[0]=="o") :
        return "4"   
    elif (L1[2]=="o" and L2[2]=="o" and L3[2]==" ") :
        return "9"
    elif (L1[2]==" " and L2[2]=="o" and L3[2]=="o") :
        return "3"
    elif (L1[2]=="o" and L2[2]==" " and L3[2]=="o") :
        return "7"
    elif (L3[0]=="o" and L3[1]=="o" and L3[2]==" ") :
        return "9"
    elif (L3[0]==" " and L3[1]=="o" and L3[2]=="o") :
        return "7"
    elif (L3[0]=="o" and L3[1]==" " and L3[2]=="o") :
        return "8"
    else:
        while 1:
            ran = random.randint(1, 9)
            ranst = str(ran)
            if (ranst!="5" and (ranst not in tirs)):
                return ranst
                break

def tauler():               # Dibuixem el tauler amb les fitxes.
    os.system("clear")
    print (" ")
    print (" "+L1[0]+" | "+L1[1]+" | "+L1[2])
    print ("---+---+---")
    print (" "+L2[0]+" | "+L2[1]+" | "+L2[2])
    print ("---+---+---")
    print (" "+L3[0]+" | "+L3[1]+" | "+L3[2])
    
def guanyador():            # Comprovem a cada tirada si ha guanyat algú.
    if (L1[0]=="o" and L1[1]=="o" and L1[2]=="o") :
        return 1
    elif (L2[0]=="o" and L2[1]=="o" and L2[2]=="o") :
        return 1
    elif (L3[0]=="o" and L3[1]=="o" and L3[2]=="o") :
        return 1
    elif (L1[0]=="o" and L2[0]=="o" and L3[0]=="o") :
        return 1
    elif (L1[1]=="o" and L2[1]=="o" and L3[1]=="o") :
        return 1
    elif (L1[2]=="o" and L2[2]=="o" and L3[2]=="o") :
        return 1
    elif (L1[0]=="o" and L2[1]=="o" and L3[2]=="o") :
        return 1
    elif (L3[0]=="o" and L2[1]=="o" and L1[2]=="o") :
        return 1
    elif (L1[0]=="x" and L1[1]=="x" and L1[2]=="x") :
        return 1
    elif (L2[0]=="x" and L2[1]=="x" and L2[2]=="x") :
        return 1
    elif (L3[0]=="x" and L3[1]=="x" and L3[2]=="x") :
        return 1
    elif (L1[0]=="x" and L2[0]=="x" and L3[0]=="x") :
        return 1
    elif (L1[1]=="x" and L2[1]=="x" and L3[1]=="x") :
        return 1
    elif (L1[2]=="x" and L2[2]=="x" and L3[2]=="x") :
        return 1
    elif (L1[0]=="x" and L2[1]=="x" and L3[2]=="x") :
        return 1
    elif (L3[0]=="x" and L2[1]=="x" and L1[2]=="x") :
        return 1
    else:
        return 0

def felicitats(g):          # Un cop ha guanyat un jugador,
    os.system("clear")      # comprovem quin i el felicitem.
    tauler()
    if guanyador()==1:
        if g%2==0 :
            print ("Felicitats, guanyen les o !!")
        else:
            print ("Felicitats, guanyen les x !!")
    else:
        print ("No hi ha guanyador...")
    tornar()

def tornar():               # Eliminem tot per tornar a posició inicial.
    resposta = raw_input("Tornar a jugar? s/n: ")
    if resposta=="s" :
        while len(L1)!=0:
            del L1[0]
        while len(L2)!=0:
            del L2[0]
        while len(L3)!=0:  
            del L3[0]
        while len(L1)!=3:
            L1.append(" ")
        L2.append(" ")
        L2.append("x")
        L2.append(" ")
        while len(L3)!=3:
            L3.append(" ")
        while len(moviments)!=1:
            del moviments[1]
        while len(tirs)!=1:
            del tirs[1]
        comenca()
    else:
        os.system("clear")

explica()
