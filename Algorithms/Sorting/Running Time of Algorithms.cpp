#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, i, j, k, e, shifts = 0 ;
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
                shifts++ ;
            }
            else
            {
                break ;
            }
        }
        a[j + 1] = e ;
    }
    cout << shifts ;
    return 0;
}
