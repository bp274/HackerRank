#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int n, e ;
    cin >> n ;
    int arr[n] ;
    for(int i = 0 ; i < n ; i++)
    {
        cin >> arr[i] ;
    }
    e = arr[n - 1] ;
    bool isSorted = false ;
    int m = n ;
    while(!isSorted)
    {
        if(e < arr[m - 2])
        {
            arr[m - 1] = arr[m - 2] ;
        }
        else
        {
            arr[m - 1] = e ;
            isSorted = true ;
        }
        m-- ;
        for(int i = 0 ; i < n ; i++)
        {
            cout << arr[i] << " " ;
        }
        cout << endl ;
    }
    return 0;
}
