#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<string>

using namespace std;

int main()
{
    int q, top = -1, t, k ;
    string str, str1, store[1000000]  ;
    cin >> q ;
    while(q--)
    {
        cin >> t ;
        if(t == 1)
        {
            cin >> str1 ;
            store[++top] = str ;
            str = str + str1 ;
        }
        else if(t == 2)
        {
            cin >> k ;
            store[++top] = str ;
            str = str.substr(0, str.size()-k);
        }
        else if(t == 3)
        {
            cin >> k ;
            cout << str[k - 1] << endl ;
        }
        else
        {
            str = store[top--] ;
        }
    }
    return 0;
}
