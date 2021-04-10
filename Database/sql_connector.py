import mysql.connector

database = mysql.connector.connect(
	host='localhost',
	user = 'root',
	password = 'root',
	)

cur = database.cursor()

cur.execute('DROP DATABASE IF EXISTS hadopi')
cur.execute('CREATE DATABASE IF NOT EXISTS hadopi')
