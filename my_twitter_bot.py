import tweepy
import time

print('this is my twitterbot', flush=True)

CONSUMER_KEY = 'cXHpMUqly6ZvIwYGopGoK4RUT'
CONSUMER_SECRET = '06ulKkDL9LWsRvhu4loczksXXH1WcDyAoXQbQp9CVbPRJLLLiH'
ACCESS_KEY = '1259905464818696196-I8DVys11FpXGSDTEv55rTM2I1HpP8n'
ACCESS_SECRET = 'blMItXivddyqStxRYs9QPKMwAC3oikaSJRFL2xeH1LE71'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def read_last_seen_id(file_name):
    # Read file and split by newline
    with open(file_name, 'r') as fh:
        data = fh.read().split('\n')

    # Remove empty lines from list
    data = list(filter(None, data))

    # Return last line
    return int(data[-1])

if __name__ == '__main__':
    file_name = 'last_seen_id.txt'
    id = read_last_seen_id(file_name)
    print(id)

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if 'Oi' in mention.full_text.lower():
            print('found #data', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    '~Oi, tudo bem?~', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)