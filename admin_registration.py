# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 16:56:36 2020

@author: reube
"""


import pymysql
from tkinter import *
from tkinter import StringVar
from tkcalendar import Calendar, DateEntry
from datetime import datetime

def adjustWindow(window):
    w = 800  # width for the window size
    h = 700  # height for the window size
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    window.resizable(False, False)    # disabling the resize option for the window
    window.configure(background='#013243')    # making the background #00b5cc of the window

def registration_form():
    
    root=Tk()
    adjustWindow(root)
    txt=[]
    root.iconbitmap("education.ico")
    root.title("REGISTRATION FORM FOR ADMIN/STAFF")
    Label(root,text=" Registration Form For Student ",font=("Open Sans", 20, 'bold'), fg='#00b5cc',bg="#013243").pack()
    big_frame = Frame(root,background='#013243')
    big_frame.place(x=150,y=90)
    Admin=StringVar()
    Label(big_frame,text="Admin Name",font=("Open Sans", 15, 'bold'), fg='#00b5cc',bg="#013243" ).grid(row=1,column=0,padx=3,pady=3, sticky = E)
    Entry(big_frame,textvariable=Admin,font=("Open Sans", 15, 'bold'), fg='#00b5cc',bg="#013243").grid(row=1,column=1,padx=3,pady=3, sticky = E)
    root.mainloop()
registration_form()