import statistics
import pandas as pd
import plotly.figure_factory as ff
import csv

df=pd.read_csv('data.csv')
height_list=df['Height(Inches)'].to_list()
weight_list=df['Weight(Pounds)'].to_list()
            #mean
height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)
            #median
height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)
            #mode
height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

print('mean,median & mode of height is {} , {} & {}'.format(height_mean,height_median,height_mode))
print('mean,median & mode of weight is {} , {} & {}'.format(weight_mean,weight_median,weight_mode))

height_std_dev=statistics.stdev(height_list)
weight_std_dev=statistics.stdev(weight_list)

print('std_dev of height= ',height_std_dev)
print('std_dev of weight= ',weight_std_dev)

                                                                                