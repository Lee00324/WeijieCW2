import pandas as pd

data_path = "Results_21Mar2022.csv"
data = pd.read_csv(data_path)

columns_of_interest = [
    'mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_ghgs_ch4',
    'mean_ghgs_n2o', 'mean_bio', 'mean_watuse', 'mean_acid'
]


aggregated_data = data.groupby(['sex', 'age_group', 'diet_group'])[columns_of_interest].mean().reset_index()


output_file_name = "aggregated_data.csv"
aggregated_data.to_csv(output_file_name, index=False)

print(f"Aggregated data saved to {output_file_name}.")
