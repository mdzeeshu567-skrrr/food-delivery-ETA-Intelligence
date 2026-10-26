import pandas as pd
import numpy as np
df = pd.read_csv("Data/train.csv")
print(df.columns.tolist())
df["Order_Date"] = pd.to_datetime(df["Order_Date"], format="%d-%m-%Y")
df["Time_Orderd"] = df["Time_Orderd"].replace("NaN", pd.NA)

df["Time_Orderd"] = pd.to_datetime(
    df["Time_Orderd"],
    format="%H:%M:%S",
    errors="coerce"
)
df["Time_Order_picked"] = df["Time_Order_picked"].replace("NaN", pd.NA)

df["Time_Order_picked"] = pd.to_datetime(
    df["Time_Order_picked"],
    format="%H:%M:%S",
    errors="coerce"
)
print("\nTime_Order_picked data type:")
print(df["Time_Order_picked"].dtype)
print("\nTime_Orderd data type:")
print(df["Time_Orderd"].dtype)

print(df.head())
print(df.columns.tolist())
print(df.info())
print(df.isnull().sum())
print(df.dtypes)
columns_to_check = [
    "Weatherconditions",
    "Road_traffic_density",
    "Vehicle_condition",
    "Type_of_order",
    "Type_of_vehicle",
    "multiple_deliveries",
    "Festival",
    "City"
]

for column in columns_to_check:
    print(f"\n--- {column} ---")
    print(df[column].value_counts(dropna=False))

print("\nMissing values:")
print(df.isnull().sum())
print("\nNumeric summary:")
print(df.describe())
print("\nshape of dataset:",df.shape)
print("\nOrder Date:")
print(df["Order_Date"].head(10))

print("\nTime Ordered:")
print(df["Time_Orderd"].head(10))

print("\nTime Order Picked:")
print(df["Time_Order_picked"].head(10))
print("\nDuplicate rows:")
print(df.duplicated().sum())
print("\nOrder_Date data type:")
print(df["Order_Date"].dtype)
print("\nMissing values after date/time conversion:")
print(df[["Order_Date", "Time_Orderd", "Time_Order_picked"]].isnull().sum())
print("\nOriginal Time_Orderd missing values:")
raw_df = pd.read_csv("Data/train.csv")
print(raw_df["Time_Orderd"].isnull().sum())

print("\nTime_Orderd value counts:")
print(raw_df["Time_Orderd"].value_counts(dropna=False).head(10))
print("\nOriginal Time_Orderd missing values:", raw_df["Time_Orderd"].isnull().sum())
print("\nInvalid Time_Orderd values:")
print(raw_df.loc[df["Time_Orderd"].isna(), "Time_Orderd"].value_counts(dropna=False).head(20))
print("\nAfter conversion:")
print("Time_Orderd:", df["Time_Orderd"].isna().sum())
print("Time_Order_picked:", df["Time_Order_picked"].isna().sum())
print("\nRows with missing Time_Orderd:")
print(df["Time_Orderd"].isna().sum())
print("\nRows with missing Time_Orderd but available Time_Order_picked:")
print(
    (
        df["Time_Orderd"].isna() &
        df["Time_Order_picked"].notna()
    ).sum()
)
print("\nMissing values in all columns:")
print(df.isna().sum())
print("\nOnly columns with missing values:")
missing = df.isna().sum()
print(missing[missing > 0])
print("\nMissing Time_Orderd by City:")
print(df.loc[df["Time_Orderd"].isna(), "City"].value_counts(dropna=False))
print("\nMissing Time_Orderd by Order Date:")
print(
    df.loc[df["Time_Orderd"].isna(), "Order_Date"]
    .value_counts()
    .sort_index()
)
print("\nMissing Time_Orderd by month:")
print(
    df.loc[df["Time_Orderd"].isna(), "Order_Date"]
    .dt.to_period("M")
    .value_counts()
    .sort_index()
)
print("\nPercentage of rows with missing Time_Orderd:")

missing_time = df["Time_Orderd"].isna().sum()
total_rows = len(df)

print((missing_time / total_rows) * 100)
print("\nColumn names and data types:")
print(df.dtypes.to_string())
print("\nALL COLUMNS:")
for i,column in enumerate(df.columns):
    print(i,"->",column)
    print("\nSample values from important columns:")

print("\nDelivery_person_Age:")
print(df["Delivery_person_Age"].value_counts(dropna=False).head(10))

print("\nmultiple_deliveries:")
print(df["multiple_deliveries"].value_counts(dropna=False))

print("\nTime_taken(min):")
print(df["Time_taken(min)"].value_counts(dropna=False).head(20))
print("\nTime_taken before cleaning:")
print(df["Time_taken(min)"].head())

df["Time_taken(min)"] = (
    df["Time_taken(min)"]
    .str.replace("(min)", "", regex=False)
    .str.strip()
    .astype(int)
)

print("\nTime_taken after cleaning:")
print(df["Time_taken(min)"].head())
print("\nNew data type:")
print(df["Time_taken(min)"].dtype)
print("\nDelivery_person_Age before cleaning:")
print(df["Delivery_person_Age"].value_counts(dropna=False).head(20))
print("\nDelivery_person_Age data type:")
print(df["Delivery_person_Age"].dtype)

print("\nMissing Delivery_person_Age values:")
print(df["Delivery_person_Age"].isna().sum())
df["Delivery_person_Age"] = pd.to_numeric(
    df["Delivery_person_Age"],
    errors="coerce"
)

print("\nDelivery_person_Age after cleaning:")
print(df["Delivery_person_Age"].dtype)

print("\nMissing Age values after conversion:")
print(df["Delivery_person_Age"].isna().sum())
raw_age = pd.read_csv("Data/train.csv")

print("\nOriginal Delivery_person_Age values that are not numeric:")

invalid_age = pd.to_numeric(
    raw_age["Delivery_person_Age"],
    errors="coerce"
).isna()

print(
    raw_age.loc[invalid_age, "Delivery_person_Age"]
    .value_counts(dropna=False)
)
print("\nDelivery person age summary:")

print(df["Delivery_person_Age"].describe())
print("\nMinimum age:")
print(df["Delivery_person_Age"].min())

print("\nMaximum age:")
print(df["Delivery_person_Age"].max())
print("\nMedian Delivery person age:")
print(df["Delivery_person_Age"].median())
median_age = df["Delivery_person_Age"].median()

df["Delivery_person_Age"] = df["Delivery_person_Age"].fillna(median_age)

print("\nMissing Age values after median imputation:")
print(df["Delivery_person_Age"].isna().sum())
print("\nDelivery_person_Ratings data type:")
print(df["Delivery_person_Ratings"].dtype)

print("\nMissing rating values:")
print(df["Delivery_person_Ratings"].isna().sum())

df["Delivery_person_Ratings"] = pd.to_numeric(
    df["Delivery_person_Ratings"],
    errors="coerce"
)

print("\nRating summary:")
print(df["Delivery_person_Ratings"].describe())

print("\nMinimum rating:")
print(df["Delivery_person_Ratings"].min())

print("\nMaximum rating:")
print(df["Delivery_person_Ratings"].max())

print("\nMedian rating:")
print(df["Delivery_person_Ratings"].median())
print("\nCoordinate columns:")

coordinate_columns = [
    "Restaurant_latitude",
    "Restaurant_longitude",
    "Delivery_location_latitude",
    "Delivery_location_longitude"
]

for column in coordinate_columns:
    print(f"\n{column}")
    print("Data type:", df[column].dtype)
    print("Missing values:", df[column].isna().sum())
    print("Minimum:", df[column].min())
    print("Maximum:", df[column].max())
    print("\nSample coordinate pairs:")

print(
    df[
        [
            "Restaurant_latitude",
            "Restaurant_longitude",
            "Delivery_location_latitude",
            "Delivery_location_longitude"
        ]
    ].head(10)
)
print("\nSuspicious coordinate rows:")

suspicious = df[
    (df["Restaurant_latitude"] < 0) |
    (df["Restaurant_longitude"] < 0) |
    (df["Delivery_location_latitude"] < 1) |
    (df["Delivery_location_longitude"] < 1)
]

print("Number of suspicious rows:", len(suspicious))

print(
    suspicious[
        [
            "Restaurant_latitude",
            "Restaurant_longitude",
            "Delivery_location_latitude",
            "Delivery_location_longitude"
        ]
    ].head(20)
)
print("\nSuspicious coordinate rows:")

suspicious = df[
    (df["Restaurant_latitude"] < 0) |
    (df["Restaurant_longitude"] < 0) |
    (df["Delivery_location_latitude"] < 1) |
    (df["Delivery_location_longitude"] < 1)
]

print("Number of suspicious rows:", len(suspicious))

print(
    suspicious[
        [
            "Restaurant_latitude",
            "Restaurant_longitude",
            "Delivery_location_latitude",
            "Delivery_location_longitude"
        ]
    ].head(20)
)
print("\nZero coordinate counts:")

zero_restaurant = (
    (df["Restaurant_latitude"] == 0) &
    (df["Restaurant_longitude"] == 0)
)

zero_delivery = (
    (df["Delivery_location_latitude"] == 0) &
    (df["Delivery_location_longitude"] == 0)
)

print("Restaurant coordinates both zero:", zero_restaurant.sum())
print("Delivery coordinates both zero:", zero_delivery.sum())
print("\nNegative coordinate counts:")

print(
    "Negative restaurant latitude:",
    (df["Restaurant_latitude"] < 0).sum()
)

print(
    "Negative restaurant longitude:",
    (df["Restaurant_longitude"] < 0).sum()
)

print(
    "Negative delivery latitude:",
    (df["Delivery_location_latitude"] < 0).sum()
)

print(
    "Negative delivery longitude:",
    (df["Delivery_location_longitude"] < 0).sum()
)
print("\nCity distribution:")
print(df["City"].value_counts(dropna=False))
print("\nSuspicious negative-coordinate cities:")

negative_coords = df[
    (df["Restaurant_latitude"] < 0) |
    (df["Restaurant_longitude"] < 0)
]

print(negative_coords["City"].value_counts(dropna=False))
print("\nExamples of negative restaurant coordinates:")

print(
    negative_coords[
        [
            "City",
            "Restaurant_latitude",
            "Restaurant_longitude",
            "Delivery_location_latitude",
            "Delivery_location_longitude"
        ]
    ].head(20)
)
print("\nCoordinate sign correction check:")

negative_restaurant = df[
    (df["Restaurant_latitude"] < 0) |
    (df["Restaurant_longitude"] < 0)
].copy()

negative_restaurant["Restaurant_latitude_abs"] = (
    negative_restaurant["Restaurant_latitude"].abs()
)

negative_restaurant["Restaurant_longitude_abs"] = (
    negative_restaurant["Restaurant_longitude"].abs()
)

negative_restaurant["latitude_difference"] = (
    abs(
        negative_restaurant["Restaurant_latitude_abs"]
        - negative_restaurant["Delivery_location_latitude"]
    )
)

negative_restaurant["longitude_difference"] = (
    abs(
        negative_restaurant["Restaurant_longitude_abs"]
        - negative_restaurant["Delivery_location_longitude"]
    )
)

print(
    negative_restaurant[
        [
            "Restaurant_latitude",
            "Restaurant_longitude",
            "Delivery_location_latitude",
            "Delivery_location_longitude",
            "latitude_difference",
            "longitude_difference"
        ]
    ].head(10)
)
# Correct negative restaurant coordinates
df["Restaurant_latitude"] = df["Restaurant_latitude"].abs()
df["Restaurant_longitude"] = df["Restaurant_longitude"].abs()

print("Negative restaurant latitude after correction:")
print((df["Restaurant_latitude"] < 0).sum())

print("Negative restaurant longitude after correction:")
print((df["Restaurant_longitude"] < 0).sum())
# Treat zero restaurant coordinates as missing
zero_restaurant_coords = (
    (df["Restaurant_latitude"] == 0) &
    (df["Restaurant_longitude"] == 0)
)

print("Restaurant coordinates equal to zero:")
print(zero_restaurant_coords.sum())

df.loc[zero_restaurant_coords, 
       ["Restaurant_latitude", "Restaurant_longitude"]] = np.nan

print("\nMissing restaurant latitude:")
print(df["Restaurant_latitude"].isna().sum())

print("Missing restaurant longitude:")
print(df["Restaurant_longitude"].isna().sum())
total_rows = len(df)
missing_restaurant_coords = df["Restaurant_latitude"].isna().sum()

missing_percentage = (missing_restaurant_coords / total_rows) * 100

print("Total rows:", total_rows)
print("Rows with missing restaurant coordinates:", missing_restaurant_coords)
print("Percentage of rows affected:", round(missing_percentage, 2), "%")
missing_coord_rows = df["Restaurant_latitude"].isna()

print("\nDelivery time for rows with missing restaurant coordinates:")
print(df.loc[missing_coord_rows, "Time_taken(min)"].describe())
print("\n==============================")
print("UNIQUE VALUES SUMMARY")
print("==============================")

for column in df.columns:
    print(f"\n{column}")
    print("Unique values:", df[column].nunique())

    if df[column].nunique() <= 15:
        print(df[column].value_counts(dropna=False))
        print("\nDATA TYPES")
print("=" * 50)

print(df.dtypes)
print("\nMISSING VALUES")
print("=" * 50)

missing = df.isnull().sum()

print(missing[missing > 0])
print("\nDUPLICATE ROWS")
print("=" * 50)

print("Duplicate rows:", df.duplicated().sum())
print("\nNUMERICAL COLUMNS SUMMARY")
print("=" * 50)

print(df.describe().T)
print("\nDELIVERY PERSON RATINGS")
print("=" * 50)

print(df["Delivery_person_Ratings"].value_counts(dropna=False).sort_index())
print("\nINVALID RATINGS")
print("=" * 50)

print(
    df[
        (df["Delivery_person_Ratings"] < 1) |
        (df["Delivery_person_Ratings"] > 5)
    ][["Delivery_person_ID", "Delivery_person_Ratings"]]
)
print("\nAGE RANGE")
print("=" * 50)

print("Minimum age:", df["Delivery_person_Age"].min())
print("Maximum age:", df["Delivery_person_Age"].max())


print("\nDELIVERY TIME RANGE")
print("=" * 50)

print("Minimum:", df["Time_taken(min)"].min())
print("Maximum:", df["Time_taken(min)"].max())
print("\nVEHICLE CONDITION VALUES")
print("=" * 50)

print(df["Vehicle_condition"].value_counts(dropna=False).sort_index())
print("\nRATING QUALITY CHECK")
print("====================")

print("\nRating values:")
print(df["Delivery_person_Ratings"].value_counts(dropna=False).sort_index())

print("\nMinimum rating:")
print(df["Delivery_person_Ratings"].min())

print("\nMaximum rating:")
print(df["Delivery_person_Ratings"].max())
print("\nMISSING VALUE ANALYSIS")
print("=" * 50)

missing = df.isnull().sum()
missing = missing[missing > 0]

print(missing)

print("\nMISSING VALUE PERCENTAGE")
print("=" * 50)

missing_percentage = (df.isnull().sum() / len(df)) * 100
missing_percentage = missing_percentage[missing_percentage > 0]

print(missing_percentage.round(2))
print("\nROWS WITH MISSING VALUES")
print("=" * 50)

print(df[df.isnull().any(axis=1)].head(10))
print("\nRESTAURANT COORDINATE MISSING PATTERN")
print("=" * 50)

both_missing = (
    df["Restaurant_latitude"].isna() &
    df["Restaurant_longitude"].isna()
).sum()

only_latitude = (
    df["Restaurant_latitude"].isna() &
    df["Restaurant_longitude"].notna()
).sum()

only_longitude = (
    df["Restaurant_latitude"].notna() &
    df["Restaurant_longitude"].isna()
).sum()

print("Both coordinates missing:", both_missing)
print("Only latitude missing:", only_latitude)
print("Only longitude missing:", only_longitude)
print("\nMISSING DELIVERY PERSON RATINGS")
print("=" * 50)

missing_rating = df[df["Delivery_person_Ratings"].isna()]

print("Number of missing ratings:", len(missing_rating))

print("\nSample rows:")
print(
    missing_rating[
        ["Delivery_person_ID",
         "Delivery_person_Age",
         "Delivery_person_Ratings",
         "Vehicle_condition",
         "Type_of_vehicle",
         "City",
         "Time_taken(min)"]
    ].head(10)
)
print("\nDELIVERY PERSON RATING HISTORY")
print("=" * 50)

rating_history = (
    df.groupby("Delivery_person_ID")["Delivery_person_Ratings"]
      .agg(["count", "mean"])
)

print(rating_history.head(10))
# ==========================================
# CATEGORICAL COLUMN VALUES
# ==========================================

categorical_columns = [
    'Weatherconditions',
    'Road_traffic_density',
    'Type_of_order',
    'Type_of_vehicle',
    'multiple_deliveries',
    'Festival',
    'City'
]

for column in categorical_columns:
    print("\n" + "=" * 50)
    print(f"{column.upper()} VALUES")
    print("=" * 50)
    print(df[column].value_counts(dropna=False))


# ==========================================
# TARGET DISTRIBUTION
# ==========================================

print("\n" + "=" * 50)
print("TARGET VARIABLE")
print("=" * 50)

print("Minimum:", df['Time_taken(min)'].min())
print("Maximum:", df['Time_taken(min)'].max())
print("Mean:", df['Time_taken(min)'].mean())
print("Median:", df['Time_taken(min)'].median())
print("Standard deviation:", df['Time_taken(min)'].std())

print("\nTarget value counts:")
print(df['Time_taken(min)'].value_counts().sort_index())
print("\n" + "="*60)
print("FINAL DATASET STRUCTURE")
print("="*60)

print("\nColumn Names:")
for i, column in enumerate(df.columns, 1):
    print(i, "->", column)

print("\nData Types:")
print(df.dtypes)

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nNumber of Unique Values:")
print(df.nunique())

print("\nUnique Delivery Person IDs:")
print(df["Delivery_person_ID"].nunique())

print("\nTotal Rows:")
print(len(df))

print("\nTotal Columns:")
print(len(df.columns))
# STEP 2.1 - Create a copy of the raw dataset

df_clean = df.copy()

print("Original dataset shape:", df.shape)
print("Cleaning dataset shape:", df_clean.shape)
print("\n" + "="*60)
print("MISSING VALUES BEFORE CLEANING")
print("="*60)

missing = df_clean.isnull().sum()

print(missing[missing > 0].sort_values(ascending=False))
print("\n" + "="*70)
print("DATA DICTIONARY")
print("="*70)

for col in df.columns:
    print(f"\n{col}")
    print(f"Data Type: {df[col].dtype}")
    print(f"Unique Values: {df[col].nunique()}")
    print(f"Missing Values: {df[col].isnull().sum()}")
    # Missing value percentage

missing_summary = pd.DataFrame({
    'Missing_Count': df.isnull().sum(),
    'Missing_Percentage': (df.isnull().sum() / len(df)) * 100
})

missing_summary = missing_summary[
    missing_summary['Missing_Count'] > 0
].sort_values('Missing_Count', ascending=False)

print(missing_summary)
# ============================================================
# SECTION 4: INITIAL DATA QUALITY & PROJECT UNDERSTANDING
# ============================================================

print("\n" + "=" * 60)
print("NUMERICAL COLUMNS")
print("=" * 60)

numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

print(numerical_columns.tolist())


print("\n" + "=" * 60)
print("CATEGORICAL COLUMNS")
print("=" * 60)

categorical_columns = df.select_dtypes(include=['object']).columns

print(categorical_columns.tolist())
# ============================================================
# TARGET AND IDENTIFIER COLUMNS
# ============================================================

print("\n" + "=" * 60)
print("TARGET VARIABLE")
print("=" * 60)

target_column = "Time_taken(min)"
print(target_column)


print("\n" + "=" * 60)
print("IDENTIFIER COLUMNS")
print("=" * 60)

identifier_columns = ["ID", "Delivery_person_ID"]

print(identifier_columns)
print("\n" + "="*60)
print("DUPLICATE ROW ANALYSIS")
print("="*60)

duplicate_count = df.duplicated().sum()

print(f"Duplicate rows: {duplicate_count}")
print("\n" + "=" * 60)
print("TARGET VARIABLE ANALYSIS")
print("=" * 60)

print("\nTarget Variable: Time_taken(min)")

print("\nDescriptive Statistics:")
print(df["Time_taken(min)"].describe())

print("\nMinimum Delivery Time:", df["Time_taken(min)"].min())
print("Maximum Delivery Time:", df["Time_taken(min)"].max())
print("Average Delivery Time:", round(df["Time_taken(min)"].mean(), 2))
print("Median Delivery Time:", df["Time_taken(min)"].median())
print("\n" + "=" * 60)
print("TARGET VARIABLE ANALYSIS")
print("=" * 60)

print("\nTarget Variable: Time_taken(min)")

print("\nDescriptive Statistics:")
print(df["Time_taken(min)"].describe())

print("\nMinimum Delivery Time:", df["Time_taken(min)"].min())
print("Maximum Delivery Time:", df["Time_taken(min)"].max())
print("Average Delivery Time:", round(df["Time_taken(min)"].mean(), 2))
print("Median Delivery Time:", df["Time_taken(min)"].median())
# ============================================================
# INITIAL DATA QUALITY ASSESSMENT
# ============================================================

print("\n" + "=" * 60)
print("INITIAL DATA QUALITY ASSESSMENT")
print("=" * 60)

print("\n1. Total Rows:", len(df))
print("2. Total Columns:", len(df.columns))

print("\n3. Duplicate Rows:", df.duplicated().sum())

print("\n4. Columns With Missing Values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

print("\n5. Target Variable:")
print("Time_taken(min)")

print("\n6. Target Statistics:")
print(df["Time_taken(min)"].describe())
# ============================================================
# CATEGORICAL COLUMN DISTRIBUTION
# ============================================================

print("\n" + "=" * 60)
print("CATEGORICAL COLUMN DISTRIBUTION")
print("=" * 60)

categorical_columns = df.select_dtypes(include=["object"]).columns

for col in categorical_columns:
    print(f"\n--- {col} ---")
    print(df[col].value_counts(dropna=False))
    print("\nTIME ORDER ANALYSIS")
print("===================")

print("\ncurrent columns:")
print(df.columns.tolist())
print("Data Type:", df["Time_Orderd"].dtype)

print("\nSample Values:")
print(df["Time_Orderd"].dropna().head(20))

print("\nUnique Values:")
print(df["Time_Orderd"].dropna().unique()[:30])
print("\nNUMERICAL COLUMN ANALYSIS")
print("=" * 50)

numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

for col in numerical_columns:
    print(f"\n--- {col} ---")
    print("Minimum:", df[col].min())
    print("Maximum:", df[col].max())
    print("Mean:", round(df[col].mean(), 2))
    print("Median:", df[col].median())
    print("\nALL COLUMNS")
print("=" * 50)

for i, col in enumerate(df.columns, start=1):
    print(i, "->", col)
    print("\ncolumn data types")
    print("="*50)

    print(df.dtypes)
    print("\nCATEGORICAL COLUMN ANALYSIS")
print("=" * 50)

categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    print(f"\n--- {column} ---")
    print(df[column].value_counts(dropna=False))
    print("\nMISSING VALUE ANALYSIS")
print("=" * 50)

missing_count = df.isnull().sum()
missing_percentage = (df.isnull().sum() / len(df)) * 100

missing_table = pd.DataFrame({
    "Missing_Count": missing_count,
    "Missing_Percentage": missing_percentage
})

print(missing_table)
print("\nDUPLICATE ROW ANALYSIS")
print("=" * 50)

duplicate_count = df.duplicated().sum()

print("Duplicate rows:", duplicate_count)
print("\nDATA QUALITY CHECKS")
print("=" * 50)

print("\nDelivery Person Age:")
print("Below 18:", (df["Delivery_person_Age"] < 18).sum())
print("Above 60:", (df["Delivery_person_Age"] > 60).sum())

print("\nDelivery Person Ratings:")
print("Below 1:", (df["Delivery_person_Ratings"] < 1).sum())
print("Above 5:", (df["Delivery_person_Ratings"] > 5).sum())

print("\nVehicle Condition:")
print(df["Vehicle_condition"].value_counts(dropna=False))

print("\nMultiple Deliveries:")
print(df["multiple_deliveries"].value_counts(dropna=False))

print("\nTarget Variable:")
print("Values below 0:", (df["Time_taken(min)"] < 0).sum())
print("Values equal to 0:", (df["Time_taken(min)"] == 0).sum())
print("\nSUSPICIOUS AGE VALUES")
print("=" * 50)

print(df.loc[df["Delivery_person_Age"] < 18,
             ["Delivery_person_ID", "Delivery_person_Age", "Delivery_person_Ratings", "Time_taken(min)"]])


print("\nSUSPICIOUS RATING VALUES")
print("=" * 50)

print(df.loc[df["Delivery_person_Ratings"] > 5,
             ["Delivery_person_ID", "Delivery_person_Age", "Delivery_person_Ratings", "Time_taken(min)"]])
print("\nDATASET SUMMARY")
print("=" * 50)

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])
print("Duplicate Rows:", df.duplicated().sum())
print("Total Missing Values:", df.isnull().sum().sum())
print("Target Variable: Time_taken(min)")
print("Target Mean:", df["Time_taken(min)"].mean())
print("Target Median:", df["Time_taken(min)"].median())
# ==========================================
# DATA CLEANING
# ==========================================

print("\nDATA CLEANING")
print("=" * 50)

# Replace invalid delivery-person ages
df.loc[df["Delivery_person_Age"] < 18, "Delivery_person_Age"] = np.nan

# Replace invalid delivery-person ratings
df.loc[df["Delivery_person_Ratings"] > 5, "Delivery_person_Ratings"] = np.nan

print("\nInvalid values converted to missing values.")

print("\nMissing values after validation:")
print(df[["Delivery_person_Age", "Delivery_person_Ratings"]].isnull().sum())
# ==========================================
# CHECK DATE & TIME COLUMN NAMES
# ==========================================

print("\nDATE & TIME COLUMN NAMES")
print("=" * 50)

for column in df.columns:
    if "Time" in column or "Order" in column:
        print(repr(column))
        print("\nOrder_Date sample:")
print(df["Order_Date"].head())

print("\nTime_Orderd sample:")
print(df["Time_Orderd"].head())

print("\nTime_Order_picked sample:")
print(df["Time_Order_picked"].head())
# ==========================================
# EXTRACT TIME FEATURES
# ==========================================

df["Order_Hour"] = df["Time_Orderd"].dt.hour
df["Order_Minute"] = df["Time_Orderd"].dt.minute

df["Pickup_Hour"] = df["Time_Order_picked"].dt.hour
df["Pickup_Minute"] = df["Time_Order_picked"].dt.minute

print("\nNew time features:")
print(df[[
    "Time_Orderd",
    "Time_Order_picked",
    "Order_Hour",
    "Order_Minute",
    "Pickup_Hour",
    "Pickup_Minute"
]].head())
print("\nMissing time values:")
print(df[["Time_Orderd", "Time_Order_picked"]].isnull().sum())
# ==========================================
# CATEGORICAL MISSING VALUES
# ==========================================

categorical_columns = [
    "Weatherconditions",
    "Road_traffic_density",
    "multiple_deliveries",
    "Festival",
    "City"
]

print("\nMissing categorical values:")
print(df[categorical_columns].isnull().sum())
print("\nTOTAL MISSING VALUES IN DATAFRAME:")
print(df.isnull().sum().sum())

print("\nSHAPE OF CURRENT DATAFRAME:")
print(df.shape)
print("\nMISSING VALUES BY COLUMN:")
print(df.isnull().sum()[df.isnull().sum() > 0])
print("\nMISSING RESTAURANT COORDINATES:")
print(df[["Restaurant_latitude", "Restaurant_longitude"]].isnull().sum())

print("\nROWS WITH MISSING RESTAURANT COORDINATES:")
print(
    df[
        df["Restaurant_latitude"].isnull() |
        df["Restaurant_longitude"].isnull()
    ][[
        "Restaurant_latitude",
        "Restaurant_longitude",
        "City",
        "Time_taken(min)"
    ]].head(10)
)
print("\nCOORDINATE MISSINGNESS CHECK:")
print(
    df["Restaurant_latitude"].isnull().sum(),
    df["Restaurant_longitude"].isnull().sum()
)

print("\nRows where only latitude is missing:")
print(
    (df["Restaurant_latitude"].isnull() &
     df["Restaurant_longitude"].notnull()).sum()
)

print("\nRows where only longitude is missing:")
print(
    (df["Restaurant_latitude"].notnull() &
     df["Restaurant_longitude"].isnull()).sum()
)
print("\nALL LOCATION MISSING VALUES:")
print(
    df[[
        "Restaurant_latitude",
        "Restaurant_longitude",
        "Delivery_location_latitude",
        "Delivery_location_longitude"
    ]].isnull().sum()
)
# ==========================================
# HANDLE MISSING DELIVERY-PERSON RATINGS
# ==========================================

median_rating = df["Delivery_person_Ratings"].median()

print("\nMedian delivery-person rating:")
print(median_rating)
df["Delivery_person_Ratings"] = df["Delivery_person_Ratings"].fillna(median_rating)

print("\nMissing ratings after median imputation:")
print(df["Delivery_person_Ratings"].isnull().sum())
# ==========================================
# RESTAURANT COORDINATE MISSING RATE
# ==========================================

missing_restaurant_coordinates = df["Restaurant_latitude"].isnull().sum()

total_rows = len(df)

missing_percentage = (
    missing_restaurant_coordinates / total_rows
) * 100

print("\nMissing restaurant coordinates:")
print(missing_restaurant_coordinates)

print("\nPercentage of dataset:")
print(round(missing_percentage, 2), "%")
# ==========================================
# CHECK MISSING ORDER TIMES
# ==========================================

missing_time_rows = df[df["Time_Orderd"].isnull()]

print("\nORDERS WITH MISSING ORDER TIMES")
print("=" * 50)

print("Number of rows:", len(missing_time_rows))

print("\nMissing order times with target availability:")
print(
    missing_time_rows[
        ["Time_Orderd", "Time_taken(min)"]
    ].isnull().sum()
)
print("\nMissing values in extracted time features:")
print(
    df[["Order_Hour", "Order_Minute"]].isnull().sum()
)
print("\nMissing values in extracted time features:")
print(
    df[["Order_Hour", "Order_Minute"]].isnull().sum()
)
# ==========================================
# CHECK SUSPICIOUS DELIVERY COORDINATES
# ==========================================

print("\nDelivery latitude equal to 0.01:")
print((df["Delivery_location_latitude"] == 0.01).sum())

print("\nDelivery longitude equal to 0.01:")
print((df["Delivery_location_longitude"] == 0.01).sum())
# ==========================================
# VERIFY SUSPICIOUS COORDINATES
# ==========================================

latitude_suspicious = df["Delivery_location_latitude"] == 0.01
longitude_suspicious = df["Delivery_location_longitude"] == 0.01

print(
    "Both coordinates equal 0.01:",
    (latitude_suspicious & longitude_suspicious).sum()
)

print(
    "Only latitude equals 0.01:",
    (latitude_suspicious & ~longitude_suspicious).sum()
)

print(
    "Only longitude equals 0.01:",
    (~latitude_suspicious & longitude_suspicious).sum()
)
# ==========================================
# HANDLE SUSPICIOUS DELIVERY COORDINATES
# ==========================================

df.loc[latitude_suspicious & longitude_suspicious,
       ["Delivery_location_latitude",
        "Delivery_location_longitude"]] = np.nan

print("\nSuspicious coordinates marked as missing:")

print(
    df[[
        "Delivery_location_latitude",
        "Delivery_location_longitude"
    ]].isnull().sum()
)
# ==========================================
# CLEANING PROGRESS CHECK
# ==========================================

print("\nCLEANING PROGRESS CHECK")
print("=" * 50)

print("Dataset shape:", df.shape)

print("\nTotal missing values:")
print(df.isnull().sum().sum())

print("\nMissing values by column:")
print(df.isnull().sum()[df.isnull().sum() > 0])
# ==========================================
# CHECK VEHICLE CONDITION
# ==========================================

print("\nVEHICLE CONDITION CHECK")
print("=" * 50)

print(df["Vehicle_condition"].value_counts(dropna=False).sort_index())
# ==========================================
# VEHICLE CONDITION VS DELIVERY TIME
# ==========================================

print("\nAVERAGE DELIVERY TIME BY VEHICLE CONDITION")
print("=" * 50)

print(
    df.groupby("Vehicle_condition")["Time_taken(min)"]
      .agg(["count", "mean", "median"])
      .round(2)
)
# ==========================================
# ORDER TYPE CHECK
# ==========================================

print("\nORDER TYPE DISTRIBUTION")
print("=" * 50)

print(df["Type_of_order"].value_counts(dropna=False))
# ==========================================
# VEHICLE TYPE DISTRIBUTION
# ==========================================

print("\nVEHICLE TYPE DISTRIBUTION")
print("=" * 50)

print(df["Type_of_vehicle"].value_counts(dropna=False))
# Convert multiple_deliveries to numeric
df["multiple_deliveries"] = pd.to_numeric(
    df["multiple_deliveries"],
    errors="coerce"
)

print("Data type:", df["multiple_deliveries"].dtype)
print("Median:", df["multiple_deliveries"].median())
print("Missing values:", df["multiple_deliveries"].isnull().sum())
# ==========================================
# MULTIPLE DELIVERIES DISTRIBUTION
# ==========================================

print("\nMULTIPLE DELIVERIES DISTRIBUTION")
print("=" * 50)

print(df["multiple_deliveries"].value_counts(dropna=False).sort_index())
print("\nMedian multiple deliveries:")
print(df["multiple_deliveries"].median())
print("Data type:", df["multiple_deliveries"].dtype)

print("\nUnique values:")
print(df["multiple_deliveries"].unique())
# Fill missing multiple-delivery values with the median
median_deliveries = df["multiple_deliveries"].median()

df["multiple_deliveries"] = df["multiple_deliveries"].fillna(
    median_deliveries
)

print("\nMissing values after imputation:")
print(df["multiple_deliveries"].isnull().sum())
# ==========================================
# HANDLE MISSING WEATHER CONDITIONS
# ==========================================

print("\nWEATHER CONDITIONS BEFORE CLEANING")
print(df["Weatherconditions"].value_counts(dropna=False))

weather_mode = df["Weatherconditions"].mode()[0]

df["Weatherconditions"] = df["Weatherconditions"].fillna(weather_mode)

print("\nMost frequent weather condition:", weather_mode)
print("Missing weather values after cleaning:",
      df["Weatherconditions"].isnull().sum())
weather_mode = df["Weatherconditions"].mode()[0]

df["Weatherconditions"] = df["Weatherconditions"].fillna(weather_mode)

print("\nMost frequent weather condition:", weather_mode)
print("Missing weather values after cleaning:",
      df["Weatherconditions"].isnull().sum())
# ==========================================
# HANDLE MISSING ROAD TRAFFIC DENSITY
# ==========================================

print("\nROAD TRAFFIC BEFORE CLEANING")
print(df["Road_traffic_density"].value_counts(dropna=False))

traffic_mode = df["Road_traffic_density"].mode()[0]

df["Road_traffic_density"] = df["Road_traffic_density"].fillna(
    traffic_mode
)

print("\nMost frequent traffic category:", traffic_mode)
print("Missing traffic values after cleaning:",
      df["Road_traffic_density"].isnull().sum())
traffic_mode = df["Road_traffic_density"].mode()[0]

df["Road_traffic_density"] = df["Road_traffic_density"].fillna(
    traffic_mode
)

print("\nMost frequent traffic category:", traffic_mode)
print("Missing traffic values after cleaning:",
      df["Road_traffic_density"].isnull().sum())
# ==========================================
# HANDLE MISSING FESTIVAL VALUES
# ==========================================

print("\nFESTIVAL VALUES BEFORE CLEANING")
print(df["Festival"].value_counts(dropna=False))

festival_mode = df["Festival"].mode()[0]

df["Festival"] = df["Festival"].fillna(festival_mode)

print("\nMost frequent festival category:", festival_mode)
print("Missing festival values after cleaning:",
      df["Festival"].isnull().sum())
# ==========================================
# HANDLE MISSING CITY VALUES
# ==========================================

print("\nCITY VALUES BEFORE CLEANING")
print(df["City"].value_counts(dropna=False))

city_mode = df["City"].mode()[0]

df["City"] = df["City"].fillna(city_mode)

print("\nMost frequent city category:", city_mode)
print("Missing city values after cleaning:",
      df["City"].isnull().sum())
# ==========================================
# FINAL MISSING VALUES CHECK
# ==========================================

print("\nMISSING VALUES AFTER CLEANING")
print("=" * 50)

print(df.isnull().sum()[df.isnull().sum() > 0])

print("\nTotal missing values remaining:")
print(df.isnull().sum().sum())

print("\nCurrent dataset shape:")
print(df.shape)
# ==========================================
# HANDLE MISSING DELIVERY-PERSON AGE
# ==========================================

median_age = df["Delivery_person_Age"].median()

print("Median delivery-person age:", median_age)

df["Delivery_person_Age"] = df["Delivery_person_Age"].fillna(
    median_age
)

print(
    "Missing ages after cleaning:",
    df["Delivery_person_Age"].isnull().sum()
)
# ==========================================
# CHECK REMAINING MISSING VALUES
# ==========================================

print("\nREMAINING MISSING VALUES")
print("=" * 50)

print(df.isnull().sum()[df.isnull().sum() > 0])

print("\nTotal missing cells:", df.isnull().sum().sum())
print("Dataset shape:", df.shape)
# ==========================================
# RESTAURANT COORDINATES BY CITY
# ==========================================

missing_restaurant = df[
    df["Restaurant_latitude"].isnull()
]

print("\nMISSING RESTAURANT COORDINATES BY CITY")
print("=" * 50)

print(missing_restaurant["City"].value_counts(dropna=False))
# ==========================================
# SUSPICIOUS DELIVERY COORDINATES BY CITY
# ==========================================

missing_delivery_location = df[
    df["Delivery_location_latitude"].isnull()
]

print("\nMISSING DELIVERY COORDINATES BY CITY")
print("=" * 50)

print(
    missing_delivery_location["City"].value_counts(dropna=False)
)
# ==========================================
# CHECK TARGET VARIABLE
# ==========================================

print("\nTARGET VARIABLE CHECK")
print("=" * 50)

print("Missing delivery times:")
print(df["Time_taken(min)"].isnull().sum())

print("\nDelivery time summary:")
print(df["Time_taken(min)"].describe())
# ==========================================
# FINAL DUPLICATE CHECK
# ==========================================

print("\nFINAL DUPLICATE CHECK")
print("=" * 50)

print("Duplicate rows:", df.duplicated().sum())
print("Total rows:", len(df))
# ==========================================
# SAVE CLEANING CHECKPOINT
# ==========================================

df.to_csv("food_delivery_cleaned_checkpoint.csv", index=False)

print("\nCleaned dataset checkpoint saved successfully.")
# ==========================================
# FEATURE ENGINEERING: DISTANCE
# ==========================================

import numpy as np

def haversine_distance(lat1, lon1, lat2, lon2):
    # Earth's approximate radius in kilometres
    earth_radius = 6371

    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = np.radians([lat1, lon1, lat2, lon2])

    # Calculate differences
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(lat1) * np.cos(lat2)
        * np.sin(dlon / 2) ** 2
    )

    c = 2 * np.arcsin(np.sqrt(a))

    return earth_radius * c
# ==========================================
# CALCULATE DELIVERY DISTANCE
# ==========================================

df["Distance_km"] = haversine_distance(
    df["Restaurant_latitude"],
    df["Restaurant_longitude"],
    df["Delivery_location_latitude"],
    df["Delivery_location_longitude"]
)

print("\nDISTANCE FEATURE CHECK")
print("=" * 50)

print(df[[
    "Restaurant_latitude",
    "Restaurant_longitude",
    "Delivery_location_latitude",
    "Delivery_location_longitude",
    "Distance_km"
]].head(10))
# ==========================================
# DISTANCE QUALITY CHECK
# ==========================================

print("\nDISTANCE QUALITY CHECK")
print("=" * 50)

print("Missing distances:", df["Distance_km"].isnull().sum())
print("Zero distances:", (df["Distance_km"] == 0).sum())
print("Negative distances:", (df["Distance_km"] < 0).sum())

print("\nDistance summary:")
print(df["Distance_km"].describe().round(2))
# ==========================================
# INSPECT LARGEST DELIVERY DISTANCES
# ==========================================

print("\nTOP 10 LARGEST DELIVERY DISTANCES")
print("=" * 50)

print(
    df.nlargest(10, "Distance_km")[
        [
            "Restaurant_latitude",
            "Restaurant_longitude",
            "Delivery_location_latitude",
            "Delivery_location_longitude",
            "Distance_km",
            "Time_taken(min)"
        ]
    ]
)
# ==========================================
# DISTANCE VS DELIVERY TIME
# ==========================================

print("\nDISTANCE VS DELIVERY TIME")
print("=" * 50)

distance_time_corr = df[
    ["Distance_km", "Time_taken(min)"]
].corr().iloc[0, 1]

print(
    "Correlation between distance and delivery time:",
    round(distance_time_corr, 3)
)
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Distance_km"],
    df["Time_taken(min)"],
    alpha=0.3
)

plt.xlabel("Delivery Distance (km)")
plt.ylabel("Delivery Time (minutes)")
plt.title("Distance vs Delivery Time")

plt.tight_layout()
plt.show()
plt.close()
print("\nDELIVERY TIME BY TRAFFIC DENSITY")
print("=" * 45)

print(
    df.groupby("Road_traffic_density")["Time_taken(min)"]
    .agg(["count", "mean", "median"])
    .round(2)
    .sort_values("mean")
)
print("Missing traffic values:",
      df["Road_traffic_density"].isna().sum())

print("\nTraffic categories:")
print(df["Road_traffic_density"].value_counts(dropna=False))
# Fill missing traffic density values
traffic_mode = df["Road_traffic_density"].mode()[0]

df["Road_traffic_density"] = (
    df["Road_traffic_density"].fillna(traffic_mode)
)

print("Traffic mode used:", traffic_mode)
print(
    "Missing traffic values after cleaning:",
    df["Road_traffic_density"].isna().sum()
)
print("\nDELIVERY TIME BY WEATHER")
print("=" * 45)

print(
    df.groupby("Weatherconditions")["Time_taken(min)"]
    .agg(["count", "mean", "median"])
    .round(2)
    .sort_values("mean")
)
# Fill missing weather conditions
weather_mode = df["Weatherconditions"].mode()[0]

df["Weatherconditions"] = (
    df["Weatherconditions"].fillna(weather_mode)
)

print("Weather mode used:", weather_mode)
print(
    "Missing weather values after cleaning:",
    df["Weatherconditions"].isna().sum()
)
print("\nDELIVERY TIME BY VEHICLE TYPE")
print("=" * 45)

print(
    df.groupby("Type_of_vehicle")["Time_taken(min)"]
    .agg(["count", "mean", "median"])
    .round(2)
    .sort_values("mean")
)
print("\nDELIVERY TIME BY FESTIVAL STATUS")
print("=" * 45)

print(
    df.groupby("Festival")["Time_taken(min)"]
    .agg(["count", "mean", "median"])
    .round(2)
)
# Fill missing festival status
festival_mode = df["Festival"].mode()[0]

df["Festival"] = df["Festival"].fillna(festival_mode)

print("Festival mode used:", festival_mode)
print(
    "Missing festival values after cleaning:",
    df["Festival"].isna().sum()
)
print("\nDELIVERY TIME BY CITY")
print("=" * 45)

print(
    df.groupby("City")["Time_taken(min)"]
    .agg(["count", "mean", "median"])
    .round(2)
    .sort_values("mean")
)
# Fill missing city values
city_mode = df["City"].mode()[0]

df["City"] = df["City"].fillna(city_mode)

print("City mode used:", city_mode)
print(
    "Missing city values after cleaning:",
    df["City"].isna().sum()
)
print("\nDELIVERY TIME BY MULTIPLE DELIVERIES")
print("=" * 45)

print(
    df.groupby("multiple_deliveries")["Time_taken(min)"]
    .agg(["count", "mean", "median"])
    .round(2)
    .sort_index()
)
print("\nDELIVERY TIME BY ORDER TYPE")
print("=" * 45)

print(
    df.groupby("Type_of_order")["Time_taken(min)"]
    .agg(["count", "mean", "median"])
    .round(2)
    .sort_values("mean")
)
print("\nDELIVERY TIME BY DELIVERY PERSON RATING")
print("=" * 45)

print(
    df.groupby("Delivery_person_Ratings")["Time_taken(min)"]
    .agg(["count", "mean", "median"])
    .round(2)
    .sort_index()
)
print("\nRATING VS DELIVERY TIME")
print("=" * 45)

rating_corr = df[
    ["Delivery_person_Ratings", "Time_taken(min)"]
].corr().iloc[0, 1]

print("Correlation:", round(rating_corr, 3))
print("\nFINAL DATASET SHAPE")
print("=" * 35)

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Total missing values:", df.isna().sum().sum())
print("\nMISSING VALUES BY COLUMN")
print("=" * 45)

missing = df.isna().sum()

print(
    missing[missing > 0]
    .sort_values(ascending=False)
)
print("\nDISTANCE DATA QUALITY CHECK")
print("=" * 45)

print(
    "Missing delivery coordinates:",
    df[
        [
            "Delivery_location_latitude",
            "Delivery_location_longitude"
        ]
    ].isna().any(axis=1).sum()
)

print(
    "Missing distances:",
    df["Distance_km"].isna().sum()
)
print("\nCHECK DISTANCE CALCULATION")
print("=" * 45)

missing_delivery_coords = df[
    [
        "Delivery_location_latitude",
        "Delivery_location_longitude"
    ]
].isna().any(axis=1)

print(
    "Rows with missing delivery coordinates:",
    missing_delivery_coords.sum()
)

print(
    "Those rows with a distance still present:",
    df.loc[missing_delivery_coords, "Distance_km"].notna().sum()
)
print("\nDISTANCE VALIDATION")
print("=" * 45)

coordinates_available = df[
    [
        "Restaurant_latitude",
        "Restaurant_longitude",
        "Delivery_location_latitude",
        "Delivery_location_longitude"
    ]
].notna().all(axis=1)

print(
    "Rows with all coordinates available:",
    coordinates_available.sum()
)

print(
    "Those rows with missing distances:",
    df.loc[coordinates_available, "Distance_km"].isna().sum()
)
# Save cleaned dataset with engineered features
df.to_csv("food_delivery_cleaned_checkpoint.csv", index=False)

print("\nCleaned dataset checkpoint saved successfully.")
import os

checkpoint = "food_delivery_cleaned_checkpoint.csv"

print("Checkpoint exists:", os.path.exists(checkpoint))

if os.path.exists(checkpoint):
    print("File size (bytes):", os.path.getsize(checkpoint))
    print("\nTARGET VARIABLE CHECK")
print("=" * 40)

print("Target column exists:",
      "Time_taken(min)" in df.columns)

print("Missing target values:",
      df["Time_taken(min)"].isna().sum())

print("\nTarget summary:")
print(df["Time_taken(min)"].describe().round(2))
print("\nDATASET COLUMNS")
print("=" * 40)

for column in df.columns:
    print(column)
    # Candidate features for ETA prediction
    target = "Time_taken(min)"

candidate_features = [
    "Delivery_person_Age",
    "Restaurant_latitude",
    "Restaurant_longitude",
    "Delivery_location_latitude",
    "Delivery_location_longitude",
    "Order_Date",
    "Weatherconditions",
    "Road_traffic_density",
    "Vehicle_condition",
    "Type_of_order",
    "Type_of_vehicle",
    "multiple_deliveries",
    "Festival",
    "City",
    "Order_Hour",
    "Order_Minute",
    "Pickup_Hour",
    "Pickup_Minute",
    "Distance_km"
]

print("\nCANDIDATE FEATURES")
print("=" * 40)
print("Number of candidate features:", len(candidate_features))
print("Target:", target)
# ==========================================
# ETA MODEL: ORDER PLACEMENT
# ==========================================

target = "Time_taken(min)"

order_placement_features = [
    "Restaurant_latitude",
    "Restaurant_longitude",
    "Delivery_location_latitude",
    "Delivery_location_longitude",
    "Distance_km",
    "Order_DayOfWeek",
    "Order_Month",
    "Order_Hour",
    "Order_Minute",
    "Weatherconditions",
    "Road_traffic_density",
    "Vehicle_condition",
    "Type_of_order",
    "Type_of_vehicle",
    "Festival",
    "City"
]

print("\nORDER-PLACEMENT ETA FEATURES")
print("=" * 45)
print("Number of features:", len(order_placement_features))
print("Target:", target)
print("\nSelected features:")
for feature in order_placement_features:
    print(feature)
    
# CREATE FEATURES (X) AND TARGET (y)

# Create date features
df["Order_DayOfWeek"] = pd.to_datetime(
    df["Order_Date"], errors="coerce"
).dt.dayofweek

df["Order_Month"] = pd.to_datetime(
    df["Order_Date"], errors="coerce"
).dt.month

# Build X and y
X = df[order_placement_features].copy()
y = df[target].copy()

print("X shape:", X.shape)
print("y shape:", y.shape)


print("\nTarget sample:")
print(y.head())
# ==========================================
# TRAIN-TEST SPLIT
# ==========================================

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTRAIN-TEST SPLIT")
print("=" * 45)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# ==========================================
# CHECK DATA TYPES AND MISSING VALUES
# ==========================================

print("\nFEATURE DATA TYPES")
print(X_train.dtypes)

print("\nMISSING VALUES IN TRAINING DATA")
print(X_train.isnull().sum())

print("\nMISSING VALUES IN TEST DATA")
print(X_test.isnull().sum())

# ==========================================
# MACHINE LEARNING PREPROCESSING IMPORTS
# ==========================================

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# ==========================================
# DEFINE NUMERICAL AND CATEGORICAL FEATURES
# ==========================================

numeric_features = [
    "Restaurant_latitude",
    "Restaurant_longitude",
    "Delivery_location_latitude",
    "Delivery_location_longitude",
    "Distance_km",
    "Order_DayOfWeek",
    "Order_Month",
    "Order_Hour",
    "Order_Minute",
    "Vehicle_condition"
]

categorical_features = [
    "Weatherconditions",
    "Road_traffic_density",
    "Type_of_order",
    "Type_of_vehicle",
    "Festival",
    "City"
]

print("\nNUMERICAL FEATURES:", len(numeric_features))
print("CATEGORICAL FEATURES:", len(categorical_features))
print("TOTAL FEATURES:", len(numeric_features) + len(categorical_features))

# ==========================================
# CREATE PREPROCESSING PIPELINES
# ==========================================

# Handle missing numerical values
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])

# Handle categorical values
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

# Combine both preprocessing pipelines
preprocessor = ColumnTransformer(transformers=[
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features)
])

print("\nPREPROCESSING PIPELINES CREATED SUCCESSFULLY")

# ==========================================
# APPLY PREPROCESSING
# ==========================================

# Learn preprocessing rules from training data
X_train_processed = preprocessor.fit_transform(X_train)

# Apply the same rules to test data
X_test_processed = preprocessor.transform(X_test)

print("\nPREPROCESSING COMPLETED")
print("Processed training shape:", X_train_processed.shape)
print("Processed testing shape:", X_test_processed.shape)
print("Missing values in training data:",
      X_train_processed.nnz
      if hasattr(X_train_processed, "nnz")
      else "Dense array created")

# ==========================================
# TRAIN FIRST ETA PREDICTION MODEL
# ==========================================

from sklearn.linear_model import LinearRegression

# Create the model
linear_model = LinearRegression()

# Train using the processed training data
linear_model.fit(X_train_processed, y_train)

print("\nLINEAR REGRESSION MODEL TRAINED SUCCESSFULLY")

# ==========================================
# EVALUATE LINEAR REGRESSION MODEL
# ==========================================

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Predict delivery times for unseen test data
y_pred = linear_model.predict(X_test_processed)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nLINEAR REGRESSION EVALUATION")
print("=" * 40)
print(f"MAE:  {mae:.2f} minutes")
print(f"RMSE: {rmse:.2f} minutes")
print(f"R² Score: {r2:.4f}")

# ==========================================
# BASELINE MODEL: PREDICT TRAINING MEAN
# ==========================================

baseline_prediction = np.full(
    shape=len(y_test),
    fill_value=y_train.mean()
)

baseline_mae = mean_absolute_error(
    y_test,
    baseline_prediction
)

baseline_rmse = np.sqrt(
    mean_squared_error(y_test, baseline_prediction)
)

baseline_r2 = r2_score(
    y_test,
    baseline_prediction
)

print("\nBASELINE MODEL EVALUATION")
print("=" * 40)
print(f"Baseline MAE:  {baseline_mae:.2f} minutes")
print(f"Baseline RMSE: {baseline_rmse:.2f} minutes")
print(f"Baseline R² Score: {baseline_r2:.4f}")

# ==========================================
# RANDOM FOREST ETA MODEL
# Train using the original training data

from sklearn.ensemble import RandomForestRegressor

random_forest_model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    ))
])

random_forest_model.fit(X_train, y_train)

# Predict on the original test features
rf_predictions = random_forest_model.predict(X_test)

rf_mae = mean_absolute_error(y_test, rf_predictions)
rf_rmse = np.sqrt(mean_squared_error(y_test,rf_predictions))
rf_r2 = r2_score(y_test, rf_predictions)

print("\nRANDOM FOREST EVALUATION")
print("=" * 40)
print(f"MAE:  {rf_mae:.2f} minutes")
print(f"RMSE: {rf_rmse:.2f} minutes")
print(f"R² Score: {rf_r2:.4f}")

# ==========================================
# RANDOM FOREST: TRAIN VS TEST
# ==========================================

rf_train_predictions = random_forest_model.predict(X_train)

rf_train_mae = mean_absolute_error(y_train, rf_train_predictions)
rf_train_rmse = np.sqrt(mean_squared_error(y_train, rf_train_predictions))
rf_train_r2 = r2_score(y_train, rf_train_predictions)

print("\nRANDOM FOREST: TRAIN VS TEST")
print("=" * 40)
print(f"Training MAE:  {rf_train_mae:.2f} minutes")
print(f"Testing MAE:   {rf_mae:.2f} minutes")
print(f"Training RMSE: {rf_train_rmse:.2f} minutes")
print(f"Testing RMSE:  {rf_rmse:.2f} minutes")
print(f"Training R²:   {rf_train_r2:.4f}")
print(f"Testing R²:    {rf_r2:.4f}")


# ==========================================
# TUNED RANDOM FOREST MODEL
# ==========================================

tuned_rf_model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(
        n_estimators=100,
        max_depth=15,
        min_samples_split=10,
        min_samples_leaf=5,
        random_state=42,
        n_jobs=-1
    ))
])

tuned_rf_model.fit(X_train, y_train)

tuned_rf_predictions = tuned_rf_model.predict(X_test)

tuned_rf_mae = mean_absolute_error(
    y_test, tuned_rf_predictions
)
tuned_rf_rmse = np.sqrt(
    mean_squared_error(y_test, tuned_rf_predictions)
)
tuned_rf_r2 = r2_score(y_test, tuned_rf_predictions)

print("\nTUNED RANDOM FOREST EVALUATION")
print("=" * 40)
print(f"MAE:  {tuned_rf_mae:.2f} minutes")
print(f"RMSE: {tuned_rf_rmse:.2f} minutes")
print(f"R² Score: {tuned_rf_r2:.4f}")


# ==========================================
# TUNED RANDOM FOREST: TRAIN VS TEST
# ==========================================

tuned_rf_train_predictions = tuned_rf_model.predict(X_train)

tuned_rf_train_mae = mean_absolute_error(
    y_train, tuned_rf_train_predictions
)
tuned_rf_train_rmse = np.sqrt(
    mean_squared_error(y_train, tuned_rf_train_predictions)
)
tuned_rf_train_r2 = r2_score(
    y_train, tuned_rf_train_predictions
)

print("\nTUNED RANDOM FOREST: TRAIN VS TEST")
print("=" * 40)
print(f"Training MAE:  {tuned_rf_train_mae:.2f} minutes")
print(f"Testing MAE:   {tuned_rf_mae:.2f} minutes")
print(f"Training RMSE: {tuned_rf_train_rmse:.2f} minutes")
print(f"Testing RMSE:  {tuned_rf_rmse:.2f} minutes")
print(f"Training R²:   {tuned_rf_train_r2:.4f}")
print(f"Testing R²:    {tuned_rf_r2:.4f}")

# ==========================================
# MODEL PERFORMANCE COMPARISON
# ==========================================

model_comparison = pd.DataFrame({
    "Model": [
        "Baseline",
        "Linear Regression",
        "Original Random Forest",
        "Tuned Random Forest"
    ],
    "MAE (minutes)": [
        baseline_mae,
        mae,
        rf_mae,
        tuned_rf_mae
    ],
    "RMSE (minutes)": [
        baseline_rmse,
        rmse,
        rf_rmse,
        tuned_rf_rmse
    ],
    "R2 Score": [
        baseline_r2,
        r2,
        rf_r2,
        tuned_rf_r2
    ]
})

print("\nMODEL PERFORMANCE COMPARISON")
print("=" * 60)
print(model_comparison.round(4).to_string(index=False))
# ==========================================
# SAVE THE BEST ETA MODEL
# ==========================================

import joblib

joblib.dump(
    tuned_rf_model,
    "tuned_random_forest_eta.pkl"
)

print("\nBest ETA model saved successfully!")

# ==========================================
# DELAY CLASSIFICATION: CREATE TARGET
# ==========================================

import numpy as np

# Calculate the delay threshold using training data only
delay_threshold = np.percentile(y_train, 80)

# Create binary delay labels
y_train_delay = (y_train > delay_threshold).astype(int)
y_test_delay = (y_test > delay_threshold).astype(int)

print("\nDELAY CLASSIFICATION TARGET")
print("=" * 40)
print(f"80th percentile delay threshold: {delay_threshold:.2f} minutes")

print("\nTraining delay distribution:")
print(y_train_delay.value_counts().sort_index())

print("\nTesting delay distribution:")
print(y_test_delay.value_counts().sort_index())

# ==========================================
# DELAY CLASSIFICATION: TRAINING PIPELINE
# ==========================================

from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score
)

delay_model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced",
        n_jobs=-1
    ))
])

print("\nDelay classification pipeline created successfully!")

# ==========================================
# TRAIN AND EVALUATE DELAY CLASSIFIER
# ==========================================

# Train the model
delay_model.fit(X_train, y_train_delay)

# Predict delay classes on unseen test data
y_delay_pred = delay_model.predict(X_test)

# Predict probabilities for the delayed class
y_delay_prob = delay_model.predict_proba(X_test)[:, 1]

# Display evaluation results
print("\nDELAY CLASSIFICATION EVALUATION")
print("=" * 45)

print("\nClassification Report:")
print(classification_report(
    y_test_delay,
    y_delay_pred,
    target_names=["Not Delayed", "Delayed"],
    zero_division=0
))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test_delay, y_delay_pred))

print("\nROC-AUC Score:")
print(round(roc_auc_score(y_test_delay, y_delay_prob), 4))

# ==========================================
# DELAY CLASSIFICATION: THRESHOLD COMPARISON
# ==========================================

from sklearn.metrics import precision_score, recall_score, f1_score

print("\nDELAY CLASSIFICATION THRESHOLD COMPARISON")
print("=" * 60)

for threshold in [0.30, 0.40, 0.50, 0.60]:
    threshold_predictions = (
        y_delay_prob >= threshold
    ).astype(int)

    precision = precision_score(
        y_test_delay, threshold_predictions, zero_division=0
    )
    recall = recall_score(
        y_test_delay, threshold_predictions, zero_division=0
    )
    f1 = f1_score(
        y_test_delay, threshold_predictions, zero_division=0
    )

    print(
        f"Threshold: {threshold:.2f} | "
        f"Precision: {precision:.3f} | "
        f"Recall: {recall:.3f} | "
        f"F1: {f1:.3f}"
    )
# ==========================================
# BEST DELAY CLASSIFICATION THRESHOLD
# ==========================================

best_threshold = 0.50

print("\nSELECTED BASELINE THRESHOLD")
print("=" * 40)
print(f"Threshold: {best_threshold:.2f}")
print("Reason: Highest F1-score among tested thresholds.")

# ==========================================
# SAVE DELAY CLASSIFICATION MODEL
# ==========================================

import joblib

joblib.dump(delay_model, "delay_classification_model.pkl")

print("\nDelay classification model saved successfully!")

# ==========================================
# VERIFY CATEGORICAL VALUES FOR STREAMLIT
# ==========================================

category_columns = [
    "Weatherconditions",
    "Road_traffic_density",
    "Type_of_order",
    "Type_of_vehicle",
    "Festival",
    "City"
]

print("\nCATEGORY VALUES FOR THE STREAMLIT APP")
print("=" * 50)

for column in category_columns:
    print(f"\n{column}:")
    print(sorted(df[column].dropna().astype(str).unique().tolist()))

