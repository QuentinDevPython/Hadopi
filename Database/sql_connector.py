import mysql.connector

database = mysql.connector.connect(
	host='localhost',
	user = 'root',
	password = 'root',
	)

cur = database.cursor()

cur.execute('CREATE DATABASE IF NOT EXISTS hadopi')
