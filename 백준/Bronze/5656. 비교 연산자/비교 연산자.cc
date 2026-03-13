# include <iostream>
# include <string>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, cnt = 0;
    string op;
    while (cin >> a >> op >> b) {
        bool ans;

        if (op == "E") break;
        if (op == ">") ans = (a > b);
        else if (op == ">=") ans = (a >= b);
        else if (op == "<") ans = (a < b);
        else if (op == "<=") ans = (a <= b);
        else if (op == "==") ans = (a == b);
        else if (op == "!=") ans = (a != b);
        ++cnt;

        cout << "Case " << cnt << ": " << (ans ? "true" : "false") << "\n";
        }
    
}