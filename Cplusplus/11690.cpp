/*
Author: Fabian Antoyne Garcia Gallego
Problem: 11690 - Money Matters
Credits: dfs-list-ady by Carlos Alberto Ramirez Restrepo
*/

#include <iostream>
#include <vector>

using namespace std;

int n = 10001;
int debt = 0;
bool possible = true;
vector<vector<int>> G(n);
vector<int> visited(n);
vector<int> values(n);

void dfsAux(int u){
    int i, v;
    visited[u] = 1;
    debt = debt + values[u];
    //printf("la deuda es: %d\n", debt);
    for(i = 0; i < G[u].size(); i++){
        v = G[u][i];
        if(visited[v] == 0){
            dfsAux(v);
        }
    }
}

void dfs(){
    int i;
    for(i = 0; i < n; i++){
        visited[i] = 0;
    }

    for(i = 0; i < n; i++){
        if(visited[i] == 0){
            debt = 0;
            dfsAux(i);
            //printf("%d\n", debt);
            if(debt != 0){
                possible = false;
            }
        }
    }
}

int main(){
    int m, t, i, x, y, N, sum;
    cin >> N;
    for(t = 0; t < N; t++){
        //sum = 0;
        cin >> n >> m;
        for(i = 0; i < n; i++){
            G[i].clear();
            values[i] = 0;
        }
        for(i = 0; i < n; i++){
            cin >> values[i];
            //sum = sum + values[i];
        }
        for(i = 0; i < m; i++){
            cin >> x >> y;
            G[x].push_back(y);
            G[y].push_back(x);
            //printf("x: %d, y: %d\n", x, y);
        }
        //printf("suma es %d\n", sum);
        possible = true;
        dfs();
        //printf("%d\n", possible);
        /*
        printf("Grafo\n");
        for(i = 0; i < n; ++i){
            printf("Nodo %d:", i);
            for(int j = 0; j < G[i].size(); ++j)
                printf(" %d", G[i][j]);
            printf("\n");
        }
        */
        if(possible){
            printf("POSSIBLE\n");
        } else{
            printf("IMPOSSIBLE\n");
        }

    }
}