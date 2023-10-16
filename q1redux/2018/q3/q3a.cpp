#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <chrono>

using namespace std;

int l;
string p;
string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

int lis(string a) {
    vector<char> tails(a.size());
    tails[0] = 'Z';
    int length = 1;

    for (int i = 0; i < a.size(); i++){
        int update = -1;
        auto low = upper_bound(tails.begin(),tails.begin()+length,a[i]);
        if (low-tails.begin() != length){
            update = low - tails.begin();
        }

        if (update == -1 && a[i] > tails[0]){
            length++;
            tails[length-1] = a[i];
        } else {
            tails[update] = a[i];
        }
        
    }
    return length;
}

bool valid(string config){
    return lis(config) < 3;
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

// int num_configs(string config, string remain){
//     // if for every character in remain, do it
//     if (!valid(config)){
//         return 0;
//     }
//     if (remain.size() == 0){
//         return 1;
//     }
//     int ans = 0;
//     for (auto letter: remain){
//         ans += num_configs(config+letter,remain.erase(letter));
//     }
//     return ans;



// }

int main(){
    cin >> l >> p;
    string remain = "";
    for (auto letter : alphabet){
        bool present = p.find(letter) == string::npos;
        if (present){
            remain += letter;
        }
    }
    // cout << remain;
    auto start = chrono::high_resolution_clock::now();
    cout << num_configs(p,l-p.size()) << "\n";
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;
    cout << "Elapsed time: " << elapsed.count() << " seconds\n";
    return 0;
}