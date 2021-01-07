import pandas as pd
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
from gspread-formatting import *

#Update Procedure:
# 1. Create df based on ss values
# 2. Remove the change column
# 3. Get the current date and create an empty column with date as the label.
# 4. Updates the column with the current prices of items.
#   - Creates new row with zeros up to current date if new item.
# 5. Calculates the %change between the last two columns and creates a new column 'change'

def update(ss, values):
    df = pd.DataFrame(ss.get_all_records())
    df = df.drop('Change', axis = 1)



    current_items = df['Item'].values
    date = datetime.datetime.now()
    date = date.strftime("%Y-%m-%d, %H:%M")

    df[date] = 0

    len_df = len(df.columns)

    for value in values:

        if value in current_items:
            df.loc[df["Item"] == value,date] = values[value]

        else:

            to_add = np.zeros(len_df)
            to_add[len_df - 1] = values[value]

            df.loc[len(df.index)] = to_add
            df.loc[len(df.index)-1,'Item'] = value


    change(df)

    ss.update([df.columns.values.tolist()] + df.values.tolist())



def combine(ss):
    n_days = 5
    df = pd.DataFrame(ss.get_all_records())

    change_col = df['Change']
    items_col = df['Item']

    df = df.drop('Change',axis = 1)

    col_names = df.columns[1:]
    duplicates = []

    today = datetime.date.today()


    dict = {}
    dict['Item'] = items_col

    previous = col_names[0].split(",")[0]

    for i, col_values in enumerate(df.T.values[1:]):
        date_values = col_names[i].split(",")[0].split("-")

        t1 = datetime.date(year = int(date_values[0]),month = int(date_values[1]),day = int(date_values[2]))
        delta = today - t1

        if (col_names[i].split(",")[0]) == previous and delta.days > n_days:
            duplicates.append(col_values)
            if (i == len(df.T.values) - 2):
                dict[col_names[i-1]] = averages(duplicates)
        else:
            dict[col_names[i-1]] = averages(duplicates)

            previous = col_names[i].split(",")[0]
            duplicates = []
            duplicates.append(col_values)

            if (i == len(df.T.values) - 2):
                dict[col_names[i]] = averages(duplicates)

    df_new = pd.DataFrame(dict)


    change(df_new)


    ss.update([df_new.columns.values.tolist()] + df_new.values.tolist())

def averages(arr):
    total = 0
    length = len(arr)
    new_values = []

    for i in range(len(arr[0])):
        for j in range(len(arr)):
            total += arr[j][i]
        average = total/length
        new_values.append(average)
        total = 0

    return new_values


def change(df):
    df['Change'] = np.where(df.iloc[:,-2] != 0, (df.iloc[:,-1] / df.iloc[:,-2]), 0)
