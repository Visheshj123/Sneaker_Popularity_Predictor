import tkinter as tk
from tkinter import *
import twitter_analysis
import twitter_streaming
m = tk.Tk() #creates window
m.title("Twitter Analysis")

label = Label(m, text = 'Days to Stream').grid(row=0)
e1 = Entry(m)
e1.grid(row=0, column=1)

m.mainloop()
