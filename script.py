# Read Bitcoin CSV into Pandas DF --
# Remove all NAN rows --
# Create a graph of historical Data
# Use a user defined function to create a graph from date range
# Use a user defined function to perform stat analysis over a date range
# Impliment monte carlo simulation to predict future stock price
#

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
length = 3484305
temp_length =300;

path = r'C:\Users\aaron\Desktop\Coding\UCD Data Analytics\Bitcoin Data\BitcoinData.csv'

def cleanformat(path,temp_length):
    i = 0;
    # Read in data and drop any rows with NAN
    data = pd.read_csv(path)
    data.dropna(inplace=True)
    data.reset_index(drop=True, inplace=True)

    # Read in UNIX timestamp and convert to DateTime String and replace
    timestamp = [datetime.fromtimestamp(data.iloc[i,0]) for i in range(0, temp_length+1)]  # change 101 to length

    while(i<=temp_length):  # change 100 to length
        data.iloc[i, 0] = datetime.strftime(timestamp[i], '%d/%m/%Y %H:%M:%S')
        print(i)
        i += 1

    return data


def graphing(dataset,temp_length,step,marker,markersize,rotation,ha):
    plt.plot(dataset.loc[:temp_length, 'Timestamp'], dataset.loc[:temp_length, 'Open'], marker=marker, markersize=markersize)
    space = np.arange(0,temp_length,step)
    plt.xticks(space, rotation=rotation, ha=ha)
    plt.show()

data = cleanformat(path,temp_length)
print(data)
print(data["Open"].describe())
#graphing(data,temp_length,30,"o",0.1,45,'right')