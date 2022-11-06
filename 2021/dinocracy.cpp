#include <iostream>

using namespace std;

bool check_config(char config[1100000],int n){
    int adjacents;  
    for(int i = n-3; i < n; i ++){
        if (config[i] == config[i-1]){
            adjacents++;
        } else{
            adjacents = 0;
        }
    }
    for (int i = 0; i < n; i++){
        adjacents = 0;W
    }
}

char config1[1100000], config2[1100000];
int main(){
    int n;
    cin >> n;
    for (int i = 0; i < n/2; i++){
        int spy1,spy2;
        config1[spy1] = 'A';
        config1[spy1] = 'B';

        config1[spy1] = 'B';
        config1[spy1] = 'A';

    }
}