#basic study to clean data
import pandas as pd

#extracting public data Titanic
url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url) #Using Pandas to read .csv
df.head(3) #read the first 3 rows of data
df_filter = df[df["Survived"] == 1]
df_filter = df_filter[df_filter["Sex"] == "female"]
df_filter.drop(columns=["Ticket"])
df_filter[df_filter['Cabin'].notnull() ] #final dataframe
