/*
Autor: Fabian Antoyne Garcia Gallego
Ejercicio numero 11234 de uVa: Expressions
Resumen de la solucion aplicada: Se implemento la estructura de Nodo, esto con el fin de construir un arbol para
cada expresion recibida. Este arbol se contruye recorriendo la expresion desde el final hasta el inicio, de modo
que se vaya armando el arbol desde el operador final y de mayor relevancia hasta la o las parejas de operandos
mas profundas de la expresion. Y la finalidad de construir un arbol se debe a que es la manera que halle para
recorrer la expresion reestructurada de manera que pueda quedar lista para ser leida y procesada por una queue.
Si es cierto que fui advertido de que este ejercicio se puede resolver sin la necesidad de un arbol, pero lo
reintente y no di con otra solucion. Si me gustaria saber como seria esa otra solucion, si se puede claro.
*/

#include <iostream>
#include <queue>
#include <string>
#include <stack>

using namespace std;

struct Node{
    char data;
    struct Node* left;
    struct Node* right;

    Node(char val){
        data = val;
        left = NULL;
        right = NULL;
    }
};

int makeTree( Node * root, string * exp, int height){
    int Hl = height, Hr = height;
    if(*(exp->end()-2) > 96 && *(exp->end()-3) > 96){
        root->left = new Node(*(exp->end()-2));
        root->right = new Node(*(exp->end()-3));
        exp->erase(exp->end()-1);
        exp->erase(exp->end()-1);
        return ++height;
    }
    if(*(exp->end()-2) > 96){
        root->left = new Node(*(exp->end()-2));
        exp->erase(exp->end()-1);

    } else if(*(exp->end()-2) < 96){
        root->left = new Node(*(exp->end()-2));
        exp->erase(exp->end()-1);
        Hl = makeTree(root->left, exp, Hl);
    }
    if(*(exp->end()-2) > 96){
        root->right = new Node(*(exp->end()-2));
        exp->erase(exp->end()-1);
    } else if(*(exp->end()-2) < 96){
        root->right = new Node(*(exp->end()-2));
        exp->erase(exp->end()-1);
        Hr = makeTree(root->right, exp, Hr);
    }
    if(Hl > Hr){
        return ++Hl;
    } else{
        return ++Hr;
    }
}

void levelOrder( Node * root, int level ){
   if( !root )
      return;
   if( level == 1 )
      cout << root->data;
   else if( level > 1 ){
      levelOrder( root->left, level - 1 );
      levelOrder( root->right, level - 1 );
   }
}

int main(){
    int cases;
    cin >> cases;
    for(int i = 0; i < cases; i++){
        int height;
        string expression;
        cin >> expression;
        Node * root = new Node(*(expression.end()-1));
        height = makeTree(root, &expression, 1);
        for( int i = height; i >= 1; i--){
            levelOrder( root, i );
        }
        cout << endl;
    }
    return 0;
}
