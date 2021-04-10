import Database.sql_connector
from Api.downloader import Downloader
from Api.inserter import Inserter
from Database.create_tables import (
	Region,
	Ville,
	Foyer,
	Musique,
	Consommation,
	Moment_d_écoute,
	Plateforme,
	Personne,
	Ecoute,
	Ecoute_habituellement,
	Utilise
)

if __name__ == "__main__":
	downloader = Downloader()
	data = downloader.get_data()

	inserter = Inserter(
		data,
		Region,
		Ville,
		Foyer,
		Musique,
		Consommation,
		Moment_d_écoute,
		Plateforme,
		Personne,
		Ecoute,
		Ecoute_habituellement,
		Utilise
	)
	inserter.insert()
	