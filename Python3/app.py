import tweepy
import time


CONSUMER_KEY 	= 'AOnb4y9lGhMPkad4e5lj02Ktf'
CONSUMER_SECRET = 'cFnhhnt7wNMKvS6IT9zA7aeXIMFMoRVmR5kfTywaIgz5yzwpbP'
ACCESS_KEY		= '1255858961020059648-8SL02AO5fI0nYlQe67roVQhqwqrRz1'
ACCESS_SECRET	= 'faJbx9XrPq8bqLVVbZUqUeSERAowfS9RMe2Hhzls1BcKv'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


FILE_NAME = 'oldTweets.txt'

#	The function below return the ID of the last tweet that has been replied

def retrive_lastSeenID(fileName):
	f_read = open(fileName, 'r')
	last_seenID = int(f_read.read().strip())
	f_read.close()
	return last_seenID

# This function stores the ID of the tweet that has been replied

def store_lastSeenID(last_seenID, fileName):
	f_write = open(fileName, 'w')
	f_write.write(str(last_seenID))
	f_write.close()
	return 
def reply_to_tweets():
	print("reviewing and replying to tweets", flush= True)
	last_seenID = retrive_lastSeenID(FILE_NAME)
	mentions = api.mentions_timeline(last_seenID, tweet_mode = 'extended')

	# Iterating through all tweets  
	for index in reversed(mentions):
		print(str(index.id) +" - "+ index.full_text);
		last_seenID = index.id
		store_lastSeenID(last_seenID, FILE_NAME)
		if '#askbot' in index.full_text.lower():
			print("Found the tweet with #askbot");
			print("replying to the tweets ")
			api.update_status('@'+index.user.screen_name+' have a nice day ',index.id);

while True:
	reply_to_tweets();
	time.sleep(15);