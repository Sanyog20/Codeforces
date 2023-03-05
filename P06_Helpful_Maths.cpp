# include <iostream>
# include <bits/stdc++.h>
using namespace std;
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    cin >> s;
    int one = 0;
    int two = 0;
    int three = 0;
    int plus = 0;
    for(int i = 0; i < s.length(); i++)
    {
        if(s[i] == '1')
        {
            one += 1;
        }
        else if(s[i] == '2')
        {
            two += 1;
        }
        else if(s[i] == '3')
        {
            three += 1;
        }
        else
        {
            plus += 1;
        }
    }
    string s1 = "";
    for(int i = 0; i < one; i++)
    {
        s1 = s1 + '1';
        if(plus != 0)
        {
            s1 = s1 + "+";
            plus -= 1;
        }
    }
    for(int i = 0; i < two; i++)
    {
        s1 = s1 + '2';
        if(plus != 0)
        {
            s1 = s1 + "+";
            plus -= 1;
        }
    }
    for(int i = 0; i < three; i++)
    {
        s1 = s1 + '3';
        if(plus != 0)
        {
            s1 = s1 + "+";
            plus -= 1;
        }
    }
    cout << s1 << endl;
    return 0;
}