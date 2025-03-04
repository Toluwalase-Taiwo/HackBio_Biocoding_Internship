#importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn 

#Loading the dataset
df_link = "https://raw.githubusercontent.com/PacktPublishing/Machine-Learning-in-Biotechnology-and-Life-Sciences/refs/heads/main/datasets/dataset_wisc_sd.csv"
df = pd.read_csv(df_link)
df.head().T

#rows and columns
df.shape

#total number of null values
df.isnull().sum()

#fill NaN values using the mean
df['area_mean']= df['area_mean'].fillna(df['area_mean'].mean())
df['radius_se']= df['radius_se'].fillna(df['radius_se'].mean())
df['smoothness_worst']= df['smoothness_worst'].fillna(df['smoothness_worst'].mean())
df['fractal_dimension_se']= df['fractal_dimension_se'].fillna(df['fractal_dimension_se'].mean())
df.isnull().sum()

#number of patients with malignant cancerous cells
malignant = df[df['diagnosis'] == 'M'].shape
malignant

#number of patients with benign cancerous cells
benign = df[df['diagnosis'] == "B"].shape
benign

#change object dtype into float
df['concave points_worst'] = df['concave points_worst'].str.replace('\\n\\n','').astype(float)
df.dtypes

#splitting our data into features (X) and target (y)
X = df.drop('diagnosis', axis = 1)
y = df['diagnosis']

#Normalizing our data
from sklearn.preprocessing import StandardScaler
#initialize the scaler 
scaler = StandardScaler()
#fit and transform
scaled_data = scaler.fit_transform(X)

### Elbow Method
#### Using the Elbow Method to determine the optimal number of clusters (K) in KMeans Clustering
from sklearn.cluster import KMeans

# Initialize empty list to store inertia values
inertias = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(scaled_data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()
#From the graph, our K=2 gives the best possible optimal number of clusters. We see an elbow at 2 clusters (corresponding to malignant and benign)

#KMeans Clustering
from sklearn.cluster import KMeans

#Initialize KMeans
KMeans = KMeans (n_clusters = 2, random_state = 42)

#fit the model
KMeans.fit(scaled_data)

#add the clusters to the original dataframe
df['Cluster'] = KMeans.labels_
df['Cluster']

#Principal Component Analysis
###Principal component analysis (PCA) is a dimensionality reduction and machine learning method used to simplify a large data set into a smaller set 
##while still maintaining significant patterns and trends.
from sklearn.decomposition import PCA

#reduce dimensions to 2D for better visualization
pca = PCA(n_components = 2)
principal_component = pca.fit_transform(scaled_data)

#create a new df with PCA
pc_df = pd.DataFrame(data = principal_component, columns = ['PC1', 'PC2'])
pc_df['Cluster'] = df['Cluster']

# Plot the clusters
plt.figure(figsize=(10, 6))
for cluster in pc_df['Cluster'].unique():
    cluster_data = pc_df[pc_df['Cluster'] == cluster]
    plt.scatter(cluster_data['PC1'], cluster_data['PC2'], label=f'Cluster {cluster}')
plt.title('K-Means Clustering of Cancer Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.show()

## The malignant(M) cancerous cell is Cluster 0 and the benign(B) cancerous cell is Cluster 1
