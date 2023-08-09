#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> config;

int num_seq(int n){
    if (n == 1){
        return 1;
        config.push_back(1);
    } else {
        int ans = 0;
        for (int i = 1; i < 9; i++){
            int remain = n-i;
            // printf("Remainder Initial: %d \n",remain);
            if (remain >= 1 && remain <= 9){
                ans += num_seq(remain);
            }
            if (remain == 0){
                ans += 1;
                break;
            }
        }
        return ans;
    }
}

int nth_val(int n,int target){
    for (int i = 1; i < 9;i++){
        // how many n digit configs are there
        // for 1: is the number 1 to 9
        // for 2: does value - numbers - 1 to 9 
        // for 3: 
        // use to figure out which one it is rooted from 
    }

}

int main(){
    int n;
    int s;
    cin >> n >> s;
    printf("Answer %d",num_seq(n));
}