"""
For reading in the mobiles from the csv file in a clean way.
"""

#%%
import pandas as pd
from pathlib import Path

root_dir = Path(__file__).resolve().parents[2]
data_dir = root_dir / 'data'
print(f'{root_dir=}')
print(f'{data_dir=}')

mobiles_path = data_dir / 'raw/mobiles/Mobiles Dataset (2025).csv'
# %%
def read_in_mobiles():
    """
    Read in the mobiles from the csv file.
    """
    mobiles = pd.read_csv(mobiles_path, encoding='ISO-8859-1')
    return mobiles


# %%
if __name__ == '__main__':
    mobiles = read_in_mobiles()
    print(mobiles.head())
# %%
