#include <bits/stdc++.h>

using namespace std ;

int main()
{
    int n ;
    cin >> n ;
    string s ;
    string b[100] ;
    int x ;
    for(int i = 0 ; i < n / 2 ; i++)
    {
        cin >> x >> s ;
        b[x] = b[x] + '-' + ' ' ;
    }
    for(int i = n/2 ; i < n ; i++)
    {
        cin >> x >> s ;
        b[x] = b[x] + s + ' ' ;
    }
    for(int i = 0 ; i < 100 ; i++)
    {
        cout << b[i] ;
    }
    return 0 ;
}
