import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the updated data
df = pd.read_csv('used_camera_canon_r50_cleaned.csv')

sns.set_theme(style="whitegrid")

# Create a 1x3 grid for plots
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Plot 1: Histogram (General Trend)
sns.histplot(df['Price'], bins=15, kde=True, color='#3498db', ax=axes[0])
axes[0].set_title('General Price Distribution', fontweight='bold')

# Plot 2: Boxplot by Includes_Kit
sns.boxplot(data=df, x='Includes_Kit', y='Price', palette='Set2', ax=axes[1])
axes[1].set_title('Price by Kit Lens Inclusion', fontweight='bold')

# Plot 3: Boxplot by Is_Fullbox
sns.boxplot(data=df, x='Is_Fullbox', y='Price', palette='Set3', ax=axes[2])
axes[2].set_title('Price by Fullbox Status', fontweight='bold')

plt.tight_layout()
plt.show()