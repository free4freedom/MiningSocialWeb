import twitter
import json

CONSUMER_KEY = 'Il4zL2aYkiv5gK48rOnf20ygT'
CONSUMER_SECRET = 'uzmhD58Q7VRT6ygeVUUorcMsGr2fZXfnloIS5ZUPRZPQkQYbbn'
OAUTH_TOKEN = '404911413-2wMh9NfTpr6CkLGIkdrbBsaAMZ7FnGWUcHbn8zh5'
OAUTH_TOKEN_SECRET = 'Gx2oSgxv13BQ8ROQQATncCn8tjjB6qATpCZirqqZgs55M'


auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

#print twitter_api

#-------------------------------
WORLD_WOE_ID = 1
US_WOE_ID = 23424977
INDIA_WOE_ID = 23424848
HYDERABAD_WOE_ID =  29221650
PUNE_WOE_ID = 29220306

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
#us_trends = twitter_api.trends.place(_id=US_WOE_ID)
india_trends = twitter_api.trends.place(_id=INDIA_WOE_ID)
#hyd_trends = twitter_api.trends.place(_id=HYDERABAD_WOE_ID)
#pune_trends = twitter_api.trends.place(_id=PUNE_WOE_ID)

world_trend_set = set([ trend['name'] for trend in world_trends[0]['trends'] ] )
india_trend_set = set([ trend['name'] for trend in india_trends[0]['trends'] ] )
#hyd_trend_set = set([ trend['name'] for trend in hyd_trends[0]['trends'] ] )

print india_trend_set
#print hyd_trend_set

print world_trend_set.intersection(india_trend_set)
#print india_trend_set.intersection(hyd_trend_set)
#print json.dumps(world_trends, indent=1)
