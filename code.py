import random
import statistics
import plotly.figure_factory as ff

diceresult=[]
for i in range (0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceresult.append(dice1+dice2)
mean=sum(diceresult)/len(diceresult)
median=statistics.median(diceresult)
mode=statistics.mode(diceresult)
std_dev=statistics.stdev(diceresult)
fig=ff.create_distplot([diceresult],['Result'],show_hist=False)
print('mean= ',mean)
print('std_dev= ',std_dev)
print('median= ',median)
print('mode= ',mode)
fig.show()