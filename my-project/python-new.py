import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
diamonds_url = "https://raw.githubusercontent.com/TrainingByPackt/Interactive-Data-Visualization-with-Python/master/datasets/diamonds.csv"
diamonds_df = pd.read_csv(diamonds_url)
diamonds_df['price_per_carat'] = diamonds_df['price']/diamonds_df['carat']
diamonds_df['price_per_carat_is_high'] = np.where(diamonds_df['price_per_carat']>3500,1,0)
diamonds_df['price']= diamonds_df['price']*1.3
import math
diamonds_df['rounded_price']=diamonds_df['price'].apply(math.ceil)
print(diamonds_df.head())
diamonds_df = sns.load_dataset('diamonds')
ax=sns.barplot(x="cut", y="price", hue='color', data=diamonds_df)
plt.show()
mpg_df = sns.load_dataset("mpg")
## set the plot style to include ticks on the axes.
sns.set(style="ticks")
## hexbin plot
sns.jointplot(mpg_df.weight, mpg_df.mpg, kind="hex",color="#4CB391")
plt.show()