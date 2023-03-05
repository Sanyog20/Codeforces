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
    int count = 1;
    int max_count = 0;
    for(int i = 0; i < n - 1; i++)
    {
        if((a[i] * 2) >= a[i + 1])
        {
            count += 1;
        }
        else
        {
            if(count > max_count)
            {
                max_count = count;
            }
            count = 1;
        }
    }
    if(count > max_count)
    {
        max_count = count;
    }
    cout << max_count;
    return 0;
}