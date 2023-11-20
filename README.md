# datasci_9_data_prep
## HHA 507 Homework Assignment 9

Concentrate on the identification of datasets well-suited for a machine learning experiment, emphasizing the essential steps of data cleaning, encoding, and transformation required to adequately prepare the data.

## **2. Data Cleaning and Transformation Plan:**

### **NYPD_Arrest_Data__Year_to_Date_ Dataset:**

### Dataset  Description:

The dataset includes information on arrests with various features such as ARREST_KEY, ARREST_DATE, PD_CD, PD_DESC, KY_CD, OFNS_DESC, LAW_CODE, LAW_CAT_CD, ARREST_BORO, ARREST_PRECINCT, JURISDICTION_CODE, AGE_GROUP, PERP_SEX, PERP_RACE, X_COORD_CD, Y_COORD_CD, Latitude, Longitude, and a New Georeferenced Column.

### Intended Machine Learning Task:

The machine learning task is classification, predicting the law category (LAW_CAT_CD) based on the available features.

### Data Cleaning and Transformation Steps:

1. **Handling Missing Values:**
   - Identify and handle missing values in each column. Consider removal based on the extent of missing data.

2. **Outlier Detection and Treatment:**
   - Explore numerical columns for outliers and apply appropriate strategies to address them.

3. **Encoding Categorical Variables:**
   - Encode categorical variables (e.g., PERP_SEX, PERP_RACE).

4. **Date Transformation:**
   - Convert ARREST_DATE to datetime format and extract relevant temporal features.

5. **Geospatial Data Handling:**
   - Utilize Latitude and Longitude to derive meaningful features, considering conversion or distance calculations.

6. **Feature Scaling:**
   - Standardize or normalize numerical features to ensure consistent scales.

7. **Identify Dependent and Independent Variables:**
   - Define LAW_CAT_CD as the dependent variable and select relevant features as independent variables.


### **Warehouse_and_Retail_Sales Dataset:**

### Dataset  Description:

The dataset contains information on alcohol sales, featuring columns such as YEAR, MONTH, SUPPLIER, ITEM CODE, ITEM DESCRIPTION, ITEM TYPE, RETAIL SALES, RETAIL TRANSFERS, and WAREHOUSE SALES.

### Intended Machine Learning Task:

The machine learning task is regression, aiming to predict sales quantities (RETAIL SALES, WAREHOUSE SALES) based on various features.

### Data Cleaning and Transformation Steps:

1. **Handling Missing Values:**
   - Identify and address missing values in each column, considering imputation for numerical columns like RETAIL SALES and WAREHOUSE SALES.

2. **Outlier Detection and Treatment:**
   - Examine numerical columns for outliers, particularly in sales-related columns. Apply appropriate strategies to handle outliers.

3. **Encoding Categorical Variables:**
   - Encode categorical variables (SUPPLIER, ITEM TYPE) using one-hot encoding or label encoding, based on the number of categories.

4. **Feature Scaling:**
   - Standardize or normalize numerical features like RETAIL SALES and WAREHOUSE SALES to ensure consistent scales.

5. **Identify Dependent and Independent Variables:**
   - Define RETAIL SALES and WAREHOUSE SALES as dependent variables, with SUPPLIER, ITEM TYPE, and other relevant features as independent variables.
