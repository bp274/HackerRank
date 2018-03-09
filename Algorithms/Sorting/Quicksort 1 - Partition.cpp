#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, r = -1 ;
    cin >> n ;
    int a[n], right[n] ;
    for(int i = 0 ; i < n ; i++)
    {
        cin >> a[i] ;
        if(a[i] > a[0])
        {
            right[++r] = a[i] ;
        }
        if(a[i] < a[0])
        {
            cout << a[i] << " " ;
        }
    }
    cout << a[0] << " " ;
    for(int i = 0 ; i <= r ; i++)
    {
        cout << right[i] << " " ;
    }
    return 0;
}
