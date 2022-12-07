# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:02:29 2022

@author: tanay
"""

# package: is basically collection of python programs
# module: is  a collection of packages

import pandas as pd

data = pd.read_csv('bank.csv')
# print(data.columns)
# print(data.dtypes)
# print(data.select_dtypes('O'))


data.rename(columns= {'job': 'jobs'}, inplace= True)
data.drop(columns= ['jobs'], inplace= True)
df = data['age']

adults = data.loc[data['age']>18]

max_age = data.age.max()
min_age = data.age.min()
mean_age = data.age.mean()
median_age = data.age.median()


# h.w. --> read the csv file and tell me what are the diffrent job title in the data?
# how to solve this in python
# -----------------------------------------------------------------
# a = {'age':21, 'name':'abc', 'marrital_status': 'single'}
# print(a.keys())
# print(a.items())
# print(a.values())


# a = {1,1,1,2,3,45,6,6}
# print(a)

# -----------------------------------------------------------------
print(data.dtypes)
def age_count(df):
    if df.age>=18 and df.age<60:
        return 'Junior'
    else:
        return 'Senior Citizen'
    
    
data['age_group'] = data.apply(age_count, axis=1)

data.to_csv('a.csv', index= False)

age_count = data.groupby('age', as_index= False)['education'].count()
marital_coount = data.groupby('marital status').agg({'age': 'count'})

marital_coount.to_excel('abc.xlsx')
# df = pd.read_excel('name_of_xcl.xlsx')
# pd.read_json('name.json'


# h.w. --> what is a json file and example of it?

# -------------------------------------------------------------------
# a = data.sort_values('age', ascending= False)