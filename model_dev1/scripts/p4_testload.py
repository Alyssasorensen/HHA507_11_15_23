import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler


### try and load the model back
loaded_model = pickle.load(open('model_dev1/models/xgboost100.sav', 'rb'))
### load scaler
loaded_scaler = pickle.load(open('model_dev1/models/scaler.sav', 'rb'))

## now lets create a new dataframe with the same column names and values
df_test = pd.DataFrame(columns=['year_occ', 'month_occ', 'supplier', 'item_code', 'item_description',
       'item_type', 'retail_sales', 'retail_transfers', 
       'warehouse_sales'])


# year,month,supplier,item_code,item_description,item_type,retail_sales,retail_transfers,warehouse_sales
## year_occ = 3.0 
## month_occ = 0.0
## supplier = 273.0
## item_code = 3.0
## item_description = 4504.0
## item_type = 7.0
## retail_sales = 29.0
## retail_transfers = 68.0
## warehouse_sales = 176.0

df_test.loc[0] = [3.0, 0.0, 273.0, 3.0, 4504.0, 7.0, 29.0, 68.0, 176.0]
df_test_scaled = loaded_scaler.transform(df_test)


# Assuming the loaded_scaler was fitted on X_train, which has the original feature names
original_feature_names = X_train.columns

# Use the same feature names in df_test
df_test.columns = original_feature_names

# Now you can safely transform df_test
df_test_scaled = loaded_scaler.transform(df_test)






# Predict on the test set
y_test_pred = loaded_model.predict(df_test)
# print value of prediction
print(y_test_pred[0])



