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
from scipy.stats import norm

path = 'Cleaned.csv'

def load_Data(path):
    dataset = pd.read_csv(path, parse_dates=True)
    return dataset


def graphing(dataset, rotation, horizontal_align, x_column, y_column):
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
    #plt.show()


def simulator(dataset, from_date, length, num_sims):
    length_df = dataset['Date'].count()

    for x in range(0, length_df):
        if str(dataset.iloc[x, 0]) == from_date:
            date_index_start = x
        else:
            pass


    temp_dataset = dataset.iloc[date_index_start: , 1]
    ln_return = np.log(1 + temp_dataset.pct_change())
    mean = ln_return.mean()
    variance = ln_return.var()
    drift = mean - (0.5*variance)
    std_dev = ln_return.std()

    daily_returns = np.exp(drift + std_dev * norm.ppf(np.random.rand(length, num_sims)))

    price_list = np.zeros_like(daily_returns)
    price_list[0] = dataset.iloc[-1, 1]

    for x in range(1, length):
        price_list[x] = price_list[x-1] * daily_returns[x]


    plot_list = np.zeros((length, 1))
    for i in range(0, length):
        plot_list[i] = price_list[i].mean()


    plt.figure()
    plt.title('{days} days after {start}'.format(days=length, start=dataset.iloc[-1, 0]))
    plt.ylabel('Prices ($)')
    plt.xlabel('Days After')
    plt.plot(plot_list)
    plt.show()





data = load_Data(path)
graphing(data, 45, 'right', 'Date', 'Price')
simulator(data, '01-January-2015', 30, 1000000)