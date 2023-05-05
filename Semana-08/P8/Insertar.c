#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
    struct Node *prev;
} Node;

Node *head = NULL;

void insert(int data, int position) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    if (head == NULL) {
        newNode->next = newNode->prev = newNode;
        head = newNode;
        return;
    }
    Node *temp = head;
    if (position == 0) {
        newNode->prev = temp->prev;
        temp->prev->next = newNode;
        newNode->next = temp;
        temp->prev = newNode;
        head = newNode;
    } else {
        for (int i = 0; i < position - 1; i++) {
            temp = temp->next;
        }
        newNode->next = temp->next;
        temp->next->prev = newNode;
        newNode->prev = temp;
        temp->next = newNode;
    }
}

void delete(int position) {
    if (head == NULL) {
        printf("\nLa lista está vacía\n");
        return;
    }
    Node *temp = head;
    if (position == 0) {
        head->prev->next = head->next;
        head->next->prev = head->prev;
        head = head->next;
        free(temp);
    } else {
        for (int i = 0; i < position; i++) {
            temp = temp->next;
        }
        temp->prev->next = temp->next;
        temp->next->prev = temp->prev;
        free(temp);
    }
}

void display() {
    if (head == NULL) {
        printf("\nLa lista está vacía\n");
    } else {
        Node *temp = head;
        printf("\nMostrando estructura:\n");
        do {
            printf("--> %d ", temp->data);
            temp = temp->next;
        } while (temp != head);
        printf("-->\n");
    }
}

int main() {
    insert(1, 0);
    insert(2, 1);
    insert(3, 2);

    int option, data, position;
    
    display();

    printf("\nBienvenido va a realizar una operacion\n");
    printf("\n1 Insertar\n");
    printf("2 Eliminar\n");
    printf("\nIngrese la opcion: ");
    scanf("%d", &option);

    switch (option) {
        case 1:
            printf("\nIngrese el valor: ");
            scanf("%d", &data);
            printf("Ingrese la posición: ");
            scanf("%d", &position);
            insert(data, position);
            printf("\n%d se ha insertado en la estructura!\n", data);
            break;
        case 2:
            printf("\nIngrese la posición: ");
            scanf("%d", &position);
            delete(position);
            printf("\nSe ha borrado el elemento en la posición %d de la estructura!\n", position);
            break;
        default:
            printf("\nOpción inválida\n");
            break;
    }

    display();

    return 0;
}