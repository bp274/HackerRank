#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <iostream>
using namespace std;

int main()
{
    int n, i, j, k, e ;
    cin >> n ;
    int a[n] ;
    for(int i = 0 ; i < n ; i++)
    {
        cin >> a[i] ;
    }
    for(i = 1 ; i < n ; i++)
    {
        e = a[i] ;
        for(j = i - 1 ; j >= 0 ; j--)
        {
            if(e < a[j])
            {
                a[j + 1] = a[j] ;
            }
            else
            {
                break ;
            }
        }
        a[j + 1] = e ;
        for(k = 0 ; k < n ; k++)
        {
            cout << a[k] << " " ;
        }
        cout << endl ;
    }
    return 0;
}
