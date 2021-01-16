import pandas as pd
import numpy as np

df = pd.read_csv(
    "https://raw.githubusercontent.com/reuben21/Google-Play-Store-App-Lauch-Study/master/InternshipFinal/App-data.csv")
df = df.replace(np.NaN, -1)


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
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    df['Installs'] = pd.to_numeric(df['Installs'])
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
    df['Installs'] = df['Installs'].map(lambda x: x.rstrip('+'))
    df['Installs'] = df['Installs'].map(lambda x: ''.join(x.split(',')))
    df['Installs'] = pd.to_numeric(df['Installs'])
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
    print(val, label)
    new_list = []
    for i in val:
        new_list.append(int(i))
    return new_list, label
