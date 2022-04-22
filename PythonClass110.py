import random
import statistics
import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go

data = pd.read_csv("data.csv")

data1 = data["temp"].to_list()

mean = statistics.mean(data1)

median = statistics.median(data1)

mode = statistics.mode(data1)

std = statistics.stdev(data1)

##figure = ff.create_distplot([data1],["temp"],show_hist=False)

##figure.show()

def randomSample(counter):
    dataSet = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data1))
        value = data1[random_index]
        dataSet.append(value)
    sample1Mean = statistics.mean(dataSet)
    return sample1Mean

def show_figure(finalMean_list):
    df = finalMean_list
    finalMean = statistics.mean(finalMean_list)
    print("Final mean value of all samples are {}".format(finalMean))
    fig = ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="Mean"))
    fig.show()

def main():
    finalMean_list = []
    for i in range(0,1000):
        random_sample_mean = randomSample(100)
        finalMean_list.append(random_sample_mean)
    show_figure(finalMean_list)
main()

def std():
    finalMean_list = []
    for i in range(0,1000):
        std_sample = randomSample(100)
        finalMean_list.append(std_sample)
        
    final_std = statistics.stdev(finalMean_list)
    print("The standard deviation of sample distribution is",final_std)
    
std()    

