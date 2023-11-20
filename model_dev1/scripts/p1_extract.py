import pandas as pd 

## get data 

# original link: https://catalog.data.gov/dataset/warehouse-and-retail-sales
# data download link: 
datalink = 'https://data.montgomerycountymd.gov/api/views/v76h-r7br/rows.csv?accessType=DOWNLOAD'

df = pd.read_csv(datalink)
df.size
df.sample(5)


## Saving data as a csv to model_dev/data/raw/Warehouse_and_Retail_Sales
df.to_csv('model_dev1/data/raw/Warehouse_and_Retail_Sales.csv', index=False)

## Saving as pickle to model_dev/data/raw/Warehouse_and_Retail_Sales
df.to_pickle('model_dev1/data/raw/Warehouse_and_Retail_Sales.pkl')