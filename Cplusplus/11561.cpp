/*
Author: Fabian Antoyne Garcia Gallego
Problem: 11561 - Getting Gold
Credits: dfs-list-ady and solution to problem 784 by Carlos Alberto Ramirez Restrepo
*/

#include <iostream>

using namespace std;

int n, m;
int gold;
char map[51][51];
int cambioX[] = {1, 0, -1, 0};
int cambioY[] = {0, 1, 0, -1};

void dfsAux(int x, int y){
    int nextX, nextY;
    bool trapDetected = false;
    //cout << "me movi a " << "(" << x << ", " << y << ")" << " = " << map[x][y] << endl;
    if(map[x][y] == 'G'){
        gold++;
    }
    map[x][y] = '#';
    for( int i = 0; i < 4; i++){
        nextX = x + cambioX[i];
        nextY = y + cambioY[i];
        if(map[nextX][nextY] == 'T'){
            trapDetected = true;
        }
    }
    if(!trapDetected){
        for(int i = 0; i < 4; i++){
            nextX = x + cambioX[i];
            nextY = y + cambioY[i];
            if(nextX >= 0 && nextY >= 0 && nextX <= m && nextY <= n && map[nextX][nextY] != '#'){
                dfsAux(nextX, nextY);
            }
        }
    }

}

int main(){
    int i, j, playerX, playerY;
    while(cin >> n >> m){
        gold = 0;
        for( i = 0; i < m; i++){
            cin >> map[i];
        }
        for( i = 0; i < m; i++){
            for( j = 0; j < n; j++){
                //cout << map[i][j];
                if(map[i][j] == 'P'){
                    playerX = i;
                    playerY = j;
                }
            }
            //cout << endl;
        }
        dfsAux(playerX, playerY);
        cout << gold << endl;
    }
    return 0;
}