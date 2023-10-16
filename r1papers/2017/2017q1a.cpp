#include <iostream>
#include <string>

using namespace std;

string row;
int main(){
    cin >> row;
    while (row.size() != 1){
        string new_row = "";
        for (int i = 0; i < row.size()-2; i++){
            if (row[i] == 'R' && row[i+1] == 'R'){
                new_row += row[i];
            }
            
        }

    }
    cout << row;
    return 0;
}