#coding:utf-8
import math

class point:
	'''point est une classe permettant de creer des vecteur dans l'espace i.e A(2,3,4)'''
	point_cree = 0
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
		point.point_cree+=1
	
	def norme(self):
		Norme = (((self.x)**2) + ((self.y)**2) + ((self.z)**2))
		print("la norme du veucteur {} est {}".format(point.point_cree,math.sqrt(Norme)))
#------------------------------------------------------------------------------------------------------		


def prod_vect(A,B,C):
		C.x = ((A.y*B.z)-(A.z*B.y))
		C.y = ((A.z*B.x)-(A.x*B.z))
		C.z = ((A.x*B.y)-(A.y*B.x))

		print("le produit vectorielle de vos vecteur \n U1 et U2 de coordonnees respectives ({},{},{}) et ({},{},{}) est \n {},{},{})".format(A.x,A.y,A.z,B.x,B.y,B.z,C.x,C.y,C.z))

#---------------------------------------------------------------------------------------------
def coordonne(X):
	X.x = int(input("entrer l'Abscisse du vecteur numero {} : ".format(point.point_cree)))
	X.y = int(input("entrer l'ordone du vecteur numero {} : ".format(point.point_cree)))
	X.z = int(input("entrer la cote du vecteur {} : ".format(point.point_cree)))
#--------------------------------------------------------------------

def affiche_coordone(X):
	print("les coordonnes du vecteur {} sont ({},{},{}) ".format(point.point_cree,X.x,X.y,X.z))
	X.norme()

#-------------------------------------------------------------------------------------

def entete():
	print("ATTENTION A VOUS CAR LE PROGRAMME QUE VOUS EXECUTEZ EST PRODUIT DE LA TEAM L'INTELIGENCIA.")
	print("CE PROGRAMME CALCULE LE PRODUIT VECTORIEL DE DEUX VECTEUR AB ET AC ENTRER PAR L'UTILISATEUR")
#---------------------------------------------------------------------------------------------------------


def pied():
	print("\t\t\tCOPYRIGHT 2023, INTELLIGENCIA CORPORATION CAMEROON.")

#---------------------------------------------------------------------------------------------------------
