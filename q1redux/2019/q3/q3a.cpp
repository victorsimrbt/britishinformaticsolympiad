#include <iostream>
#include <string>

using namespace std;

int l;
string p;
string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";


bool valid(string config){
    for (int a = 0; a < config.size(); a++){
        for (int b = a; b < config.size(); b++){
            for (int c = b; c < config.size(); c++){
                if (config[a] < config[b] && config[b] < config[c]){
                    return false;
                }
            }
        }
    }
    return true;
}

int num_configs(string config, int remain){
    if (!valid(config)){
        return 0;
    }
    if (remain == 0){
        return 1;
    }
    int ans = 0;
    for (int chara = 0; chara < l; chara++){
        bool present = config.find(alphabet[chara]) != string::npos;
        if (!present){
            ans += num_configs(config+alphabet[chara],remain-1);
        }
    }
    return ans;
}

int main(){
    cin >> l >> p;
    cout << num_configs(p,l-p.size());
}
