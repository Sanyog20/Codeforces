    # include <iostream>
    # include <bits/stdc++.h>
    using namespace std;
    
    int main()
    {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        string s;
        cin >> s;
        int l = s.length();
        int count = 1;
        bool flag = 0;
        for(int i = 0; i < l - 1; i++)
        {
            if(s[i] == s[i + 1])
            {
                count += 1;
            }
            else
            {
                count = 1;
            }
            if(count >= 7)
            {
                flag = 1;
                break;
            }
        }
        if(flag == 1)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
        return 0;
    }