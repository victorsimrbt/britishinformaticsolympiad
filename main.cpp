#include <iostream>
#include <vector>
#include <string.h>

using namespace std;
int ans[501];
int cows[501][501];
vector<int> graph[501];
int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    for (int x = 0; x < n; x++) {
      cin >> cows[i][x];
    }
  }

  // Setup adjacency list (correct)
  for (int i = 0; i < n; i++) {
    for (int v : cows[i]) {
      if (v == i + 1) {
        break;
      }
      graph[i + 1].push_back(v);
    }
  }
    for (int i = 1; i <= n; i++){
        vector<pair<int, vector<int>>> stack;
        pair<int, vector<int>> start;
        int visited[501];

        cout << "COW "<< i << endl;
        start.first = i;
        vector<int> source_vec;
        source_vec.push_back(i);
        start.second = source_vec;
        stack.push_back(start);

        vector<int> reassign;
        reassign.push_back(start.first);

        while (!stack.empty()) {
        pair<int, vector<int>> last = stack.back();
        if (last.first == start.first && last.second.size() != 1) {
            cout << "FOUND PATH" << endl;
            for (auto path : last.second) {
            cout << path;
            }
            cout << endl;
            reassign.push_back(last.second[1]);
        }
        stack.pop_back();
        vector<int> next_states = graph[last.first];
        cout << "ORIGINAL STATE: " << last.first << endl;
        cout << "NEIGHBOURS: " << endl;
        for (auto neighbour : next_states) {
            cout << neighbour << " VISITED: " << visited[neighbour] << endl;
        }
        cout << endl;

        visited[last.first] = 1;
        for (auto state : next_states) {
            if (visited[state] != 1 || state == start.first) {
            //cout << "NEW STATE: " << state << endl;
            pair<int, vector<int>> new_state;
            new_state.first = state;
            auto path = last.second;
            path.push_back(state);
            new_state.second = path;
            stack.push_back(new_state);
            }
        }
        }
        bool found = false;
        for (int i = 0; i < n; i++) {
        for (auto re : reassign) {
            if (re == cows[start.first-1][i]) {
            ans[start.first] = re;
            cout << "ANS" << ans[start.first] << endl;
            found = true;
            break;
            }
        }
        if (found){
            break;
        }
        }
        memset(visited, 0, sizeof(visited));
    }
}