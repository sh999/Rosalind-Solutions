#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;
int main()
{
    ifstream myFile ("rosalind_rna.txt");
    ofstream outputFile ("outputfile.txt");
    string content;
    string line;
    ostringstream output;
    while(getline(myFile, line))
    {
        content = line + content;
    }
    string rna(content.length(), ' ');


    for(int i = 0; i < content.length(); i++){
        if (content[i] == 'T'){
            rna[i] = 'U';
        }
        else rna[i] = content[i];
    }

    outputFile << rna;
    
    myFile.close();
    
}