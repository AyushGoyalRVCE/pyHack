import tweepy
import tweepy as twitter
import time, datetime


API_KEY = "TcBIaNyX4Y4kbdqN8fe1TxF3P"
API_SECRET_KEY = "ayDmV53D4kLKewfYJiDv3F1iN1HMeGbGFPbrZuwdvpOeb8f1e9"
ACCESS_TOKEN = "1563058515706802177-PgOee9SPuyPbuhf70mTiLcUv1kl6Fv"
SECRET_ACCESS_TOKEN = "3zl50tYyAy6nUOWOhrgGcucjHWhphtl9uCTKFcG9WThm2"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAACSJgQEAAAAAtAPHPKBaYjY3PuIBql%2F4GLEEDnM%3DYukS22hT8xgIhA4ZrG4XhcU9XZPEODPcaCsgdBZ3xWA89wYTzH"
TWITTER_USERNAME = "AayushGoyaal"

client = tweepy.Client(BEARER_TOKEN,API_KEY,API_SECRET_KEY,ACCESS_TOKEN,SECRET_ACCESS_TOKEN)
auth = twitter.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,SECRET_ACCESS_TOKEN)
api = twitter.API(auth)

list_tweet_text = []

MESSAGE = "THNX"
client_id = client.get_me().data.id


#
# start_id = 1
# initialisation_resp = client.get_users_mentions(client_id)
# if initialisation_resp.data != None:
#     start_id = initialisation_resp.data[0].id
#
# response = client.get_users_mentions(client_id,since_id=start_id)

file = open("file.txt", mode="a")

def retweeter(hashtag1,hashtag2,delay):  #hastag should be positive hash


        print(f"\n{datetime.datetime.now()}\n")



        for tweet in twitter.Cursor(api.search_tweets,q = hashtag1,rpp =4).items(4):
            try:
                print(tweet.text)
                tweet_id = dict(tweet._json)["id"]
                tweet_text = dict(tweet._json)["text"]
                list_tweet_text.append(tweet_text)

                print("id:  "+str(tweet_id))
                print("text:  "+str(tweet_text))

                api.retweet(tweet_id)

            except twitter.errors.TweepyException as error:
                 print(error)

        for tweet in twitter.Cursor(api.search_tweets, q=hashtag2, rpp=4).items(4):
            try:
                if tweet.author.name != TWITTER_USERNAME:
                    if not tweet.favorited :
                            print(f"liking {tweet.id} ({tweet.author.name})")
                            api.create_favorite(tweet.id)
                            #api.update_status(status ="dbjkdcs",in_reply_to_tweet_id = tweet.id, text = "hello this ngo thnx for posting review")
                            #api.update_status("thnx", in_reply_to_status_id=tweet.id)
            except twitter.errors.TweepyException as error:
                 print(error)


        # if response.data != None:
        #     for tweet in response.data:
        #         try:
        #             print(tweet.text)
        #             client.create_tweet(in_reply_to_tweet_id=tweet.id,text=MESSAGE)
        #             start_id=tweet.id
        #         except Exception as error:
        #             print(error)
        #






        time.sleep(delay)
        return list_tweet_text


def appreciate(ngohash,delay): #hastag is the normal hastag that links to ngo
    while True:
        print(f"\nstart liking tweets related to ngo")

        for tweet in twitter.Cursor(api.search_tweets,q= ngohash, rpp= 10).items(1):
            try:
                if tweet.author.name != TWITTER_USERNAME:
                    if not tweet.favorited :
                            print(f"liking {tweet.id} ({tweet.author.name})")
                            api.create_favorite(tweet.id)
                            api.update_status(status = "thnx", in_reply_to_tweet_id=tweet.id)
            except twitter.errors.TweepyException as error:
                 print(error)

        time.sleep(delay)

while True:
    retweeter("#pyhackquadsquad","#gopyhackquadsquad",18)
    #appreciate("#ourngo", 18)
    print(list)
