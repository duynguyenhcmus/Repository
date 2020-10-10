import pandas as pd
import numpy as np
url_co2 = 'https://raw.githubusercontent.com/TrainingByPackt/Interactive-Data-Visualization-with-Python/master/datasets/co2.csv'
co2 = pd.read_csv(url_co2)
url_gm = 'https://raw.githubusercontent.com/TrainingByPackt/Interactive-Data-Visualization-with-Python/master/datasets/gapminder.csv'
gm = pd.read_csv(url_gm)
df_gm = gm[['Country', 'region']].drop_duplicates()
df_w_regions = pd.merge(co2, df_gm, left_on ='country', right_on='Country', how ='inner')
df_w_regions = df_w_regions.drop('Country', axis='columns')
new_co2 = pd.melt(df_w_regions, id_vars=['country', 'region'])
columns = ['country', 'region', 'year', 'co2']
new_co2.columns = columns
#print(new_co2)
"""
modified_co2=new_co2[new_co2['year']!='Country']
#print(modified_co2)
df_co2 = modified_co2[(modified_co2['year']).astype('int64') > 1963]
df_co2 = df_co2.sort_values(by=['country', 'year'])
df_co2['year'] = df_co2['year'].astype('int64')
print(df_co2.head())
df_gdp = gm[['Country', 'Year', 'gdp']]
df_gdp.columns = ['country', 'year', 'gdp']
print(df_gdp.head())
data = pd.merge(df_co2, df_gdp, on=['country', 'year'], how='left')
data = data.dropna()
print(data.head())
"""
df_co2 = new_co2[new_co2['year'].astype('int64') > 1963]
df_co2 = df_co2.sort_values(by=['country', 'year'])
df_co2['year'] = df_co2['year'].astype('int64')
print(df_co2.head())
df_gdp = gm[['Country', 'Year', 'gdp']]
df_gdp.columns = ['country', 'year', 'gdp']
print(df_gdp.head())
data = pd.merge(df_co2, df_gdp, on=['country', 'year'], how='left')
data = data.dropna()
print(data.head())
np_co2 = np.array(data['co2'])
np_gdp = np.array(data['gdp'])
print(np.corrcoef(np_co2, np_gdp))

from bokeh.io import curdoc, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import HoverTool, ColumnDataSource,CategoricalColorMapper, Slider
from bokeh.palettes import Spectral6
from bokeh.layouts import widgetbox, row

output_notebook()
