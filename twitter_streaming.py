# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "1058915490494668800-a85hFJQjWQXCydzcCrlUgT5BDqKAm1"
access_token_secret = "xcsmZhlnke8o6ax1x1HWQpyEGZJ28io23NQSJ2uLz4nwu"
consumer_key = "CZrjAjfGWxvG1e6x5c4uyxyOM"
consumer_secret = "3RF1kyAYeWxSZBcRSMxkKf1pusk9GeVHrjNzQu7D32GQIruBfl"

#This is basic listener that just prints received tweets to stdout
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True
    def en_error(self, status):
        print(status)

if __name__ == '__main__':
    #Handles twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #Filters Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python'])
