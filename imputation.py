from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

file_path = '/Users/seanjackson/Downloads/Extended_Industry_Performance_Data.xlsx'
df = pd.read_excel(file_path)

# Replace negative values with null
df['Year 2 Revenue ($M)'] = df['Year 2 Revenue ($M)'].apply(lambda x: np.nan if x < 0 else x)

# Columns for dynamic regression imputation
columns = ['Year 1 Revenue ($M)', 'Year 2 Revenue ($M)', 'Year 3 Revenue ($M)', 'Year 4 Revenue ($M)',
           'Year 5 Revenue ($M)']

for col in columns:
    # Rows where current column is missing
    missing_rows = df[df[col].isnull()]

    for idx, row in missing_rows.iterrows():
        # The predictors for columns with missing values will be other revenue columns for the same row
        predictors = [c for c in columns if c != col and not pd.isnull(row[c])]
        if len(predictors) < 2:
            continue

        # training data
        # drop rows with missing predictors
        train_data = df.dropna(subset=predictors + [col])
        X_train = train_data[predictors]
        y_train = train_data[col]

        # make sure there are enough rows to train the regression model
        if len(X_train) < 2:
            continue

        # Prepare test data as a df
        X_test = pd.DataFrame([row[predictors]], columns=predictors)

        # Train regression model
        reg = LinearRegression()
        reg.fit(X_train, y_train)

        # Predict missing values
        predicted_value = reg.predict(X_test)

        # Fill in missing values
        df.at[idx, col] = predicted_value[0]

output_path = '/Users/seanjackson/Downloads/Cleaned_Data.xlsx'
df.to_excel(output_path, index=False)
