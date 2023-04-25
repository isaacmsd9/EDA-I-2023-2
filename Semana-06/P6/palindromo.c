#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Nodo {
    char dato;
    struct Nodo *siguiente;
    struct Nodo *anterior;
};

struct ColaDoble {
    struct Nodo *frente;
    struct Nodo *final;
    int size;
};

struct ColaDoble *createDeque() {
    struct ColaDoble *cola = (struct ColaDoble *)malloc(sizeof(struct ColaDoble));
    cola ->frente = cola->final = NULL;
    cola->size = 0;
    return cola;
}

void inicializar(struct ColaDoble *cola) {
    cola->frente = NULL;
    cola->final = NULL;
}

int estaVacia(struct ColaDoble *cola) {
    return cola->frente == NULL;
}

void encolarFrente(struct ColaDoble *cola, char dato) {
    struct Nodo *nuevo = (struct Nodo *)malloc(sizeof(struct Nodo));
    nuevo->dato = dato;
    nuevo->siguiente = cola->frente;
    nuevo->anterior = NULL;
    if (estaVacia(cola)) {
        cola->final = nuevo;
    } else {
        cola->frente->anterior = nuevo;
    }
    cola->frente = nuevo;
}

void encolarFinal(struct ColaDoble *cola, char dato) {
    struct Nodo *nuevo = (struct Nodo *)malloc(sizeof(struct Nodo));
    nuevo->dato = dato;
    nuevo->siguiente = NULL;
    nuevo->anterior = cola->final;
    if (estaVacia(cola)) {
        cola->frente = nuevo;
    } else {
        cola->final->siguiente = nuevo;
    }
    cola->final = nuevo;
}

char desencolarFrente(struct ColaDoble *cola) {
    if (estaVacia(cola)) {
        printf("La cola está vacía\n");
        return '\0';
    }
    struct Nodo *temporal = cola->frente;
    char dato = temporal->dato;
    cola->frente = temporal->siguiente;
    if (cola->frente == NULL) {
        cola->final = NULL;
    } else {
        cola->frente->anterior = NULL;
    }
    free(temporal);
    return dato;
}

char desencolarFinal(struct ColaDoble *cola) {
    if (estaVacia(cola)) {
        printf("La cola está vacía\n");
        return '\0';
    }
    struct Nodo *temporal = cola->final;
    char dato = temporal->dato;
    cola->final = temporal->anterior;
    if (cola->final == NULL) {
        cola->frente = NULL;
    } else {
        cola->final->siguiente = NULL;
    }
    free(temporal);
    return dato;
}

int esPalindromo(char *palabra) {
    
  struct ColaDoble *cola= createDeque();
  
  int i, n = strlen(palabra);
  
  for (i = 0; i < n; i++) {
        struct Nodo *node = (struct Nodo *)malloc(sizeof(struct Nodo));
        node->dato = palabra[i];
        node->siguiente = node->anterior = NULL;
        if (cola->final == NULL) {
            cola->frente = cola->final = node;
        } else {
            node->anterior = cola->final;
            cola->final->siguiente = node;
            cola->final = node;
        }
        cola->size++;
    }
    while (cola->size > 1) {
        if (cola->frente->dato != cola->final->dato) {
            return 0;
        }
        struct Nodo *tempFront = cola->frente;
        struct Nodo *tempRear = cola->final;
        cola->frente = cola->frente->siguiente;
        if (cola->frente != NULL) {
            cola->frente->anterior = NULL;
        }
        cola->final = cola->final->anterior;
        if (cola->final != NULL) {
            cola->final->siguiente = NULL;
        }
        free(tempFront);
        free(tempRear);
        cola->size -= 2;
    }
    return 1;
}

int main() {
  printf("Bienvenido al Revisor de Palabras\n");
  printf("\nIngrese la palabra: ");
  char palabra[100];
  scanf("%s", palabra);
  if (esPalindromo(palabra)) {
      printf("\nLa palabra %s es palíndromo!\n", palabra);
  } else {
      printf("\nLa palabra %s no es palíndromo!\n", palabra);
  }
  return 0; 
}