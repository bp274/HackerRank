#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int stack[100000], max[10000], N, top = -1 ;
    cin >> N ;
    while(N--)
    {
        int type ;
        cin >> type ;
        switch(type)
        {          
            case 1 :
                cin >> stack[++top] ;
                if(top > 0)
                {
                    if(stack[top] > max[top - 1])
                    {
                        max[top] = stack[top] ;
                    }
                    else
                    {
                        max[top] = max[top - 1] ;
                    }
                }
                else
                {
                    max[top] = stack[top] ;
                }
                break ;
            case 2 :
                top-- ;
                break ;
            case 3 :
                cout << max[top] << endl ;
                break ;
        }
    }
    return 0;
}
