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


int main(){
    int s;
    int t;
    cin >> s >> t;
    int a;
    int b;
    cin >> a >> b;
    int m;
    int n;
    cin >> m >> n;
    int count=0,d;
    while(m--)
    {
        cin >> d ;
        if((a+d)<=t&&(a+d)>=s)
        {
            count++;
        }
    }
    cout << count << endl;
    count=0;
    while(n--)
    {
        cin >> d ;
        if((b+d)<=t&&(b+d)>=s)
        {
            count++;
        }
    }
    cout << count << endl;
    return 0;
}
