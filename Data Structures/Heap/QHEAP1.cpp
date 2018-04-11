#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std ;

class Heap
{
    private :
        int arr[100000];
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

        void del(int v)
        {
            int index;
            index = search(v);

            arr[index] = arr[size - 1];
            arr[size - 1] = '\0';
            size--;

            heapifyDown(index);
        }

        int search(int v)
        {
            for(int i = 0; i < size; i++)
            {
                if(arr[i] == v)
                {
                    return i;
                }
            }
            return -1;
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

        void min()
        {
            cout << arr[0] << endl;
        }

};

int main()
{
    Heap heap;

    int q;
    cin >> q ;
    while(q--)
    {
        int n, v;
        cin >> n ;
        switch(n)
        {
            case 1:
                cin >> v;
                heap.add(v);
                break;

            case 2:
                cin >> v;
                heap.del(v);
                break;

            case 3:
                heap.min();
                break;

            default:
                cout << "Illegal Input" << endl;
                break;
        }
    }
    return 0;
}
