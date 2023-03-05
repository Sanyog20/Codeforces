#include <bits/stdc++.h>
using namespace std;
#define test              int T;cin>>T;while(T--)
#define int               unsigned long long
#define rep(i,a,b)        for(int i=a;i<b;i++)
const int MOD = 1e9 + 7;
 
int fact(int n)
{
  unsigned long long res = 1;
  rep(i, 3, (2 * n) + 1)
  res = (res * i) % MOD;
  return res;
}

signed main()
{
  int t;
  cin >> t;
  while(t--){
      int n;
      cin >> n;
      if(n == 1){
          cout << 1 << endl;
      }
      else{
          cout << fact(n) << endl;
      }
  }
  return 0;
}
