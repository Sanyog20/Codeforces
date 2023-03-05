# include <iostream>
# include <bits/stdc++.h>
using namespace std;
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    int a[n];
    for(int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    int b, c;
    cin >> b >> c;
    int sum = 0;
    for(int i = b; i <= c; i++)
    {
        sum = sum + a[i];
    }
    cout << sum;
    return 0;
}