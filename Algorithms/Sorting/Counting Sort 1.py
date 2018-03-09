#include <bits/stdc++.h>

using namespace std;

int* countingSort(int arr[], int n)
{
    int* answer = new int[100] ;
    answer[100] = {0} ;
    for(int i = 0 ; i < n ; i++)
    {
        answer[arr[i]]++ ;
    }
    return answer ;
}

int main()
{
    int n;
    cin >> n;
    int arr[n] ;
    for(int i = 0 ; i < n ; i++)
    {
       cin >> arr[i];
    }
    int* result = countingSort(arr, n);
    for (int i = 0 ; i < 100 ; i++)
    {
        cout << result[i] << " " ;
    }
    return 0;
}
