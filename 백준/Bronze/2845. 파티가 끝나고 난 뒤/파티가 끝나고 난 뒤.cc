# include <iostream>
using namespace std;

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int L, P, totalP;
    cin >> L >> P;
    totalP = L * P;
    for (int i=0; i<5; ++i)
    {
        int eachP;
        cin >> eachP;
        cout << eachP - totalP << " ";

    }
}