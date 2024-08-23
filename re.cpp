#include <bits/stdc++.h>
#include <string>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        string s = to_string(n);
        string str=s.substr(0,2);
       
        int x = stoi(str);
        int size = s.size();
        string s1 = s.substr(2, size);
        int y = stoi(s1);

        if (x == 10 && y > 2)
        {
            cout << "yes";
        }
        else
        {
            cout << "no";
        }
    }
}
