#include <string.h>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    int n, m = -1, k = -1, q ;
    cin >> n ;
    char str[1000][20], substr[1000][20] ;
    while(n--)
    {
        cin >> str[++k] ;
    }
    cin >> q ;
    while(q--)
    {
        cin >> substr[++m] ;
    }
    for(int i = 0 ; i <= m ; i++)
    {
        int count = 0 ;
        for(int j = 0 ; j <= k ; j++)
        {
            if(strcmp(substr[i], str[j]) == 0)
            {
                count++ ;
            }
        }
        cout << count << endl ;
    }
    return 0;
}
