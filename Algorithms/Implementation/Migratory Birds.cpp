#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n,max=0,maxindex;
    cin >> n;
    int a[n],b[5]={0};
    for(int i=0; i<n; i++)
    {
        cin >> a[i];
    }
    for(int i=0; i<n; i++)
    {
        b[a[i]-1]++;
        if(b[a[i]-1] > max || (a[i]<maxindex && b[a[i]-1] == max))
        {
            max=b[a[i]-1];
            maxindex=a[i];
        }
    }
    cout << maxindex ;
    return 0;
}
