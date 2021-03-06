#This code needs to compute initial centroids, cluster tweets, and then choose 1 tweet to keep out of each cluster
import mysql.connector
from compute_clusters import compute_clusters
from remove_tweets import remove_tweets
import datetime

if __name__ == '__main__':
	start = datetime.datetime.now()
        cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
			      charset='utf8',
                     	      use_unicode=True)
        cursor = cnx.cursor()
        teams = ['bulls', 'celtics', 'knicks', 'lakers', 'warriors']
        for team_name in teams:
		query = ('select id, text, score from ' + team_name.lower() + '_tweets;')
		cursor.execute(query)
		tweets = []
		tweets_to_delete = []
		for (id, text, score) in cursor:
			tweet = {'id': str(id), 'text': text, 'score': score}
			tweets.append(tweet)
		
		clusters = compute_clusters(tweets)
		remove_tweets(clusters, team_name)


	end = datetime.datetime.now()
	timeelapsed = (end - start).seconds
	logfile = open("/var/www/SocialSensingProject/log.txt", 'a')
	logfile.write("Deleted duplicate tweets at " + str(datetime.datetime.now())+ ". It took " + str(timeelapsed) + " seconds." + '\n')
	logfile.close()

	cnx.commit()
	cnx.close()	

		
