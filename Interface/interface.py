import Database.sql_connector
from Api.downloader import Downloader
from Api.inserter import Inserter

class Interface:

	def __init__(self, Region, Ville, Foyer, Musique, Consommation, Moment_d_écoute, Plateforme, Personne, Ecoute, Ecoute_habituellement, Utilise):
		self.Region = Region
		self.Ville = Ville
		self.Foyer = Foyer
		self.Musique = Musique
		self.Consommation = Consommation
		self.Moment_d_écoute = Moment_d_écoute
		self.Plateforme = Plateforme
		self.Personne = Personne
		self.Ecoute = Ecoute
		self.Ecoute_habituellement = Ecoute_habituellement
		self.Utilise = Utilise

	def choose_download(self):
		download = int(
			input(
				"Voulez-vous télécharger la base de donnée ?\n"
				"1 - Oui\n"
				"2 - Non\n \n"
			))
		if download == 1:
			downloader = Downloader()
			data = downloader.get_data()
			inserter = Inserter(
				data,
				self.Region,
				self.Ville,
				self.Foyer,
				self.Musique,
				self.Consommation,
				self.Moment_d_écoute,
				self.Plateforme,
				self.Personne,
				self.Ecoute,
				self.Ecoute_habituellement,
				self.Utilise
			)
			inserter.insert()
		else:
			print('Vous avez choisi de ne pas (re)télécharger la base de donnée')
