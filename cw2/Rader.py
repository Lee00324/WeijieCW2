import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler


data = pd.read_csv("diet_group_Averages.csv")


categories = ['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_ghgs_ch4', 'mean_ghgs_n2o', 'mean_bio', 'mean_watuse', 'mean_acid']
labels = np.array(categories)


scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data[categories])
data_scaled = pd.DataFrame(data_scaled, columns=categories)
data_scaled['diet_group'] = data['diet_group']


num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, axes = plt.subplots(figsize=(20, 10), nrows=2, ncols=3, subplot_kw=dict(polar=True))
axes = axes.flatten()


for ax, (index, row) in zip(axes, data_scaled.iterrows()):
    values = row[categories].values.flatten().tolist()
    values += values[:1]
    ax.fill(angles, values, alpha=0.25)
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=row['diet_group'])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=13)
    ax.set_title(row['diet_group'], size=16, color='blue', y=1.1)


plt.tight_layout(pad=2.0)
fig.legend(data['diet_group'].unique(), loc='upper right', title='diet_group')

plt.show()

