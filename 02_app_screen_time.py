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

#Graph for daily screen time per app (monthly data)


daily = df.groupby(["Date", "App"])["Screen Time (min)"].sum().reset_index()


figure3 = px.line(daily,
              x="Date",
              y="Screen Time (min)",
              color="App", 
              title="Daily Screen Time per App")
figure3.show()