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

class Personne(BaseModel):
	id_personne = peewee.AutoField(primary_key = True)
	sexe = peewee.CharField(5)
	tranche_age = peewee.CharField(50)
	statut_social = peewee.CharField(12)

class Appareil(BaseModel):
	id_appareil = peewee.AutoField(primary_key = True)
	type_appareil = peewee.CharField(15)
	frequence_utilisation_internet = peewee.CharField(50)

class Utilise(BaseModel):
	id_personne = peewee.ForeignKeyField(Personne)
	id_appareil = peewee.ForeignKeyField(Appareil)

class Habitation(BaseModel):
	id_habitation = peewee.AutoField(primary_key = True)
	id_personne = peewee.ForeignKeyField(Personne)
	region = peewee.CharField(50)
	nb_habitants_par_ville = peewee.CharField(50)
	nb_personne_foyer = peewee.SmallIntegerField()
	nb_enfants_foyer = peewee.SmallIntegerField()

class Question(BaseModel):
	id_question = peewee.AutoField(primary_key = True)
	id_personne = peewee.ForeignKeyField(Personne)
	enonce = peewee.CharField(255)

class Q1_Type_de_question(BaseModel):
	id_personne = peewee.ForeignKeyField(Personne, primary_key=True)
	id_question = peewee.ForeignKeyField(Question)
	musique = peewee.BooleanField()
	films = peewee.BooleanField()
	series_TV = peewee.BooleanField()
	photos = peewee.BooleanField()
	jeux_videos = peewee.BooleanField()
	livres = peewee.BooleanField()
	logiciels = peewee.BooleanField()
	presse = peewee.BooleanField()
	retransmission_sportive = peewee.BooleanField()

class Q2_Mode_de_consommation(BaseModel):
	id_personne = peewee.ForeignKeyField(Personne, primary_key=True)
	id_question = peewee.ForeignKeyField(Question)
	frequence_illegal_musique = peewee.CharField()
	frequence_illegal_films = peewee.BooleanField()
	frequence_illegal_series_TV = peewee.BooleanField()
	frequence_illegal_photos = peewee.BooleanField()
	frequence_illegal_jeux_videos = peewee.BooleanField()
	frequence_illegal_livres = peewee.BooleanField()
	frequence_illegal_logiciels = peewee.BooleanField()
	frequence_illegal_presse = peewee.BooleanField()
	frequence_illegal_retransmission_sportive = peewee.BooleanField()

class Q3_Lieu_ecoute_musique(BaseModel):
	id_personne = peewee.ForeignKeyField(Personne, primary_key=True)
	id_question = peewee.ForeignKeyField(Question)
	reveil_avant_dormir = peewee.BooleanField()
	au_travail = peewee.BooleanField()
	en_cuisine = peewee.BooleanField()
	sous_la_douche = peewee.BooleanField()
	dans_les_transports = peewee.BooleanField()
	en_faisant_du_sport = peewee.BooleanField()
	en_voiture = peewee.BooleanField()
	avec_des_amis = peewee.BooleanField()

class Q4_Facon_de_consommer_musique(BaseModel):
	id_personne = peewee.ForeignKeyField(Personne, primary_key=True)
	id_question = peewee.ForeignKeyField(Question)
	ecoute_jours = peewee.CharField(100)
	frequence_musique = peewee.CharField(100)
	nb_concert = peewee.CharField(100)
	radio_via_internet = peewee.BooleanField()
	appareil_plus_frequent = peewee.CharField(100)
	frequence_seul = peewee.CharField(100)
	frequence_accompagne = peewee.CharField(100)

class Q5_Type_de_musique(BaseModel):
	id_personne = peewee.ForeignKeyField(Personne, primary_key=True)
	id_question = peewee.ForeignKeyField(Question)
	variete = peewee.BooleanField()
	jazz = peewee.BooleanField()
	dance = peewee.BooleanField()
	electronique = peewee.BooleanField()
	metal = peewee.BooleanField()
	R_B = peewee.BooleanField()
	soul = peewee.BooleanField()
	reggae = peewee.BooleanField()
	musiques_du_monde = peewee.BooleanField()
	autres_genres = peewee.BooleanField()
	pop_rock = peewee.BooleanField()
	classique = peewee.BooleanField()

mysql_db.create_tables([
	Personne, 
	Appareil, 
	Habitation, 
	Question, 
	Q1_Type_de_question, 
	Q2_Mode_de_consommation,
	Q3_Lieu_ecoute_musique,
	Q4_Facon_de_consommer_musique,
	Q5_Type_de_musique
	])

mysql_db.close()


