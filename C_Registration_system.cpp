# include <iostream>
# include <bits/stdc++.h>
using namespace std;
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    map<string, int> count;
    vector<pair<string, int>> registration(n + 1);
    string name[n];
    for(int i = 0; i < n; i++)
    {
        cin >> name[i];
        registration[i].first = name[i];
        registration[i].second = count[name[i]]++;
    }
    for(int i = 0; i < n; i++)
    {
        if(registration[i].second == 0)
        {
            cout << "OK" << endl;
        }
        else
        {
            cout << registration[i].first << registration[i].second << endl;
        }
    }
    return 0;
}
