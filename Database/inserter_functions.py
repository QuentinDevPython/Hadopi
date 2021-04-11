import Database.create_tables

class Inserter_functions:


	def insert_Region(self, data, Region):
		Region.get_or_create(
			nom_region = data[6]
		) 

	def insert_Ville(self, data, Ville, Region):
		Ville.get_or_create(
			nb_habitants_ville = data[5],
			id_region = Region.get(Region.nom_region == data[6])
		)

	def insert_Foyer(self, data, Foyer, Ville, Region):
		Foyer.get_or_create(
			nb_personnes_foyer = data[3],
			nb_enfants_foyer = data[4],
			id_ville = Ville.select(Ville.id_ville).where(
					(Ville.nb_habitants_ville == data[5])
					& (Ville.id_region == Region.select(Region.id_region).where(
							Region.nom_region == data[6]
						)
					)
				).get()
		)

	def insert_Musique(self, data, Musique):
		data_dict = data[7].split(',')
		for item in data_dict:
			if item != '':
				Musique.get_or_create(
					style_de_musique = item
				)

	def insert_Consommation(self, data, Consommation):
		Consommation.get_or_create(
			ecoute_jours = data[9],
			frequence_musique = data[10],
			nb_concert = data[11],
			appareil_plus_frequent = data[12],
			frequence_seul = data[13],
			frequence_conso_illegale = data[14],
			frequence_accompagne = data[15]
		)

	def insert_Moment_d_écoute(self, data, Moment_d_écoute):
		data_dict = data[8].split(',')
		for item in data_dict:
			if item != '':
				Moment_d_écoute.get_or_create(
					moment_d_ecoute = item
				)

	def insert_Plateforme(self, data, Plateforme):
		data_dict = data[16].split(',')
		for item in data_dict:
			if item != '':
				Plateforme.get_or_create(
					plateforme = item
				)

	def insert_Personne(self, data, Personne, Consommation, Foyer, Ville, Region):
		Personne.create(
			sexe = data[0],
			tranche_age = data[1],
			statut_social = data[2],
			id_consommation = Consommation.select(Consommation.id_consommation).where(
				(Consommation.ecoute_jours == data[9])
				& (Consommation.frequence_musique == data[10])
				& (Consommation.nb_concert == data[11])
				& (Consommation.appareil_plus_frequent == data[12])
				& (Consommation.frequence_seul == data[13])
				& (Consommation.frequence_conso_illegale == data[14])
				& (Consommation.frequence_accompagne == data[15])
				).get(),
			id_foyer = Foyer.select(Foyer.id_foyer).where(
					(Foyer.nb_personnes_foyer == data[3])
					& (Foyer.nb_enfants_foyer == data[4])
					& (Foyer.id_ville == Ville.select(Ville.id_ville).where(
							(Ville.nb_habitants_ville == data[5])
							& (Ville.id_region == Region.select(Region.id_region).where(
								Region.nom_region == data[6]
							))
						)
					)
				).get()
		)
	def insert_Ecoute(self, index, data, Ecoute, Personne, Musique):
		data_dict = data[7].split(',')
		for item in data_dict:
			if item != '':
				Ecoute.get_or_create(
					id_personne = Personne.get(Personne.id_personne == index+1),
					id_musique = Musique.get(Musique.style_de_musique == item)
				)

	def insert_Ecoute_habituellement(self, index, data, Ecoute_habituellement, Personne, Moment_d_écoute):
		data_dict = data[8].split(',')
		for item in data_dict:
			if item != '':
				Ecoute_habituellement.get_or_create(
					id_personne = Personne.get(Personne.id_personne == index+1),
					id_moment_d_ecoute = Moment_d_écoute.get(Moment_d_écoute.moment_d_ecoute == item)
				)

	def insert_Utilise(self, index, data, Utilise, Personne, Plateforme):
		data_dict = data[16].split(',')
		for item in data_dict:
			if item != '':
				Utilise.get_or_create(
					id_personne = Personne.get(Personne.id_personne == index+1),
					id_plateforme = Plateforme.get(Plateforme.plateforme == item)
				)
