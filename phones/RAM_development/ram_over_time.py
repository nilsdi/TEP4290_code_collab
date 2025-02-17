"""
checking the devolopment of RAM over time.
"""
#%%
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from phones.utils.read_in_mobiles import read_in_mobiles 

root_dir = Path(__file__).resolve().parents[2]
#print(f'{root_dir=}')
#%%

def ram_over_time(mobiles:pd.DataFrame, save_as:str = None):

    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111)
    time = mobiles['Launched Year']
    # mobile_type = mobiles['Model Name']
    # for t, m in zip(time, mobile_type):
    #     print(t, m)
    ram = mobiles['RAM']
    # filter out the highest year entry as it is an outlier
    outlier_year = time.max()
    outlier_index = time[time == outlier_year].index
    time_filtered = time.drop(outlier_index)
    ram_filtered = ram.drop(outlier_index)
    # convert ram to numeric
    numbers_only = ram_filtered.str.replace('GB', '')
    ram_final = []
    time_final = []
    for t, r in zip(time_filtered, numbers_only):
        try:
            ram_number = float(r)
            ram_final.append(ram_number)
            time_final.append(t)
        except:
            pass
    
    #print(ram_final)
    #ram_filtered = pd.to_numeric(ram_filtered.str.replace('GB', ''))
    ax.plot(time_final, ram_final, 'o', label='RAM')

    if save_as:
        plt.savefig(root_dir/"data/figures"/save_as, dpi=300, bbox_inches='tight')
    
    return fig



# %%
if __name__ == '__main__':
    mobiles = read_in_mobiles()
    #print(mobiles.head())
    ram_over_time(mobiles, save_as='ram_over_time.png')
    #print(mobiles.columns)



# %%
