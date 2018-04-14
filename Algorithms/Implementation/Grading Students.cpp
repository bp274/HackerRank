#include <bits/stdc++.h>

using namespace std;


int main() {
    int n;
    cin >> n;
    while(n--)
    {
        int grade ;
        scanf("%d", &grade) ;
        if(grade>37)
        {
            if(grade%5>2)
            {
                grade=(1+grade/5)*5;
            }
        }
        cout << grade << endl;
    }
    return 0;
}
