#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int max(int a, int b, int c)
{
    int max ;
    max = (a > b)  ?  a : b ;
    max =  (c > max)  ?  c : max ;
    return max ;
}

int main()
{
    int i, j, k ;
    int n1, n2, n3 ;
    cin >> n1 >> n2 >> n3 ;
    int stack1[n1], stack2[n2], stack3[n3], height1, height2, height3 ;
    height1 = height2 = height3 = 0 ;
    for(i=0; i<n1; i++)
    {
        cin >> stack1[i] ;
        height1 += stack1[i] ;
    }
    for(j=0; j<n2; j++)
    {
        cin >> stack2[j] ;
        height2 += stack2[j] ;
    }
    for(k=0; k<n3; k++)
    { 
        cin >> stack3[k] ;
        height3 += stack3[k] ;
    }
    i = j = k = -1 ;
    while(height1 != height2 || height1 != height3)
    {
        if(max(height1, height2, height3) == height1)
            height1 -= stack1[++i] ;
        else if(max(height1, height2, height3) == height2)
            height2 -= stack2[++j] ;
        else
            height3 -= stack3[++k] ;
    }
    cout << height1 ;
    return 0;
}
