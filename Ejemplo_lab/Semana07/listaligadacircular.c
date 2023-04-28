#include <stdio.h>
#include <stdlib.h>

struct Nodo {
    int dato;
    struct Nodo *siguiente;
};

struct Nodo* addToEmpty(struct Nodo* ultimo, int dato) {
    if (ultimo != NULL)
    {
        return ultimo;
    }

    //asigns memoria al nuevo nodo
    struct Nodo* nuevoNodo = (struct Nodo*)malloc(sizeof(struct Nodo));

    //se asignna dato al nuevo nodo
    nuevoNodo->dato = dato;

    //se asigna como ultimo al nuevo nodo
    ultimo = nuevoNodo;

    //Se crea enlace a si mismo
    ultimo->siguiente = ultimo;

    return ultimo;
}

//agregar nodo por el frente
struct Nodo* addFront(struct Nodo* ultimo, int  dato){
    
    //se revisa si la lista está vacía
    
    if(ultimo == NULL){
        return addToEmpty(ultimo, dato);
    }
    
    //Se asigna memoria al nuevo nodo
    struct Nodo* nuevoNodo = (struct Nodo*)malloc(sizeof(struct Nodo));
    
    //se agraga dato al nuevo nodo
    nuevoNodo->dato = dato;
    
    //se guarda la dirección del primer nodo actual en el nuevo nodo
    nuevoNodo->siguiente = ultimo->siguiente;
    
    //Se hace al nuevo nodo como la cabeza
    ultimo->siguiente = nuevoNodo;

    return ultimo;
}

//agregar nodo final
struct Nodo* addEnd(struct Nodo* ultimo, int dato){
    
    //se revisa si el nodo está vacío
    
    if(ultimo == NULL){
        return addToEmpty(ultimo, dato);
    }
    
    //Se asigna memoria al nuevo nodo
    struct Nodo* nuevoNodo = (struct Nodo*)malloc(sizeof(struct Nodo));
    
    //se agraga dato al nuevo nodo
    nuevoNodo->dato = dato;
    
    //se almacena la dirección del nodo cabeza al siguiente del nuevo nodo
    nuevoNodo->siguiente = ultimo->siguiente;
    
    //Se hace al nuevo nodo como el último nodo
    ultimo->siguiente = nuevoNodo;

    //Se hace al nuevo nodo como el último nodo
    ultimo = nuevoNodo;

    return ultimo;
}

// insertar nodo después de un nodoespecífico

struct Nodo* addAfter(struct Nodo* ultimo, int dato, int objeto){
    
    //se revisa si el nodo está vacío
    
    if(ultimo == NULL){
        return addToEmpty(ultimo, dato);
    }
    struct Nodo *nuevoNodo, *p;

    p= ultimo->siguiente;

    do{
        //si se encontó el elemento, se coloca el nuevo no después de él
        if(p->dato == objeto) 
        {    
            //Se asigna memoria al nuevo nodo
            struct Nodo* nuevoNodo = (struct Nodo*)malloc(sizeof(struct Nodo));
            
            //se agraga dato al nodo
            nuevoNodo->dato = dato;
            
            //se hace como siguiente el nodo actual siguiente del nuevo nodo
            
            nuevoNodo->siguiente = p->siguiente;
            
            //Se pone el nuevo nodo como siguiente de p
            p->siguiente = nuevoNodo;

            //si p es el último nodo, se hace al nuevo nodo como el último nodo
            if(p == ultimo)
            {
                ultimo = nuevoNodo;
            }

            return ultimo;
        }

        p = p->siguiente;
    } while (p != ultimo->siguiente);

    printf("\nEl nodo dado no esta presente en la lista");

    return ultimo;
}

//borrar un nodo
void delateNodo(struct Nodo** ultimo, int llave){
    
    //si la lista ligada está vacía
    
    if(*ultimo = NULL)
    {
        return;
    }

    //si la lista contiene solo un nodo

    if((*ultimo)->dato == llave && (*ultimo)-> siguiente == *ultimo)
    {
        free(*ultimo);
        *ultimo = NULL;
        return;
    }

    struct Nodo *temporal = *ultimo, *d;

    //si se va a eliminar el último
    
    if((*ultimo)->dato == llave) 
    {
        //encontrar el nodo antes del último nodo
        while (temporal->siguiente != *ultimo)
        {
            temporal = temporal->siguiente;
        }

        // apuntar un nodo temporal al siguiente del último es decir el primer nodo
        temporal->siguiente = (*ultimo)->siguiente;
        free(*ultimo);
        *ultimo=temporal->siguiente;
    }

    //recorido al nodo que va ser eliminado
    while ( temporal->siguiente != *ultimo && temporal->siguiente->dato != llave)
    {
        temporal = temporal->siguiente;
    }

    //Si el nodo a eliminar se encuentra
    if (temporal->siguiente->dato = llave)
    {
        d = temporal->siguiente;
        temporal->siguiente = d->siguiente;
        free(d);
    }
}

void traverse(struct Nodo* ultimo) 
{
    struct Nodo *p;

    if(ultimo = NULL)
    {
        printf("La lista esta vacía");
        return;
    }

    p = ultimo->siguiente;

    do
    {
        printf("%d", p->dato);
        p = p->siguiente;

    }while( p != ultimo->siguiente);
}

int main() 
{
    struct Nodo* ultimo = NULL;

    ultimo = addToEmpty(ultimo, 6);
    ultimo = addEnd(ultimo, 8);
    ultimo = addFront(ultimo, 2);

    ultimo = addAfter(ultimo, 10, 2);

    traverse(ultimo);

    delateNodo(&ultimo, 8);

    printf("\n");

    traverse(ultimo);

    return 0;
}