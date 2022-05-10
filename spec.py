from numpy import NaN
import pandas as pd


input_file = 'source_data/team_cese_alltime_stats.csv'
df = pd.read_csv(input_file, delimiter=",")
df['dreisätzer?'] = df['Punkte Satz 3 Team A']>=0
print(df)
print(df.groupby(['Jahr', 'dreisätzer?']).count()['Reihenfolge'])