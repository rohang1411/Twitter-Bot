import tweepy

print("this is my twitter bot")

CONSUMER_KEY = 'XXXXX'
CONSUMER_SECRET = 'XXXXX'
ACCESS_TOKEN = 'XXXXX'
ACCESS_TOKEN_SECRET = 'XXXXX'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

id_list = []

# mentions.__dict__

# print(mentions)
# print(type(mentions[0].id))
# print(type(mentions[0].text))

#last_seen_id = idlist
mentions = api.mentions_timeline()

for i in reversed(mentions):
    t = mentions
    print(i.id_str + ' - ' + i.text)
    if 'tweetme' in i.text.lower():
        api.update_status('@' + i.user.screen_name + ' hello from my side', i.id)