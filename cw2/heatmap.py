import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data_path = 'Results_21Mar2022.csv'
df = pd.read_csv(data_path)


columns_of_interest = [
    'mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut',
    'mean_ghgs_ch4', 'mean_ghgs_n2o', 'mean_bio', 'mean_watuse', 'mean_acid'
]


corr_matrix = df[columns_of_interest].corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))


plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, mask=mask, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix of Environmental Variables')
plt.show()

