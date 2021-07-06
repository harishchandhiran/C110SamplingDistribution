import statistics
import pandas as pd
import plotly.figure_factory as pff
import csv
import random

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
print(population_mean)
fig = pff.create_distplot([data],["reading_time"], show_hist=False)
fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = pff.create_distplot([df],["reading_time"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    #show_fig(mean_list)
    print("sampling mean:- ", statistics.mean(mean_list))

setup()