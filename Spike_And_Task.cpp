#include <bits/stdc++.h>
#include <iostream>
using ll = long long int;
using namespace std;
int main()
{
    ll t;
    cin >> t;
    while (t--)
    {
        ll n;
        cin >> n;
        string s;
        cin >> s;
        ll a = 0, b = 0, c = 0, d = 0;
        for (int i = 0; i < n; i++)
        {
            if (i % 2 == 0)
            {
                if (s[i] == '0')
                {
                    a++;
                }
                else
                {
                    b++;
                }
            }
            else
            {
                if (s[i] == '0')
                {
                    c++;
                }
                else
                {
                    d++;
                }
            }
        }
        ll x = max(b, c);
        ll y = max(a, d);
        ll z = min(x, y);
        cout << z << endl;
    }
    return 0;
}
