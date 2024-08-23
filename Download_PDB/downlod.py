import subprocess
import urllib.request

# Function to convert text file
def convert_txt(file_name):
    with open(file_name, 'r') as file:
        data = file.read().split(',')
    with open('C:\\Users\\SBLAB\\Desktop\\BTP_clone\\BTP_clone\\Download_PDB\\new.txt', 'w') as new_file:
        new_file.write('\n'.join(data))

# Function to download files
def download_files():
    with open("C:\\Users\\SBLAB\\Desktop\\BTP_clone\\BTP_clone\\Download_PDB\\new.txt", 'r') as file:
        for item in file:
            item = item.strip()
            url = f"https://files.rcsb.org/download/{item}.pdb"
            urllib.request.urlretrieve(url, f"C:/Users/SBLAB/Desktop/BTP_clone/BTP_clone/Download_PDB/downloaded_files/{item}.pdb")

# Main function
def main():
    convert_txt("C:\\Users\\SBLAB\\Desktop\\BTP_clone\\BTP_clone\\Download_PDB\\PDB_IDS.txt")
    download_files()

if __name__ == "__main__":
    main()