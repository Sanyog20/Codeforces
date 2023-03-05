# include <iostream>
# include <bits/stdc++.h>
using namespace std;
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    string s;
    cin >> s;
    int eight = 0;
    for(int i = 0; i < n; i++)
    {
        if(s[i] == '8')
        {
            eight += 1;
        }
    }
    int num = n / 11;
    cout << min(eight, num);
    return 0;
}