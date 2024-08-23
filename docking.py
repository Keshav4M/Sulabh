import os
import subprocess
from Bio.PDB import PDBParser

class PDBQTParser(PDBParser):
    def __init__(self):
        super(PDBQTParser, self).__init__()

    def _parse_atom_line(self, line):
        return super(PDBQTParser, self)._parse_atom_line(line.replace('A ', '  '))


def get_center_and_size(protein_path, ligand_path):
    parser = PDBQTParser()

    
    protein_structure = parser.get_structure("protein", protein_path)
    ligand_structure = parser.get_structure("ligand", ligand_path)

    all_atoms = [atom for atom in protein_structure.get_atoms()] + [atom for atom in ligand_structure.get_atoms()]
    all_coords = [atom.coord for atom in all_atoms]

    min_coords = [min(coord) for coord in zip(*all_coords)]
    max_coords = [max(coord) for coord in zip(*all_coords)]

    center = [(max_coords[i] + min_coords[i]) / 2 for i in range(3)]
    size = [max_coords[i] - min_coords[i] for i in range(3)]


    return center, size

vina_path = "\"C:/Program Files (x86)/The Scripps Research Institute/Vina/vina.exe\""

protein_folder = os.path.join(os.getcwd(), "targetproteinfordocking")
ligand_folder = os.path.join(os.getcwd(), "Ligand")
output_folder = os.path.join(os.getcwd(), "Outputs")


proteins = [os.path.join(protein_folder, f) for f in os.listdir(protein_folder) if f.endswith('.pdbqt')]
ligands = [os.path.join(ligand_folder, f) for f in os.listdir(ligand_folder) if f.endswith('.pdbqt')]

def run_vina(protein_path, ligand_path, output_path):
    center, size = get_center_and_size(protein_path, ligand_path)
    # Command
    command = '{} --receptor "{}" --ligand "{}" --center_x {} --center_y {} --center_z {} --size_x {} --size_y {} --size_z {} --out "{}" --log "{}.log"'.format(
        vina_path, protein_path, ligand_path, center[0], center[1], center[2], size[0], size[1], size[2], output_path, output_path)
    
    print("Executing command:", command)  # Debugging line
    subprocess.call(command, shell=True)




# Iterate through all protein and ligand combinations
for protein_path in proteins:
    for ligand_path in ligands:
        protein = os.path.basename(protein_path).split('.')[0]
        ligand = os.path.basename(ligand_path).split('.')[0]
        output_filename = "{}_{}_docked.pdbqt".format(protein, ligand)
        output_path = os.path.join(output_folder, output_filename)
        # Run Vina
        run_vina(protein_path, ligand_path, output_path)
