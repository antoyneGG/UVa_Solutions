/*
Author: Fabian Antoyne Garcia Gallego
Problem: 10342 - Always Late
Credits: dijkstra by Carlos Alberto Ramirez Restrepo
*/

#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

int n = 100;
vector<vector<pair<int, int>>> G(100);
vector<int> father(100);
vector<int> d(100);
vector<int> d2(100);

int dijkstra(int s, int query){
    int i, j, k, u, v, weight, cost, secondPath = INT_MAX;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> queue;

    for(i = 0; i < n; i++){
        d[i] = INT_MAX;
        d2[i] = INT_MAX;
        father[i] = -1;
    }

    d[s] = 0;

    queue.push(make_pair(0, s));

    while(!queue.empty()){
        cost = queue.top().first;
        u = queue.top().second;
        queue.pop();
        
        //if(cost == d[u]){
            for(j = 0; j < G[u].size(); j++){
                v = G[u][j].first;
                weight = G[u][j].second;
                if(v == query){
                    //printf("%d -> %d: %d\n", u, v, d[u] + weight);
                }
                if(d[u] != INT_MAX && d[u] + weight < d[v]){
                    if(v == query && d[v] < secondPath){
                        secondPath = d[v];
                    }
                    d2[v] = d[v];
                    d[v] = d[u] + weight;
                    father[v] = u;
                    queue.push(make_pair(d[v], v));
                } else if(d2[u] != INT_MAX && d2[u] + weight < d2[v] && d2[u] + weight > d[v]){
                    
                    d2[v] = d2[u] + weight;
                    if(v == query && d2[v] < secondPath){
                        secondPath = d2[v];
                    }
                    queue.push(make_pair(d2[v], v));
                } else if(d[u] != INT_MAX && d[u] + weight < d2[v] && d[u] + weight > d[v]){
                    
                    d2[v] = d[u] + weight;
                    if(v == query && d2[v] < secondPath){
                        secondPath = d2[v];
                    }
                    queue.push(make_pair(d2[v], v));
                }
                //printf("es %d\n", secPath);
            }
        //}
    }

    return secondPath;

}



int main(){
    int m, i, x, y, val, q, cont = 1, min, secondPath;
    while(cin >> n >> m){
        for(i = 0; i < n; i++){
            G[i].clear();
        }
        for(i = 0; i < m; i++){
            cin >> x >> y >> val;
            G[x].push_back(make_pair(y, val));
            G[y].push_back(make_pair(x, val));
        }
        cin >> q;
        printf("Set #%d\n", cont);
        for(i = 0; i < q; i++){
            cin >> x >> y;
            
            secondPath = dijkstra(x, y);
            //secondPath = bellmanFord(x, y);
            //printf("el minimo es %d\n", d[y]);
            if(secondPath != INT_MAX){
                /*
                secondPath = INT_MAX;
                for(int j = 0; j < 100; j++){
                    if(d[j][y] < secondPath && d[j][y] != min){
                        secondPath = d[j][y];
                    }
                }
                */
                printf("%d\n", secondPath);
            } else{
                printf("?\n");
            }
            
            //printf("%d\n", dijkstra(x, y));
            
        }

        
        /*
        for(i = 0; i < n; ++i){
            //for(int j = 0; j < n; j++){
                printf("Distancia a nodo %d con %d aristas es %d\n", y, i, d[i][y]);
            //}
            //cout << "Distancia a nodo " << i << ": " << d[i][n - 1] << endl;
            
        }
        */
        cont++;
    }

    return 0;
}