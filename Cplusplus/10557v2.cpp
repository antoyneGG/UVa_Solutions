/*
Author: Fabian Antoyne Garcia Gallego
Problem: 10557 - XYZZY
Credits: dfs-list-ady and dijkstra by Carlos Alberto Ramirez Restrepo
*/

#include <iostream>
#include <vector>
#include <queue>
#include <deque>
#include <climits>

using namespace std;

int n = 101;
vector<vector<int>> G(101);
vector<int> energies(101);
vector<int> d(101);
vector<int> counter(101);
vector<int> visited(101);

bool dfsAux(int u){
    int v, i;
    visited[u] = 1;
    if(u == n - 1){
        return true;
    }
    for(i = 0; i < G[u].size(); i++){
        v = G[u][i];
        if(visited[v] == -1){
            if(dfsAux(v)){
                return true;
            }
        }
    }
    return false;
}

bool dfs(int u){
    int i;
    for(i = 0; i < n; i++){
        visited[i] = -1;
    }
    return dfsAux(u);
}

bool dijkstra(){
    int i, j, k, u, v, weight, cost;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>> > cola;

    for(i = 0; i < n; i++){
        d[i] = INT_MIN;
        counter[i] = 0;
    }

    d[1] = 100;
    cola.push(make_pair(100, 1));

    while(!cola.empty()){
        cost = cola.top().first;
        u = cola.top().second;
        cola.pop();

        if(cost == d[u]){
            for(j = 0; j < G[u].size(); ++j){
                v = G[u][j];
                weight = energies[v];
                if(d[u] != INT_MIN && d[u] + weight > 0 && d[u] + weight > d[v] && counter[v] <= n){
                    d[v] = d[u] + weight;
                    counter[v]++;
                    cola.push(make_pair(d[v], v));
                } else if(counter[v] > n && d[u] + weight > 0 && d[u] + weight > d[v]){
                    if(dfs(v)){
                        return true;
                    }
                }
            }
        }
    }
    //printf("dis: %d\n", d[n - 1]);
    if(d[n - 1] > 0){
        return true;
    }
    return false;
}

int main(){
    int i, j, m, y, energy, sum = 0;
    cin >> n;
    while(n != -1){
        n++;
        for(i = 1; i < n; i++){
            G[i].clear();
            energies[i] = 0;
        }
        for(i = 1; i < n; i++){
            cin >> energy;
            cin >> m;
            energies[i] = energy;
            for(j = 0; j < m; j++){
                cin >> y;
                G[i].push_back(y);
            }
        }
        
        
        if(dijkstra()){
            printf("winnable\n");
        } else{
            printf("hopeless\n");
        }
        
        
        /*
        if(tarjan() || dijkstra()){
            printf("winnable => %d, %d\n", n - 1, sum);
        } else{
            printf("hopeless => %d, %d\n", n - 1, sum);
        }
        sum += n - 1;
        */

        //printf("%d\n", d[n - 1]);

        /*
        for(i = 0; i < n; ++i)
            printf("Distancia a nodo %d: %d\n", i, d[i]);
        */
    
        cin >> n;
    }

    return 0;
}