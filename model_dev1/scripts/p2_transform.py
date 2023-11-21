import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

## get data raw
df = pd.read_pickle('model_dev1/data/raw/warehouse_and_retail_sales_data.pkl')

## get item_description
df_item_description = pd.read_csv('model_dev1/data/raw/warehouse_and_retail_sales_data.csv')

## get column names
df.columns

## do some data cleaning of colun names, 
## make them all lower case, replmove white spaces and rpelace with _ 
df.columns = df.columns.str.lower().str.replace(' ', '_')

## get data types
df.dtypes # nice combination of numbers and strings/objects 

## drop columns
to_drop = [
    'month',
    'year',
    'item_code'
    'item_description',
    'item_type',
]

df.drop(to_drop, axis=1, inplace=True, errors='ignore')


## perform ordinal encoding on year
enc = OrdinalEncoder()
enc.fit(df[['year']])
df['year'] = enc.transform(df[['year']])

## create dataframe with mapping
df_mapping_year = pd.DataFrame(enc.categories_[0], columns=['year_occ'])
df_mapping_year['year_ordinal'] = df_mapping_year.index
df_mapping_year.head(5)

## save mapping to csv
df_mapping_year.to_csv('model_dev1/data/processed/mapping_date.csv', index=False)




## perform ordinal encoding on retail transfers
enc = OrdinalEncoder()
enc.fit(df[['retail_transfers']])
df['retail_transfers'] = enc.transform(df[['retail_transfers']])


## create dataframe with mapping
df_mapping_retail_transfers = pd.DataFrame(enc.categories_[0], columns=['retail_transfers_occ'])
df_mapping_retail_transfers['retail_transfers'] = df_mapping_retail_transfers.index
df_mapping_retail_transfers.head(5)

## retail_transfers --> will need to encode this
df.retail_transfers.value_counts()

# save mapping to csv
df_mapping_retail_transfers.to_csv('model_dev1/data/processed/mapping_retail_transfers.csv', index=False)

## perform orindla encoding on retail sales
enc = OrdinalEncoder()
enc.fit(df[['retail_sales']])
df['retail_sales'] = enc.transform(df[['retail_sales']])

## create dataframe with mapping
df_mapping_retail_sales = pd.DataFrame(enc.categories_[0], columns=['retail_sales'])
df_mapping_retail_sales['retail_sales'] = df_mapping_retail_sales.index
df_mapping_retail_sales.head(5)

# save mapping to csv
df_mapping_retail_sales.to_csv('model_dev1/data/processed/mapping_retail_sales.csv', index=False)









## perform ordinal encoding on warehouse sales
enc = OrdinalEncoder()
enc.fit(df[['warehouse_sales']])
df['warehouse_sales'] = enc.transform(df[['warehouse_sales']])

## create dataframe with mapping
df_mapping_warehouse_sales = pd.DataFrame(enc.categories_[0], columns=['warehouse_sales'])
df_mapping_warehouse_sales['warehouse_sales_ordinal'] = df_mapping_warehouse_sales.index
df_mapping_warehouse_sales.head(5)
## save mapping to csv
df_mapping_warehouse_sales.to_csv('model_dev1/data/processed/mapping_warehouse_sales.csv', index=False)



## item type
df.item_type.value_counts()
## drop if value is '-'
df = df[df['item_type'] != '-']

## perform ordinal encoding on item_type
enc = OrdinalEncoder()
enc.fit(df[['item_type']])
df['item_type'] = enc.transform(df[['item_type']])

## create dataframe with mapping
df_mapping_item_type = pd.DataFrame(enc.categories_[0], columns=['item_type'])
df_mapping_item_type['item_type_ordinal'] = df_mapping_item_type.index
df_mapping_item_type.head(5)
item_type_mapping = {
    'A': 'Beer',
    'B': 'Dunnage',
    'C': 'Kegs',
    'D': 'Liquor',
    'F': 'Non-alcohol',
    'G': 'Str_supplies',
    'H': 'Ref',
    'I': 'Wine'
}

df_mapping_item_type['item_type'] = df_mapping_item_type['item_type'].map(item_type_mapping)
## save mapping to csv
df_mapping_item_type.to_csv('model_dev1/data/processed/mapping_item_type.csv', index=False)



#### save a temporary csv file of 1000 rows to test the model
df.head(100).to_csv('model_dev1/data/processed/warehouse_and_retail_sales_data.csv', index=False)