This project focuses on handling missing revenue data for the take home analysis task. Missing values were addressed using regression imputation, a method I have successfully applied in past projects. Given the importance of accurate and reliable data for financial decision-making, this approach provided an ideal solution in this scenario. The code ensures that negative revenue values, assumed to be input errors, are treated as nulls and appropriately imputed.

The script performs the following steps:

Data Preparation:
- Reads the dataset and identifies missing or invalid (negative) revenue values.
- Treats negative values as nulls, assuming that revenue is gross revenue.

Regression Imputation:
- For each missing value, a regression model is trained on the existing data for that company.
- Predictors include other non-missing revenue years for the same company.
- The model predicts the missing revenue value, which is then filled in.

The script also ensures that at least two non-missing predictors are available before applying regression. 

The cleaned dataset with missing values imputed is exported and this is what I used for the rest of my analysis.



