# include <iostream>
# include <bits/stdc++.h>
using namespace std;
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int a, b, c;
    cin >> a >> b >> c;
    if((a >= b && a <= c) || (a <= b && a >= c))
    {
        cout << a;
    }
    else if((b >= a && b <= c) || (b <= a && b >= c))
    {
        cout << b;
    }
    else if((c >= a && c <= b) || (c <= a && c >= b))
    {
        cout << c;
    }
    return 0;
}
