#coding:utf-8
import math

class point:
	'''la classe point est une classe permettant de creer des vecteur dans l'espace i.e A(2,3,4)'''
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


def prod_vect(A,B):
	'''Cette fonction calcule le produit vectorielle de deux vecteur AB et AC. i.e pour AB(-3,-1,5) et AC(-1,1,3) on AB^AC = (-8,4,-4)'''

	print("le produit vectorielle de vos vecteur \n U1 et U2 de coordonnees respectives ({},{},{}) et ({},{},{}) est \n {},{},{})".format(A.x,A.y,A.z,B.x,B.y,B.z,((A.y*B.z)-(A.z*B.y)),((A.z*B.x)-(A.x*B.z)),((A.x*B.y)-(A.y*B.x))))

#---------------------------------------------------------------------------------------------
def entrer_coordonne(X):
	'''Cette fontionest charge de recuperer les coordonees d'un vecteur pris en parametre'''
	X.x = int(input("entrer l'Abscisse du vecteur numero {} : ".format(point.point_cree)))
	X.y = int(input("entrer l'ordone du vecteur numero {} : ".format(point.point_cree)))
	X.z = int(input("entrer la cote du vecteur {} : ".format(point.point_cree)))
#--------------------------------------------------------------------

def affiche_coordone(X):
	'''cette fonction est charge d'afficher les coordones d'un vecteur A example A(3,4,5)'''
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

def vecteur(A,B,C,D,E):
	'''Cette fonction calcule a partir de deux vecteur A et B, le vecteur AB i.e pour 
	A(2,3,1) et B(3,1,5), AB(1,-2,4)'''
	D.x = ((B.x)-(A.x))
	D.y = ((B.y)-(A.y))
	D.z = ((B.z)-(A.z))
	print("le vecteur AB a pour coordone ({},{},{})".format(D.x,D.y,D.z))

	E.x = ((C.x)-1*(A.x))
	E.y = ((C.y)-1*(A.y))
	E.z = ((C.z)-1*(A.z))
	print("le vecteur Ac a pour coordone ({},{},{})".format(E.x,E.y,E.z))

	prod_vect(D,E)