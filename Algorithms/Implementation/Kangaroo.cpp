#include <bits/stdc++.h>

using namespace std;

string kangaroo(int x1, int v1, int x2, int v2)
{
    string a="YES", b="NO" ;
    if(v1 == v2)
    {
        if(x1 == x2)
        {
            return a ;
        }
        else
        {
            return b ;
        }
    }
    else if((x1-x2)%(v2-v1) == 0 && (x1-x2)/(v2-v1)>=0)
    {
        return a ;
    }
    else
    {
        return b ;
    }
}

int main() {
    int x1;
    int v1;
    int x2;
    int v2;
    cin >> x1 >> v1 >> x2 >> v2;
    string result = kangaroo(x1, v1, x2, v2);
    cout << result << endl;
    return 0;
}
