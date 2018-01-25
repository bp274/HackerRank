#include <bits/stdc++.h>

using namespace std;

long largestRectangle(int h[], int n)
{
    int i, j, k ;
    long area, answer = 0 ;
    for(i = 0 ; i < n ; i++)
    {
        area = h[i] ;
        j = i + 1 ;
        while(j < n && h[j] >= h[i])
        {
            area = area + h[i] ;
            j++ ;
        }
        k = i - 1 ;
        while(k >= 0 && h[k] >= h[i])
        {
            area = area + h[i] ;   
            k-- ;
        }
        if(area > answer)
        {
            answer = area ;
        }
    }
    return answer ;
}

int main()
{
    int n;
    cin >> n;
    int h[n] ;
    for(int i = 0 ; i < n ; i++)
    {
       cin >> h[i] ;
    }
    long result = largestRectangle(h, n);
    cout << result << endl;
    return 0;
}
