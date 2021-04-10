import csv 
from tqdm import tqdm


class Downloader:

	def __init__(self):
		self.data = list()

	def download(self):
		file = open("excel_hadopi_BDD.csv", "r")
		data_reader = csv.reader(file, delimiter = ",")
		for row in data_reader:
			self.data.append(row)
		file.close()

	def get_data(self):
		Downloader.download(self)
		return self.data[1:]