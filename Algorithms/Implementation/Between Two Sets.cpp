#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, m, max=0, min=100, count=0, number=0 ;
    cin >> n >> m ;
    int a[n], b[m] ;
    for(int i=0; i<n; i++)
    {
        cin >> a[i] ;
        if(a[i] > max)
        {
            max = a[i] ;
        }
    }
    for(int i=0; i<m; i++)
    {
        cin >> b[i] ;
        if(b[i] < min)
        {
            min = b[i] ;
        }
    }
    for(int i=max; i<=min; i++)
    {
        count = 0 ;
        for(int j=0; j<n; j++)
        {
            if(i%a[j] == 0)
            {
                count++;
            }
        }
        for(int j=0; j<m; j++)
        {
            if(b[j]%i == 0)
            {
                count++;
            }
        }
        if(count == n+m)
        {
            number++;
        }
    }
    cout << number ;
    return 0;
}
