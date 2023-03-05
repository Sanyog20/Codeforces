# include <iostream>
# include <bits/stdc++.h>
# define int               long long
using namespace std;
 
signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t--)
    {
        int l, n;
        cin >> l;
        string s;
        cin >> s;
        cin >> n;
        char c[n];
        for(int i = 0; i < n; i++)
        {
            cin >> c[i];
        }
        int count = 0;
        int flag = 1;
        while(flag != 0)
        {
            flag = 0;
            string s2 = "";
            for(int i = 1; i < l; i++)
            {
                int t = 0;
                for(int j = 0; j < n; j++)
                {
                    if(s[i] == c[j])
                    {
                        t = 1;
                    }
                }
                if(t == 0)
                {
                    s2 = s2 + s[i - 1];
                }
                else
                {
                    flag = 1;   
                }
            }
            count++;
            s2 = s2 + s[l - 1];
            s = s2;
            l = s.length();
            // cout << s << l << endl;
        }
        cout << count - 1 << endl;
    }
    return 0;
}
