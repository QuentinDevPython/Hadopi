from Database.inserter_functions import Inserter_functions
from tqdm import tqdm


class Inserter:

	def __init__(self, data):
		self.data = data
		self.inserter_functions = Inserter_functions()

	def insert(self):
		for row in tqdm(self.data):
			self.inserter_functions.insert_Personne(row)
			type_appareil = row[3].split(' / ')
			for item in type_appareil:
				self.inserter_functions.insert_Appareil(item,row)
				#self.inserter_functions.insert_Utilise()




