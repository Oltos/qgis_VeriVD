#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Aide:
	"""Class used to load the help"""
	def __init__(self):
		self.webSpatialite = 'https://www.gaia-gis.it/fossil/libspatialite/index'
		self.webMoPublic = 'https://www.cadastre.ch/fr/services/service/mopublic.html'
		self.webNormeVD = 'https://dwa.vd.ch/PROD/DINF/publicationdinf1_p.nsf/normesformulaires?SearchView&Query='
		self.requete = '(FIELD%20TitreNorme%20CONTAINS%20{})'
		self.webChecker = 'https://www.vd.ch/themes/territoire-et-construction/informations-sur-le-territoire/mensuration-officielle/informations-aux-bureaux-de-geometres/checker-interlis/'

		self.messageFichier = """Le fichier .sqlite qui alimente ce plugin, contient une base de donn�es spatiale au format <a href='{}'>spatialite</a>. 
Ce fichier est gener�e � l'OIT sur la base d'un fichier interlis d�crit selon le mod�le MD01MOVDMN95.""".format(self.webSpatialite)
		self.messageBase = """Cet onglet permet le chargement des couches de bases. Celles-ci sont inspir�es du mod�le simplif� de la mensuration officielle: <a href='{}'>MO-Public</a>. 
Quelques �l�ments importants issues du  <a href='{}'>mod�le officiel</a>  ont �t� ajout�s � ces donn�es avec un 'pr�fixe VD'. 
La symbologie provient de la <a href='{}'>norme vaudoise 6411</a>""".format(self.webMoPublic, self.webNormeVD+self.requete.format('6021'), self.webNormeVD+self.requete.format('6411'))
		self.messageIliValidator = """A d�fnir"""
		self.messageChecker = """Cet onglet permet le chargement des donn�es issues du <a href='{}'>checker interlis vaudois</a>. 
Pour plus d'informations, veuiller consulter la page web s'y ref�rant.""".format(self.webChecker)
		self.messageVerif = """Cet onglet permet le chargement des donn�es des tests de v�rification d�velop�s en interne � l'OIT (office de l'information sur le t�rritoire). Des explications relatives � chacun de ces tests sont disponnible dans la norme <a href='{}'>v�rification des mensurations</a>.""".format(self.webChecker)