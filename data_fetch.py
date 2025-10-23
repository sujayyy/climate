# src/data_fetch.py
import pandas as pd
import requests
from io import StringIO
import os

def fetch_owid_co2(save_path='../data/owid_co2.csv'):
    url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    print('Downloading OWID CO2 dataset from GitHub...')
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    df = pd.read_csv(StringIO(r.text))
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"Saved OWID CSV to {save_path} (rows={len(df)})")
    return df

if __name__ == '__main__':
    fetch_owid_co2()
