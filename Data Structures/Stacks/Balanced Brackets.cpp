#include <bits/stdc++.h>

using namespace std;

string isBalanced(string s)
{
    int stack[1000], top = -1 ;
    for(int i=0; s[i] != '\0'; i++)
    {
        if(s[i] == '{' || s[i] == '[' || s[i] == '(')
        {
            stack[++top] = s[i] ;
        }
        else
        {
            if(s[i] == '}' && stack[top] == '{')
            {
                top-- ;
            }
            else if(s[i] == ']' && stack[top] == '[')
            {
                top-- ;
            }
            else if(s[i] == ')' && stack[top] == '(')
            {
                top-- ;
            }
            else
            {
                return "NO" ;
            }
        }
    }
    if(top == -1)
    {
        return "YES" ;
    }
    else
    {
        return "NO" ;
    }
}

int main()
{
    int t;
    cin >> t;
    for(int i = 0; i < t; i++)
    {
        string s;
        cin >> s;
        string result = isBalanced(s);
        cout << result << endl;
    }
    return 0;
}
