#include <iostream>
#include <string>
#include <vector>
using namespace std;
string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXY";

string target = "";
string input_string = "";
string empty = "";

int state[25];


int main(){
    cin >> target;
    vector<pair<string,string>> queue;
    string root_string;
    for i in range(len(state)):
        if state[i] == 2:
            string += alphabet[i].upper()
        elif state[i] == 1:
            string += alphabet[i].lower()
    queue.push_back({state,empty});
}