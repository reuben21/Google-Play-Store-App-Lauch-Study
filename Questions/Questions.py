import operator

import pandas as pd
import numpy as np

df = pd.read_csv(
    "https://raw.githubusercontent.com/reuben21/Google-Play-Store-App-Lauch-Study/master/InternshipFinal/App-data.csv")
df = df.replace(np.NaN, -1)
df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
df['Installs'] = pd.to_numeric(df['Installs'])


def ques0():
    catcount = {}
    for index in range(len(df)):
        if df['Category'][index] == -1:
            continue

        if df['Category'][index] in catcount:
            catcount[df['Category'][index]] += 1
        else:
            catcount[df['Category'][index]] = 1

    return catcount


# print(catcount)

def ques1():
    list1 = {}
    df['Installs'] = df['Installs'].str.replace('+', '')
    df['Installs'] = df['Installs'].str.replace(',', '')
    df['Installs'] = df['Installs'].astype(int)

    category = {}
    sum1 = []
    for i in df['Category']:
        category.update({i: 0})

    for i in category.keys():
        t2 = df[i == df.Category].Installs.tolist()
        sum1.append(sum(t2))
        category.update({i: float(((sum(t2)) / (sum(df['Installs']))) * 100)})
    # print(category)
    # list1 = list(category.values())

    return category
    # for i in category.keys():
    #     if float(category[i]) < 0.5:
    #         print(category[i])
    # if category[i] < 0:


def ques2():
    list2 = ["More than 5M", "500k-5M", "150k-500k", "50k-150k", "10k-50k"]
    dict1, dict2, dict3, dict4, dict5 = {}, {}, {}, {}, {}
    dict1 = (pd.value_counts(df['Installs'] >= 5000000))
    a1 = len(df) - dict1.values[0]
    dict2 = (pd.value_counts((df["Installs"] >= 500000) & (df["Installs"] < 5000000)))
    a2 = len(df) - dict2.values[0]
    dict3 = (pd.value_counts((df["Installs"] >= 150000) & (df["Installs"] < 500000)))
    a3 = len(df) - dict3.values[0]
    dict4 = (pd.value_counts((df["Installs"] >= 50000) & (df["Installs"] < 150000)))
    a4 = len(df) - dict4.values[0]
    dict5 = (pd.value_counts((df["Installs"] >= 10000) & (df["Installs"] < 50000)))
    a5 = len(df) - dict5.values[0]
    #    dict6=pd.value_counts(df["Installs"]<10000)
    #    a6=len(df)-dict6.values[0]
    list1 = [a1, a2, a3, a4, a5]
    new_list = []
    for i in list1:
        new_list.append(int(i))
    return new_list, list2


def ques3():
    category = df['Category'].unique()
    list1 = df['Installs']
    ans = []
    count = []

    for i in category:
        total = 0
        c = 0
        for j in range(len(df['Category'])):
            if df['Category'][j] == i:
                total = total + list1[j]
                c += 1
        #   print(total)
        ans.append(total)
        count.append(c)
    # print(ans)
    #    print(count)
    cat, avg = [], []
    for index in range(len(ans)):
        cat.append(category[index])
        avg.append(round(ans[index] / count[index]))
    # print(avg)
    #  print(cat)
    lowest = []
    for index in range(len(avg)):
        if avg[index] < 250000:
            lowest.append(category[index])

    label = category
    #    print(label)
    val = avg
    new_list1 = []
    new_list2 = []
    for i in val:
        new_list1.append(int(i))
    for i in label:
        new_list2.append(str(i))
    return new_list1, new_list2


def ques4():
    catreview = {}
    for index in range(len(df)):
        if df['Category'][index] in catreview:
            catreview[df['Category'][index]][0] += df['Rating'][index]
            catreview[df['Category'][index]][1] += 1
        #            rating+=df['Rating'][index]
        else:
            catreview[df['Category'][index]] = [df['Rating'][index], 1]
    #            rating+=df['Rating'][index]
    total = 0
    count = 0
    for i in df['Rating']:
        total += i
        count += 1
    avg = total / count
    y = []
    x = []
    for i in catreview:
        if catreview[i][0] / catreview[i][1] >= avg:
            avgcat = (catreview[i][0] / catreview[i][1])
            x.append(i)
            y.append(float(avgcat))

    return x, y


def ques5():
    list2 = ['More than 30 mb', '20-30 mb', '10-20 mb']

    df['Size'] = df['Size'].map(lambda x: x.rstrip('M'))
    df['Size'] = df['Size'].map(lambda x: str(round((float(x.rstrip('k')) / 1024), 1)) if x[-1] == 'k' else x)
    df['Size'] = df['Size'].map(lambda x: np.nan if x.startswith('Varies') else x)

    df['Size'] = df['Size'].replace(np.NaN, -999)
    df['Size'] = df['Size'].astype(float)

    # print(df['Category'].unique())

    # print(df['Size'])
    df['Installs'] = df['Installs'].str.replace('+', '')
    df['Installs'] = df['Installs'].str.replace(',', '')
    df['Installs'] = df['Installs'].astype(int)

    a, b, c = [], [], []
    for i in range(len(df)):
        if df["Size"][i] >= 30:
            a.append(df['Installs'][i])
        elif 20 <= df["Size"][i] < 30:
            b.append(df['Installs'][i])
        elif 10 <= df["Size"][i] < 20:
            c.append(df['Installs'][i])

    a2 = (sum(b))
    a3 = (sum(c))
    a1 = (sum(a))

    list1 = [a1, a2, a3]
    new_list1 = []
    for i in list1:
        new_list1.append(int(i))
    return new_list1, list2


# Question 6 - Harsh
def ques6():
    return


def ques7_a():
    varwith = []
    novar = []

    for i in range(len(df['App'])):
        if df['Android Ver'][i] == 'Varies with device':
            varwith.append(df['Installs'][i])

        else:
            novar.append(df['Installs'][i])

    x = (len(varwith), len(novar))
    #     print(x)
    android_version_label = ['Varying', 'Not varying']
    return x, android_version_label


def ques7_b():
    d = pd.DatetimeIndex(df['Last Updated'])
    df['year'] = d.year
    df['month'] = d.month

    # 6) For the years 2016,2017,2018 what are the category of apps that have got the most and the least downloads. What is the percentage increase or decrease that the

    dict_years = {}

    for year in df['year'].unique():
        dict_years[year] = 0

    for index in range(len(df)):
        dict_years[df['year'][index]] += df['Installs'][index]

    Years = []
    list_install = []

    for year in dict_years:
        Years.append(year)
        list_install.append(dict_years[year])

    # print(Years)

    # print(list_install)
    new_dict = {}
    for i in range(0, 9):
        new_dict.update({Years[i]: list_install[i]})
    new_dict1 = dict(sorted(new_dict.items(), key=operator.itemgetter(0), reverse=True))
    print(new_dict1)
    keys = list(new_dict1.keys())
    values = list(new_dict1.values())
    print(keys)
    print(values)

    return keys, values


def ques8():
    return


def ques9():
    return


def ques10():
    return
