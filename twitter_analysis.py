import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
import sys

def main():
    keyword = str(sys.argv[1:])
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
    #print ("Number of tweets that mention Javascript " + str(tweets['javascript'].value_counts()[True]))
    #print ("Number of tweets that mention Ruby " + str(tweets['ruby'].value_counts()[True]))


    #reformatting  from String to print
    tweets['month'] = tweets['created_at'].map(lambda x: str(x)[4:7])
    tweets['day'] = tweets['created_at'].map(lambda x: str(x)[8:10])
    tweets['time'] = tweets['created_at'].map(lambda x: str(x)[11:16])



    #converting month from string to int
    months_map = {'Aug': 8, 'Sept': 9, 'Oct': 10, 'Dec': 11}
    def mapper(month):
        return months_map[month]
    tweets['month'] = tweets['month'].apply(lambda x: mapper(x))


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


    #finds the number of True values for each hour of a day of a specific month and puts it into Dataframe
    #tweets.set_index('month', inplace=True)
    #tweets = tweets.groupby(['day']).sum()

    #Takes desired month and day from user
    df = pd.DataFrame()
    df = tweets.loc[lambda df: df['month'] == 8]
    df = df.loc[lambda df: df['day'] == 27]
    #counts number of repeat instances every hour
    df_count = pd.DataFrame()
    df_count['count'] = df['time'].value_counts()
    df_count.index.name = 'time'
    #df_count.rename( columns={'' :'count'}, inplace=True )
    print(df_count.head())




    df_count.plot(kind = 'bar')
    plt.savefig('foo.png')



    """
    plt.figure(figsize=(8,5))
    x_data, y_data = (df_count.time.values, df_count["count"].values)
    plt.plot(x_data, y_data, 'ro')
    plt.ylabel('count')
    plt.xlabel('time')
    plt.savefig('foo.png')
    #Seperate Df that has created_at as index, and keywords (python column values)
    #tweets.set_index('created_at', inplace = True)
    def create_graph(month, day):
        #Obtain data from user's desired month and day
        print(tweets.loc[lambda df: df['month'] == 8])
    #create scatter plot of keyword over time
        tweets.plot(kind = 'bar')
        plt.title("Number of mentions of the word 'Nike'")
        plt.ylabel('Number of tweets')
        plt.xlabel('Days')
        plt.savefig('foo.png')
    plt.figure(figsize=(8,5))
    x_data, y_data = (df["Year"].values, df["Value"].values)
    plt.plot(x_data, y_data, 'ro')
    plt.ylabel('GDP')
    plt.xlabel('Year')
    plt.show()
    """
if __name__ == "__main__":
    main()
