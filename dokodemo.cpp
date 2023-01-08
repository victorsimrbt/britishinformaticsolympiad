#include <iostream>
#include <vector>
using namespace std;
int n,m,c;
vector<int> graph[10001];
int dist[10001];

int main(){
    int city1,city2;
    cin >> n >> m >> c;

    for (int i = 1; i <= m; i++){
        cin >> city1 >> city2;
        graph[city1].push_back(city2);
        graph[city2].push_back(city1);
    }

    int root = 1;
    vector<int> queue;
    queue.push_back(root);
    dist[root] = 0;
    int head = 0;
    while (head < queue.size()){
        int last = queue[head];
        head++;
        vector<int> next_states = graph[last];
        for (auto state: next_states){
            if (!dist[state]){
                dist[state] = dist[last] + 1;
                queue.push_back(state);
            }
            if (state == n){
                cout << dist[state]-c << endl;
                return 0;
            }
        }

    }
    cout << -1 << endl;
    /*
    for (int i = 1; i <= n; i++){
        cout << i << ":" << endl;
        for(auto connection:graph[i]){
            cout << connection << " ";
        }
        cout << endl;
    }
    */
   return 0;
}
/*
Construct adjacency list with input
run bfs between 1 and N
do C-length of BFS
if not reached return -1
*/