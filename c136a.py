print(final_star_list)
    temp_dict ={}
    final_star_list.append(temp_dict)
     temp_dict["gravity"]= gravity[i]
     temp_dict["distance"]=dist[i]
     temp_dict["radius"]=radius[i]
     temp_dict["radius"]=radius[i]
     temp_dict["mass"]=mass[i]
     temp_dict["name"]=name[i]
for i in range(0,len(name)):
temp_dict ={}

final_star_list = []


gravity = df["Distance"].to_list()
dist = df["Distance"].to_list()
radius = df["Radius"].to_list()
mass = df["Mass"].to_list()
name = df["Star_name"].to_list()

df.drop(['Unnamed: 0'],axis =1,inplace=True)

df.head()
df = pd.read_csv("star_with_gravity.csv")

import pandas as pd

"""
@author: Vishal

Created on Thu Oct 29 12:44:15 2020
"""
# -*- coding: utf-8 -*-