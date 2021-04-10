from Database.create_tables import Personne, Appareil, Habitation, Question, Q1_Type_de_question, Q2_Mode_de_consommation, Q3_Lieu_ecoute_musique, Q4_Facon_de_consommer_musique, Q5_Type_de_musique

class Inserter_functions:

	def __init__(self):
		self.Personne = Personne
		self.Appareil = Appareil
		self.Habitation = Habitation
		self.Question = Question
		self.Q1_Type_de_question = Q1_Type_de_question
		self.Q2_Mode_de_consommation = Q2_Mode_de_consommation
		self.Q3_Lieu_ecoute_musique = Q3_Lieu_ecoute_musique
		self.Q4_Facon_de_consommer_musique = Q4_Facon_de_consommer_musique
		self.Q5_Type_de_musique = Q5_Type_de_musique

	def insert_Personne(self, row_data):
		self.Personne.get_or_create(
			sexe=row_data[0], 
			tranche_age=row_data[1], 
			statut_social=row_data[2]
		) 
	def insert_Appareil(self, item, row_data):
		self.Appareil.get_or_create(
			type_appareil=item,
			frequence_utilisation_internet = row_data[4]
		)
	#def insert_Utilise(self, row_data):
	#	self.Utilise.get_or_create(

	#	)
