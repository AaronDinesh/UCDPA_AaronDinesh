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

path = 'TestCleaned.csv'


def graphing(path, rotation, horizontal_align, x_column, y_column):
    # Reading the Cleaned Dataset
    dataset = pd.read_csv(path, parse_dates=True)
    length = dataset[x_column].count()

    # Calculating max y value
    max_y = 0
    for x in dataset['Price']:
        if x > max_y:
            max_y = x
        else:
            pass

    # Graphing part of the dataset using the x-column and the y-column parameters passed in
    x_range = np.arange(0, length, 389)
    y_range = np.arange(0, round(max_y)+1700, 1700)
    plt.plot(dataset[x_column], dataset[y_column], marker="o", markersize=0.1)
    plt.xlabel('Time')
    plt.ylabel('Price ($)')
    plt.title('Price of Bitcoin from 18/07/10-12/03/21')
    plt.xticks(x_range, rotation=rotation, ha=horizontal_align)
    plt.yticks(y_range, ha=horizontal_align)
    plt.margins(0, 0, tight=True)
    plt.show()


def simulator():


graphing(path, 45, 'right', 'Timestamp', 'Price')
simulator()