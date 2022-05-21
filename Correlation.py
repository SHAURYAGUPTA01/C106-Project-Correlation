import plotly.express as px
import csv
import numpy as np

def getDataSource(dp):
    marks=[]
    present = []
    with open(dp) as f:
        data = csv.DictReader(f)
        for i in data:
            marks.append(float(i["Marks In Percentage"]))
            present.append(float(i["Days Present"]))
    return { "x" : present  , "y" : marks }

def FindCorrelation(ds):
    c = np.corrcoef(ds["x"],ds["y"])
    print(c[0,1])

def setup():
    dp = "Student Marks vs Days Present.csv"
    ds=getDataSource(dp)
    FindCorrelation(ds)

setup()
# Corrcoef is 0 therefore we can say that data is not correlated