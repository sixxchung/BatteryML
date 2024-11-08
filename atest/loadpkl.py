import pickle
from pathlib import Path
import pandas as pd

def load_pickle(path):
    with open(path, 'rb') as file:
        data = pickle.load(file)
    return data

# if __name__=="__main__":
Path_for_pickle = Path('data/hust_data/our_data')
cell_file = Path_for_pickle/'8-3.pkl'

if cell_file.exists():
    filedata= load_pickle(cell_file)
    print(filedata)

# data['2-5'].keys() # dict_keys(['rul', 'dq', 'data'])
cell_id = cell_file.stem
cell_name = f'HUST_{cell_id}'

data_rul = filedata[cell_id]['rul']
data_dq = filedata[cell_id]['dq']
cell_data = filedata[cell_id]['data']
cycle = range(len(cell_data))
cycle = cycle[0]
df = cell_data[cycle+1]
# isinstance(data_rul, dict)
# isinstance(data_dq, dict)
# isinstance(cell_data, dict)

data_rul_pd = pd.DataFrame.from_dict(data_rul, orient='index')
data_dp_pd  = pd.DataFrame.from_dict(data_dq, orient='index')
# cell_data_pd = pd.DataFrame.from_dict(cell_data, orient='index')
cell_data[1]
cell_data[2]

data_rul_pd.shape
data_dp_pd.shape
cell_data[2]

cell_data[2]['Status'].unique()
cell_data[2].columns
{col: cell_data[2][col].unique() for col in cell_data[2].columns}

import matplotlib.pyplot as plt

cell_data[2000] = cell_data[2].sort_values(by='Time (s)')
grouped = cell_data[2000].groupby('Status')



# Plot each group
plt.figure(figsize=(10, 6))
for v in ['Cycle number', 'Current (mA)', 'Voltage (V)', 'Capacity (mAh)']:
    print(f'v={v}')
    for name, group in grouped:
        print(f'name ={name}')
        plt.plot(
            group['Time (s)'],
            group[v],
            marker='o', markersize=1,
            linestyle='-', label=name)
    plt.xlabel('Time (s)')
    plt.ylabel(v)
    # plt.title(name)
    # plt.legend()
    plt.show()


# -----------------------------------------------------------------------------
Path_for_pickle = Path('data/hust_data/')
cell_file = Path_for_pickle/'HUST_1-1.pkl'

if cell_file.exists():
    filedata= load_pickle(cell_file)
    print(filedata)

filedata.keys()
filedata['cell_id']
len(filedata['cycle_data'])  # 1504


# data['2-5'].keys() # dict_keys(['rul', 'dq', 'data'])
cell_id = cell_file.stem
cell_name = f'HUST_{cell_id}'

dict_keys(
    ['cell_id',
    'cycle_data',
    'form_factor',
    'anode_material',
    'cathode_material',
    'electrolyte_material',
    'nominal_capacity_in_Ah',
    'depth_of_charge',
    'depth_of_discharge',
    'already_spent_cycles',
    'max_voltage_limit_in_V',
    'min_voltage_limit_in_V',
    'max_current_limit_in_A',
    'min_current_limit_in_A',
    'reference',
    'description',
    'charge_protocol',
    'discharge_protocol'])

for col in filedata.keys():
    if col != 'cycle_data':
        print(f'{col} : {filedata[col]}')




data_rul = filedata[cell_id]['rul']
data_dq = filedata[cell_id]['dq']
cell_data = filedata[cell_id]['data']
cycle = range(len(cell_data))
cycle = cycle[0]
df = cell_data[cycle+1]
# isinstance(data_rul, dict)
# isinstance(data_dq, dict)
# isinstance(cell_data, dict)

data_rul_pd = pd.DataFrame.from_dict(data_rul, orient='index')
data_dp_pd  = pd.DataFrame.from_dict(data_dq, orient='index')
# cell_data_pd = pd.DataFrame.from_dict(cell_data, orient='index')
cell_data[1]
cell_data[2]

data_rul_pd.shape
data_dp_pd.shape
cell_data[2]