#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    int lastAnswer = 0, N, Q, m, x, y, index ;
    cin >> N >> Q ;
    vector<int> seqList[N] ;
    while(Q--)
    {
        cin >> m >> x >> y ;
        index = (x ^ lastAnswer) % N ;
        switch(m)
        {
            case 1 :
                seqList[index].push_back(y) ;
                break ;
            case 2 :
                lastAnswer = seqList[index][y % ( seqList[index].size() )] ;
                cout << lastAnswer << endl ;
                break ;
        }
    }
    return 0;
}
