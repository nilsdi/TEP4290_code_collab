"""
For reading in the exchange rates to Euro from the csv file in a clean way.
"""

#%%
import pandas as pd
from pathlib import Path

root_dir = Path(__file__).resolve().parents[2]
data_dir = root_dir / 'data'
print(f'{root_dir=}')
print(f'{data_dir=}')

exchanges_path = data_dir / 'raw/exchange_rates/exchange_rates.csv'

# %%
def read_in_exchanges():
    """
    Read in the mobiles from the csv file.
    """
    exchanges = pd.read_csv(exchanges_path, encoding='ISO-8859-1')
    return exchanges

# %%
if __name__ == '__main__':
    exchanges = read_in_exchanges()
    print(exchanges.head())
# %%
