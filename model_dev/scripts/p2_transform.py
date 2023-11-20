import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

## Loading raw data (pickle)
df = pd.read_pickle('model_dev/data/raw/arrest_data.pkl')

## Getting column names
df.columns

## Cleaning column names 
## Making them all lower case and removing white spaces
df.columns = df.columns.str.lower().str.replace(' ', '_')
df.columns

## Getting data types
df.dtypes 

## drop columns
to_drop = [
    'arrest_key',
    'x_coord_cd',
    'y_coord_cd',
    'latitude',
    'longitude']
df.drop(to_drop, axis=1, inplace=True, errors='ignore')

#######################

## Changing occur_date column from mm/dd/yyyy format to day of the week 
df['arrest_date'] = pd.to_datetime(df['arrest_date'])
df['arrest_date'] = df['arrest_date'].dt.day_name()

# Performing ordinal encoding on occur_date column. 1-Monday, 2-Tuesday....7-Sunday. 
day_to_number = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
df['arrest_date'] = df['arrest_date'].replace(day_to_number).astype(int)

# Creating dataframe with mapping
df_mapping_date = pd.DataFrame({'arrest_date': list(day_to_number.keys()), 'arrest_date_num': list(day_to_number.values())})
df_mapping_date

# Saving mapping to csv
df_mapping_date.to_csv('model_dev/data/processed/mapping_date.csv', index=False)

############

## Encoding the perp_sex column
enc = OrdinalEncoder()
enc.fit(df[['perp_sex']])
df['perp_sex'] = enc.transform(df[['perp_sex']])

# Creating a dataframe with mapping
df_mapping_perp_sex = pd.DataFrame(enc.categories_[0], columns=['perp_sex'])
df_mapping_perp_sex['perp_sex_ordinal'] = df_mapping_perp_sex.index
df_mapping_perp_sex.head(5)
# save mapping to csv
df_mapping_perp_sex.to_csv('model_dev/data/processed/mapping_perp_sex.csv', index=False)

############

## Encoding the perp_race column
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd

enc = OrdinalEncoder()
enc.fit(df[['perp_race']])
df['perp_race'] = enc.transform(df[['perp_race']])

# Creating a dataframe with mapping
df_mapping_perp_race = pd.DataFrame(enc.categories_[0], columns=['perp_race'])
df_mapping_perp_race['perp_race_ordinal'] = df_mapping_perp_race.index
df_mapping_perp_race.head(5)
# save mapping to csv
df_mapping_perp_race.to_csv('model_dev/data/processed/df_mapping_perp_race.csv', index=False)

############

## Encoding the perp_age_group column
enc = OrdinalEncoder()
enc.fit(df[['perp_age_group']])
df['perp_age_group'] = enc.transform(df[['perp_age_group']])

# Creating a dataframe with mapping
df_mapping_perp_age_group = pd.DataFrame(enc.categories_[0], columns=['perp_age_group'])
df_mapping_perp_age_group['perp_age_group_ordinal'] = df_mapping_perp_age_group.index
df_mapping_perp_age_group.head(5)
# save mapping to csv
df_mapping_perp_age_group.to_csv('model_dev/data/processed/mapping_perp_age_group.csv', index=False)

#######################

## Saving processed dataset to a csv file to test the model
df.to_csv('model_dev/data/processed/processed_arrest_data.csv', index=False)