import Database.sql_connector
from Api.downloader import Downloader
#from Api.inserter import Inserter

if __name__ == "__main__":
	downloader = Downloader()
	data = downloader.get_data()
	#inserter = Inserter(data)
	#inserter.insert()
	