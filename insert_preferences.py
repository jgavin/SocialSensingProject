import mysql.connector
from mysql.connector import Error

def insert_preferences(email, virality, time, relevance):
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor(buffered=True)
	
	#Check if user exists
	query = ('select username from users;')
	cursor.execute(query)
	
	exists = 0
	users = ''
	for (username) in cursor:
		user = str(''.join(username))
		if user == str(email):
			exists = 1
			break
		
	if exists == 1:
		query = ("UPDATE preferences SET virality=" + str(virality) + ", time=" +  str(time) +  ", relevance=" + str(relevance) + " where username='" + email + "';")
		try:
			cursor.execute(query)
			cnx.commit()
			cnx.close()	
			return 1	
		except Error as e:		
			return 0	
	else:
		return 0

	