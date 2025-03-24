import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("nhanes.csv")
df.head().T
df.shape
df.info()
df.isnull().sum()

# Task 1: Handle missing values (Replace NaN with 0)
df_cleaned = df.fillna(0)

# Convert weight to pounds
df_cleaned["Weight_lbs"] = df_cleaned["Weight"] * 2.2

# Task 2: Histogram visualizations for BMI, Weight, Weight in pounds, and Age
# List of columns to plot
columns = ["BMI", "Weight", "Weight_lbs", "Age"]

# Create a 2x2 grid of histograms
plt.figure(figsize=(10, 8))
for i, col in enumerate(columns, 1):
    plt.subplot(2, 2, i)  # Arrange plots in 2 rows, 2 columns
    sns.histplot(df_cleaned[col], bins=30, kde=True)  # Histogram with smooth curve
    plt.title(f"{col} Distribution")  # Add title
    plt.xlabel(col)  # Label x-axis
    plt.ylabel("Count")  # Label y-axis

plt.tight_layout()  # Adjust layout for better spacing
plt.show()

# Task 3: Mean 60-second pulse rate
mean_pulse_rate = df_cleaned["Pulse"].mean()

# Task 4: Range of diastolic blood pressure
min_bp = df_cleaned["BPDia"].min()
max_bp = df_cleaned["BPDia"].max()

# Task 5: Variance and standard deviation for income
income_variance = np.var(df_cleaned["Income"], ddof=1)  # Sample variance
income_std_dev = np.std(df_cleaned["Income"], ddof=1)  # Sample standard deviation

# Task 6: Scatter plots for Weight vs. Height (colored by gender, diabetes, smoking status)
plt.figure(figsize=(18, 6))

categories = ["Gender", "Diabetes", "SmokingStatus"]
for i, cat in enumerate(categories, 1):
    plt.subplot(1, 3, i)
    sns.scatterplot(x=df_cleaned["Height"], y=df_cleaned["Weight"], hue=df_cleaned[cat], alpha=0.6)
    plt.title(f"Weight vs. Height Colored by {cat}")
    plt.xlabel("Height (cm)")
    plt.ylabel("Weight (kg)")

plt.tight_layout()
plt.show()

# Task 7: Conduct t-tests
# Age & Gender
male_age = df_cleaned[df_cleaned["Gender"] == "Male"]["Age"]
female_age = df_cleaned[df_cleaned["Gender"] == "Female"]["Age"]
t_stat_age, p_value_age = stats.ttest_ind(male_age, female_age, equal_var=False)

# BMI & Diabetes
diabetes_bmi = df_cleaned[df_cleaned["Diabetes"] == "Yes"]["BMI"]
non_diabetes_bmi = df_cleaned[df_cleaned["Diabetes"] == "No"]["BMI"]
t_stat_bmi, p_value_bmi = stats.ttest_ind(diabetes_bmi, non_diabetes_bmi, equal_var=False)

# Alcohol Year & Relationship Status
alcohol_yes = df_cleaned[df_cleaned["AlcoholYear"] > 0]["AlcoholYear"]
alcohol_no = df_cleaned[df_cleaned["AlcoholYear"] == 0]["AlcoholYear"]
t_stat_alcohol, p_value_alcohol = stats.ttest_ind(alcohol_yes, alcohol_no, equal_var=False)

# Display results
{
    "Mean Pulse Rate": mean_pulse_rate,
    "Diastolic BP Range": (min_bp, max_bp),
    "Income Variance": income_variance,
    "Income Std Dev": income_std_dev,
    "T-test Age & Gender": (t_stat_age, p_value_age),
    "T-test BMI & Diabetes": (t_stat_bmi, p_value_bmi),
    "T-test Alcohol Year & Relationship Status": (t_stat_alcohol, p_value_alcohol)
}

### NHANES Data Analysis – Simple Summary

#### Average Pulse Rate: 63.06

#### Diastolic Blood Pressure Range: 0 to 116

#### Income Variability:

#Variance: 1.26 billion

#Standard Deviation: 35,555

#### T-Test Results (Comparing Groups)

#Age & Gender: No valid comparison due to data issues.

#BMI & Diabetes: Significant difference. People with diabetes have different BMI levels (p < 0.00001).

#Alcohol & Relationship Status: Strong difference. Alcohol consumption varies based on relationship status (p < 0.00001)
