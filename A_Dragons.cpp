# include <iostream>
# include <bits/stdc++.h>
using namespace std;
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int s, n;
    cin >> s >> n;
    int x[n];
    int y[n];
    string ans = "YES";
    for(int i = 0; i < n; i++)
    {
        cin >> x[i] >> y[i];
    }
    int t1, t2;
    for(int i = 0; i < n; i++)
    {
        for(int j = i; j < n; j++)
        {
            if(x[i] > x[j])
            {
                t1 = x[i];
                t2 = y[i];
                x[i] = x[j];
                x[j] = t1;
                y[i] = y[j];
                y[j] = t2;
            }
        }
    }
    for(int i = 0; i < n; i++)
    {
        if(s > x[i])
        {
            s = s + y[i];
        }
        else
        {
            ans = "NO";
            break;
        }
    }
    cout << ans;
    return 0;
}