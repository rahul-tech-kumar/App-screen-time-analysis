# Screentime analysis is the task of analysing and creating a report 

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

#loading the files
df=pd.read_csv("app_screen_time.csv")
# print(df.duplicated())
#checking reading or not
print(df.head(10))

#checking is there any null value in csv file
print(df.isnull().sum())
print(df.describe())


#1. Screen Time vs Notifications per day

fig = px.scatter(
    df,
    x="Notifications",
    y="Screen Time (min)",
    color="App",
    size="Times Opened",
    title="Screen Time vs Notifications per App (per day data)"
)
fig.show()
