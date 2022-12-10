/*
Autor: Fabian Antoyne Garcia Gallego
Ejercicio numero 12100 de uVa: Printer Queue
Resumen de la solucion aplicada: Se crea un vector para cada caso. A este vector se le ingresan
los valores de prioridad de los elementos de la cola. Una vez se haya creado esta "cola" se va a entrar en
un ciclo el cual solo acabaria cuando la variable in_queue sea falsa, es decir, cuando el elemento que 
se esta observando haya salido de la cola. Entonces dentro de este ciclo se comienza buscando la posicion
del elemento con mayor prioridad, una vez se encuentra se reorganiza toda la cola de manera que este elemento
encontrado quede al frente de la cola, debido a su prioridad, y claramente este organizamiento se realiza manteniendo
ubicado al elemento que se esta observando, y aqui ya procede a salir el elemento que quedo al frente y se va
a repetir el proceso hasta que se verifique que efectivamente el elemento que acaba de salir era el que se estaba
observando, de este modo se procede a mostrar cuanto tiempo le tardo, tiempo que se cuenta durante todo el ciclo.
*/

#include <iostream>
#include <vector>

using namespace std;

int main(){
    int t, n, m, priority, mins, i, max_pos;
    bool in_queue;
    cin >> t;
    for(int k = 0; k < t; k++){
        cin >> n;
        cin >> m;
        mins = 0;
        vector<int> jobs;
        for(int j = 0; j < n; j++){
            cin >> priority;
            jobs.push_back(priority);
        }
        in_queue = true;
        while(in_queue){
            i = 0;
            max_pos = 0;
            while(i < jobs.size()){
                if(jobs[i] == 9){
                    max_pos = i;
                    i = jobs.size() - 1;
                } else if(jobs[i] > jobs[max_pos]){
                    max_pos = i;
                }
                i++;
            }
            for(int j = 0; j < max_pos; j++){
                jobs.push_back(jobs[0]);
                jobs.erase(jobs.begin());
                if(m == 0){
                    m = jobs.size() - 1;
                } else{
                    m--;
                }
            }
            jobs.erase(jobs.begin());
            mins++;
            if(m == 0){
                in_queue = false;
            } else{
                m--;
            }
        }
        cout << mins << endl;
    }
}