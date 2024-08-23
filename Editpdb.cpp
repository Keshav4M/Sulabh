#include<bits/stdc++.h>

using namespace std;

int main()
{
    ifstream fin("7e6g.pdb");

    if (fin.fail())
    {
        cout << "Cant Read the file.";
        return 0;
    }

    string line;
    int count = 0;
    ofstream fout("Output.pdb"); // Open output file here

    while (getline(fin, line))
    {
        if (line.size() == 0)
            continue;

        istringstream iss(line);

        string word;
        iss >> word;

        if (word == "TER")
        {
            count++;
            fout << line << "\n"; // Write the "TER" line to the output file
            break; // Stop reading lines after encountering the first "TER" line
        }
        
        fout << line << "\n"; // Write the current line to the output file
    }

    // Continue writing the remaining lines to the output file
    while (getline(fin, line))
    {
        if (line.size() == 0)
            continue;

        istringstream iss(line);

        string word;
        iss >> word;

        if (word == "TER")  
            count--;

        fout << line << "\n";

        if (count == 0)
            break;
    }

    fout << "END"; // Add "END" to the end of the output file
    return 0;
}
