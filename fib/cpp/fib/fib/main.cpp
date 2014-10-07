#include <iostream>
using namespace std;
int main(){
    int generation = 5;
    int fecundity = 3;
    int prev_young = 1;
    int prev_adult = 0;
    int current_adult, current_young, current_total;
    for(int i = 0; i < generation-1; i++){
        current_adult = prev_young + prev_adult;
        current_young = prev_adult * fecundity;
        current_total = current_adult + current_young;
        prev_young = current_young;
        prev_adult = current_adult;
        cout << current_total << " ";
    }
}