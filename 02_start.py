import twitter
import json

CONSUMER_KEY = 'Il4zL2aYkiv5gK48rOnf20ygT'
CONSUMER_SECRET = 'uzmhD58Q7VRT6ygeVUUorcMsGr2fZXfnloIS5ZUPRZPQkQYbbn'
OAUTH_TOKEN = '404911413-2wMh9NfTpr6CkLGIkdrbBsaAMZ7FnGWUcHbn8zh5'
OAUTH_TOKEN_SECRET = 'Gx2oSgxv13BQ8ROQQATncCn8tjjB6qATpCZirqqZgs55M'


auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

#--------------------------------------------

q = '@narendramodi'
count = 10

search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']

for _ in range(5) :
	print "Length of statuses : ", len(statuses)

	try : 
		next_results = search_results['search_metadata']['next_results']
	except  KeyError, e :
		break

	kwargs = dict( [ kv.split('=') for kv in next_results[1:].split("&")  ])

	search_results = twitter_api.search.tweets(**kwargs)
	statuses += search_results['statuses']


for i in range(len(statuses) ) : 
	print json.dumps(statuses[i]['text'], indent=1 )
	print json.dumps(statuses[i]['created_at'], indent=1 )
	print 
