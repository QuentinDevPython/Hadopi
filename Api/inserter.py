from Database.inserter_functions import Inserter_functions
from tqdm import tqdm


class Inserter:

	def __init__(self, data, Region, Ville, Foyer, Musique, Consommation, Moment_d_écoute, Plateforme, Personne, Ecoute, Ecoute_habituellement, Utilise):
		self.data = data
		self.database_inserter = Inserter_functions()
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


	def insert(self):
		for row in tqdm(range(len(self.data))):
			self.database_inserter.insert_Region(self.data[row], self.Region)
			self.database_inserter.insert_Ville(self.data[row], self.Ville, self.Region)
			self.database_inserter.insert_Foyer(self.data[row], self.Foyer, self.Ville, self.Region)
			self.database_inserter.insert_Musique(self.data[row], self.Musique)
			self.database_inserter.insert_Consommation(self.data[row], self.Consommation)
			self.database_inserter.insert_Moment_d_écoute(self.data[row], self.Moment_d_écoute)
			self.database_inserter.insert_Plateforme(self.data[row], self.Plateforme)
			self.database_inserter.insert_Personne(self.data[row], self.Personne, self.Consommation, self.Foyer, self.Ville, self.Region)
			self.database_inserter.insert_Ecoute(row, self.data[row], self.Ecoute, self.Personne, self.Musique)
			self.database_inserter.insert_Ecoute_habituellement(row, self.data[row], self.Ecoute_habituellement, self.Personne, self.Moment_d_écoute)
			self.database_inserter.insert_Utilise(row, self.data[row], self.Utilise, self.Personne, self.Plateforme)



