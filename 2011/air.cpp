//bfs 
#include <iostream>
#include <vector>

using namespace std;

vector<int> neighbours[257];
int time_cost[66050];

int visited[257];

int second_fastest(){
    // bfs
    vector<pair<int,int>> queue;
    queue.push_back({0,0});
    for (int i = 0; i < queue.size(); i++){
        int timecost = queue[i].first;
        for (int x = 0; x < neighbours[i].size(); x++){
            if (visited[i] == 0){
                queue.push_back({neighbours[i][x],time_cost+time_cost});
                visited[i] = 1;
            }
        }
    }

}

int main(){
    int w;
    cin >> w;
    while (true){
        int waypoint1, waypoint2, time;
        cin >> waypoint1 >> waypoint2 >> time;
        if (waypoint1 == -1){
            break;
        }
        neighbours[waypoint1].push_back(waypoint2);
        neighbours[waypoint2].push_back(waypoint1);
    }

    for (int i = 0; i < w; i++){
        cout << "NEIGHBOURS OF " << i << " ";
        for (int x = 0;x < neighbours[i].size();x++){
            cout << neighbours[i][x] << " ";
        }
        cout << endl;
    }
    return 0;
}