# include <iostream>
# include <bits/stdc++.h>
using namespace std;
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t--)
    {
        double x1, p1, x2, p2, t1;
        cin >> x1 >> p1 >> x2 >> p2;
        t1 = log10(x1 / x2) + p1 - p2;
        if(t1 > 0)
        {
            cout << ">" << endl;
        }
        else if(t1 == 0)
        {
            cout << "=" << endl;
        }
        else
        {
            cout << "<" << endl;
        }
    }
    return 0;
}
