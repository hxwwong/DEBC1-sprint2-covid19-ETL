# imports
import pandas as pd
import requests
import json
import argparse
import datetime

# date range - last 100 days from yesterday (since data today is not always uploadad on time)
i = pd.date_range(datetime.date.today()-datetime.timedelta(days=100), datetime.date.today()-datetime.timedelta(days=1)).strftime('%Y-%m-%d').tolist()

# date range in proper format 
dates = [str(x) for x in i]

# get requests - from API

def get_data(date):
    url = "https://covid-19-statistics.p.rapidapi.com/reports"
    
    querystring = {"iso":"PHL","date":date}

    headers = {
        "X-RapidAPI-Key": "d2d6c905afmsh5b36aa3d76ceb64p1d9360jsn7951abdab2ed",
        "X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    to_cast = response.text
    return to_cast

# create naked DF
cols = ['date',
 'confirmed',
 'deaths',
 'recovered',
 'confirmed_diff',
 'deaths_diff',
 'recovered_diff',
 'last_update',
 'active',
 'active_diff',
 'fatality_rate']

df = pd.DataFrame(columns=cols)

# run loop and append stuff
for date in dates:
    response_dict = json.loads(get_data(date))
    # slice off unnecessary data
    x = response_dict['data'][0]
    # remove last field - always in the PH
    del x["region"]

    # append to dataframe
    df = df.append(x, ignore_index=True)

df.to_csv('rapid_API.csv')
print(df)