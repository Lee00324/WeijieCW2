import pandas as pd

data = pd.read_csv("Results_21Mar2022.csv")

columns_of_interest = ['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_ghgs_ch4', 'mean_ghgs_n2o', 'mean_bio', 'mean_watuse', 'mean_acid']

if 'diet_group' not in data.columns:
    raise ValueError("The dataset does not contain a 'diet_group' column.")

group_averages = data.groupby('diet_group')[columns_of_interest].mean()

group_averages.reset_index(inplace=True)

print(group_averages)

group_averages.to_csv("diet_group_Averages.csv", index=False)

