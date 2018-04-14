#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n ;
    int s[n] ;
    for(int i = 0; i < n; i++)
    {
       cin >> s[i] ;
    }
    int d, m ;
    cin >> d >> m ;
    int count=0, sum ;
    for(int i=0; i<=n-m; i++)
    {
        sum=0 ;
        for(int j=i; j<m+i; j++)
        {
            sum = sum + s[j] ;
        }
        if(sum == d)
        {
            count++ ;
        }
    }
    cout << count ;
    return 0;
}
