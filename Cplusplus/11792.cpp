/*
Author: Fabian Antoyne Garcia Gallego
Problem: 11792 - Krochanska is Here!
Credits: bfs-list-ady by Carlos Alberto Ramirez Restrepo
*/

#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int cont = 0;
int n = 10001;
vector<int> importantCont(n);
vector<int> d(n);
vector<bool> important(n);
vector<bool> visited(n);
vector<vector<int>> G(n);
vector<int> inLines(n);
tuple<int, int> kro;

void bfsAux(int u){
    int v, w;

    queue<int> queueu;
    visited[u] = true;
    queueu.push(u);
    d[u] = 0;
    while(!queueu.empty()){
        v = queueu.front();
        queueu.pop();
        //cout << v << " - " << d[v] << endl;
        for(int i = 0; i < G[v].size(); i++){
            w = G[v][i];
            if(!visited[w]){
                d[w] = d[v] + 1;
                visited[w] = true;
                queueu.push(w);
                if(important[w]){
                    cont = cont + d[w];
                }
            }
        }
    }
}

void bfs(int init){
    for(int i = 0; i < n; i++){
        visited[i] = false;
    }
    cont = 0;
    bfsAux(init);
    if(cont < get<1>(kro)){
        kro = make_tuple(init, cont);
    } else if(cont < get<1>(kro)){
        if(init < get<0>(kro)){
            kro = make_tuple(init, cont);
        }
    }
}

int main(){
    int T, i, j, r, lines, a, b;
    cin >> T;
    while(T != 0){
        cin >> n >> lines;
        n++;
        for( i = 0; i < n; i++){
            inLines[i] = 0;
            G[i].clear();
        }
        for( i = 0; i < lines; i++){
            cin >> a;
            cin >> b;
            inLines[a]++;
            while(b != 0){
                G[a].push_back(b);
                G[b].push_back(a);
                a = b;
                inLines[a]++;
                cin >> b;
            }
        }
        for( j = 0; j < n; j++){
            important[j] = false;
        }
        for( j = 0; j < n; j++){
            if(inLines[j] >= 2){
                important[j] = true;
            }
        }
        /*
        cout << "Grafo" << endl;

        for(i = 0; i < n; ++i){
            cout << "Nodo " << i << ":";
            for(j = 0; j < G[i].size(); ++j)
            cout << " " << G[i][j];
            cout << endl;
        }
        */
        kro = make_tuple(10001, 10001);
        for( j = 0; j < n; j++){
            if(important[j]){
                bfs(j);
                //cout << "Es la estacion " << j << " y tardo " << cont << endl;
            } 
        }
        //cout << "Es la estacion " << get<0>(kro) << " y tardo " << get<1>(kro) << endl;
        cout << "Krochanska is in: " << get<0>(kro);
        cout << endl;
        T--;
    }
}