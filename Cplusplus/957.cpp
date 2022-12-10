/*
█ Problema 957 - Popes
*/

#include <iostream>

using namespace std;

int main(){
    int y, p, i, fYear, lYear, low, hi, mid, max;
    bool found;
    while(cin >> y){
        cin >> p;
        int popes[p];
        for(i = 0; i < p; i++){
            cin >> popes[i];
        }
        i = 0;
        max = 0;
        while(i < p - 1){
            low = i;
            hi = p - 1;
            found = false;
            while(low != hi - 1 && !found){
                mid = low + (hi - low)/2;

                if(popes[mid]-popes[i] == y - 1){
                    found = true;
                } else if(popes[mid]-popes[i] > y - 1){
                    hi = mid;
                } else if(popes[mid]-popes[i] < y - 1){
                    low = mid;
                }
            }
            if(!found){
                mid = low;
            }
            while(popes[mid] == popes[mid + 1]){
                mid++;
            }
            if((mid - i) + 1 > max){
                max = (mid - i) + 1;
                fYear = popes[i];
                lYear = popes[mid];
            }
            i++;
        }
        cout << max << " " << fYear << " " << lYear << endl;
    }
    return 0;
}