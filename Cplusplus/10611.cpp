/*
█ Problema 10611 - The Playboy Chimp
*/

#include <iostream>

using namespace std;

int main(){
    int i, n, q, querie, lady, firstL, lastL, midL, l1, l2, cont = 1;
    bool querieFound;
    cin >> n;
    int ladies[n];
    cin >> ladies[0];
    for(i = 1; i < n; i++){
        cin >> lady;
        if(lady != ladies[cont - 1]){
            ladies[cont] = lady;
            cont++;
        }
    }
    cin >> q;
    int queries[q];
    for(i = 0; i < q; i++){
        cin >> queries[i];
    }
    for(i = 0; i < q; i++){
        n = cont;
        querie = queries[i];
        firstL = 0;
        lastL = n - 1;
        querieFound = false;
        if(firstL == lastL){
            l1 = ladies[0];
            l2 = ladies[0];
        } else{
            while(firstL != lastL - 1 && !querieFound){
                midL = firstL + ((lastL - firstL)/2);
                if(ladies[midL] == querie){
                    l1 = midL - 1;
                    l2 = midL + 1;
                    querieFound = true;
                } else if(querie < ladies[midL]){
                    lastL = midL;
                } else if(querie > ladies[midL]){
                    firstL = midL;
                }
            }
            if(!querieFound){
                l1 = firstL;
                l2 = lastL;
            }
        }
        if(querie > ladies[n-1]){
            cout << ladies[l2] << " X" << endl;
        } else if(querie == ladies[n-1]){
            cout << ladies[l1] << " X" << endl;
        } else if(querie < ladies[0]){
            cout << "X " << ladies[l1] << endl;
        } else if(querie == ladies[0]){
            cout << "X " << ladies[l2] << endl;
        } else{
            cout << ladies[l1] << " " << ladies[l2] << endl;
        }
    }
    return 0;
}