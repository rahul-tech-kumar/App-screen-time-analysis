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


# Filter for May 2025 for example
# df["Date"] = pd.to_datetime(df["Date"])  # Ensure it's datetime type

        
# df_month = df[df["Date"].dt.to_period("M") == "2025-06"]



monthly_screen_time = df.groupby("App")["Screen Time (min)"].sum().reset_index()

#we have to sort in orer


monthly_screen_time = monthly_screen_time.sort_values(by="Screen Time (min)", ascending=False)

#Total Screen Time in One Month by App
figure1=px.bar(data_frame=monthly_screen_time,
              x="App",
              y="Screen Time (min)",
              color="App",
              title= "Total Screen Time in One Month by App",
              template="plotly_dark"
              )

figure1.show()

#Total Notifications per App in one month"

notif = df.groupby("App")["Notifications"].sum().reset_index()
notif = notif.sort_values(by="Notifications", ascending=False)
figure2 = px.bar(notif,
                 x="App",
                 y="Notifications", 
                 color="App",
                 title="Total Notifications per App in one month",
                 template="plotly_dark"
                 )


figure2.show()



