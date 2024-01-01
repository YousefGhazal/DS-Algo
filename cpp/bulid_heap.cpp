#include <iostream>
using namespace std;

void MaxHeapify(int arr[], int n, int i)
{
    int big = i;
    int left = i * 2 + 1;
    int right = i * 2 + 2;
    if (left < n && arr[left] > arr[big])
    {
        big = left;
    }
    if (right < n && arr[right] > arr[big])
    {
        big = right;
    }
    if (big != i)
    {
        swap(arr[i], arr[big]);
        MaxHeapify(arr, n, big);
    }
}
void BuildMaxHeap(int arr[], int n)
{
    int start = (n / 2) - 1;
    for (int i = n; i >= 0; i--)
    {
        MaxHeapify(arr, n, i);
    }
}
void HeapSort(int arr[], int n)
{
    BuildMaxHeap(arr, n);
    for (int i = n - 1; i >= 0; i--)
    {
        swap(arr[i], arr[0]);
        MaxHeapify(arr, i, 0);
    }
}

void PrintHeap(int arr[], int n)
{
    cout << "Array is: \n";
    for (int i = 0; i < n; ++i)
    {
        cout << arr[i] << " ";
    }
    cout << "\n";
}

int main()
{
    int arr[] = {16, 4, 10, 14, 7, 9, 3, 2, 8, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    PrintHeap(arr, n);
    // MaxHeapify(arr, n, 1);
    // PrintHeap(arr, n);
    // BuildMaxHeap(arr, n);
    HeapSort(arr, n); 
    PrintHeap(arr, n);
}