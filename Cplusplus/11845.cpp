/*
Author: Fabian Antoyne Garcia Gallego
Problem: 11845 - Preferential Romance
Credits: tarjan2 by Carlos Alberto Ramirez Restrepo
*/

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <bits/stdc++.h>
#include <iterator>
#include <algorithm>

using namespace std;

int cont = 0, numSCC, t = 0;
vector<vector<int>> G(100);
int visited[100];
int low[100];
bool inStack[100];
stack<int> stackSCC;
vector<vector<int>> sccNodes;
set<vector<int>> connections;

bool check(int num){
    int j, i;
    for(i = 0; i < sccNodes.size(); i++){
        if(sccNodes[i].size() > 1){
            for(j = 0; j < sccNodes[i].size(); j++){
                if(num == sccNodes[i][j]){
                    return true;
                }
            }
        }
    }
    return false;
}

bool search(){
    int i;
    for(i = 0; i < sccNodes.size(); i++){
        if(sccNodes[i].size() > 1){
            return false;
        }
    }
    return true;
}

void tarjanAux(int u){
    int v, i;
    //printf("hola\n");
    visited[u] = low[u] = ++t;
    stackSCC.push(u);
    inStack[u] = true;

    for(i = 0; i < G[u].size(); i++){
        v = G[u][i];
        if(visited[v] == -1){
            tarjanAux(v);
            low[u] = min(low[u], low[v]);
        } else if(inStack[v]){
            low[u] = min(low[u], visited[v]);
        }
    }

    if(low[u] == visited[u]){
        //cout << "SCC con indice " << low[u] << ": ";
        sccNodes.push_back(vector<int>());
        numSCC++;
        while(stackSCC.top() != u){
            //cout << stackSCC.top() << " ";
            inStack[stackSCC.top()] = false;
            sccNodes[numSCC - 1].push_back(stackSCC.top());
            stackSCC.pop();
        }
        //cout << stackSCC.top() << endl;
        inStack[stackSCC.top()] = false;
        sccNodes[numSCC - 1].push_back(stackSCC.top());
        stackSCC.pop();
    }
}

void tarjan(){
    int i;

    for(i = 0; i < cont; i++){
        low[i] = visited[i] = -1;
        inStack[i] = false;
    }
    numSCC = 0;
    for(i = 0; i < cont; i++){
        if(visited[i] == -1){
            tarjanAux(i);
        }
    }
}

int main(){
    int i, x, y, j;
    bool elim;
    string name1, name2, line, element, tempL;
    cin >> name1 >> name2;
    //cout << name1 << " " << name2 << endl;
    //printf("%d", name1.compare("*"));
    cin.ignore();
    while(name1.compare("*") != 0 || name2.compare("*") != 0){
        for(i = 0; i < cont; i++){
            G[i].clear();
        }
        sccNodes.clear();
        connections.clear();
        cont = 0;
        map<string, int> preferences;
        map<string, int>::iterator itr;
        for(i = 0; i < 2; i++){
            element = " ";
            getline(cin, line);
            for(j = 0; j < line.size(); j++){
                //cout << (int)line[j] << endl;
                if(line[j] < 91 && line[j] > 64){
                    tempL = (char)((int)line[j] + 32);
                    line.replace(j, 1, tempL);
                }
                /*
                if((line[j] == ',' || line[j] == ';') && j != 0){
                    line.insert(j, " ");
                    j++;
                }
                */
            }
            //cout << line << endl;
            stringstream tok(line);

            while(element.compare(";") != 0){
                vector<int> conn;
                tok >> element;
                if(preferences.find(element) == preferences.end()){
                    preferences.insert(pair<string, int>(element, cont));
                    x = cont;
                    cont++;
                    //cout << "El elemento " << element << " tiene el nodo: " << x << endl;
                } else{
                    itr = preferences.find(element);
                    x = itr->second;  
                }
                conn.push_back(x); 
                tok >> element;
                while(element.compare(",") != 0 && element.compare(";") != 0){
                    if(preferences.find(element) == preferences.end()){
                        preferences.insert(pair<string, int>(element, cont));
                        y = cont;
                        cont++;
                        //cout << "El elemento " << element << " tiene el nodo: " << y << endl;
                    } else{
                        itr = preferences.find(element);
                        y = itr->second;  
                    }
                    conn.push_back(y);
                    G[x].push_back(y);
                    x = y;
                    tok >> element;
                }
                connections.insert(conn);
            }
        }
        
        /*
        for(set<vector<int>>::iterator it = connections.begin(); it != connections.end(); ++it){
            vector<int> temp = *it;
            printf("[");
                for(i = 0; i < temp.size(); i++){
                    printf("%d, ", temp[i]);
                }
            printf("], ");
        }
        cout << endl;
        */

        tarjan();
        
        for(set<vector<int>>::iterator it = connections.begin(); it != connections.end(); ++it){
            elim = false;
            vector<int> temp = *it;
            for(i = 0; i < temp.size(); i++){
                if(!check(temp[i])){
                    elim = true;
                }
            }
            if(elim){
                temp.clear();
            }
        }

        /*
        printf("Grafo\n");
        for(i = 0; i < cont; ++i){
            printf("Nodo %d:", i);
            for(int j = 0; j < G[i].size(); ++j)
                printf(" %d", G[i][j]);
            printf("\n");
        }
        */

        if(search()){
            printf("F\n");
        } else{
            bool passably = false;
            set<vector<int>>::iterator it = connections.begin();
            vector<int>::iterator pos;
            while(it != connections.end() && !passably){
                i = 0;
                vector<int> temp = *it;
                while(i != temp.size() && !passably){
                    if(i != temp.size() - 1){
                        pos = find(G[temp[i]].begin(), G[temp[i]].end(), temp[i + 1]);
                        G[temp[i]].erase(pos);
                        sccNodes.clear();
                        tarjan();
                        if(search()){
                            passably = true;
                        } else{
                            G[temp[i]].push_back(temp[i + 1]);
                        }
                        //remove(G[temp[i]].begin(), G[temp[i]].end(), temp[i + 1]);
                        //printf("Al nodo %d le quito el %d.\n", temp[i], temp[i + 1]);
                    }
                    i++;
                }
                
                
                /*
                printf("Grafo\n");
                for(i = 0; i < cont; ++i){
                    printf("Nodo %d:", i);
                    for(int j = 0; j < G[i].size(); ++j)
                        printf(" %d", G[i][j]);
                    printf("\n");
                }
                */

                
                ++it;
            }
            if(passably){
                printf("P\n");
            } else{
                printf("N\n");
            }
        }

        cin >> name1 >> name2;
        cin.ignore();
        
    }
}