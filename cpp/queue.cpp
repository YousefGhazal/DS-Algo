#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
    Node()
    {
        data = 0;
        next = NULL;
    };
};
class Queue
{
public:
    Node *front;
    Node *rear;
    Queue()
    {
        front = rear = NULL;
    };
    bool IsEmpty()
    {
        if (front == NULL)
            return true;
        else
            return false;
    };
    void Enqueue(int item)
    {
        Node *newnode = new Node();
        newnode->data = item;
        if (IsEmpty())
        {
            front = rear = newnode;
        }
        else
        {
            rear->next = newnode;
            rear = newnode;
        }
    };
    void Display()
    {
        Node *temp = front;
        while (temp != NULL)
        {
            cout << temp->data << endl;
            temp = temp->next;
        }
    }
    int Dequeue()
    {
        int value = -1;
        if (IsEmpty())
        {
            cout << "queue is empty\n";
        }
        else if (front == rear)
        {
            value = front->data;
            delete front;
            front = rear = NULL;
        }
        else
        {
            Node *delptr = front;
            value = front->data;
            front = front->next;
            delete delptr;
        }
        return value;
    }
    void Clear()
    {
        while (!IsEmpty())
        {
            Dequeue();
        }
    }
};
int main() {}