/*
Autor: Fabian Antoyne Garcia Gallego
Ejercicio numero 551 de uVa: Nesting a Bunch of Brackets
Resumen de la solucion aplicada: Se van guardando en una pila los signos de apertura,
los cuales comenzaran a desaparecer de la pila a medida que vayan ingresando a la pila sus respectivos
signos de cierre, armando cada pareja de signos "()", pero si se encuentra un signo de cierre que no coincida
con el signo de apertura que esta en el tope de la pila, se encuentra un signo de apertura que nunca cierra o
se encuentra un signo de cierre que nunca cierra nada se emitira error y se mostrara la ubicacion del error.///
*/

#include <iostream>
#include <string>
#include <stack>
#include <vector>

using namespace std;

int main(){
    string line;
    bool error;
    int cont;
    while(getline(cin, line)){
        stack<char> brackets;
        error = false;
        cont = 0;
        for(int j = 0; j < line.length(); j++){
            if(line[j] != 13){
                cont++;
            }
            if(line[j] == '(' || line[j] == '[' || line[j] == '{' || line[j] == '<'){
                if(line[j] == '(' && line[j + 1] == '*'){
                    brackets.push('|');
                    j++;
                } else{
                    brackets.push(line[j]);
                }
            } else if(line[j] == ')'){
                if(!brackets.empty() && brackets.top() == '('){
                    brackets.pop();
                } else{
                    error = true;
                }
            } else if(line[j] == ']'){
                if(!brackets.empty() && brackets.top() == '['){
                    brackets.pop();
                } else{
                    error = true;
                }
            } else if(line[j] == '}'){
                if(!brackets.empty() && brackets.top() == '{'){
                    brackets.pop();
                } else{
                    error = true;
                }
            } else if(line[j] == '>'){
                if(!brackets.empty() && brackets.top() == '<'){
                    brackets.pop();
                } else{
                    error = true;
                }
            } else if(line[j] == '*' && line[j + 1] == ')'){
                if(!brackets.empty() && brackets.top() == '|'){
                    brackets.pop();
                } else{
                    error = true;
                }
                j++;
            }
            if(error){
                cout << "NO " << cont << "\n";
                j = line.length() - 1;
            }
        }
        if(!error && !brackets.empty()){
            cout << "NO " << cont + 1 << "\n";
        } else if(!error){
            cout << "YES" << "\n";
        }
    }
    return 0;
}