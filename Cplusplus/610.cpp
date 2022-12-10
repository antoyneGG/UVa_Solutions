/*
Author: Fabian Antoyne Garcia Gallego
Problem: 610 - Street Directions
Credits: tarjanBridges by Carlos Alberto Ramirez Restrepo
*/


#include <iostream>
#include <vector>
#include <set>

using namespace std;

int n, t;
vector<vector<int>> G(1001);
int visited[1001];
int low[1001];
int father[1001];
set<pair<int, int>> bridges;
set<pair<int, int>> streets;

void bridgesAux(int u){
    int v, i;
    t++;
    visited[u] = t;
    low[u] = t;

    for(i = 0; i < G[u].size(); i++){
        v = G[u][i];
        if(streets.find(make_pair(v, u)) == streets.end() && streets.find(make_pair(u, v)) == streets.end()){
            streets.insert(make_pair(u, v));
        }
        if(visited[v] == -1){
            father[v] = u;
            bridgesAux(v);
            low[u] = min(low[u], low[v]);
            if(low[v] > visited[u]){
                bridges.insert(make_pair(u, v));
            }
        } else if(v != father[u]){
            low[u] = min(low[u], visited[v]);
        }
    }
}

void bridgesTarjan(){
    int i;
    for(i = 1; i < n; i++){
        low[i] = -1;
        visited[i] = -1;
        father[i] = -1;
    }
    t = 0;
    for(i = 1; i < n; i++){
        if(visited[i] == -1){
            bridgesAux(i);
        }
    }
}

int main(){
    int m, x, y, i, j, cont = 1;
    cin >> n >> m;
    while(n != 0 && m != 0){
        n++;
        for(i = 1; i < n; i++){
            G[i].clear();
        }
        bridges.clear();
        streets.clear();
        for(i = 0; i < m; i++){
            cin >> x >> y;
            G[x].push_back(y);
            G[y].push_back(x);
        }

        bridgesTarjan();
        
        cout << cont << endl << endl;
        
        //cout << "Total de Streets: " << streets.size() << endl;
        for(set<pair<int, int> >::iterator it = streets.begin(); it !=  streets.end(); ++it){
            cout << it->first << " " << it->second << endl;
            
            if(bridges.find(make_pair(it->first, it->second)) != bridges.end() || bridges.find(make_pair(it->second, it->first)) != bridges.end()){
                cout << it->second << " " << it->first << endl;
            }
            
        }
        
        cout << "#" << endl;
        cont++;

        cin >> n >> m;
    }

}