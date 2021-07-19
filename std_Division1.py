import csv
import pandas as pd
import plotly.express as px
import math
with open('data1.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
totalMarks=0
totalEnteries=len(file_data)
for marks in file_data:
    totalMarks+=float(marks[1])
mean=totalMarks/totalEnteries
print('Mean is',mean)
df=pd.read_csv('data1.csv')
fig=px.scatter(df,x='Student Number',y='Marks')
fig.update_layout(shapes=[dict(type='line',y0=mean,y1=mean,x0=0,x1=totalEnteries)])
fig.update_yaxes(rangemode='tozero')
fig.show()
#finding out std div
square_list=[]
for number in file_data:
    a=int(number[1])-mean
    a=a**2
    square_list.append(a)
sum=0
for i in square_list:
    sum+=i
result=sum/totalEnteries
stdDeviation=math.sqrt(result)
print (stdDeviation)