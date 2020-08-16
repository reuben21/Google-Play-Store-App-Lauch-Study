# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 14:34:15 2020

@author: reube
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:39:12 2019

@author: GANDHI
"""

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import pandas as pd
import operator
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.cm as cm
from collections import OrderedDict
def adjustWindow(window):
    w = 600  # width for the window size
    h = 600  # height for the window size
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    window.resizable(False, False)    # disabling the resize option for the window
    window.configure(background='white')    # making the background white of the window
def _quit():
        global screen
        screen.quit()     # stops mainloop
        screen.destroy()
def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)        







def functq0():
    global screen
    screen = Tk()
    screen.iconbitmap(r"C:\\InternshipFinal\\google.ico")
#    big_frame = Frame(screen,bg='white',width='1010',height=450,bd=4)
#    big_frame.place(x=10,y=60)
    screen.title("percentage of category")  # mentioning title of the window
    w = 1000 # width for the window size
    h = 700  # height for the window size
    ws = screen.winfo_screenwidth()  # width of the screen
    hs = screen.winfo_screenheight()  # height of the screen
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    screen.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    screen.resizable(False, False)    # disabling the resize option for the window
    screen.configure(background='white')   # configuring the window
    df = pd.read_csv("C:\\InternshipFinal\\App-data.csv")
    df=df.replace(np.NaN,-1)
    catcount={}
    for index in range(len(df)):
        if df['Category'][index]==-1:
            continue
        
        if df['Category'][index] in catcount:
            catcount[df['Category'][index]]+=1
        else:
            catcount[df['Category'][index]]=1

    figure1 = plt.Figure(figsize=(14,9), dpi=70)
    
    # color = cm.rainbow(np.linspace(0, 1, len(x_label)))
    #fig1, ax1 = plt.subplots()
    axesObject = figure1.add_subplot(111)
    labels = ['{0} = {1}  '.format(i,j) for i,j in zip(catcount.keys(),catcount.values())]
    
    theme = plt.get_cmap('hsv')
    axesObject.set_prop_cycle("color", [theme(1. * i / len(catcount))for i in range(len(catcount))])
    axesObject.pie(list(catcount.values()),autopct='%1.2f ',startangle=90)    
    axesObject.set_title("Percentage Download in Each Category")
    #ax3.xlim(0,3.0)
    figure1.legend(labels,bbox_to_anchor=(0.3,1))
 
    canvas = FigureCanvasTkAgg(figure1, master=screen)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack( fill=BOTH, expand=True)    
    toolbar = NavigationToolbar2Tk(canvas, screen)
    toolbar.update()

    canvas.mpl_connect("key_press_event", on_key_press)
      # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    button = Button(master=screen, text="Quit", command=_quit)
    button.pack(side=BOTTOM)
    screen.mainloop()       
def functq1():
    
    global screen
    screen = Tk()
    
    big_frame = Frame(screen,width='1010',height=750)
    big_frame.place(x=10,y=60)
    screen.iconbitmap(r"C:\\InternshipFinal\\google.ico")
    
    w=1000
    h=900
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    screen.geometry("%dx%d+%d+%d"%(w,h,x,y))
    screen.configure(background='white')
    
    
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
            category.update({i:float(((sum(t2))/(sum(df['Installs'])))*100)})
    print(category)
    list1=list(category.values())
    # print(list1)
    
    figure1 = plt.Figure(figsize=(14,9), dpi=70)
    
    # color = cm.rainbow(np.linspace(0, 1, len(x_label)))
    #fig1, ax1 = plt.subplots()
    axesObject = figure1.add_subplot(111)
    labels = ['{0} = {1:1.2f} % '.format(i,j) for i,j in zip(category.keys(),category.values())]
    
    theme = plt.get_cmap('hsv')
    axesObject.set_prop_cycle("color", [theme(1. * i / len(list1))for i in range(len(list1))])
    axesObject.pie(list1,autopct='%1.2f ',startangle=90)    
    axesObject.set_title("Percentage of Downloads in Each Category")
    #ax3.xlim(0,3.0)
    
    
    canvas = FigureCanvasTkAgg(figure1,big_frame)
    canvas.draw()
    canvas.get_tk_widget().pack( fill=BOTH, expand=True)
    toolbar = NavigationToolbar2Tk(canvas,big_frame)
    toolbar.update()
    canvas._tkcanvas.pack( fill=BOTH, expand=True)
    figure1.legend(labels,bbox_to_anchor=(0.3,1))
    string="""From The Above Pie Chart,
     We get the percentage of Downloads in Each Category """
    Label(screen,text=string,font=("Calibri",13,'italic')).place(x=500,y=590)
    button = Button(master=screen, text="Quit", command=_quit)
    button.pack(side=BOTTOM)         
    # figureObject, axesObject = plt.subplots(figsize=(10,10))
    
      # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    screen.mainloop()    
def functq2():
     # initializing the tkinter window
    global screen
    screen = Tk()
    screen.iconbitmap(r"C:\\InternshipFinal\\google.ico")
    screen.title("Apps vs Downloads")  # mentioning title of the window
    adjustWindow(screen)  # configuring the window
    df = pd.read_csv("C:\\InternshipFinal\\App-data.csv")
    df=df.replace(np.NaN,-1)
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    df['Installs'] = pd.to_numeric(df['Installs'])   
    list2=["More than 5M","500k-5M","150k-500k","50k-150k","10k-50k"]
    dict1,dict2,dict3,dict4,dict5={},{},{},{},{}
#    dict6={}
    dict1=(pd.value_counts(df['Installs']>=5000000))
    a1=len(df)-dict1.values[0]
    dict2=(pd.value_counts((df["Installs"]>=500000) & (df["Installs"]<5000000)))
    a2=len(df)-dict2.values[0]
    dict3=(pd.value_counts((df["Installs"]>=150000) & (df["Installs"]<500000)))
    a3=len(df)-dict3.values[0]
    dict4=(pd.value_counts((df["Installs"]>=50000) & (df["Installs"]<150000)))
    a4=len(df)-dict4.values[0]
    dict5=(pd.value_counts((df["Installs"]>=10000) & (df["Installs"]<50000)))
    a5=len(df)-dict5.values[0]
#    dict6=pd.value_counts(df["Installs"]<10000)
#    a6=len(df)-dict6.values[0]
    list1=[a1,a2,a3,a4,a5]
    color = cm.rainbow(np.linspace(0, 2, 10))
    fig=Figure(figsize=(5,4),dpi=100)
    chart=fig.add_subplot(111)
    chart.bar(list2,list1,color=color)
    chart.set_ylabel("Frequency")
    chart.set_xlabel("Installs")
    chart.grid()
    fig.suptitle("Count-plot for Installs")
    canvas = FigureCanvasTkAgg(fig, master=screen)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    toolbar = NavigationToolbar2Tk(canvas, screen)
    toolbar.update()

    canvas.mpl_connect("key_press_event", on_key_press)
      # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    
    button = Button(master=screen, text="Quit", command=_quit)
    button.pack(side=BOTTOM)
    screen.mainloop()
#def on_key_press(event):
#    print("you pressed {}".format(event.key))
#    key_press_handler(event, canvas, toolbar)
#    
#canvas.mpl_connect("key_press_event", on_key_press)
def functq3():
    global screen
    screen = Tk()
    screen.iconbitmap(r"C:\\InternshipFinal\\google.ico")
    screen.title("Apps vs Downloads")
    w = 600  # width for the window size
    h = 700  # height for the window size
    ws = screen.winfo_screenwidth()  # width of the screen
    hs = screen.winfo_screenheight()  # height of the screen
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    screen.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    screen.resizable(False, False)    # disabling the resize option for the window
    screen.configure(background='white')  # configuring the window
    df = pd.read_csv("C:\\InternshipFinal\\App-data.csv")
    df=df.replace(np.NaN,0)
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    df['Installs'] = pd.to_numeric(df['Installs'])
    category=df['Category'].unique()
    list1=df['Installs']
    ans=[]
    count = []
    
    for i in category:
        total=0
        c=0
        for j in range(len(df['Category'])):
                if df['Category'][j]==i:
                    total=total+list1[j]
                    c+=1
     #   print(total)            
        ans.append(total)
        count.append(c)
    #print(ans)    
#    print(count)     
    cat,avg = [],[]    
    for index in range(len(ans)):
        cat.append(category[index])
        avg.append(round(ans[index]/count[index]))
  # print(avg)    
  #  print(cat) 
    lowest = []
    for index in range(len(avg)):
        if avg[index]<250000:
            lowest.append(category[index])
            
    print(lowest)    
    label = category
#    print(label)
    val = avg
    color = cm.rainbow(np.linspace(0, 1, len(label)))
    fig=Figure(figsize=(8,5),dpi=60)
    chart=fig.add_subplot(111)
    chart.barh(label,val,color=color)
    chart.set_ylabel("Category")
    chart.set_xlabel("Average Installs")
    chart.grid()
    fig.suptitle("Category with Their Average Download")

    canvas = FigureCanvasTkAgg(fig, master=screen)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    toolbar = NavigationToolbar2Tk(canvas, screen)
    toolbar.update()

    canvas.mpl_connect("key_press_event", on_key_press)
      # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    string=f"""The categories below average of 250000 {lowest[0]} and {lowest[1]} """
    Label(screen,text=string,font=("Calibri",13,'italic')).place(x=100,y=590)
    button = Button(master=screen, text="Quit", command=_quit)
    button.pack(side=BOTTOM)
    screen.mainloop()


def functq4():    
    global screen
    screen = Tk()
    screen.iconbitmap(r"C:\\InternshipFinal\\google.ico")
    screen.title("Rating Vs Category ")  # mentioning title of the window
    adjustWindow(screen)  # configuring the window
    category ={}
    df = pd.read_csv("C:\\InternshipFinal\\App-data.csv")
    df=df.replace(np.NaN,0)
    catreview = {}
    for index in range(len(df)):
        if df['Category'][index] in catreview:
            catreview[df['Category'][index]][0]+=df['Rating'][index]
            catreview[df['Category'][index]][1]+=1
#            rating+=df['Rating'][index]
        else:
            catreview[df['Category'][index]]=[df['Rating'][index],1]
#            rating+=df['Rating'][index]   
    total=0
    count=0
    for i in df['Rating']:
            total+=i
            count+=1
    avg= total/count
    y=[]
    x=[]
    for i in catreview:
        if catreview[i][0]/catreview[i][1]>=avg:
            avgcat = (catreview[i][0]/catreview[i][1])    
            x.append(i)
            y.append(float(avgcat))
#    print(y)
#    print(x)    
    color = cm.rainbow(np.linspace(0, 2, 15))
    figure3 = plt.Figure(figsize=(5,4), dpi=80)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(y,x,color=color)
    scatter3 = FigureCanvasTkAgg(figure3, screen) 
    scatter3.get_tk_widget().place(x=10,y=0)
    ax3.grid()
    ax3.set_xlabel("RATING")
    ax3.set_ylabel("CATEGORY")
    ax3.set_title('CATEGORIES WITH HIGHEST MAXIMUM AVERAGE RATING') 
    canvas = FigureCanvasTkAgg(figure3, master=screen)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, screen)
    toolbar.update()
#    canvas.mpl_connect("key_press_event", on_key_press)
      # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    button = Button(master=screen, text="Quit", command=_quit)
    button.pack(side=BOTTOM)
    screen.mainloop()
    
def functq5():


    global screen
    screen = Tk()
    screen.iconbitmap(r"C:\\InternshipFinal\\google.ico")
    w = 600  # width for the window size
    h = 600  # height for the window size
    ws = screen.winfo_screenwidth()  # width of the screen
    hs = screen.winfo_screenheight()  # height of the screen
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    screen.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    screen.resizable(False, False)    # disabling the resize option for the window
    screen.configure(background='white')    # configuring the window
    df= pd.read_csv("C:\\InternshipFinal\\App-data.csv")
    list2=['More than 30 mb','20-30 mb','10-20 mb']
    
    df['Size'] = df['Size'].map(lambda x: x.rstrip('M'))
    df['Size'] = df['Size'].map(lambda x: str(round((float(x.rstrip('k'))/1024), 1)) if x[-1]=='k' else x)
    df['Size'] = df['Size'].map(lambda x: np.nan if x.startswith('Varies') else x)
    
    df['Size']=df['Size'].replace(np.NaN,-999)
    df['Size']=df['Size'].astype(float)
    
    #print(df['Category'].unique())

    #print(df['Size'])
    df['Installs']=df['Installs'].str.replace('+','')
    df['Installs']=df['Installs'].str.replace(',','')
    df['Installs']=df['Installs'].astype(int)
    
    a,b,c=[],[],[]
    for i in range(len(df)):
        if df["Size"][i]>=30:
             a.append(df['Installs'][i])
        elif 20<=df["Size"][i]<30:
             b.append(df['Installs'][i])
        elif 10<=df["Size"][i]<20:
             c.append(df['Installs'][i])
    
    a2=(sum(b))
    a3=(sum(c))
    a1=(sum(a))         
            
    list1=[a1,a2,a3]
    print(list1)
       
    color = cm.rainbow(np.linspace(0, 2, 10))
    fig=Figure(figsize=(5,4),dpi=100)
    chart=fig.add_subplot(111)
    chart.bar(list2,list1,color=color)
    chart.set_ylabel("No of Installs")
    chart.set_xlabel("Sizes")
    chart.grid()
    fig.suptitle("No. of Installs Vs Size")
 
    canvas = FigureCanvasTkAgg(fig, master=screen)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, screen)
    toolbar.update()

    canvas.mpl_connect("key_press_event", on_key_press)
      # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    button = Button(master=screen, text="Quit", command=_quit)
    button.pack(side=BOTTOM)
    screen.mainloop()


def functq6():
    global screen  
    screen=Tk()
    screen.iconbitmap(r"C:\\InternshipFinal\\google.ico")
    w=700
    h=600
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    screen.geometry("%dx%d+%d+%d"%(w,h,x,y))
    screen.configure(background='white')
    df = pd.read_csv("C:\\InternshipFinal\\App-data.csv")
    
    # Data cleaning for "Installs" column
    #print(df['Installs'].head(5))
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    #print(df['Installs'].head(5))
    
    
    df['Installs'] = pd.to_numeric(df['Installs'])
    
    d = pd.DatetimeIndex(df['Last Updated'])
    
    df['year'] = d.year
    df['month'] = d.month    
    #print((df['year'][5]))    
    #6) For the years 2016,2017,2018 what are the category of apps that have got the most and the least downloads. What is the percentage increase or decrease that the    
    dict_2016 = {}
    dict_2017 = {}
    dict_2018 = {}
    
    Category = []
    for cat in df['Category'].unique():
        Category.append(cat)
        dict_2016[cat]=0
        dict_2017[cat]=0
        dict_2018[cat]=0
    #print(Category)        
    for index in range(len(df)):
        if df['year'][index]==2016:
            dict_2016[df['Category'][index]] += df['Installs'][index]
        if df['year'][index]==2017:
            dict_2017[df['Category'][index]] += df['Installs'][index]
        if df['year'][index]==2018:
            dict_2018[df['Category'][index]] += df['Installs'][index]
    
    #print(len(dict_2016))
    #print(len(dict_2017))
    #print(len(dict_2018))    
    #print(dict_2016)    
    #print(dict_2017)    
    #print(dict_2018)        
    max_2016_install = ["",0]
    max_2017_install = ["",0]
    max_2018_install = ["",0]
    
    
    min_2016_install = ["",99999999999]
    min_2017_install = ["",99999999999]
    min_2018_install = ["",99999999999]
    
    for cat in dict_2016:
        if max_2016_install[1] < dict_2016[cat]:
            max_2016_install[1] = dict_2016[cat]
            max_2016_install[0] = cat
        if max_2017_install[1] < dict_2017[cat]:
            max_2017_install[1] = dict_2017[cat]
            max_2017_install[0] = cat
        if max_2018_install[1] < dict_2018[cat]:
            max_2018_install[1] = dict_2018[cat]
            max_2018_install[0] = cat
            
        if min_2016_install[1] > dict_2016[cat]:
            min_2016_install[1] = dict_2016[cat]
            min_2016_install[0] = cat
        if min_2017_install[1] > dict_2017[cat]:
            min_2017_install[1] = dict_2017[cat]
            min_2017_install[0] = cat
        if min_2018_install[1] > dict_2018[cat]:
            min_2018_install[1] = dict_2018[cat]
            min_2018_install[0] = cat
    #print(max_2016_install)
    #print(max_2017_install)
    #print(max_2018_install)    
    #print(min_2016_install)
    #print(min_2017_install)
    #print(min_2018_install)
    max_install = [max_2016_install[1],max_2017_install[1],max_2018_install[1]]
    min_install = [min_2016_install[1],min_2017_install[1],min_2018_install[1]]
    Years = ['2016','2017','2018']
    
    pos = np.arange(len(Years))
    bar_width = 0.3
    
    figure2 = plt.Figure(figsize=(8,4), dpi=85)

    chart = figure2.add_subplot(111)
    
    Max_bar = chart.bar(Years,max_install,bar_width,color='blue',edgecolor='blue')
    Min_bar = chart.bar(pos+bar_width,min_install,bar_width,color='red',edgecolor='red')
    chart.grid()
    chart.set_ylabel("Download")
    chart.set_xlabel('Years')
    figure2.suptitle('Max and Min download across 2016-17-18 years for a category',fontsize=18)
    plt.legend(['max','min'],loc=10)
    
    max_month = [max_2016_install[0],max_2017_install[0],max_2018_install[0]]
    min_month = [min_2016_install[0],min_2017_install[0],min_2018_install[0]]
    
    for idx,rect in enumerate(Max_bar):
                height = rect.get_height()
                chart.text(rect.get_x() + rect.get_width()/2., 1.05*height,max_month[idx],ha='center', va='bottom', rotation=0) 
          
    for idx,rect in enumerate(Min_bar):
                height = rect.get_height()
                chart.text(rect.get_x() + rect.get_width()/2., 1.05*height,min_month[idx],ha='center', va='bottom', rotation=0) 
    canvas = FigureCanvasTkAgg(figure2, master=screen)
    canvas.get_tk_widget().pack()            
    toolbar = NavigationToolbar2Tk(canvas, screen)
    toolbar.update()

    canvas.mpl_connect("key_press_event", on_key_press)
      # this is necessary on Windows to prevent
      # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    Label(screen,text="The Downloads in the Last Three Years",font=("Helvetica",11,'bold') ,borderwidth=2).place(x=200,y=500)
    button = Button(master=screen, text="Quit", command=_quit)
    button.pack(side=BOTTOM)
    
   
    
    screen.mainloop()    
    
    
    
def functq7():
     global screen  
     screen=Tk()
     screen.iconbitmap(r"C:\\InternshipFinal\\google.ico")
     w=720
     h=600
     ws=screen.winfo_screenwidth()
     hs=screen.winfo_screenheight()
     x=(ws/2)-(w/2)
     y=(hs/2)-(h/2)
     screen.geometry("%dx%d+%d+%d"%(w,h,x,y))
     screen.configure(background='white')
     df= pd.read_csv("C:\\InternshipFinal\\App-data.csv")
     df=df.replace(np.NaN,0)
     df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
     df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
     df['Installs'] = pd.to_numeric(df['Installs'])
     
     varwith=[]
     novar=[]
     varcategory={}
     nocat={}
     for i in range(len(df['App'])):
         if df['Android Ver'][i]=='Varies with device':
             varwith.append(df['Installs'][i])
       
         else: 
             novar.append(df['Installs'][i])
       
            
     print(varwith)    
     print(novar) 
     print(varcategory)
     print(nocat)

    #     print(sumvarcategory)
    #     print(sumnocat)
     x=(len(varwith),len(novar))
    #     print(x)
     androidver = ['Varying', 'Not varying']          
     figure1 = plt.Figure(figsize=(10,7), dpi=70)

     color = cm.rainbow(np.linspace(0, 1, len(x)))
    #fig1, ax1 = plt.subplots()
     axesObject = figure1.add_subplot(111)
    #     labels = ['{0} '.format(i,j) for i,j in zip(catcount.keys(),catcount.values())]

    #     axesObject.set_prop_cycle("color", [theme(1. * i / len(catcount))for i in range(len(catcount))])
     axesObject.pie(x,labels=androidver,autopct='%1.2f',startangle=90,colors=color,shadow=True,explode=[0.1,0])    
     axesObject.set_title("Frequency of Varying Apps in Android version vs Apps in Non-varying Android Version in dataset")
    #ax3.xlim(0,3.0)
    #     figure1.legend(labels,bbox_to_anchor=(0.3,1))
     canvas = FigureCanvasTkAgg(figure1, master=screen)  # A tk.DrawingArea.
     canvas.get_tk_widget().pack( fill=BOTH, expand=True)

     canvas.draw()

     toolbar = NavigationToolbar2Tk(canvas, screen)
     toolbar.update()

     canvas.mpl_connect("key_press_event", on_key_press)
      # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate
     
     button = Button(master=screen, text="Quit", command=_quit)
     button.pack(side=BOTTOM)
     screen.mainloop()
     
def functq7_2():
    global screen
  
    screen = tk.Tk()
    screen.iconbitmap(r"C:\\InternshipFinal\\google.ico")

    big_frame = tk.Frame(screen,bg='white',width='700',height=450,bd=4,relief=RIDGE)
    big_frame.place(x=10,y=60)

    w=720
    h=550
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    screen.geometry("%dx%d+%d+%d"%(w,h,x,y))

    screen.configure(background='white')

    tk.Label(screen,text="",bg='white').pack()
   
    df = pd.read_csv("C:\\InternshipFinal\\App-data.csv")

    #print(df.head(5))

    #df.drop(9148,axis=0, inplace=True)
    #df.drop(10472,axis=0,inplace=True)

    # Data cleaning for "Installs" column
    #print(df['Installs'].head(5))
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    #print(df['Installs'].head(5))


    df['Installs'] = pd.to_numeric(df['Installs'])

    d = pd.DatetimeIndex(df['Last Updated'])
    df['year'] = d.year
    df['month'] = d.month

    #print((df['year'][5]))

    #6) For the years 2016,2017,2018 what are the category of apps that have got the most and the least downloads. What is the percentage increase or decrease that the

    dict_years = {}

    for year in df['year'].unique():
        dict_years[year]=0

    for index in range(len(df)):
        dict_years[df['year'][index]] += df['Installs'][index]
        

    Years = []
    list_install  = []


    #    for year in dict_years:
    #        if year==2016 or year==2017 or year==2018:
    #            Years.append(str(year))
    #            list_install.append(dict_years[year])
    for year in dict_years:
         Years.append((year))
         list_install.append(dict_years[year])

    # print(Years)

    # print(list_install)
    new_dict={}
    for i in range(0,9):
        new_dict.update({Years[i]:list_install[i]})
    new_dict1=dict(sorted(new_dict.items(), key=operator.itemgetter(0),reverse=True))
    keys=list(new_dict1.keys())
    values=list(new_dict1.values())
    print(keys)
    print(values)
    # for i in 
    #    print(dict_years)    
        
    x = dict_years[2016]
    y = dict_years[2017]
    z=dict_years[2018]

    per2016=1
    per2017=((y-x)/(x+y))*100
    per2018=((z-y)/(y+z))*100
    # print(per2016,per2017,per2018)


    Years.reverse()
    list_install.reverse()

    figure2 = plt.Figure(figsize=(8,4), dpi=85)

    chart = figure2.add_subplot(111)

    chart.plot(keys,values,color='blue')
    #Min_bar = chart.bar(pos+bar_width,min_install,bar_width,color='pink',edgecolor='black')

    chart.set_ylabel("Years")
    chart.set_xlabel('Installs')
    figure2.suptitle('Barchart on Installs on each Year ',fontsize=18)
    chart.grid()
       
    canvas = FigureCanvasTkAgg(figure2, master=big_frame)
    canvas.get_tk_widget().place(x=5,y=10)

    String = """  
             % increase in 2016-17 is {:.1f}% and % increase in 2017-18 is {:.1f}%
             """.format(per2017,per2018)
    tk.Label(big_frame,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=40,y=360)
    toolbar = NavigationToolbar2Tk(canvas, screen)
    toolbar.update()

             
    screen.mainloop()
#x axis in order 2014    
    
    

    
def functq8():    
    global screen
    screen = Tk()
    screen.iconbitmap(r"C:\\InternshipFinal\\google.ico")
    screen.title("Apps to be most likely downloaded in the Upcoming Years")  # mentioning title of the window
    w = 600  # width for the window size
    h = 800  # height for the window size
    ws = screen.winfo_screenwidth()  # width of the screen
    hs = screen.winfo_screenheight()  # height of the screen
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    screen.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    screen.resizable(False, False)      # configuring the window
    df = pd.read_csv("C:\\InternshipFinal\\App-data.csv")
    df=df.replace(np.NaN,0)
    
    cat={'SPORTS':0,'ENTERTAINMENT':0,'SOCIAL':0,'NEWS_AND_MAGAZINES':0,'EVENTS':0,'TRAVEL_AND_LOCAL':0,'GAME':0}
    
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    #print(df['Installs'].head(5))        
    df['Installs'] = pd.to_numeric(df['Installs'])    
    d = pd.DatetimeIndex(df['Last Updated'])
    df['year'] = d.year
    df['month'] = d.month
    
#    dict_2018={}
          
    for i in range(len(df)):                    
        if (df['year'][i]==2018):
            if df['Category'][i] in cat:
                if cat[df['Category'][i]]==0:
                    cat[df['Category'][i]]=df['Installs'][i]
                else:
                    cat[df['Category'][i]]+=df['Installs'][i] 
                    
            
#    print(cat)                
    color = cm.rainbow(np.linspace(0, 2, 15))
    fig=Figure(figsize=(5,4),dpi=100)
    chart=fig.add_subplot(111)
    k=list(cat.keys())
    v=list(cat.values())
    l=v.index(max(v))
    print(k[l])
    chart.barh(k,v,color=color)

    chart.set_ylabel("No of Installs")
    chart.set_xlabel("Categories")
    chart.grid()
    fig.suptitle("Count-plot for Installs")
    
    canvas = FigureCanvasTkAgg(fig, master=screen)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    toolbar = NavigationToolbar2Tk(canvas, screen)
    toolbar.update()

    canvas.mpl_connect("key_press_event", on_key_press)
      # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    String = (f""" The Most Likely App to be downloaded in the 
        upcoming Years is {k[l]}""")
    Label(screen,text=String,font=("Calibri",13,'italic')).place(x=200,y=690)
    button = Button(master=screen, text="Quit", command=_quit)
    button.pack(side=BOTTOM)
    screen.mainloop()
    
def functq9():
    
    global screen
    
    df = pd.read_csv("C:\\InternshipFinal\\App-data.csv")
    screen = tk.Tk()
    screen.iconbitmap(r"C:\\InternshipFinal\\google.ico")
    big_frame = tk.Frame(screen,bg='white',width='600',height='630',bd=4)
    big_frame.place(x=50,y=60)
    w=700
    h=700
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    screen.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    screen.configure(background='white')
    rating = 4.1
    installs = 100000
    
    df = pd.read_csv("C:\\InternshipFinal\\App-data.csv")
    print(df['Rating'])
    temp = []
    for index in range(len(df['Rating'])):
        if df['Rating'][index] >= rating:
            temp.append(1)
        else:
            temp.append(0)
            
    cat_rating= pd.DataFrame(zip(temp,temp),columns=["cat_Ratings","ignore"])
    
#    df = pd.concat([df,cat_rating],axis=1)
#    
#    df.drop("ignore",axis=1,inplace=True)
    

    
    # Data cleaning for "Installs" column
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    
    df['Installs'] = pd.to_numeric(df['Installs'])
    
    rating_sum = 0 
    
    rate=[]
    #1169
    """ """
    counter=0
    for index in range(len(df)):
        try:
            if df['Installs'][index]>=installs:
                    rate.append(1)
                    rating_sum+=df['Rating'][index]
                    counter+=1
                    """ """
            else:
                    rate.append(0)
                
        except:
            #print(index)
            continue
        
    
    #print(len(rate))
    avg_rating = (rating_sum/counter)
    """ """
    #print(df['Installs'].corr(df['Rating']))
    
    """ """
    val = "Yes" if (rating_sum/counter)>=rating else "No"
    rel = "Greater than" if val == "Yes" else "Lesser than"
    
    fig, ax = plt.subplots(figsize=(10, 10))
    
    l1 ='{}>='.format(installs)
    l2 ='<{}'.format(installs)
    
    size=[rate.count(1),rate.count(0)]
    label = [l1,l2]
    title = 'Count of {}'.format(rating)
    
    figure1 = plt.Figure(figsize=(8,8), dpi=70)
    labels1 = ['{0} = {1:1.2f} % '.format(i,j) for i,j in zip(label,size)]
    #color = cm.rainbow(np.linspace(0, 1, 10))
    #fig1, ax1 = plt.subplots()
    ax3 = figure1.add_subplot(111)
    ax3.pie(size, labels=label,colors = ['green','cyan'], autopct='%1.1f%%', startangle=200)
    ax3.set_title(title)
    ax3.legend(labels1,bbox_to_anchor=(1,1))
    #ax3.xlim(0,3.0)
    pie_plot = FigureCanvasTkAgg(figure1, big_frame) 
    pie_plot.get_tk_widget().place(x=-50,y=-70)
    
    
    Label(big_frame,text="--Results--",font=("Calibri",13,'italic')).place(x=220,y=470)
    
    
    String = "Average rating of all the apps who managed to get over {} download is {:.1f}".format(installs,avg_rating)
    
    Label(big_frame,text=String,font=("Calibri",13,'italic')).place(x=0,y=500)
      
    String ="""{}! All those apps who have managed to get over {} downloads , 
            they have to get an average rating of {:.1f} which is {} than {} """.format(val,installs,avg_rating,rel,rating)
    
    Label(big_frame,text=String,font=("Calibri",13,'italic')).place(x=0,y=530)
    
             
    #ax3.legend(loc=0) 
    
    toolbar = NavigationToolbar2Tk(pie_plot, screen)
    toolbar.update()

    pie_plot.mpl_connect("key_press_event", on_key_press)
      # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    button = Button(master=screen, text="Quit", command=_quit)
    button.pack(side=BOTTOM)
   
            
    screen.mainloop()

    
def functq10_2():
    global screen
    screen = Tk()
    screen.iconbitmap(r"C:\\InternshipFinal\\google.ico")
    screen.title("Apps vs Downloads")  # mentioning title of the window
    adjustWindow(screen)  # configuring the window
    df = pd.read_csv("C:\\InternshipFinal\\App-data.csv")
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    
    df['Installs'] = pd.to_numeric(df['Installs'])
    df=df.replace(np.NaN,0)
    ratio={'Teen':0,'Mature 17+':0}
    for i in range(len(df)):
        if df['Content Rating'][i] in ratio:
            if ratio[df['Content Rating'][i]]==0:
                ratio[df['Content Rating'][i]]=df['Installs'][i]
            else:
                ratio[df['Content Rating'][i]]+=df['Installs'][i]
                
    print(ratio)            
    color = cm.rainbow(np.linspace(0, 2, 10))
    fig=Figure(figsize=(5,4),dpi=100)
    chart=fig.add_subplot(111)
    chart.bar(ratio.keys(),ratio.values(),color=color)
    chart.set_ylabel("Ratio")
    chart.set_xlabel("Content Rating")
    chart.grid()
    fig.suptitle("Ratio")
    chart.legend()
    canvas = FigureCanvasTkAgg(fig, master=screen)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    toolbar = NavigationToolbar2Tk(canvas, screen)
    toolbar.update()

    canvas.mpl_connect("key_press_event", on_key_press)
      # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    button = Button(master=screen, text="Quit", command=_quit)
    button.pack(side=BOTTOM)
    screen.mainloop()



def question11():
    
    screen = Tk()
    screen.iconbitmap(r"C:\\InternshipFinal\\google.ico")
    screen.title("Apps vs Downloads")
    w = 1000  # width for the window size
    h = 600  # height for the window size
    ws = screen.winfo_screenwidth()  # width of the screen
    hs = screen.winfo_screenheight()  # height of the screen
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    screen.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    screen.configure(background='white')  # configuring the window
    Years=[2010,2011,2012,2013,2014,2015,2016,2017,2018]
    data = pd.read_csv("C:\\InternshipFinal\\App-data.csv")
    data['Installs'] = data['Installs'].map(lambda x: x.rstrip('+'))
    data['Installs'] = data['Installs'].map(lambda x: ''.join(x.split(',')))
    #print(data['Installs'].head(5))
    data['Installs'] = pd.to_numeric(data['Installs'])
    
    d = pd.DatetimeIndex(data['Last Updated'])
    data['year'] = d.year
    data['month'] = d.month
    list_year=[]
   
    for j in Years:
        quar1={1:0,2:0,3:0}
        quar2={4:0,5:0,6:0}
        quar3={7:0,8:0,9:0}
        quar4={10:0,11:0,12:0}
        
        
        for i in range(len(data)):
            if data['year'][i]== j: 
                if data['month'][i] in quar1:
                         quar1[data['month'][i]]+=data['Installs'][i]
                elif data['month'][i] in quar2:
                         quar2[data['month'][i]]+=data['Installs'][i]
                elif data['month'][i] in quar3:
                         quar3[data['month'][i]]+=data['Installs'][i]
                elif data['month'][i] in quar4:
                         quar4[data['month'][i]]+=data['Installs'][i]         
        if sum(quar1.values())>sum(quar2.values()) and sum(quar1.values())>sum(quar3.values()) and sum(quar1.values())>sum(quar4.values()):
            list_year.append(quar1)    
        elif sum(quar2.values())>sum(quar3.values()) and sum(quar2.values())>sum(quar4.values()):
            list_year.append(quar2)
        elif sum(quar3.values())>sum(quar4.values()):
            list_year.append(quar3)
        else:
            list_year.append(quar4)
    print(list_year)
    #dict1={}
    #for i in range(len(list_year)):
    #    dict1.update({Years[i]:list_year[i]})
    #print(dict1)  
    list10=[]
    Month1,Month2,Month3 = [],[],[]
    for i in range(len(list_year)):
            list2=[]            
            for j in (list_year[i].keys()):
                print(j)
                list2.append(j)    
            list10.append(list2)    
    #print(list10) 
    for j in range(1): 
        for i in range(len(list10)):
                Month1.append(list10[i][j])         
    for j in range(1,2): 
        for i in range(len(list10)):
                Month2.append(list10[i][j])
    for j in range(2,3): 
        for i in range(len(list10)):
                Month3.append(list10[i][j])
     
    print(Month1)
    print("---------")
    print(Month2)
    print("---------")
    print(Month3)    
    print("---------")
    
    list1=[]
    for i in range(len(list_year)):
            list2=[]            
            for j in (list_year[i].values()):
                print(j)
                list2.append(j)    
            list1.append(list2)    
    Years = []
    for i in range(2010,2019):
        Years.append(str(i))
    Quatmonth_list=[]  
    for j in range(0,3): 
        list2=[] 
        for i in range(len(list1)):
                list2.append(list1[i][j])
        Quatmonth_list.append(list2)   
    
    pos = np.arange(len(Years))
    bar_width = 0.3
        
      
        
    figure2 = plt.Figure(figsize=(10,4), dpi=100)
    
    chart = figure2.add_subplot(111)
        
    bar1 = chart.bar(Years,Quatmonth_list[0],bar_width,color='green',edgecolor='black')
    bar2 = chart.bar(pos+bar_width,Quatmonth_list[1],bar_width,color='yellow',edgecolor='black')
    bar3 = chart.bar(pos+bar_width*2,Quatmonth_list[2],bar_width,color='red',edgecolor='black')
        
    chart.set_ylabel("Installs")
    chart.set_xlabel('Years')
    figure2.suptitle('Group Barchart - Quater Month across the year',fontsize=18)
    
    for idx,rect in enumerate(bar1):
                    height = rect.get_height()
                    chart.text(rect.get_x() + rect.get_width()/2., 1.05*height,Month1[idx],ha='center', va='bottom', rotation=0) 
              
    for idx,rect in enumerate(bar2):
                    height = rect.get_height()
                    chart.text(rect.get_x() + rect.get_width()/2., 1.05*height,Month2[idx],ha='center', va='bottom', rotation=0) 
                    
    for idx,rect in enumerate(bar3):
                    height = rect.get_height()
                    chart.text(rect.get_x() + rect.get_width()/2., 1.05*height,Month3[idx],ha='center', va='bottom', rotation=0) 
          
    
    canvas = FigureCanvasTkAgg(figure2, master=screen)
    canvas.get_tk_widget().place(x=0,y=100)
    
    toolbar = NavigationToolbar2Tk(canvas, screen)
    toolbar.update()
    String="In the above Graph Quarter of each Year with their Higher Installs are plotted From 2010 to 2018"
    tk.Label(screen,text=String,font=("Calibri",13,'italic'),fg='#ad023e',bg='white').place(x=10,y=520)        
    screen.mainloop()
    
    
    
    

def newRelation1(app,x,y):
    global dict_app_relation
        
    for i in x:
        if i==-999:
            x.remove(i)
            y.remove(i)
        
    if x==[] or y==[]:
        return
        
    data = pd.DataFrame({'Sentiment_pol':y , 'Sentiment_sub': x})
    val = data['Sentiment_pol'].corr(data['Sentiment_sub'])
        
    dict_app_relation[app] = val

def function_q13():
    global screen,df,dict_app_relation
    dict_app_relation={}
    
    root = Tk()
    root.iconbitmap(r"C:\\InternshipFinal\\google.ico")
    big_frame = tk.Frame(root,bg='white',width='700',height='630',bd=4,relief=RIDGE)
    big_frame.place(x=50,y=60)
    w=700
    h=600
    ws=root.winfo_screenwidth()
    hs=root.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))

    root.configure(background='white')

    
    df = pd.read_csv("C:\\InternshipFinal\\user.csv")
    df=df.replace(np.NaN,-999)
    
    dict_app_index_count={}
    for index in range(len(df['App'])):
        app = df['App'][index]
        if app in dict_app_index_count:
            dict_app_index_count[app][1]+=1
        else:
            dict_app_index_count[app]=[index,1]
            
    # after this for loop dict_app_index_count will hold the app name as key and it's first index in data set and total count in data set as item
    
    for app in dict_app_index_count:
        index = dict_app_index_count[app][0]
        count = dict_app_index_count[app][1]
        sub,pol=[],[]
        
        for i in range(count):
            c = index+i
            sub.append(df['Sentiment_Subjectivity'][c])
            pol.append(df['Sentiment_Polarity'][c])
        
        newRelation1(app,sub,pol)
    
    app_no = np.arange(len(dict_app_relation.keys()))
    
    relation = []
    
    for i in dict_app_relation:
        relation.append(dict_app_relation[i])
 
    figure3 = plt.Figure(figsize=(6,4), dpi=100)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(app_no,relation, color = '#102131')
    scatter3 = FigureCanvasTkAgg(figure3, root) 
    scatter3.get_tk_widget().place(x=50,y=45)
    ax3.grid()
    ax3.set_xlabel("Applications in sequence")
    ax3.set_ylabel("Correlation")
    ax3.set_title("The Co-rrelation for Polarity V/s Subjectivity for all apps")
    toolbar = NavigationToolbar2Tk(scatter3,root)
    toolbar.update()    
    String = """
            In this Scatter plot each point represent the correlation 
            between sentiment polarity and sentiment subjectivity And
            Most of apps have positive relation with between sentiment polarity and subjectivity
            """
    tk.Label(root,text=String,font=("Calibri",13,'italic'),fg='#102131',bg='white').place(x=0,y=420)
    root.mainloop()

def functq17():
    global screen
    screen = Tk()
    screen.iconbitmap(r"C:\\InternshipFinal\\google.ico")
    w = 600  # width for the window size
    h = 700  # height for the window size
    ws = screen.winfo_screenwidth()  # width of the screen
    hs = screen.winfo_screenheight()  # height of the screen
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    screen.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    screen.resizable(False, False)    # disabling the resize option for the window
    screen.configure(background='white')    # configuring the window
    df= pd.read_csv("C:\\InternshipFinal\\App-data.csv")
    list2=['More than 30 mb','20-30 mb','10-20 mb','Less Than 10 mb']
    df['Size'] = df['Size'].map(lambda x: x.rstrip('M'))
    df['Size'] = df['Size'].map(lambda x: str(round((float(x.rstrip('k'))/1024), 1)) if x[-1]=='k' else x)
    df['Size'] = df['Size'].map(lambda x: np.nan if x.startswith('Varies') else x)
    df['Size']=df['Size'].replace(np.NaN,-999)
    df['Size']=df['Size'].astype(float)
    #print(df['Category'].unique())

    #print(df['Size'])
    df['Installs']=df['Installs'].str.replace('+','')
    df['Installs']=df['Installs'].str.replace(',','')
    df['Installs']=df['Installs'].astype(int)
    dict1,dict2,dict3,dict4,dict5,dict6={},{},{},{},{},{}
    a,b,c,d=[],[],[],[]
    for i in range(len(df)):
        if df["Size"][i]>=30:
             a.append(df['Installs'][i])
        elif 20<=df["Size"][i]<30:
             b.append(df['Installs'][i])
        elif 10<=df["Size"][i]<20:
             c.append(df['Installs'][i])
        elif (df['Size'][i]<10):
            d.append(df['Installs'][i])
    a2=(sum(b))
    a3=(sum(c))
    a1=(sum(a))   
    a4=(sum(d))      
            
  
    list1=[a1,a2,a3,a4]
    print(list1)
    color = cm.rainbow(np.linspace(0, 2, 10))
    fig=Figure(figsize=(3,2),dpi=100)
    chart=fig.add_subplot(111)
    chart.bar(list2,list1,color=color)
    chart.set_ylabel("No of Installs")
    chart.set_xlabel("Sizes")
    chart.grid()
    fig.suptitle("No. of Installs Vs Size")
 
    canvas = FigureCanvasTkAgg(fig, screen)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, screen)
    toolbar.update()

    canvas.mpl_connect("key_press_event", on_key_press)
    Label(screen,text="From The Above Bar Graph We Say That the Size of the App Does Influence The No of Installs \nAnd the Trend is Positive As The Install Increases with Size",font=("Lucida",10,'bold')).place(x=0,y=610)
    button = Button(master=screen, text="Quit", command=_quit)
    button.pack(side=BOTTOM)
    screen.mainloop()



def month(x):
    if x[0:3]=='Jan':
        return 1
    elif x[0:3]=='Feb':
        return 2
    elif x[0:3]=='Mar':
        return 3
    elif x[0:3]=='Apr':
        return 4
    elif x[0:3]=='Ma' or x[0:3]=='May':
        return 5
    elif x[0:3]=='Jun':
        return 6
    elif x[0:3]=='Jul':
        return 7
    elif x[0:3]=='Aug':
        return 8
    elif x[0:3]=='Sep':
        return 9
    elif x[0:3]=='Oct':
        return 10
    elif x[0:3]=='Nov':
        return 11
    elif x[0:3]=='Dec':
        return 12

def install():
    global sample
    Installs=[]
    for i in sample['Installs']:  #converting string based installs into integer based
        if i=='Free':
           Installs.append(0)
        else:
           Installs.append(int(i.replace('+','').replace(',','')))
    return Installs

def dates_str_to_int():
    global sample
    dates=sample['Last Updated']
    year=[]
    counter=0
    for i in dates:       
        year.append([int(i[-8:-6]),month(i[:-9]),int(i[-4:])])
        counter=counter+1
    return year

def display(x,y,z):
    for i in x:
        for j in set(i):
            y.insert('end',j)
       
def filtering(value,canvas_listbox):
    global sample
    installs=install()
    year=dates_str_to_int()
    rating=sample['Rating']
    
    category=sample['Category'].unique()
    ans=[]
    for i in category:
        ans.append([])

    for i in range(len(installs)):
        if i!= 10472 and installs[i]>=value[0]:
            if rating[i]>=value[1]:
                if year[i][2]==value[2]:
                    if sample['Category'][i]==value[3]:
                        for j in range(len(category)):
                            if category[j]==sample['Category'][i] :
                                ans[j].append(sample['App'][i])
    canvas_listbox.delete(0,'end')
    display(ans,canvas_listbox,category)


def getting(install,rating,year,category,canvas_listbox):
    if install.get().strip()!='' and rating.get().strip()!='' and year.get().strip()!=''  and category.get().strip()!='':
        value=[int(install.get().replace(',','').replace('+','')),float(rating.get()),int(year.get()),str(category.get())]
        filtering(value,canvas_listbox)
    else:
        tk.messagebox.showerror('Error','Please select values')
    
    
    



def searchapp():
    global screen,sample
    
    
    sample = pd.read_csv("C:\\InternshipFinal\\App-data.csv")
    screen = tk.Tk()
    w=1300
    h=730
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    screen.geometry("%dx%d+%d+%d"%(w,h,x,y))
    category=list(sample['Category'].unique())
                                      
    
    big_frame = tk.Frame(screen,bg='#102131',width='1300',height='730')
    big_frame.place(x=0,y=0)
    
    sample.drop(index=[10472],inplace=True)
    sample=sample.replace(np.NaN,0)

    
    year=[2010,2011,2012,2013,2014,2015,2016,2017,2018]
    rating=[]
    for i in range(5):
        for j in range(10):
            rating.append(i+(j/10))
    rating.append(5.0)

    tk.Label(big_frame,text='Installs',width=10,height=1,font=("Helvetica",15,'bold'),fg='#ffffff',bg='#000000', borderwidth=2, relief="groove").place(x=550,y=60)
    tk.Label(big_frame,text='Rating',width=10,height=1,font=("Helvetica",15,'bold'),fg='#ffffff',bg='#000000', borderwidth=2, relief="groove").place(x=350,y=60)
    tk.Label(big_frame,text='Year',width=10,height=1,font=("Helvetica",15,'bold'),fg='#ffffff',bg='#000000', borderwidth=2, relief="groove").place(x=150,y=60)
    tk.Label(big_frame,text='Category',width=10,height=1,font=("Helvetica",15,'bold'),fg='#ffffff',bg='#000000', borderwidth=2, relief="groove").place(x=750,y=60)
    combo_category=ttk.Combobox(big_frame,width=17,values=category,state="readonly")
    combo_category.place(x=750,y=110)
    combo_install=ttk.Combobox(big_frame,width=17,values=['0','10+','100+','1,000+','10,000+','1,00,000+','10,00,000+','1,00,00,000+'],state="readonly")
    combo_install.place(x=550,y=110)
    combo_rating=ttk.Combobox(big_frame,width=17,values=rating,state="readonly")
    combo_rating.place(x=350,y=110)
    combo_year=ttk.Combobox(big_frame,width=17,values=year,state="readonly")
    combo_year.place(x=150,y=110)
    
    canvas=tk.Canvas(big_frame,width=970,height=450,bg='pink')
    canvas.place(x=150,y=150)
    scroll1=tk.Scrollbar(canvas)
    canvas_listbox=tk.Listbox(canvas,yscrollcommand = scroll1.set,height=20,width=96,bg='#A9D0F5',font=('Calibri',14,'bold'))
    canvas_listbox.pack( side = 'left', fill = 'both' )
    scroll1.pack(side='right', fill='y' )
    scroll1.config( command = canvas_listbox.yview )
    
    
    btn_search=tk.Button(big_frame,text='Search',height=1,font=("Helvetica",15,'bold'),fg="white",width=15,bg="black",command=lambda:getting(combo_install,combo_rating,combo_year,combo_category,canvas_listbox))
    btn_search.place(x=1020,y=85)

    
    screen.mainloop()
    

