# include <iostream>
# include <bits/stdc++.h>
using namespace std;
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, L, a;
    cin >> n >> L >> a;
    int t[n], l[n];
    int t1, t2;
    for(int i = 0; i < n; i++)
    {
        cin >> t1 >> t2;
        t[i] = t1;
        l[i] = t2;
    }
    int time = 0;
    int breaks = 0;
    int i = 0;
    while(time <= L && i != n)
    {
        if(t[i] > time + a)
        {
            breaks += 1;
            time = time + a;
        }
        else
        {
            time = t[i] + l[i];
            i++;
        }
    }
    if(time < L)
    {
        breaks = breaks + (L - time) / a;
    }
    cout << breaks;
    return 0;
}
