import pandas as pd

data = pd.read_csv("Results_21Mar2022.csv")

columns_of_interest = [
    'mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_ghgs_ch4',
    'mean_ghgs_n2o', 'mean_bio', 'mean_watuse', 'mean_acid'
]

sex_averages = data.groupby('sex')[columns_of_interest].mean()
sex_averages.to_csv("sex_averages.csv")

age_group_averages = data.groupby('age_group')[columns_of_interest].mean()
age_group_averages.to_csv("age_group_averages.csv")

print("Sex Averages:\n", sex_averages.head())
print("Age Group Averages:\n", age_group_averages.head())
