#include <bits/stdc++.h>

using namespace std;

class Heap
{
    private :
        int arr[1000000];
        int size;

        int getLeftChildIndex(int parentIndex) { return 2 * parentIndex + 1; }
        int getRightChildIndex(int parentIndex) { return 2 * parentIndex + 2; }
        int getParentIndex(int childIndex) { return (childIndex - 1) / 2; }

        bool hasLeftChild(int index) { return getLeftChildIndex(index) < size; }
        bool hasRightChild(int index) { return getRightChildIndex(index) < size; }
        bool hasParent(int index) { return index > 0; }

        int leftChild(int index) { return arr[getLeftChildIndex(index)]; }
        int rightChild(int index) { return arr[getRightChildIndex(index)]; }
        int parent(int index) { return arr[getParentIndex(index)]; }

        void swap(int indexA, int indexB)
        {
            int temp;
            temp = arr[indexA];
            arr[indexA] = arr[indexB];
            arr[indexB] = temp;
        }

    public :
        Heap()
        {
            size = 0;
        }

        void add(int v)
        {
            arr[size] = v;
            size++;
            heapifyUp();
        }

        void del()
        {
            int index;
            index = 0;

            arr[index] = arr[size - 1];
            arr[size - 1] = '\0';
            size--;

            heapifyDown(index);
        }

        void heapifyUp()
        {
            int index = size - 1;

            while(hasParent(index) && parent(index) > arr[index])
            {
                swap(getParentIndex(index), index);
                index = getParentIndex(index);
            }
        }

        void heapifyDown(int index)
        {
            while(hasLeftChild(index))
            {
                int smallestChildIndex = getLeftChildIndex(index);

                if(hasRightChild(index) && rightChild(index) < leftChild(index))
                {
                    smallestChildIndex = getRightChildIndex(index);
                }

                if(arr[index] < arr[smallestChildIndex])
                {
                    break;
                }
                else
                {
                    swap(index, smallestChildIndex);
                }

                index = smallestChildIndex;
            }
        }

        bool isEmpty()
        {
            if (size <= 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        int min()
        {
            return arr[0];
        }

};

int main()
{
    Heap heap;

    int n, k, x, y, count = 0;
    bool isPossible = true;
    cin >> n >> k;

    for (int i = 0; i < n; i++)
    {
        cin >> x;
        heap.add(x);
    }

    while (heap.min() < k)
    {
        x = heap.min();
        heap.del();

        if (heap.isEmpty())
        {
            isPossible = false;
            break;
        }

        y = 2 * heap.min();
        heap.del();

        heap.add(x + y);

        count++;
    }

    if (isPossible)
    {
        cout << count << endl;
    }
    else
    {
        cout << -1 << endl;
    }

    return 0;
}
