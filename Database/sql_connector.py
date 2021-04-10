import mysql.connector

database = mysql.connector.connect(
	host='localhost',
	user = 'root',
	password = 'root',
	auth_plugin='mysql_native_password'
	)

cur = database.cursor()

cur.execute('CREATE DATABASE IF NOT EXISTS hadopi')
