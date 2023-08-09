#include <iostream>
#include <vector>
#include <math.h>

using namespace std;
int l,p,q;
int dist[200000000];

vector<int> primes(int n){
    vector<int> primes;
    vector<bool> is_prime(n+1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i <= n; i++) {
        if (is_prime[i] && (long long)i * i <= n) {
            for (int j = i * i; j <= n; j += i)
                is_prime[j] = false;
        }
        if (is_prime[i]){
            primes.push_back(i);
        }
    }
    return primes;
}
int main(){
    cin >> l >> p >> q;
    vector<int> prime_numbers = primes(l);
    int root = p;
    dist[root] = 0;
    vector<int> queue;
    queue.push_back(root);

    int head = 0;
    while (head < queue.size()){
        int last = queue[head];
        head++;
        int counter = 0;
        for (int prime:prime_numbers){
            counter ++; 
            if (log2(abs(last-prime))==int(log2(abs(last-prime)))
                && !dist[prime]){
                dist[prime] = dist[last] + 1;
                queue.push_back(prime);
                if (prime == q){
                    cout << dist[prime]+1;
                    return 0;
                }
            }
        }
    }
}