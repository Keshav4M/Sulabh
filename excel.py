import os
import shutil
import pandas as pd

source_folder = r"C:\Users\SBLAB\Desktop\BTP_clone\BTP_clone\Outputs"
excel_file_path = r'C:\Users\SBLAB\Desktop\BTP_clone\BTP_clone\Atom_energies.xlsx'

files = os.listdir(source_folder)
txt_files = [file for file in files if file.endswith('.log')]

def get_affinity(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if '   1' in line:
                return float(line.split()[1])
    
    print(f"File '{file_path}' does not contain the specified string.")
    return float('inf')


data = {'File Name': [], 'Energy Value': []}

for file in txt_files:
    source_file_path = os.path.join(source_folder, file)
    energy_value = get_affinity(source_file_path)
    data['File Name'].append(file)
    data['Energy Value'].append(energy_value)

df = pd.DataFrame(data)

df.to_excel(excel_file_path, index=False)


print(f"Energy values saved in '{excel_file_path}'.")