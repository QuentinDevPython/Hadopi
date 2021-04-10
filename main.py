from Interface.interface import Interface
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
	interface = Interface(
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
	interface.choose_download()


	