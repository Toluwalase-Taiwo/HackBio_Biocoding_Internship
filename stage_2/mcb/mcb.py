import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("nhanes.csv")
df.head().T
df.shape

# Step 2: Define strain groups (WT vs. MUT)
strain_groups = {
    "Strain1_WT": ["A1", "A3", "B1", "B3", "C1", "C3"],
    "Strain1_MUT": ["A2", "A4", "B2", "B4", "C2", "C4"],
    "Strain2_WT": ["A5", "A7", "B5", "B7", "C5", "C7"],
    "Strain2_MUT": ["A6", "A8", "B6", "B8", "C6", "C8"],
    "Strain3_WT": ["A9", "B9", "C9"],
    "Strain3_MUT": ["A10", "B10", "C10"],
}

# Step 2: Define strain groups (WT vs. MUT)
strain_groups = {
    "Strain1_WT": ["A1", "A3", "B1", "B3", "C1", "C3"],
    "Strain1_MUT": ["A2", "A4", "B2", "B4", "C2", "C4"],
    "Strain2_WT": ["A5", "A7", "B5", "B7", "C5", "C7"],
    "Strain2_MUT": ["A6", "A8", "B6", "B8", "C6", "C8"],
    "Strain3_WT": ["A9", "B9", "C9"],
    "Strain3_MUT": ["A10", "B10", "C10"],
}

# Step 4: Function to determine carrying capacity time
def get_carrying_capacity_time(df, columns):
    carrying_times = {}
    for col in columns:
        max_od = df[col].max()
        threshold = 0.95 * max_od  # 95% of max OD600
        carrying_time = df[df[col] >= threshold]['time'].min()
        carrying_times[col] = carrying_time
    return carrying_times

# Compute carrying capacity times
wt_times = get_carrying_capacity_time(df, [col for strain, cols in strain_groups.items() 
                                           if "WT" in strain for col in cols])
mut_times = get_carrying_capacity_time(df, [col for strain, cols in strain_groups.items() 
                                            if "MUT" in strain for col in cols])

# Convert results into a DataFrame
carrying_df = pd.DataFrame({
    "Strain": list(wt_times.keys()) + list(mut_times.keys()),
    "Time_to_Carrying_Capacity": list(wt_times.values()) + list(mut_times.values()),
    "Type": ["WT"] * len(wt_times) + ["MUT"] * len(mut_times)
})

carrying_df

# Step 5: Scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=carrying_df, x="Type", y="Time_to_Carrying_Capacity", hue="Strain", style="Type")
plt.title("Time to Carrying Capacity (WT vs MUT)")
plt.xlabel("Strain Type")
plt.ylabel("Time (minutes)")
plt.show()

# Step 6: Box plot
plt.figure(figsize=(8, 6))
sns.boxplot(data=carrying_df, x="Type", y="Time_to_Carrying_Capacity")
plt.title("Comparison of Carrying Capacity Time (WT vs MUT)")
plt.xlabel("Strain Type")
plt.ylabel("Time (minutes)")
plt.show()

# Step 7: Perform statistical test (t-test)
wt_values = carrying_df[carrying_df["Type"] == "WT"]["Time_to_Carrying_Capacity"].dropna()
mut_values = carrying_df[carrying_df["Type"] == "MUT"]["Time_to_Carrying_Capacity"].dropna()

t_stat, p_value = stats.ttest_ind(wt_values, mut_values, equal_var=False)

# Step 8: Interpretation of statistical results
if p_value < 0.05:
    print(f"Statistically Significant Difference (p = {p_value:.3f})")
else:
    print(f"No Significant Difference (p = {p_value:.3f})")

### Observations & Insights
#### Growth Patterns:
Both wild-type (WT) and mutant (MUT) strains grow in a pretty similar way overall.

Some mutant strains show slight differences, but nothing too dramatic.

#### Time to Carrying Capacity:
Looking at the scatter and box plots, we see some variation in how long each strain takes to reach carrying capacity.

But there’s no obvious trend where WT or MUT strains consistently reach carrying capacity faster or slower.

#### Statistical Test (t-test):
The p-value is 0.488, which is greater than 0.05—meaning there’s no significant difference between WT and MUT in terms of carrying capacity time.

In other words, based on this dataset, knocking out the gene doesn’t really affect how quickly the strains reach their max population.
