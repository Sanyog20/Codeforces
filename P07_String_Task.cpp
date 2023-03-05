# include <iostream>
# include <bits/stdc++.h>
using namespace std;
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    cin >> s;
    string s1 = "";
    for(int i = 0; i < s.length(); i++)
    {
        if(s[i] == 'A' || s[i] == 'a' || s[i] == 'O' || s[i] == 'o' || s[i] == 'Y' || s[i] == 'y' || s[i] == 'E' || s[i] == 'e' || s[i] == 'U' || s[i] == 'u' || s[i] == 'I' || s[i] == 'i')
        {
            s1 = s1;
        }
        else
        {
            s1 = s1 + ".";
            char t = tolower(s[i]);
            s1 = s1 + t;
        }
    }
    cout << s1 << endl;
    return 0;
}