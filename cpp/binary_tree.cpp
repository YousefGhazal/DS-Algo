#include <iostream>
using namespace std;

// Definition of Node
struct Node
{
    int data;
    Node *left;
    Node *right;
};
// Function to create a new Node in heap.
Node *CreateNewNode(int data)
{
    Node *newNode = new Node();
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}
// To insert data in BST, returns address of root node.
Node *Insert(Node *root, int data)
{
    if (root == NULL) // empty tree.
    {
        root = CreateNewNode(data);
    }
    else if (root->data >= data)
    {
        root->left = Insert(root->left, data);
    }
    else
    {
        root->right = Insert(root->right, data);
    }
    return root;
}
bool Search(Node *root, int data)
{
    if (root == NULL)
    {
        return false;
    }
    else if (root->data == data)
    {
        return true;
    }
    else if (data <= root->data)
    {
        return Search(root->left, data);
    }
    else
    {
        return Search(root->right, data);
    }
}
// Iterative solution
int IterFindMin(Node *root)
{
    if (root == NULL)
    {
        return -1;
    }
    Node *temp = root;
    while (temp->left != NULL)
    {
        temp = temp->left;
    }
    return temp->data;
}
// Recursie solution
int FindMin(Node *root)
{
    if (root == NULL)
    {
        return -1;
    }
    else if (root->left == NULL)
    {
        return root->data;
    }
    return FindMin(root->left);
}
// Height of a tree.
int FindHeight(Node *root)
{
    if (root == NULL)
    {
        return 0;
    }
    return max(FindHeight(root->left), FindHeight(root->right)) + 1;
}
int main()
{
    Node *root = NULL;
    root = Insert(root, 15);
    root = Insert(root, 10);
    root = Insert(root, 50);
    root = Insert(root, 30);
    root = Insert(root, 25);
    root = Insert(root, 13);
    root = Insert(root, 43);
    root = Insert(root, 33);

    // int num;
    // cout << "Enter num be searched \n";
    // cin >> num;
    // if (Search(root, num) == true)
    // {
    //     cout << "Found \n";
    // }
    // else
    // {
    //     cout << "Not Found \n";
    // }
    cout << FindHeight(root) << endl ;
    return 0;
}
