#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

struct node* createNode(int data) {
    struct node* ptr = (struct node*)malloc(sizeof(struct node));
    ptr->data = data;
    ptr->next = NULL;
    return ptr;
}

struct node* push(int data, struct node* top) {
    struct node* p = createNode(data);
    p->data = data;
    p->next = top;
    return p;
}

int isEmpty(struct node* top) {
    return top == NULL;
}

struct node* pop(struct node* top) {
    if (isEmpty(top)) {
        printf("Stack Underflow\n");
        return NULL;
    } else {
        struct node* temp = top;
        top = top->next;
        printf("Popped element %d\n", temp->data);
        free(temp);
        return top;
    }
}


void display(struct node* top) {
    if (isEmpty(top)) {
        printf("Stack is empty\n");
    } else {
        printf("Stack elements: ");
        while (top != NULL) {
            printf("%d ", top->data);
            top = top->next;
        }
        printf("\n");
    }
}

int main() {
    struct node *top = NULL;
    int choice, value;

    do {
        printf("\nStack Menu:\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter the value to push: ");
                scanf("%d", &value);
                top = push(value, top);
                break;
            case 2:
                top = pop(top);
                break;
            case 3:
                display(top);
                break;
            case 4:
                printf("Exiting the program\n");
                break;
            default:
                printf("Invalid choice. Please enter a valid option.\n");
        }
    } while (choice != 4);

    return 0;
}
