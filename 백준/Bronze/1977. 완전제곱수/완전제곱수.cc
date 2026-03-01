# include <iostream>
# include <cmath>
using namespace std;

int main() {
    int M, N;
    cin >> M >> N;

    int start = (int)ceil(sqrt(M));
    int end = (int)floor(sqrt(N));

    if (start > end)
    {
        cout << -1;
        return 0;
    }

    int minvalue = start*start;
    int sum = 0;
    for (int i = start; i <= end; ++i)
    {
        sum += i*i;
    }
    cout << sum << "\n" << minvalue;
    return 0;
}