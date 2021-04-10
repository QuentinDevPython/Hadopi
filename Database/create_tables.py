import peewee

mysql_db = peewee.MySQLDatabase(
	host = 'localhost',
	user = 'root',
	password = 'root',
	database = 'hadopi')

mysql_db.connect()

class BaseModel(peewee.Model):
	class Meta:
		database = mysql_db

class Region(BaseModel):
	id_region = peewee.AutoField(primary_key=True)
	nom_region = peewee.CharField(50)

class Ville(BaseModel):
	id_ville = peewee.AutoField(primary_key = True)
	nb_habitants_ville = peewee.CharField(30)
	id_region = peewee.ForeignKeyField(Region)

class Foyer(BaseModel):
	id_foyer = peewee.AutoField(primary_key = True)
	nb_personnes_foyer = peewee.CharField(20)
	nb_enfants_foyer = peewee.CharField(30)
	id_ville = peewee.ForeignKeyField(Ville)

class Musique(BaseModel):
	id_musique = peewee.AutoField(primary_key=True)
	style_de_musique = peewee.CharField(250)

class Consommation(BaseModel):
	id_consommation = peewee.AutoField(primary_key=True)
	ecoute_jours = peewee.CharField(100)
	frequence_musique = peewee.CharField(100)
	nb_concert = peewee.CharField(100)
	appareil_plus_frequent = peewee.CharField(100)
	frequence_seul = peewee.CharField(100)
	frequence_conso_illegale = peewee.CharField(100)
	frequence_accompagne = peewee.CharField(100)

class Moment_d_écoute(BaseModel):
	id_moment_d_ecoute = peewee.AutoField(primary_key=True)
	moment_d_ecoute = peewee.CharField(350)

class Plateforme(BaseModel):
	id_plateforme = peewee.AutoField(primary_key=True)
	plateforme = peewee.CharField(500)

class Personne(BaseModel):
	id_personne = peewee.AutoField(primary_key = True)
	sexe = peewee.CharField(5)
	tranche_age = peewee.CharField(20)
	statut_social = peewee.CharField(12)
	id_consommation = peewee.ForeignKeyField(Consommation)
	id_foyer = peewee.ForeignKeyField(Foyer)

class Ecoute(BaseModel):
	id_personne = peewee.ForeignKeyField(Personne)
	id_musique = peewee.ForeignKeyField(Musique)

	class Meta:
		primary_key = peewee.CompositeKey('id_personne', 'id_musique')

class Ecoute_habituellement(BaseModel):
	id_personne = peewee.ForeignKeyField(Personne)
	id_moment_d_ecoute = peewee.ForeignKeyField(Moment_d_écoute)

	class Meta:
		primary_key = peewee.CompositeKey('id_personne', 'id_moment_d_ecoute')

class Utilise(BaseModel):
	id_personne = peewee.ForeignKeyField(Personne)
	id_plateforme = peewee.ForeignKeyField(Plateforme)

	class Meta:
		primary_key = peewee.CompositeKey('id_personne', 'id_plateforme')


mysql_db.create_tables([
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
	])

mysql_db.close()


