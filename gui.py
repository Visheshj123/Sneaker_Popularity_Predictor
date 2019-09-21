from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_streaming
from tkinter import *
import threading
import subprocess


choices = { 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec'}

r = Tk()
r.title('Key Word Twitter Search')

#adds stop button and places it in row = 0, column = 1
button = Button(r, text='Stop', width=25, command=r.destroy)
button.grid(row=3, column=1)


#Enter keyword you want to search
Label(r, text='Keyword').grid(row=0)
e1 = Entry(r)
e1.grid(row=0, column=1)


#desired month and day you want for the data
tkvar = StringVar(r)
tkvar.set('Jan')
popupMenu = OptionMenu(r, tkvar, *choices)
popupMenu.grid(row=2, column=1)
#Use tkvar.get to obtain value

#Button to stream twitter data using keyword you entered
"""button = Button(r, text='Search', width=25, command=twitter_streaming.stream_data(e1.get()))
button.grid(row=3, column = 2)
"""
def get_keyword():
    keyword = e1.get()
    return str(keyword)

def launch_analysis():
    keyword = get_keyword()
    subprocess.call(['python', 'twitter_analysis.py', keyword, tkvar.get()])



#Button to run analysis on keyword
button = Button(r, text='Analyze', width=25, command=launch_analysis)
button.grid(row=3, column = 2)


#subprocess.call(['python', 'twitter_analysis.py', 'nike'])


r.mainloop()
