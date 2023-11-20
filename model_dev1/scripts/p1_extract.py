import pandas as pd 

## Loading/Extracting Data

# Landing Page: https://catalog.data.gov/dataset/warehouse-and-retail-sales
# Data Download Link: 
datalink = 'https://data.montgomerycountymd.gov/api/views/v76h-r7br/rows.csv?accessType=DOWNLOAD'

df = pd.read_csv(datalink)
df.shape
df.sample(5)

df.columns

## Saving data as a csv to model_dev1/data/raw folder
df.to_csv('model_dev1/data/raw/warehouse_and_retail_sales_data.csv', index=False)

## Saving as pickle to model_dev1/data/raw folder
df.to_pickle('model_dev1/data/raw/warehouse_and_retail_sales_data.pkl')