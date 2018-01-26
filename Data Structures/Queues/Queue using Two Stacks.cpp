#include <stack>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    stack<int> front, rear ;
    int q, n, x ;
    cin >> q ;
    while(q--)
    {
        cin >> n ;
        if(n == 1)
        {
            cin >> x ;
            rear.push(x) ;
        }
        else
        {
            if(front.empty())
            {
                while(!rear.empty())
                {
                    front.push(rear.top()) ;
                    rear.pop() ;
                }
            }
            if(!front.empty())
            {
                if(n == 2)
                {
                    front.pop() ;
                }
                else if(n == 3)
                {
                    cout << front.top() << endl ;
                }
            }
        }
    }
    return 0;
}
