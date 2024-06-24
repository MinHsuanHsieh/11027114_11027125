import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the provided CSV file
file_path = 'combined_mbti_df.csv'
data = pd.read_csv(file_path)

data = data.drop(columns=["mbti", "function_pair"])

# Calculate the correlation matrix
correlation_matrix = data.corr()

# Mask for significant correlations (absolute value greater than 0.5)
significant_mask = (correlation_matrix.abs() >= 0.5)

# Apply the mask to filter the correlation matrix
significant_corr_matrix = correlation_matrix.where(significant_mask)

# Plot the heatmap with significant correlations only
plt.figure(figsize=(14, 12))
heatmap = sns.heatmap(significant_corr_matrix, annot=True, cmap='coolwarm', linewidths=.5, mask=~significant_mask)
plt.title('Heatmap of Significant Correlations (|r| > 0.5) with Masking')
plt.show()
