import csv
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff 

df=pd.read_csv("Data.csv")
data=df["temp"].tolist()

def random_set_of_mean(Counter):
    dataset=[]
    for i in range(0,Counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    Mean=statistics.mean(dataset)
    return Mean  

def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)        

setup()