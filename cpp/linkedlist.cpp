#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
};
class Linkedlist
{
public:
    Node *head;
    Linkedlist()
    {
        head = NULL;
    }
    bool isempty()
    {
        return (head == NULL);
    }
    void InsertFirst(int newvalue)
    {
        Node *newnode = new Node;
        newnode->data = newvalue;
        if (isempty())
        {
            newnode->next = NULL;
            head = newnode;
        }
        else
        {
            newnode->next = head;
            head = newnode;
        }
    }
    void Display()
    {
        Node *temp = head;
        while (temp != NULL)
        {
            cout << temp->data << " ";
            temp = temp->next;
        }
    }
    int Count()
    {
        int counter = 0;
        Node *temp = head;
        while (temp != NULL)
        {
            counter++;
            temp = temp->next;
        }
        return counter;
    }
    bool Isfound(int key)
    {
        bool found = false;
        Node *temp = head;
        while (temp != NULL)
        {
            if (temp->data == key)
            {
                found = true;
                break;
            }
            temp = temp->next;
        }
        return found;
    }
    void InsertBefore(int item, int newvalue)
    {
        if (Isfound(item))
        {

            Node *newnode = new Node();
            newnode->data = newvalue;
            Node *temp = head;
            while (temp != NULL && temp->next->data != item)
            {
                temp = temp->next;
            }
            newnode->next = temp->next;
            temp->next = newnode;
        }
        else
        {
            cout << "Sorry, item not found \n";
        }
    }
    void Append(int value)
    {
        Node *newnode = new Node();
        newnode->data = value;
        Node *temp = head;
        while (temp->next != NULL)
        {
            temp = temp->next;
        }
        temp->next = newnode;
        newnode->next = NULL;
    }
    void Delete(int item)
    {
        if (isempty())
        {
            cout << "List is empty, no items to delete \n";
        }
        Node *delptr = head;
        if (head->data == item)
        {
            head = head->next;
            delete delptr;
        }
        else
        {
            Node *ptr = NULL;
            delptr = head;
            while (delptr->data != item)
            {
                ptr = delptr;
                delptr = delptr->next;
            }
            ptr->next = delptr->next;
            delete delptr;
        }
    }
};

int main()
{
    Linkedlist lst;
    if (lst.isempty())
    {
        cout << "The List is Empty \n";
    }
    else
    {
        cout << "The List contains" << lst.Count() << endl;
    }
    int item;
    cout << "Enter item to insert in the list \n";
    cin >> item;
    lst.InsertFirst(item);
    lst.Display();
    cout << "Enter item to inset in the list \n";
    cin >> item;
    lst.InsertFirst(item);
    lst.Display();
    cout << "Enter item to inset in the list \n";
    cin >> item;
    lst.InsertFirst(item);
    lst.Display();
    cout << "The List contains" << lst.Count() << endl;
    cout << "Enter item to delete :";
    cin >> item;
    lst.Delete(item);
    lst.Display();

    // int newvalue;
    // cin >> newvalue;
    // lst.Append(newvalue);
    // lst.Display();
    // cin >> item;
    // cin >> newvalue;
    // lst.InsertBefore(item, newvalue);
    // lst.Display();
    // cout << "The List contains" << lst.Count() << endl;

    // cout << "Enter item to search for \n";
    // cin >> item;
    // if (lst.Isfound(item))
    // {
    //     cout << "Item Found \n";
    // }
    // else
    // {
    //     cout << "Item not Found \n";
    // }
}