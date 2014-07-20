/*
 Degree array-Rosalind program
 
 */
#include <iostream>
#include <fstream>
using std::fstream;;

int main(int argc, const char * argv[])
{
    fstream myFile;
    myFile.open("asdf.txt", std::ios::out);
    myFile << "Writing to file.\n";
    myFile << fflush;
    myFile.close();
    return 0;
}

