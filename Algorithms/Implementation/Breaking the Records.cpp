#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, max, min, count1=0, count2=0 ;
    cin >> n ;
    long int s[n] ;
    cin >> s[0] ;
    min = max = s[0] ;
    for(int i=1; i<n; i++)
    {
        cin >> s[i] ;
        for(int j=0; j<i; j++)
        {
            if(s[i] > max)
            {
                max = s[i] ;
                count1++ ;
            }
            if(s[i] < min)
            {
                min = s[i] ;
                count2++ ;
            }
        }
    }
    cout << count1 << " " << count2 ;
    return 0;
}
