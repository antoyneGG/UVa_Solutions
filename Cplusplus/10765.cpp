/*
Author: Fabian Antoyne Garcia Gallego
Problem: 10765 - Doves and Bombs
Credits: tarjanAP  by Carlos Alberto Ramirez Restrepo
*/

#include <iostream>
#include <vector>
#include <set>
#include <bits/stdc++.h>

using namespace std;

int n, t;
vector<vector<int>> G(10001);
int visited[10001];
int low[10001];
int father[10001];
int values[10001];
set<int> apNodes;

bool comparator(int x, int y){
    return (values[x] > values[y] || (values[x] == values[y] && x < y));
}

void apTarjanAux(int u){
    int i, v, numSons;
    numSons = 0;
    t++;
    visited[u] = t;
    low[u] = t;

    for(i = 0; i < G[u].size(); i++){
        v = G[u][i];
        if(visited[v] == -1){
            numSons++;
            father[v] = u;
            apTarjanAux(v);
            low[u] = min(low[u], low[v]);
            if(father[u] != -1 && low[v] >= visited[u]){
                apNodes.insert(u);
                values[u] += 1;
            }
        } else if(v != father[u]){
            low[u] = min(low[u], visited[v]);
        }
    }
    if(father[u] == -1 && numSons > 1){
        apNodes.insert(u);
        values[u] += numSons;
    } else if(father[u] == -1){
        values[u] += numSons;
    } else if(father[u] != -1){
        values[u] += 1;
    }
}

void apTarjan(){
    int i;
    for(i = 0; i < n; i++){
        low[i] = -1;
        visited[i] = -1;
        father[i] = -1;
        values[i] = 0;
    }
    t = 0;
    for(i = 0; i < n; i++){
        if(visited[i] == -1){
            apTarjanAux(i);
        }
    }
}

int main(){
    int m, i, j, x, y;
    cin >> n >> m;
    while(n != 0 && m != 0){
        cin >> x >> y;
        for(i = 0; i < n; i++){
            G[i].clear();
        }
        apNodes.clear();
        while(x != -1 && y != -1){
            G[x].push_back(y);
            G[y].push_back(x);
            cin >> x >> y;
        }

        apTarjan();

        vector<int> v(apNodes.begin(), apNodes.end());
        sort(v.begin(), v.end(), comparator);

        /*
        cout << "[";
        for(j = 0; j < n; j++){
            cout << father[j] << ", ";
        }
        cout << "]" << endl;
        */
        vector<int>::iterator it = v.begin();
        while(it != v.end() && m != 0){
            cout << *it << " " << values[*it] << endl;
            visited[*it] = -2;
            m--;
            ++it;
        }
        i = 0;
        while(i < n && m != 0){
            if(visited[i] != -2){
                cout << i << " " << values[i] << endl;
                m--;
            }
            i++;
        }

        cout << endl;

        cin >> n >> m;
    }
}