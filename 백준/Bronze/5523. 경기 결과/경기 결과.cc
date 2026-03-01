# include <iostream>
using namespace std;

int main() {
    int aWin = 0, bWin = 0, aScore, bScore, N;
    cin >> N;
    
    for (int i=0; i<N; ++i)
    {
        cin >> aScore >> bScore;
        if (aScore > bScore)
        {
            aWin += 1;
        }
        else if (aScore < bScore)
        {
            bWin += 1;
        }
    }
    cout << aWin << ' ' << bWin;
    return 0;
}