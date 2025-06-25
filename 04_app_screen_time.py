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


fig = px.line(
    df,
    x="Times Opened",
    y="Screen Time (min)",
    color="App",
    title="Screen Time vs Times Opened(with line)"
)
fig.show()


fig = px.scatter(
    df,
    x="Times Opened",
    y="Screen Time (min)",
    color="App",
    title="Screen Time vs Times Opened(with dots)"
)
fig.show()
