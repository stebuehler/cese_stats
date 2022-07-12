import pandas as pd
import numpy as np

def load_data() -> pd.DataFrame:
    df = pd.read_csv('source_data/team_cese_alltime_stats.csv')
    return df

def get_all_entries_for_column(column, df=None):
    df = load_data() if df is None else df
    entries = df[column].unique()
    entries.sort()
    return entries

def get_all_players(df=None):
    columns = ['Spieler 1 Team A', 'Spieler 2 Team A', 'Spieler 1 Team B', 'Spieler 2 Team B']
    all_entries = np.array([])
    for col in columns:
        all_entries = np.append(all_entries, get_all_entries_for_column(col))
    return np.unique(all_entries)