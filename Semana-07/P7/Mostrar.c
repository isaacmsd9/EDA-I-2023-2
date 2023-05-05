#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

Node *head = NULL;

void insert(int data) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = head;
    if (head == NULL) {
        head = newNode;
        newNode->next = head;
    } else {
        Node *temp = head;
        while (temp->next != head) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

void search(int key) {
    Node *current = head;
    if (head == NULL) {
        printf("\nLa lista está vacía\n");
    } else {
        do {
            if (current->data == key) {
                printf("\n%d se encuentra en la estructura!\n", key);
                return;
            }
            current = current->next;
        } while (current != head);
        printf("\n%d no se encuentra en la estructura...\n", key);
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
    insert(1);
    insert(2);
    insert(3);

    int key;
    printf("Bienvenido va a realizar una busqueda\n");
    printf("Ingrese el valor: ");
    scanf("%d", &key);

    search(key);
    display();

    return 0;
}
