import os
from Bio.PDB import *

input_folder = r"C:\Users\SBLAB\Desktop\BTP_clone\BTP_clone\Edit-PDB-Files\PDB-Files-with-H2O"
output_folder = r"C:\Users\SBLAB\Desktop\BTP_clone\BTP_clone\Edit-PDB-Files\PDB-Files-without-H2O"

parser = PDBParser(QUIET=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".pdb"):
        structure = parser.get_structure('pdb', os.path.join(input_folder, filename))
        
        # Create a list to store chains other than chain A
        chains_to_remove = []
        
        # Iterate over each model in the structure
        for model in structure:
            # Iterate over each chain in the model
            for chain in model:
                # If the chain is not chain A, mark it for removal
                if chain.id != 'A':
                    chains_to_remove.append(chain)
        
        # Remove chains other than chain A
        for chain in chains_to_remove:
            model.detach_child(chain.id)
        
        # Remove all HETATM records and non-amino acid residues
        for model in structure:
            for chain in model:
                residues_to_remove = []
                for residue in chain:
                    if not is_aa(residue):
                        residues_to_remove.append(residue)
                for residue in residues_to_remove:
                    chain.detach_child(residue.id)
        
        io = PDBIO()
        io.set_structure(structure)
        io.save(os.path.join(output_folder, filename))
