import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
import sys
from tkinter import *

def main():
    keyword = ''
    keyword = str(keyword.join(sys.argv[1]))
    month = ''
    month = str(month.join(sys.argv[2]))

    print('the keyword is ', keyword)
    #read in the data from the txt file
    tweets_data_path = './twitter_data.txt'

    tweets_data = []
    tweet_file = open(tweets_data_path, 'r')
    for line in tweet_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    print (len(tweets_data)) #number of tweets in dataset

    tweets = pd.DataFrame()

    #runs lambda function that takes in a tweet, outputs the text from the tweet, text is one of the built in structures from the twitter data
    tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
    tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
    tweets['created_at'] = list(map(lambda tweet: tweet['created_at'], tweets_data))


    tweets_by_lang = tweets['lang'].value_counts() #finds frequency of each unique term


    #detrmines if word is found in text, returns bool value_counts
    def word_in_text(word, text):
            word = word.lower()
            text = text.lower()
            match = re.search(word, text)
            if match:
                return True
            return False

    #runs lambda function that takes in tweet['text'] amd outputs true into new column if word is found in a tweet
    #keyword = 'nike'
    tweets['keyword'] = tweets['text'].apply(lambda tweet: word_in_text(keyword, tweet))

    #prints number of tweets with these key words by counting the number of True values
    print ("Number of tweets that mention Python " + str(tweets['keyword'].value_counts()[True]))



    #reformatting  from String to print
    tweets['month'] = tweets['created_at'].map(lambda x: str(x)[4:7])
    tweets['day'] = tweets['created_at'].map(lambda x: str(x)[8:10])
    tweets['time'] = tweets['created_at'].map(lambda x: str(x)[11:16])



    #converting month from string to int
    months_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7,'Aug': 8, 'Sept': 9, 'Oct': 10, 'Dec': 12}
    def mapper(month):
        return months_map[month]
    tweets['month'] = tweets['month'].apply(lambda x: mapper(x))
    month = mapper(month)
    print('the value of month is', month)


    #converts month, day, time to type prints
    tweets['month'] =tweets['month'].astype('int64')
    tweets['day'] =tweets['day'].astype('int64')
    #drops ':' from time
    tweets['time'] = tweets['time'].replace({':':''}, regex=True)
    tweets['time'] =tweets['time'].astype('int64')
    tweets.drop(['created_at'], axis=1, inplace=True)
    tweets.drop(['text'], axis=1, inplace=True)





    #delete tuples that have 'false' in keyword column
    indexnames = tweets[tweets['keyword'] == False].index
    tweets.drop(indexnames, inplace=True)

    #Takes desired month and day from user
    df = pd.DataFrame()

    df = tweets.loc[lambda df: df['month'] == month]
    df = df.loc[lambda df: df['day'] == 27]

    #counts number of repeat instances every hour
    df_count = pd.DataFrame()
    df_count1 = pd.DataFrame()
    df_count2 = pd.DataFrame()




    df_count = df.groupby(['month','day','time'])['time'].count().reset_index(name = 'count')




    df_count.plot(kind = 'scatter', x='time', y='count')
    #plt.scatter(df.time, df_count)
    print(df_count.head())

    plt.savefig('foo.png')


if __name__ == "__main__":
    try:
        main()
    except:
        r = Tk()
        Label(r, text='Unable to process , try checking another month or changing the keyword', fg = 'red').grid(row=0)
        button = Button(r, text='Close', width=25, command=r.destroy)
        button.grid(row=3, column=1)
        r.mainloop()
