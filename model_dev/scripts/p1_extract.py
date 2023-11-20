import pandas as pd 

## Loading/Extracting Data

# Landing Page: https://catalog.data.gov/dataset/nypd-arrest-data-year-to-date
# Data Download Link: 
datalink = 'https://data.cityofnewyork.us/api/views/uip8-fykc/rows.csv?accessType=DOWNLOAD'

df = pd.read_csv(datalink)
df.shape
df.sample(5)

df.columns




## Saving data as a csv to model_dev/data/raw folder
df.to_csv('model_dev/data/raw/arrest_data.csv', index=False)

## Saving as pickle to model_dev/data/raw folder folder
df.to_pickle('model_dev/data/raw/arrest_data.pkl')