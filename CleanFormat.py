import pandas as pd
from datetime import datetime

path = 'TestData.csv'
save_path = 'TestCleaned.csv'
format = '%d-%B-%Y'


def cleanformat(path, save_path, format_string):
    i = 0;
    # Read in data and drop any rows with NAN and reset index
    data = pd.read_csv(path)
    data.dropna(inplace=True)
    data.reset_index(drop=True, inplace=True)

    # Counts number of rows
    length = data['Timestamp'].count()

    # Read in UNIX timestamp into timestamp list using list comprehension
    timestamp = [datetime.fromtimestamp(data.iloc[i,0]) for i in range(0, length)]

    # WHILE Loop to parse timestamp list and convert to datetime string using the format specified.
    while(i<=(length-1)):
        data.iloc[i, 0] = datetime.strftime(timestamp[i], format_string)
        percent_complete = (i/length)*100
        print("{:.4f}".format(percent_complete))
        i += 1

    # Save cleaned dataset to its own csv file
    data.to_csv(save_path, index=False)

cleanformat(path,save_path, format)

