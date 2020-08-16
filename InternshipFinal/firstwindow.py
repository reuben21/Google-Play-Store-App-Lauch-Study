# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 14:31:23 2020

@author: harsh
"""
from functques import *
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import PhotoImage
import functques as fn

from collections import OrderedDict 
import tkinter as tk
#from adddata import *
import time
import os
import pandas as pd
import numpy as np
import tkinter.messagebox as tm
from PIL import Image

import pymysql
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.cm as cm
from collections import OrderedDict



def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
def cancel():
    mcanvas.delete("all")
    head=Label(mcanvas,text="Google \nPlayStore \n App launch \nStudy",width=30,font=("Lucida",50,'bold'),fg='#ffffff',bg='#102131')
    mcanvas.create_window(400, 200, window=head)
    mcanvas.update()
def _quit():
        global screen
        screen.quit()     # stops mainloop
        screen.destroy() 



 


def saveing(x,y,z,p):
    global data
    
    value=[]  
    if z=='C:\\InternshipFinal\\App-data.csv':
        date1=p[0].get()
        month=p[1].get()
        year=p[2].get()
        date=month+' '+date1+','+' '+year
        print(date)
        dd=data.columns.tolist()
    elif z=='C:\\InternshipFinal\\user.csv':
        dd=sample.columns.tolist()
     
    for i in x:
        value.append(i.get())
    print(value)
    
    
    if z=='C:\\InternshipFinal\\App-data.csv':
        try:
            connection = pymysql.connect(host="localhost", user="root", password="", database="googleplaystore") # database connection
            cursor = connection.cursor()
            insert_query = "INSERT INTO appdata (appname,category,rating,review,size,install,type,price,cont_rat,genres,last_updated,current_version,android_version) VALUES('"+ value[0]+ "', '"+ value[1]+ "', '"+ value[2] + "', '"+ value[3] + "', '"+ value[4] + "', '"+ value[5]+ "', '"+ value[6]+ "', '"+ value[7]+ "', '"+ value[8]+ "', '"+ value[9]+ "', '"+ date+ "', '"+ value[10] + "', '"+ value[11] + "' );" # queries for inserting values
            cursor.execute(insert_query) # executing the 
            connection.commit() # commiting the connection then closing it.
            connection.close() # closing the connection of the database
           
            
            value.insert(10,date)
            #print(value)
            value[5]=str(value[5])
            value[7]=str(value[7])
            #print(value)
            print(dd)
           
            dp=pd.DataFrame([value],columns=dd)
            dat=data.append(dp)
            tk.messagebox.showinfo('Success','Data Successfully Written')

        except pymysql.Error:
            tk.messagebox.showinfo('Error',"Database Error")
    elif z=='C:\\InternshipFinal\\user.csv':  
        try:
            connection = pymysql.connect(host="localhost", user="root", password="", database="googleplaystore") # database connection
            cursor = connection.cursor()
            insert_query = "INSERT INTO addreview (app,trans_rev,sentiment,sent_polar,sent_subj) VALUES('"+ value[0]+ "', '"+ value[1]+ "', '"+ value[2] + "', '"+ value[3] + "', '"+ value[4] + "' );"
            cursor.execute(insert_query)
            print(insert_query)
            connection.commit() # commiting the connection then closing it.
            connection.close() # closing the connection of the database
            
            dp=pd.DataFrame([value],columns=dd)
            print(dd)
            dat=sample.append(dp)
            tk.messagebox.showinfo('Success','Data Successfully Written')

        except pymysql.Error:
            tk.messagebox.showinfo('Error',"Database Error")      
            
            
        
        

#
#    if z=='C:\\InternshipFinal\\App-data.csv':
#              
#        value.insert(10,date)
#        #print(value)
#        value[5]=str(value[5])
#        value[7]=str(value[7])
#        #print(value)
#        print(dd)
#        dp=pd.DataFrame([value],columns=dd)
#        dat=data.append(dp)
#        
#        
#    elif z=='C:\\InternshipFinal\\user.csv':
#
#        dp=pd.DataFrame([value],columns=dd)
#        print(dd)
#        dat=sample.append(dp)



    dat.to_csv(z,index=False)
    y.config(state='disabled')
    
    

        

def check1(x):
        d=[]
      
        for i in x:
            if i.get()=='':
                tk.messagebox.showwarning('Fields empty','Please provide all the fields')
                return True
            
        try:
           if(isinstance(float(x[3].get()), float) and isinstance(float(x[4].get()), float)):
               if x[2].get()=='Neutral':
                   if float(x[3].get())==0 and 1>=float(x[4].get())>=0:
                       d.append(False)
                   else:
                       tk.messagebox.showwarning('Neutral sentiment','Please provide a 0 in Sentiment polarity and Sentiment Subjectivity.')
                       return True
               elif x[2].get()=='Positive':
                   if float(x[3].get())>0 and 1>=float(x[4].get())>=0:
                       d.append(False)
                   else:
                       tk.messagebox.showwarning('Positive sentiment','Please provide a positive value in Sentiment polarity and Sentiment Subjectivity.')
                       return True
               elif x[2].get()=='Negative':
                   if float(x[3].get())<0 and 1>=float(x[4].get())>=0:
                       d.append(False)
                   else:
                       tk.messagebox.showwarning('Positive sentiment','Please provide a negative value in Sentiment polarity and non negative value in Sentiment Subjectivity.')
                       return True
        except:
            tk.messagebox.showwarning('Wrong Value','Please provide a float value in Sentiment polarity and Sentiment Subjectivity.')
            return True
        
        if set(d)==False:
            return False    
        tk.messagebox.showinfo('Validate Succesfully','Now click on the Save Button')
       
def validate2(x,y):
    global sample
    for i in range(5):
        print(x[i].get())
    App=x[0].get()
    d=0
    ap=sample['App'].unique()
    for i in ap:
        if i.strip()==App.strip():
            msg='App named '+App+' is already present'
            tk.messagebox.showerror("Error",msg)
            d=1
    if(check1(x)):
        d=1
    if d==0:
        y.config(state='normal')
    
def add_rev():
    global screen,df,data,sample
    
    dates=[]
    sample=pd.read_csv('C:\\InternshipFinal\\user.csv')
    header2=sample.columns.tolist()
    global mcanvas
    val=Label(mcanvas,width=600,height=8,font=("Lucida",30,'bold'),fg='black',bg='#102131')
    mcanvas.create_window(300,250, window=val)
    txt=[]
    datecombo=[]
    month=['January', 'February', 'March', 'April','May','June','July','August','September', 'October', 'November','December']
    years=[]
    for i in range(1,32):
        dates.append(i)
    for i in range(2010,2020):
        years.append(i)

    mcanvas.delete("all")
    val=Label(mcanvas,width=600,height=8,font=("Lucida",30,'bold'),fg='black',bg='#102131')
    mcanvas.create_window(300,250, window=val)
#    
      
    txt2=[]
    for i in range(1,6):
        tk.Label(val,text=header2[i-1],width=17,font=("Lucida",11,'italic'),fg='#ffffff',bg='#102131').grid(row=i,column=0,padx=5,pady=5)
          
    for i in range(1,6):
        if i!=3:
            txtfield=tk.Entry(val,bg="white")
            txt2.append(txtfield)
            txtfield.grid(row=i,column=2)
        elif i==3:
            combo=ttk.Combobox(val,values=['Positive','Negative','Neutral'],state="readonly")
            txt2.append(combo)
            combo.grid(row=3,column=2)
    
    btn_save1=tk.Button(val,text='Save',state="disabled",fg='#ffffff',width=10,command=lambda:saveing(txt2,btn_save1,'C:\\InternshipFinal\\user.csv',''))    
    btn_validate1=tk.Button(val,text='Validate',width=10,fg='#ffffff',bg="#102131",command=lambda:validate2(txt2,btn_save1))
    btn_validate1.grid(row=7,column=2)
    btn_save1.grid(row=7,column=3)
    root.mainloop()       
    

def check(x,z):
    d=[]
    for i in x:    
        if i.get()=='':
            tk.messagebox.showwarning('Fields empty','Please provide all the fields')
            return True
    for j in z:
        if j.get()=='':
            tk.messagebox.showwarning('Fields empty','Please provide all the fields')
            return True

    try:
        if(isinstance(float(x[2].get()), float)):# code for checking the user entered a valid rating in the entry field
            if(float(x[2].get())<=5 and float(x[2].get())>=0):
                d.append(False)
            else:
                tk.messagebox.showerror('Out of range','Rating should be between 0 to 5 only')
                return True
    except:
        tk.messagebox.showwarning('Wrong Value','Please provide a float value in rating column')
        return True
    try:
        if(isinstance(int(x[3].get()), int)):
            d.append(False)
    except:
        tk.messagebox.showwarning('Wrong Value','Please provide a integer value in Reviews')
        return True
    try:
        
        if(isinstance(float(x[4].get()[:-1]), float)):
            if(x[4].get()[-1]=='k' or x[4].get()[-1]=='M'):
                d.append(False)
            else:
                tk.messagebox.showerror('Size',"Size should end with 'k' or 'M'")
                return True           
    except:
        tk.messagebox.showwarning('Wrong Value','Please provide a integer value followed in size column')
        return True
    try:
        if(isinstance(float(x[5].get()), float)):
            d.append(False)
    except:
        tk.messagebox.showwarning('Wrong Value','Please provide a integer value in Installs')
        return True
    try:
        if x[6].get()=='Free':
            if x[7].get()=='0':
                d.append(False)
            else:
                tk.messagebox.showwarning('Free app','Please enter 0 in price column')
                return True
    except:
        print('hi')
            
    try:
        if(isinstance(float(x[7].get()), float)):
            d.append(False)
    except:
        tk.messagebox.showwarning('Wrong Value','Please provide a float value in Price')
        return True

    
    if set(d)==False:
        tk.messagebox.showwarning('Successful','Please click on save')
        return False   
       
         
def validate(x,y,z):
    print("hello")
    for i in range(12):
        print(x[i].get())
    for i in range(3):
        print(z[i].get())
    App=x[0].get()
    d=0
    ap=data['App']
    for i in ap:
        if i.strip()==App.strip():
            msg='App named '+App+' is already present'
            tk.messagebox.showerror("Error",msg)
            d=1
            break
            
    if check(x,z):
        d=1

    if d==0:
        y.config(state='normal')    

def add_app_data():
    global mcanvas,screen,df,data
    dates=[]
    month=['January', 'February', 'March', 'April','May','June','July','August','September', 'October', 'November','December']
    years=[]
    for i in range(1,32):
        dates.append(i)
    for i in range(2010,2020):
        years.append(i)
    data=pd.read_csv("C:\\InternshipFinal\\App-data.csv")
    mcanvas.delete("all")
    val=Label(mcanvas,width=600,height=8,font=("Lucida",30,'bold'),fg='black',bg='#102131')
    mcanvas.create_window(300,250, window=val)
    header=data.columns.tolist()
    category= list(OrderedDict.fromkeys(data['Category']))
    content=list(OrderedDict.fromkeys(data['Content Rating']))
    genre=list(OrderedDict.fromkeys(data['Genres']))
    txt = []
    datecombo=[]
    dateco = Frame(val)
    for i in range(1,14):
        Label(val,text=header[i-1],width=11,font=("Lucida",11,'italic'),fg='white',bg='#102131').grid(row=i,column=0,padx=2,pady=2)
    for i in range(1,14):
        if i!=2 and i!=10 and i!=9 and i!=7 and i!=11 and i!=13:
            txtfield=tk.Entry(val,bg="white")
            txt.append(txtfield)
            txtfield.grid(row=i,column=1,padx=2,pady=2)
        elif i==2:
            combo=ttk.Combobox(val,values=category)
            txt.append(combo)
            combo.grid(row=2,column=1,padx=2,pady=2)
        elif i==9:
            combo=ttk.Combobox(val,values=content,state="readonly")
            txt.append(combo)
            combo.grid(row=9,column=1,padx=2,pady=2)
        elif i==10:
            combo=ttk.Combobox(val,values=genre,state="readonly")
            txt.append(combo)
            combo.grid(row=10,column=1,padx=2,pady=2)
        elif i==7:
            combo=ttk.Combobox(val,values=['Free','Paid'],state="readonly")
            txt.append(combo)
            combo.grid(row=7,column=1,padx=2,pady=2)
        elif i==11:
            
            combo=ttk.Combobox(dateco,values=dates,width=2,state="readonly")
            datecombo.append(combo)
            combo.grid(row=0,column=0,padx=2,pady=2)
            
            
            combo=ttk.Combobox(dateco,values=month,width=10,state="readonly")
            datecombo.append(combo)
            combo.grid(row=0,column=1,padx=2,pady=2)
            
            combo=ttk.Combobox(dateco,values=years,width=6,state="readonly")
            datecombo.append(combo)
            combo.grid(row=0,column=2,padx=2,pady=2)
            dateco.grid(row=11, column=1, padx=5, pady=5)
            
        elif i==13:
            combo=ttk.Combobox(val,values=list(data['Android Ver'].unique()),state="readonly")
            txt.append(combo)
            
            combo.grid(row=13,column=1,padx=2,pady=2)    
    btn_save=tk.Button(val,text='Save',state="disabled",width=10,bg="#102131",fg="white",command=lambda:saveing(txt,btn_save,'C:\\InternshipFinal\\App-data.csv',datecombo))    
    btn_validate=tk.Button(val,text='Validate',width=10,bg="#102131",fg="white",command=lambda:validate(txt,btn_save,datecombo))
    btn_validate.grid(row=14,column=1)
    btn_save.grid(row=14,column=2) 
    mcanvas.create_window()
    mcanvas.update()
    
    
    
def login_verify():
    global username_verify
    global password_verify
    try:
        connection = pymysql.connect(host="localhost", user="root", password="", database="googleplaystore") # database connection
        cursor = connection.cursor()
        select_query =  "SELECT * FROM details where empid = '" + username_verify.get() + "' AND password = '" + password_verify.get() + "';" # queries for retrieving values
        print(select_query)
        cursor.execute(select_query) # executing the queries
        student_info = cursor.fetchall()
        print(student_info)
        connection.commit() # commiting the connection then closing it.
        connection.close() # closing the connection of the database                    
        if student_info:
            messagebox.showinfo("Congratulation", "Login Succesfull") # displaying message for successful login
            add_app_data()# opening welcome window
        else:
            messagebox.showerror("Error", "Invalid Username or Password") #  
    except pymysql.Error:
        
        tk.messagebox.showinfo('Error',"Database Error")
    
def login():
    global mcanvas
    global username_verify
    global password_verify
    mcanvas.delete("all")
    val=Label(mcanvas,width=400,height=8,font=("Lucida",30,'bold'),fg='black',bg='#102131')
    mcanvas.create_window(400,250, window=val)
    # df= pd.read_csv("C:\\Users\\Harsh\\Desktop\\internship\\googleplaystore-App-data.csv")
    username_verify = StringVar()
    password_verify = StringVar()
    Label(val, text="Employee Login", width="400", height="2", font=("Lucida", 22, 'bold'), fg='white', bg='#102131').pack()
    
    Label(val, text="", bg='#102131',width='100', height='17').place(x=45, y=120) # blue background in middle of window
    Label(val, text="Please enter details below to login", bg='#102131', fg='white').pack()
    Label(val, text="", bg='#102131').pack() # for leaving a space in between
    Label(val, text="Employee ID * ", font=("Open Sans", 10, 'bold'), bg='#102131', fg='white').pack()
    Entry(val, textvar=username_verify).pack()
    Label(val, text="", bg='#102131').pack() # for leaving a space in between
    Label(val, text="Password * ", font=("Open Sans", 10, 'bold'), bg='#102131', fg='white').pack()
    Entry(val, textvar=password_verify, show="*").pack()
    Label(val, text="", bg='#102131').pack() # for leaving a space in between
    Button(val, text="LOGIN", bg="black", width=15, height=1, font=("Open Sans", 13, 'bold'), fg='white',command=login_verify).pack()
    Label(val, text="", bg='#102131').pack() # for leaving a space in between
    Button(val, text="New User? Register Here", height="2", width="30", bg='black', font=("Open Sans", 10, 'bold'), fg='white',command=register).pack()
    
    mcanvas.update()
    
    
#displaying message for invalid details

def register_user():
    
    global mcanvas
    global fullname
    global email
    global password
    global repassword
    global phone
    global gender
    global tnc
    

    if fullname.get() and email.get() and password.get() and repassword.get() and gender.get(): # checking for all empty values in entry field
        if (len(phone.get())!=10) and int(phone.get()): # checking for selection of university
            ph_no=Label(mcanvas, text="Enter the Valid Phone Number", fg="red",font=("Lucida", 11), width='30', anchor=W, bg='white')
            mcanvas.create_window(200,480,window=ph_no)
            return
        else:
            if tnc.get(): # checking for acceptance of agreement
                if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email.get()): # validating the email
                    if password.get() == repassword.get(): # checking both password match or not
                        # if u enter in this block everything is fine just enter the values in database
                        gender_value = 'male'
                        if gender.get() == 2:
                            gender_value = 'female'
                        try:
                            connection = pymysql.connect(host="localhost", user="root", password="", database="googleplaystore") # database connection
                            cursor = connection.cursor()
                            insert_query = "INSERT INTO details (empid,fullname,email, password, gender) VALUES('"+ phone.get() + "', '"+ fullname.get() + "', '"+ email.get() + "', '"+password.get() + "', '"+gender_value  + "' );" # queries for inserting values
                            cursor.execute(insert_query) # executing the queries
                            connection.commit() # commiting the connection then closing it.
                            connection.close() # closing the connection of the database
                            rs=Label(mcanvas, text="Registration Sucess", fg="green", font=("Lucida", 11), width='30', anchor=W, bg='white')
                            
                            mcanvas.create_window(200,480,window=rs)# printing successful registration message
                            pl=Button(mcanvas, text='Proceed to Login ->', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=login)
                            mcanvas.create_window(500,480,window=pl) # button to navigate back to login page
                        except pymysql.Error:
                            tk.messagebox.showinfo('Error',"Database Error")
                    else:
                        ps=Label(mcanvas, text="Password does not match", fg="red", font=("Lucida", 11), width='30', anchor=W, bg='white')
                        mcanvas.create_window(200,480,window=ps)
                        return
                else:
                    pvi=Label(mcanvas, text="Please enter valid email id", fg="red", font=("Lucida", 11), width='30', anchor=W, bg='white')
                    mcanvas.create_window(200,480,window=pvi)
                    return
            else:
                pat=Label(mcanvas, text="Please accept the agreement", fg="red", font=("Lucida", 11), width='30', anchor=W, bg='white')
                mcanvas.create_window(200,480,window=pat)
                return
    else:
        pfi=Label(mcanvas, text="Please fill all the details", fg="red",font=("Lucida", 11), width='30', anchor=W, bg='white')
        mcanvas.create_window(200,480,window=pfi)
        return
    mcanvas.update()

def register():
   
    global mcanvas
    global fullname
    global email
    global password
    global repassword
    global phone
    global gender
    global tnc
    global mcanvas




    mcanvas.delete("all")
    val=Label(mcanvas,width=400,height=8,font=("Lucida",30,'bold'),fg='black',bg='#102131')
    mcanvas.create_window(400,250, window=val)
    fullname = StringVar()
    email = StringVar()
    password = StringVar()
    repassword = StringVar()
    phone= StringVar()
    gender = IntVar()
    tnc = IntVar() 
     # configuring the window
    Label(val, text="Registration Form", width='32', height="2", font=("Lucida", 22, 'bold'), fg='white', bg='#102131').pack()
    Label(val, text="", bg='#102131', width='100', height='20').place(x=45, y=120)
    Label(val, text="Full Name:", font=("Open Sans", 11, 'bold'), fg='white', bg='#102131', anchor=W).pack()
    Entry(val, textvar=fullname).pack()
    Label(val, text="Email ID:", font=("Open Sans", 11, 'bold'), fg='white', bg='#102131', anchor=W).pack()
    Entry(val, textvar=email).pack()
    Label(val, text="Gender:", font=("Open Sans", 11, 'bold'), fg='white', bg='#102131', anchor=W).pack()
    Radiobutton(val, text="Male", variable=gender, value=1, bg='#102131').pack()
    Radiobutton(val, text="Female", variable=gender, value=2, bg='#102131').pack()
    Label(val, text="Employee ID :", font=("Open Sans", 11, 'bold'), fg='white', bg='#102131', anchor=W).pack()
    Entry(val, textvar=phone).pack()
    phone.set('Enter Phone Number')
    Label(val, text="Password:", font=("Open Sans", 11, 'bold'), fg='white', bg='#102131', anchor=W).pack()
    Entry(val, textvar=password, show="*").pack()
    Label(val, text="Re-Password:", font=("Open Sans", 11, 'bold'), fg='white', bg='#102131', anchor=W).pack()
    entry_4 = Entry(val, textvar=repassword, show="*")
    entry_4.pack()
    Checkbutton(val, text="I accept all terms and conditions", variable=tnc, bg='#102131', font=("Open Sans", 9, 'bold'), fg='brown').pack()
    Button(val, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='black', fg='white',command=register_user).pack()
    mcanvas.update()    
"""THE END OF ADDING DATA FORMS AND LOGIN AND REGISTRATION FORM """



""" QUESTION 10 CODE"""
def mont():
    
    global root
    global cat
    global can
    root = Tk()
    root.title("Insight of Google App's")
    width_value=root.winfo_screenwidth()
    root.configure(background='white') # configuring the window
    height_value=root.winfo_screenheight()
    root.geometry("%dx%d+300+200"%(700,700))
    mcan=Canvas(root,width=800,height=700,bg='white')
     
    mcan.place(x=0,y=0)   
    data=pd.read_csv('C:\\InternshipFinal\\App-data.csv')
    data=data.replace(np.nan,'Not Available')
    data['Installs'] = data['Installs'].map(lambda x: x.rstrip('+'))
    data['Installs'] = data['Installs'].map(lambda x: ''.join(x.split(',')))
    data['Installs'] = pd.to_numeric(data['Installs'])    
    d = pd.DatetimeIndex(data['Last Updated'])
    data['year'] = d.year
    data['month'] = d.month
    mon={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    for i in range(len(data)):
        if data['Category'][i]== cat.get(): 
            if data['month'][i] in mon:
                if mon[data['month'][i]]==0:
                    mon[data['month'][i]]=data['Installs'][i]
                else:
                    mon[data['month'][i]]+=data['Installs'][i] 
    print(mon)
    x=list(mon.keys())    
    y=list(mon.values())  
    z=max(y)    
    ind=y.index(z)      
    figure1 = plt.Figure(figsize=(10,8), dpi=70)
    axesObject = figure1.add_subplot(111)
    axesObject.bar(x,y)    
    axesObject.set_title(f"Maximum Downloads in a month for a {cat.get()} ")
    axesObject.grid()
    can= FigureCanvasTkAgg(figure1,mcan)    
    can.get_tk_widget().pack( fill=BOTH, expand=True)

    toolbar = NavigationToolbar2Tk(can,mcan)
    toolbar.update()   

def funct10():          
    global cat
    global mcanvas
    mcanvas.delete("all")
    val=Label(mcanvas,width=600,height=8,font=("Lucida",30,'bold'),fg='black',bg='#102131')
    mcanvas.create_window(300,250, window=val)
    data=pd.read_csv('C:\\InternshipFinal\\App-data.csv')
    data=data.replace(np.nan,'Not Available')
    cat=StringVar() 
    choices = list(data['Category'].unique())   
    Label(val, text='Select Category', anchor='w').grid(row=0, column=0 ,padx=5,pady=5, sticky="w")
    app=ttk.Combobox(val, width=40,state="readonly",text=cat,values=choices)
    app.grid(row=0, column=1 ,padx=5,pady=5, sticky="w") 
    app.set("--select--")          
    r=Button(val,text='Search',width=12,command=mont)
    r.grid(row=0, column=3 ,padx=5,pady=5)
    mcanvas.create_window()     
    mcanvas.update()    

"""Question 12"""

def sentim():
    global senti
    root = Tk()
    root.title("Insight of Google App's")
    width_value=root.winfo_screenwidth()
    height_value=root.winfo_screenheight()
    root.geometry("%dx%d+400+100"%(300, 600))
    root.configure(background='white')
    big_frame = Frame(root)
    big_frame.pack()
    canvas=[]
    for i in range(1):
            can=Canvas(big_frame,width=320,height=600,bg='white')
            canvas.append(can)
            can.grid(row=1,column=i)
    scroll1=Scrollbar(canvas[0])
    positive=Listbox(canvas[0],yscrollcommand = scroll1.set,height=35,width=45,bg='light green')
    scroll1.pack(side = 'right', fill = 'both')
    positive.pack(side = 'left', fill = 'both')
    updated_app={}
    data=pd.read_csv('C:\\InternshipFinal\\user.csv')
    data=data.replace(np.nan,'Not Available')
    app={}
    
    
    
    
    if senti.get()=='--select--' :
        root.destroy()
    
    
    for i in data['App']:
        app.update({i:0})   
    
    
       
    for i in range(len(data)): 
        if (data['App'][i] in app) and data['Sentiment'][i]==senti.get():
            if app[data['App'][i]]==0: 
                app[data['App'][i]]=1
            else:    
                app[data['App'][i]]+=1  
    
#    print(app)
    
    
    
    for key, value in sorted(app.items(), key=lambda item: item[1],reverse=True):
        updated_app.update({key:value})
    if senti.get()!='Same Ratio':
        for i in updated_app:
            positive.insert(END,i,updated_app[i])
    
#    print(updated_app)
              
    if senti.get()=='Same Ratio':
        app={}
        for i in data['App']:
           app.update({i:[0,0]})  
           print(app)   
        for i in range(len(data)): 
            if (data['App'][i] in app) and data['Sentiment'][i]=='Positive':
                if (app[data['App'][i]][0]) == 0: 
                    app[data['App'][i]][0]=1
                else:    
                    app[data['App'][i]][0]+=1  
        for i in range(len(data)): 
            if (data['App'][i] in app) and data['Sentiment'][i]=='Negative':
                if (app[data['App'][i]][1])==0: 
                    app[data['App'][i]][1]=1
                else:    
                    app[data['App'][i]][1]+=1 
        same={}           
        for i in app:
                if app[i][0]==0 or app[i][1]==0:
                    continue
                elif 0.75<float((app[i][0]/app[i][1]))<1.25:
                    if (1-app[i][0]/app[i][1])<0:
                         a=(1-app[i][0]/app[i][1])*(-1)
                    else:
                        a=(1-app[i][0]/app[i][1])
                    same.update({i:a})
        for i in same:
             positive.insert(END,i)            
        
def twelve():
    global senti
    mcanvas.delete("all")
    val=Label(mcanvas,width=600,height=8,font=("Lucida",30,'bold'),fg='black',bg='#102131')
    mcanvas.create_window(300,250, window=val)
    data=pd.read_csv('C:\\InternshipFinal\\user.csv')
    data=data.replace(np.nan,'Not Available')
    senti=StringVar() 
    choices=['Positive','Negative','Same Ratio']      
    Label(val, text='Select Sentiment', anchor='w').grid(row=0, column=0 ,padx=5,pady=5, sticky="w")
    app=Combobox(val , width=40,state="readonly",text=senti,values=choices)
    app.grid(row=0, column=1 ,padx=5,pady=5, sticky="w") 
    app.set("--select--")          
    r=Button(val,text='Search',width=12,command=sentim)
    r.grid(row=0, column=3 ,padx=5,pady=5)
    mcanvas.update()



"""Question 14 And Question 15"""
def revv():
     global root
     global search    
     global big_frame
     global filtered
     global appli
     global list_of_apps_most_positive_sentiments
     global list_of_apps_most_negative_sentiments
     global list_of_apps_most_average_sentiments
     root = Tk()
     root.title("Insight of Google App's")
     width_value=root.winfo_screenwidth()
     height_value=root.winfo_screenheight()
     root.geometry("%dx%d+0+0"%(1300,650))
     root.configure(background='white')
     big_frame = Frame(root)
     big_frame.pack()
     l=Label(big_frame,text='Positive',width=15,anchor=CENTER)
     l.config(font=("Lucida", 16,'bold'))
     l.grid(row=0, column=1 ,padx=5,pady=5)
     l=Label(big_frame,text='Neutral',width=15,anchor=CENTER)
     l.config(font=("Lucida", 16,'bold'))
     l.grid(row=0, column=2 ,padx=5,pady=5)
     l=Label(big_frame,text='Negative',width=15,anchor=CENTER)
     l.config(font=("Lucida", 16,'bold'))
     l.grid(row=0, column=3 ,padx=5,pady=5)
     data=pd.read_csv('C:\\InternshipFinal\\user.csv')
#     print(data)
     data=data.replace(np.nan,'Not Available')
     x = search.get()
     print(appli[filtered.index(search.get())])
     list_of_apps_most_positive_sentiments = []
     list_of_apps_most_negative_sentiments = []
     list_of_apps_most_average_sentiments = []
     list_of_apps_most_zero_sentiments = []
     
     
     list_of_apps_most_positive_sentiments = (data[(data.App == appli[filtered.index(search.get())]) & (data.Sentiment == 'Positive')].Translated_Review).tolist()
#     print(list_of_apps_most_positive_sentiments)    
     list_of_apps_most_negative_sentiments = (data[(data.App == appli[filtered.index(search.get())]) & (data.Sentiment == 'Negative')].Translated_Review).tolist()
#     print(list_of_apps_most_negative_sentiments)        
     list_of_apps_most_average_sentiments = (data[(data.App == appli[filtered.index(search.get())]) & (data.Sentiment == 'Neutral')].Translated_Review).tolist()
#     print(list_of_apps_most_average_sentiments ) 
     
     canvas=[]
     for i in range(4):
            can=Canvas(big_frame,width=320,height=600,bg='#003b6b')
            canvas.append(can)
            can.grid(row=1,column=i)
     scroll1=Scrollbar(canvas[1])

     scroll2=Scrollbar(canvas[3])

     scroll3=Scrollbar(canvas[2])
     positive=Listbox(canvas[1],yscrollcommand = scroll1.set,height=35,width=45,bg='light green')
     negative=Listbox(canvas[3],yscrollcommand = scroll2.set,height=35,width=43,bg='white')
     neutral=Listbox(canvas[2],yscrollcommand = scroll3.set,height=35,width=45,bg='#ffcccb')
     scroll1.pack(side = 'right', fill = 'both')
     scroll2.pack(side = 'right', fill = 'both')
     scroll3.pack(side = 'right', fill = 'both')
     positive.pack(side = 'left', fill = 'both')
     negative.pack( side = 'left', fill = 'both' )
     neutral.pack( side = 'left', fill = 'both' )     
     for i in list_of_apps_most_positive_sentiments:
         positive.insert(END,i)
     for i in list_of_apps_most_average_sentiments:
         neutral.insert(END,i) 
     for i in list_of_apps_most_negative_sentiments:
         negative.insert(END,i)    
     
     if  (len(list_of_apps_most_positive_sentiments)>len(list_of_apps_most_negative_sentiments)) and (len(list_of_apps_most_positive_sentiments)>len(list_of_apps_most_average_sentiments)):
         Label(canvas[0],text='User liked this app',width=25,anchor=CENTER,font=("Helvetica",15,'bold','italic')).pack()
     elif (len(list_of_apps_most_negative_sentiments)>len(list_of_apps_most_average_sentiments)):
         Label(canvas[0],text='User disliked this app',width=25,anchor=CENTER,font=("Helvetica",15,'bold','italic')).pack() 
     else:
         Label(canvas[0],text='User neither liked nor disliked this app',width=25,anchor=CENTER,font=("Helvetica",15,'bold','italic')).pack()         
    
def fourteen():
    global search
    global mcanvas
    global filtered
    global appli
    mcanvas.delete("all")
    val=Label(mcanvas,width=600,height=8,font=("Lucida",30,'bold'),fg='black',bg='#102131')
    mcanvas.create_window(400,250, window=val)
    data=pd.read_csv('C:\\InternshipFinal\\user.csv')
    data=data.replace(np.nan,'Not Available')
    appli=list(OrderedDict.fromkeys(data['App']))
     
     
    filtered=[]
    for i in appli:
         filtered.append(i[0:10])            
#     print(canvas)  
    search=StringVar()       
    Label(val, text='Search apps', anchor='w').grid(row=0, column=0 ,padx=5,pady=5, sticky="w")
    app=Combobox(val , width=40,state="readonly",text=search,values=filtered)
    app.grid(row=0, column=1 ,padx=5,pady=5, sticky="w") 
    app.set("--select--") 
    r=Button(val,text='Review',width=12,command=revv)
    r.grid(row=0, column=3 ,padx=5,pady=5)
    mcanvas.update() 
""" QUESTION 16 CODE"""
def year():
    global root
    global cat
    global can
    root = Tk()
    root.title("Insight of Google App's")
    width_value=root.winfo_screenwidth()
    root.configure(background='white') # configuring the window
    height_value=root.winfo_screenheight()
    root.geometry("%dx%d+400+50"%(700,600))
    mcan=Canvas(root,width=800,height=700,bg='white')
     
    mcan.place(x=0,y=0)

    data=pd.read_csv('C:\\InternshipFinal\\App-data.csv')
    data=data.replace(np.nan,'Not Available')
    data['Installs'] = data['Installs'].map(lambda x: x.rstrip('+'))
    data['Installs'] = data['Installs'].map(lambda x: ''.join(x.split(',')))
    data['Installs'] = pd.to_numeric(data['Installs'])    
    d = pd.DatetimeIndex(data['Last Updated'])
    data['year'] = d.year
    data['month'] = d.month
#    print(data['month'])
#    print(data['year'])
    mon={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    for i in range(len(data)):
        a=int(cat.get())
#        print(a)
#        print(data['year'][i])
        if int(data['year'][i]) == a:
            # print(data['month'][i])
            if data['month'][i] in mon:
                # print(data['month'][i])
                if mon[data['month'][i]]==0:
                    mon[data['month'][i]]=data['Installs'][i]
                    # print(data['Installs'][i])
                   
                else:
                    mon[data['month'][i]]+=data['Installs'][i]                        
    x=list(mon.keys())
    y=list(mon.values())
    figure1 = plt.Figure(figsize=(10,8), dpi=70)
    axesObject = figure1.add_subplot(111)
    axesObject.bar(x,y)    
    axesObject.set_title(f"Maximum Downloads in a month for a {cat.get()}")
    can= FigureCanvasTkAgg(figure1,mcan)    
    can.get_tk_widget().pack( fill=BOTH, expand=True)

    toolbar = NavigationToolbar2Tk(can,mcan)
    toolbar.update()    
def funct16():          
    global cat
    global mcanvas
    mcanvas.delete("all")
    val=Label(mcanvas,width=600,height=8,font=("Lucida",30,'bold'),fg='black',bg='#102131')
    mcanvas.create_window(300,250, window=val)
    data=pd.read_csv('C:\\InternshipFinal\\App-data.csv')
    data=data.replace(np.nan,'Not Available')
    d = pd.DatetimeIndex(data['Last Updated'])
    data['year'] = d.year
    data['month'] = d.month
    cat=StringVar() 
    choices = list(data['year'].unique())   
    Label(val, text='Select Year', anchor='w').grid(row=0, column=0 ,padx=5,pady=5, sticky="w")
    app=ttk.Combobox(val, width=40,state="readonly",text=cat,values=choices)
    app.grid(row=0, column=1 ,padx=5,pady=5, sticky="w") 
    app.set("--select--")          
    r=Button(val,text='Search',width=12,command=year)
    r.grid(row=0, column=3 ,padx=5,pady=5)
    mcanvas.update()  

"""TO UPDATE CATEGORIES INSTALL Q8 part 2"""     
def Update_cat():
    
    
    
    
    df = pd.DataFrame()
    df = pd.read_csv("C:\\InternshipFinal\\App-data.csv")
    # dict1={}
    # dict1=pd.value_counts(df['Category'])
    
    
    list1={}
    print(list1)
    
    
    df['Installs']=df['Installs'].str.replace('+','')
    df['Installs']=df['Installs'].str.replace(',','')
    df['Installs']=df['Installs'].astype(int)
    # print(sum(df['Installs']))
    category ={}
    sum1=[]
    for i in df['Category']:
        category.update({i:0}) 
        
        
    for i in category.keys(): 
            t2 = (df[i==(df.Category)].Installs).tolist()  
            sum1.append(sum(t2))
            category.update({i:sum(t2)})
#    print(category)
    list1=list(category.values())
    print(list1)
    list2=list(category.keys())
    print(list2)
    try:
        connection = pymysql.connect(host="localhost", user="root", password="", database="googleplaystore") # database connection
        cursor = connection.cursor()
        cursor.execute("TRUNCATE TABLE catupdate")
        for i in range(len(list2)):
            insert_query = "INSERT INTO catupdate (Categories,Downloads) VALUES('"+ list2[i] + "', '"+ str(list1[i]) + "' );" # queries for inserting values
            cursor.execute(insert_query) # executing the queries
        connection.commit() # commiting the connection then closing it.
        connection.close() 
        tk.messagebox.showinfo('Updated',"The Number Of Installs Have Been Updated")
    except pymysql.Error:
        tk.messagebox.showinfo('Error',"Database Error")

"""THE MAIN SCREEN GUI  """
def category():
    global mcanvas

    mcanvas.delete("all")
    
#    q=mcanvas.create_rectangle(40,40,500,80,fill='black')
    q1 = Button(mcanvas,text = "The percentage download in each category in the playstore.",width=70,height=2,font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=fn.functq1)
#    q3.bind("<Button-1>", function_q3)
    mcanvas.create_window(375, 120, window=q1) 
    
    q3 = Button(mcanvas,text = """Which category of apps have managed to get the most,
                least and an average of 2,50,000 downloads atleast.""",width=70,height=2,font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=fn.functq3)
#    q4.bind("<Button-1>", function_q4)
#    q4.place(x=40,y=120)
    mcanvas.create_window(375,200, window=q3) 
       
    
    q0 = Button(mcanvas,text = "The percentage of Apps in  each category in the playstore .",width=70,height=2,font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=fn.functq0)
#    q5.bind("<Button-1>", function_q5)          
    mcanvas.create_window(375,280, window=q0)
    
    q6 = Button(mcanvas,text = """For the years 2016,2017,2018 what are the category of apps that have got the 
                most and the least downloads""",width=70,height=2,font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=fn.functq6)
    #    q5.bind("<Button-1>", function_q5)  
    mcanvas.create_window(375,380, window=q6) 
    
    b=Button(mcanvas, text="Next",font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=nextc1)
    mcanvas.create_window(700,475, window=b) 
    mcanvas.update()
def nextc1(): 
    global mcanvas

    mcanvas.delete("all")
    
#    q=mcanvas.create_rectangle(40,40,500,80,fill='black')
    q8 = Button(mcanvas,text = """Amongst Sports, Entertainment,social,News,Events,Travel and Game,
                which is the category of app that is most likely to be downloaded""",width=70,height=2,font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=fn.functq8)
#    q3.bind("<Button-1>", function_q3)
    mcanvas.create_window(375, 120, window=q8) 
    b=Button(mcanvas, text="Previous",font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=category)
    mcanvas.create_window(700,475, window=b) 
    
    mcanvas.update()

def install():
    global mcanvas
    mcanvas.delete("all")
    #    q=mcanvas.create_rectangle(40,40,500,80,fill='black')
    q2 = Button(mcanvas,text = """Number of apps that have managed to get the following number of downloads
a) Between 10,000 and 50,000
b) Between 50,000 and 150000
c) Between 150000 and 500000
d) Between 500000 and 5000000
e) More than 5000000""",width=90,height=6,font=("Lucida",10,'bold'),fg='#ffffff',bg='black',command=fn.functq2)
    #    q3.bind("<Button-1>", function_q3)
#    q3.place(x=40,y=120)       
    mcanvas.create_window(375,120, window=q2) 

    q5 = Button(mcanvas,text = """What is the number of installs for the following app sizes.
a) Size between 10 and 20 mb
b) Size between 20 and 30 mb
c) More than 30 mb""",width=90,height=6,font=("Lucida",10,'bold'),fg='#ffffff',bg='black',command=fn.functq5)
    #    q4.bind("<Button-1>", function_q4)
#    q4.place(x=40,y=200)
    mcanvas.create_window(375,240, window=q5) 
    
    
    q10_1 = Button(mcanvas,text = "Month with maximum downloads for each of the category.",width=72,height=2,font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=funct10)
#    q3.bind("<Button-1>", function_q3)
    mcanvas.create_window(375, 330, window=q10_1) 
    b=Button(mcanvas, text="Next",font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=nexti1)
    mcanvas.create_window(700,475, window=b) 
    

    mcanvas.update()
def nexti1():
    global mcanvas

    mcanvas.delete("all")
    
#    q=mcanvas.create_rectangle(40,40,500,80,fill='black')
    q10_2 = Button(mcanvas,text = "Ratio of downloads for the App that qualifies as teen vs mature17+",width=70,height=2,font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=fn.functq10_2)
#    q3.bind("<Button-1>", function_q3)
    mcanvas.create_window(375, 120, window=q10_2) 
    
    q11 = Button(mcanvas,text = "Which quarter of which year has generated the highest number of install for each app used",width=72,height=2,font=("Lucida",12,'bold'),fg='#ffffff',bg='black',command=fn.question11)
#    q3.bind("<Button-1>", function_q3)
    mcanvas.create_window(375, 200, window=q11)
    b=Button(mcanvas, text="Previous",font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=install)
    mcanvas.create_window(700,475, window=b) 
    
    
    mcanvas.update()
def rrev():
    global mcanvas

    mcanvas.delete("all")
    q12 = Button(mcanvas,text = """Which app has manage to generate the most positive, negative 
                 sentiments and generated approximately the same ratio""",width=70,height=2,font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=twelve)
#    q3.bind("<Button-1>", function_q3)
    mcanvas.create_window(375, 120, window=q12)
    
    q13 = Button(mcanvas,text = """the relation between the sentiment-polarity and sentiment-subjective,
                 the sentiment subjectivity for a sentiment polarity of 0.4""",width=70,height=2,font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=fn.function_q13)
#    q3.bind("<Button-1>", function_q3)
    mcanvas.create_window(375, 200, window=q13)
#    q=mcanvas.create_rectangle(40,40,500,80,fill='black')
    q14_15 = Button(mcanvas,text = """Positive, negative and neutral reviews of an app,
                 does the user like these app""",width=70,height=2,font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=fourteen)
#    q3.bind("<Button-1>", function_q3)
    mcanvas.create_window(375, 280, window=q14_15) 
     
    mcanvas.update()
def app():
    global mcanvas

    mcanvas.delete("all")
    
#    q=mcanvas.create_rectangle(40,40,500,80,fill='black')
    q7 = Button(mcanvas,text = """All those apps,whose android version is not an issue and can 
                work with varying devices.""",width=70,height=2,font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=fn.functq7)
#    q3.bind("<Button-1>", function_q3)
    mcanvas.create_window(375, 100, window=q7) 
    
    q7_2 = Button(mcanvas,text = "What is the percentage increase or decrease in the downloads.",width=70,height=2,font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=fn.functq7_2)
#    q3.bind("<Button-1>", function_q3)
    mcanvas.create_window(375, 180, window=q7_2) 
    
    q4 = Button(mcanvas,text = "The apps that managed to get the highest maximum rating from the user.",width=70,height=2,font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=fn.functq4)
#    q5.bind("<Button-1>", function_q5)          
    mcanvas.create_window(375,260, window=q4) 
    q9 = Button(mcanvas,text = """App managed to get get over 1,00,000 downloads, 
                and managed to get an average rating of 4.1 and above.""",width=70,height=2,font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=fn.functq9)
#    q5.bind("<Button-1>", function_q5)          
    mcanvas.create_window(375,340, window=q9) 
    q16 = Button(mcanvas,text = """Which month of the year, is the best indicator to the average 
                 downloads that an app will generate over the entire year .""",width=70,height=2,font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=funct16)
#    q5.bind("<Button-1>", function_q5)          
    mcanvas.create_window(375,420, window=q16) 
    b=Button(mcanvas, text="Next",font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=nexta1)
    mcanvas.create_window(700,475, window=b) 
    
    mcanvas.update()   
def nexta1():
    global mcanvas

    mcanvas.delete("all")
    
#    q=mcanvas.create_rectangle(40,40,500,80,fill='black')
    q17 = Button(mcanvas,text = "Does the size of the app influence the number of install that it get?",width=70,height=2,font=("Lucida",12,'bold'),fg='#ffffff',bg='black',command=fn.functq17)
#    q3.bind("<Button-1>", function_q3)
    mcanvas.create_window(375, 200, window=q17)
    b=Button(mcanvas, text="Previous",font=("Lucida",13,'bold'),fg='#ffffff',bg='black',command=app)
    mcanvas.create_window(700,475, window=b) 
    
    
    mcanvas.update()


#===============================================main screen======================================================        

root=Tk()
root.title("Insight of Google App's")
width_value=root.winfo_screenwidth()
height_value=root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(width_value, height_value))
root.configure(background='#102131')
root.iconbitmap(r"C:\\InternshipFinal\\google.ico")
#=================================top canvas===================================================================
photocanvas=Canvas(root,width =1355,height=177,bg='#102131')
photocanvas.place(x=0,y=0) 
myimg=PhotoImage(file="C:\\InternshipFinal\\predictive_analytics_banner.png")
photocanvas.create_image(0,0,anchor=NW,image=myimg)
photocanvas.image =myimg

#================================================main canvas ==============================
mcanvas=Canvas(width = 760,height=500,bg='#102131',bd='0')
mcanvas.place(x=300,y=180)
head=Label(mcanvas,text="Google \nPlayStore \n App launch \nStudy",width=30,font=("Lucida",50,'bold'),fg='#ffffff',bg='#102131')
mcanvas.create_window(400, 200, window=head)
#=====================================================options==================================================
lbl_over = Button(root,text = "Add Data",width=25,height='2',font=("Lucida",13,'italic'),fg='#ffffff',bg='black',command=login)
#lbl_over.bind("<Button-1>")
lbl_over.place(x=8,y=220)

lbl_category = Button(root,text = "Category",width=25,height='2',font=("Lucida",13,'italic'),fg='#ffffff',bg='black',command=category)
#lbl_category.bind("<Button-1>")
lbl_category.place(x=8,y=220+60)

lbl_Installs = Button(root,text = "Installs",width=25,height='2',font=("Lucida",13,'italic'),fg='#ffffff',bg='black',command=install)
#lbl_Installs.bind("<Button-1>")
lbl_Installs.place(x=8,y=220+60+60)
    
lbl_searchapp = Button(root,text = "Search App",width=25,height='2',font=("Lucida",13,'italic'),fg='#ffffff',bg='black',command=fn.searchapp)
#lbl_searchapp.bind("<Button-1>")
lbl_searchapp.place(x=8,y=220+60+120)
                              
lbl_machine = Button(root,text = "App Info",width=25,height='2',font=("Lucida",13,'italic'),fg='#ffffff',bg='black',command=app)
lbl_machine.bind("<Button-1>")
lbl_machine.place(x=8,y=220+60+120+60)

lbl_review = Button(root,text = "Reviews",width=25,height='2',font=("Lucida",13,'italic'),fg='#ffffff',bg='black',command=rrev)
#lbl_review.bind("<Button-1>")
lbl_review.place(x=8,y=220+60+120+120)
                        
lbl_lastupdate = Button(root,text = "Add Reviews",width=25,height='2',font=("Lucida",13,'italic'),fg='#ffffff',bg='black',command=add_rev)
lbl_lastupdate.bind("<Button-1>")
lbl_lastupdate.place(x=8,y=220+60+120+180)
#======================================right canvas============================    
rcanvas=Canvas(width = 295,height=500,bg='#102131')
rcanvas.place(x=1060,y=180) 
Button(rcanvas,text = "Update The Installs\n Per Category",width=25,height='2',font=("Lucida",13,'italic'),fg='#ffffff',bg='black',command=Update_cat).place(x=35,y=220)
Button(rcanvas,text = "Refresh main screen",width=25,height='2',font=("Lucida",13,'italic'),fg='#ffffff',bg='black',command=cancel).place(x=30,y=120)
#======================================bottom canvas============================    
bottom=Canvas(width = 1190,height=500,bg='#102131')
bottom.place(x=0,y=682)
ball=bottom.create_oval(4,4,30,30,fill='#ffffff')

#==================================================group name==============================================    
name=Label(root,text="Ctrl+Alt+Del",width=15,height=1,font=("Helvetica",15,'bold','italic'),fg='#ffffff',bg='#102131')
name.place(x=1150,y=630)

root.mainloop()
