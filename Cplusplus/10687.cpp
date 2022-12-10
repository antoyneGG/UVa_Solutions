/*
Author: Fabian Antoyne Garcia Gallego
Problem: 10687 - Monitoring the Amazon
Credits: dfs-list-ady by Carlos Alberto Ramirez Restrepo
*/
#include <iostream>
#include <cmath>
#include <vector>
#include <tuple>

using namespace std;

int n = 1000;
vector<bool> reached(1000);
vector<vector<int>> G(1000);

void dfsAux(int u){
    int v;
    reached[u] = true;
    for(int i = 0; i < G[u].size(); i++){
        v = G[u][i];
        if(reached[v] == false){
            dfsAux(v);
        }
    }
}

void dfs(){
    reached.resize(n);
    for(int i = 0; i < n; i++){
        reached[i] = false;
    }
    dfsAux(0);
}

int main(){
    cin >> n;
    while(n != 0){
        int x, y, lastMinimumU, minimumU;
        float d, lastMinimumD, minimumD;
        vector<vector<float>> distances(n);
        vector<tuple<int, int>> stations;
        bool unreachable = false;
        for(int i = 0; i < n; i++){
            cin >> x >> y;
            stations.push_back(make_tuple(x, y));
            G[i].resize(2);
        }
        if(n > 3){
            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    d = sqrt(pow(get<0>(stations[j]) - get<0>(stations[i]), 2) + pow(get<1>(stations[j]) - get<1>(stations[i]), 2));
                    distances[i].push_back(d);
                }
            }
            for(int i = 0; i < n; i++){
                lastMinimumD = -1.0;
                lastMinimumU = -1;
                for(int s = 0; s < 2; s++){
                    minimumD = 60.0;
                    for(int j = 0; j < n; j++){
                        if(distances[i][j] < minimumD && i != j && distances[i][j] >= lastMinimumD && j != lastMinimumU){
                            minimumD = distances[i][j];
                            minimumU = j;
                        } else if(distances[i][j] == minimumD && i != j && s == 0 && get<0>(stations[j]) < get<0>(stations[minimumU]) && distances[i][j] >= lastMinimumD && j != lastMinimumU){
                            minimumU = j;
                        } else if(distances[i][j] == minimumD && i != j && s == 1 && get<1>(stations[j]) < get<1>(stations[minimumU]) && distances[i][j] >= lastMinimumD && j != lastMinimumU){
                            minimumU = j;
                        }
                    }
                    lastMinimumU = minimumU;
                    lastMinimumD = minimumD;
                    G[i][s] = minimumU;
                }
            }
            dfs();
            for(int i = 0; i < n; i++){
                if(reached[i] == false){
                    unreachable = true;
                }
            }
        }
        if(unreachable){
            cout << "There are stations that are unreachable." << endl;
        } else{
            cout << "All stations are reachable." << endl;
        }
        cin >> n;
    }
    return 0;
}