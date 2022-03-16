# importing pandas package
import seaborn as sns

import pandas as pd
sns.set_theme()
 
# making data frame from csv file
data = pd.read_csv("time_series_covid19_confirmed_global.csv", index_col="Country/Region"  )

# retrieving row by loc method
first = data.loc["France"]
second = data.loc["Germany"]
print(first, "\n\n\n" )
sns.scatterplot( y='Country/Region' ,x='3/8/22',data=first)
    