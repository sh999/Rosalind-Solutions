/*
http://rosalind.info/problems/dna/
 Solution 
 8/10/14
 */
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;
int main()
{
    string line;
    ostringstream output;
    string outputString;
    ifstream myFile ("rosalind_dna.txt");
    getline(myFile, line);
    ofstream resultFile;
    resultFile.open("output.txt");
    int a, c, g, t;
    a = 0;
    c = 0;
    t = 0;
    g = 0;
    for(int i = 0; i < line.length(); i++){
        if (line[i] == 'A'){
            a++;
        }
        else if (line[i] == 'C'){
            c++;
        }
        else if (line[i] == 'T'){
            t++;
        }
        else if (line[i] == 'G'){
            g++;
        }
        
    }
    output << a << " " << c << " " << g << " " << t;
    outputString = output.str();
    resultFile << outputString;
}