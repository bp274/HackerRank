#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    int V, n ;
    cin >> V ;
    cin >> n ;
    int ar[n] ;
    for(int i = 0 ; i < n ; i++)
    {
        cin >> ar[i] ;
    }
    for(int i = 0 ; i < n ; i++)
    {
        if(ar[i] == V)
        {
            cout << i ;
            break ;
        }
    }
    return 0;
}
