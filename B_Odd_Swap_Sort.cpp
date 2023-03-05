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
        int n, x;
        cin >> n;
        int a[n], even[n], odd[n];
        int e = 0;
        int o = 0;
        for(int i = 0; i < n; i++)
        {
            cin >> x;
            if(x % 2 == 0)
            {
                even[e] = x;
                e++;
            }
            else
            {
                odd[o] = x;
                o++;
            }
        }
        if((is_sorted(even, even + e)) && is_sorted(odd, odd + o))
        {
            cout << "Yes\n";
        }
        else
        {
            cout << "No\n";
        }
    }
    return 0;
}