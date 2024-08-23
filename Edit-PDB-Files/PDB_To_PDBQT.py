import os
import subprocess

import sys
sys.path.insert(0, r"C:\Users\SBLAB\Desktop\BTP_clone\BTP_clone\AutoDockTools_py3-master")
sys.path.insert(0, r"C:\Users\SBLAB\Desktop\BTP_clone\BTP_clone\AutoDockTools_py3-master\AutoDockTools")
sys.path.insert(0, r"C:\Users\SBLAB\Desktop\BTP_clone\BTP_clone\AutoDockTools_py3-master\AutoDockTools\Utilities24")
# for path in sys.path:
#     print(path)


from AutoDockTools.Utilities24.prepare_receptor4 import main as prepare_receptor



def convert_pdb_to_pdbqt(input_folder, output_folder):
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all PDB files in the input folder
    pdb_files = [file for file in os.listdir(input_folder) if file.endswith(".pdb")]

    for pdb_file in pdb_files:
        # Create the full path to the input PDB file
        input_pdb_path = os.path.join(input_folder, pdb_file)

        # Create the output PDBQT filename based on the input filename
        output_pdbqt_filename = os.path.splitext(pdb_file)[0] + ".pdbqt"

        # Create the full path to the output PDBQT file
        output_pdbqt_path = os.path.join(output_folder, output_pdbqt_filename)

        # Command to convert PDB to PDBQT using prepare_receptor
        command = ['python', '-m', 'AutoDockTools.Utilities24.prepare_receptor4', '-r', input_pdb_path, '-o', output_pdbqt_path]

        print("Executing command:", ' '.join(command))  # Debugging line
        subprocess.call(command)

        print("Converted {} to {}".format(pdb_file, output_pdbqt_filename))

if __name__ == '__main__':
    input_folder = "C:\\Users\\SBLAB\\Desktop\\BTP_clone\\BTP_clone\\Edit-PDB-Files\\PDB-Files-without-H2O"
    output_folder = "C:\\Users\\SBLAB\\Desktop\\BTP_clone\\BTP_clone\\Edit-PDB-Files\\Output-pdbqt-files"

    convert_pdb_to_pdbqt(input_folder, output_folder)