import tweepy

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Retrieve notifications
notifications = api.mentions_timeline(count=5)

# Output notifications in Conky format
output = ''
for notification in notifications:
    output += '${goto 10}' + notification.author.name + ': '
    output += '${goto 130}' + notification.text + '\n'
print(output)
