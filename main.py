#coding:utf-8
from os import system
from fonc_class import *
system("clear")
entete()

print("-+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-")


A = point(0,0,0)
entrer_coordonne(A)
affiche_coordone(A)

print("--------------------------------------------------------------------------------")

B = point(0,0,0)
entrer_coordonne(B)
affiche_coordone(B)

print("--------------------------------------------------------------------------------")

C = point(0,0,0)
entrer_coordonne(C)
affiche_coordone(C)

print("-------------------------------------------------------------------------------")
D = point(0,0,0)
E = point(0,0,0)
print("--------------------------------------------------------------------------------")

vecteur(A,B,C,D,E)

print("--------------------------------------------------------------------------------")

prod_vect(A,B)
pied()