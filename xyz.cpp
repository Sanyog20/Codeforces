# include <iostream>
# include <bits/stdc++.h>
# define int               long long
using namespace std;
 
signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n = 300;
    cout << n << endl;
    srand(time(0));
    while(n--)
    {
        int t;
        t = (rand() % 10000) + 1;
        cout << t << endl;
    }
    return 0;
}
