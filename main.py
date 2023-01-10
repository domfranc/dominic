#coding:utf-8
from os import system
from fonc_class import *
system("clear")
entete()

print("-+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-")


A = point(0,0,0)
coordonne(A)
affiche_coordone(A)

print("--------------------------------------------------------------------------------")

B = point(0,0,0)
coordonne(B)
affiche_coordone(B)

C = point(0,0,0)

print("-------------------------------------------------------------------------------")

prod_vect(A,B,C)

print("-*******************************************************************************-")

pied()