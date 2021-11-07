import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv 

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()
fig=ff.create_distplot([data], ["Math_score"], show_hist=False)
fig.show()
mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print("This is the mean of ur test scores guys... with indian parents... oooooo thats rough buddy", mean)
print("Don't mind this parents what u really want is up. That is ur excuse to compare ur kids to Rahul next door. He got 105%.",std_deviation)
