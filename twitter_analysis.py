import json
import pandas as pd
import matplotlib.pyplot as plt
import re
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

#graphs number of tweets written in top 5 languages
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
#plt.savefig('test.png')


#detrmines if word is found in text, returns bool value_counts
def word_in_text(word, text):
        word = word.lower()
        text = text.lower()
        match = re.search(word, text)
        if match:
            return True
        return False

#runs lambda function that takes in tweet['text'] amd ouputs true into new column if word is found in a tweet
tweets['nike'] = tweets['text'].apply(lambda tweet: word_in_text('nike', tweet))

#prints number of tweets with these key words by counting the number of True values
print ("Number of tweets that mention Python " + str(tweets['nike'].value_counts()[True]))
#print ("Number of tweets that mention Javascript " + str(tweets['javascript'].value_counts()[True]))
#print ("Number of tweets that mention Ruby " + str(tweets['ruby'].value_counts()[True]))


#Reformatting created_at column
tweets['created_at'] = tweets['created_at'].map(lambda x: str(x)[7:-20])
tweets['created_at'] =tweets['created_at'].astype('int64')

#delete tuples that have 'false' in python column
indexnames = tweets[tweets['nike'] == False].index
tweets.drop(indexnames, inplace=True)

#finds the number of True values for each day and puts it into Dataframe
tweets.set_index('created_at', inplace=True)
tweets = tweets.groupby(['created_at']).sum()


print(tweets.head())



#Seperate Df that has created_at as index, and keywords (python column values)
#tweets.set_index('created_at', inplace = True)

def create_graph():
#create scatter plot of keyword over time
    tweets.plot(kind = 'bar')
    plt.title("Number of mentions of the word 'Nike'")
    plt.ylabel('Number of tweets')
    plt.xlabel('Days')
    plt.savefig('foo.png')


"""

plt.figure(figsize=(8,5))
x_data, y_data = (df["Year"].values, df["Value"].values)
plt.plot(x_data, y_data, 'ro')
plt.ylabel('GDP')
plt.xlabel('Year')
plt.show()
"""
