import pandas as pd
import plotly.express as px

df = pd.read_csv('results.csv')

fig1 = px.treemap(df, path=['age_group', 'diet_group'], values='mean_ghgs_ch4',
                  color='mean_ghgs_ch4',
                  color_continuous_scale='RdBu',
                  title='Environmental Impact by Age Group and Diet Type (CH4)')


fig2 = px.treemap(df, path=['sex', 'age_group', 'diet_group'], values='mean_ghgs_ch4',
                  color='mean_ghgs_ch4',
                  color_continuous_scale='RdBu',
                  title='Dietary Differences Across Sex and Age Group (CH4)')


fig1.show()
fig2.show()
