/*
█ Problema 11516 - WiFi
*/

#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cmath>
#include <stdio.h>
#include <algorithm>

using namespace std;

bool check(float value, int * houses, int points, int h){
    int i = 0, j = 1;
    float point;
    printf("value: %f\n", value);
    while(j <= points && i < h){
        point = houses[i] + value;
        i++;
        while(houses[i] <= point && i < h){
            i++;
        }
        j++;
    }
    if(i == h){
        return true;
    } else{
        return false;
    }
}

int main(){
    int T, i, j, n, m;
    float result, mid, low, hi;
    cin >> T;
    for(i = 0; i < T; i++){
        cin >> n;
        cin >> m;
        int houses[m];
        for(j = 0; j < m; j++){
            cin >> houses[j];
        }
        sort(houses, houses + m);
        if(n >= m || n == 0){
            result = 0.0; 
        } else{
            low = 1.0;
            hi = houses[m-1];
            while(low + 1 != hi){
                printf("%d y %d\n", (int)hi, (int)low);
                mid = ((int)hi + (int)low)/2;
                if(check(mid, houses, n, m)){
                    hi = mid;
                } else{
                    low = mid;
                }
            }
            printf("%f\n", hi);
            result = hi/2;
            result = floor(10 * result) / 10;
        }
        printf("%0.1lf", result);
        cout << endl;
    }
    return 0;
}