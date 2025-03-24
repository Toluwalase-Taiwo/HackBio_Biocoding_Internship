import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats

url = "https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt"
df = pd.read_csv(url, sep = '/t', engine='python')
df.head()
df.shape
df.columns
df_split = df['Gene log2FoldChange pvalue padj'].str.split(' ', expand=True)

# Assign meaningful column names
df_split.columns = ['Gene', 'log2FC', 'pvalue', 'padj']
df_split.head()

df = df_split
df.shape
df.dtypes

# Convert numeric columns to appropriate data types
df["log2FC"] = pd.to_numeric(df["log2FC"], errors='coerce')
df["pvalue"] = pd.to_numeric(df["pvalue"], errors='coerce')
df["padj"] = pd.to_numeric(df["padj"], errors='coerce')

# Drop any rows with NaN values (if conversion failed for any row)
df.dropna(inplace=True)
df.dtypes

# Set significance thresholds
log2fc_threshold = 1
pvalue_threshold = 0.01

# Define gene categories for color mapping
df["category"] = "Not Significant"
df.loc[(df["log2FC"] > log2fc_threshold) & (df["pvalue"] < pvalue_threshold), "category"] = "Upregulated"
df.loc[(df["log2FC"] < -log2fc_threshold) & (df["pvalue"] < pvalue_threshold), "category"] = "Downregulated"

# Plot the volcano plot
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=df["log2FC"], 
    y=-np.log10(df["pvalue"]), 
    hue=df["category"], 
    palette={"Upregulated": "red", "Downregulated": "blue", "Not Significant": "gray"},
    alpha=0.7
)

# Add cutoff lines
plt.axvline(x=log2fc_threshold, linestyle="--", color="black")  
plt.axvline(x=-log2fc_threshold, linestyle="--", color="black")  
plt.axhline(y=-np.log10(pvalue_threshold), linestyle="--", color="black")  

# Labels and title
plt.xlabel("Log2 Fold Change")
plt.ylabel("-Log10 P-value")
plt.title("Volcano Plot")
plt.legend(title="Gene Regulation")
plt.show()

# Get upregulated and downregulated genes
upregulated = df[(df["log2FC"] > 1) & (df["pvalue"] < 0.01)]
downregulated = df[(df["log2FC"] < -1) & (df["pvalue"] < 0.01)]

# Show top 5 from each
print("Top 5 Upregulated Genes:")
print(upregulated.nlargest(5, "log2FC")[["Gene", "log2FC", "pvalue"]])

print("\nTop 5 Downregulated Genes:")
print(downregulated.nsmallest(5, "log2FC")[["Gene", "log2FC", "pvalue"]])

## Functions of top 5 Upregulated and top 5 downregulated genes
### Top 5 Upregulated Genes (More Active in Disease + Treatment Group)
#These genes showed a higher expression in the treated diseased cells.

#DTHD1 – Not much is known about its function yet.

#EMILIN2 – Helps structure tissues and may slow down cancer cell growth.

#PI16 – Peptidase Inhibitor 16 (PI16) Affects the immune system and may play a role in prostate cancer.

#C4orf45 – A protein that may work inside the cell nucleus.

#FAM180B – Scientists still don’t know exactly what it does.



### Top 5 Downregulated Genes (Less Active in Disease + Treatment Group)
#These genes showed a lower expression in the treated diseased cells.

#TBX5 – Important for heart and limb development.

#IFITM1 – Helps the immune system by stopping viruses from entering cells.

T#NN – Involved in wound healing and tissue repair.

#COL13A1 – Helps cells stick together and supports nerve-muscle connections.

#IFITM3 – Another immune-related gene that stops viruses like the flu from infecting cells.

