# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 19:03:02 2023

@author: B3ar
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


x=pd.read_csv("C:\\Users\B3ar\Desktop\data science\Standard_Metropolitan_Areas_Data-data.csv")


plt.bar(x.region, x.crime_rate, color="purple")

plt.title("Vertical Bar Graph")
plt.xlabel("Region")
plt.ylabel("Crime Rate")
plt.legend(x)
plt.show()



plt.barh(x.region, x.crime_rate, color="green")
plt.title("Horizontal Bar Graph")
plt.xlabel("Region")
plt.ylabel("Crime Rate")
plt.legend(x)
plt.show()


plt.bar(x.region, x.crime_rate, color="green")
plt.bar(x.region, x.graduates, color="blue",bottom=x.graduates)
plt.title("stacked Bar Graph")
plt.xlabel("Region")
plt.ylabel("Crime Rate")
plt.show()



divisions = ["A", "B", "C", "D", "E"]
division_avg = [70, 82, 73, 65, 68]
boys_avg = [68, 67, 77, 61, 70]

# Using the NumPy arange function to generate values for index between 0-4.
# Here,stop is 5, start is 0, and step is 1
index = np.arange(5)
width = 0.30

plt.bar(index, division_avg, width, color="green", label="Division Marks")
plt.bar(index+width, boys_avg, width, color="blue", label="Boys Marks")

plt.title("Combined Bar Graph")
plt.xlabel("Divisions")
plt.ylabel("Marks")
plt.show()




firms = ["Firm A", "Firm B", "Firm C", "Firm D", "Firm E"]
market_share = [20,25,15,10,20]

# Explode the pie chart to emphasize a certain part or some parts( Firm B in this case)
# It is useful because it makes the highlighted portion more visible.
Explode = [0,0.1,0,0,0]

plt.pie(market_share, explode=Explode, labels=firms, autopct='%1.1f%%', startangle=45)

plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Pie Chart")
plt.legend(title="List of Firms")

plt.show()

plt.scatter(x.crime_rate,x.work_force)
plt.title("Scattered Graph")
plt.xlabel("crime rate")
plt.ylabel("Work Rate")
plt.plot()
 