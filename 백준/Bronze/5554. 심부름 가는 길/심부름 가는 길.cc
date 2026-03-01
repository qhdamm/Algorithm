# include <iostream>
using namespace std;

int main() {
    int x1, x2, x3, x4;
    cin >> x1 >> x2 >> x3 >> x4;
    
    int sum_min, x, y;
    sum_min = x1 + x2 + x3 + x4;
    x = (int)sum_min / 60;
    y = (int)sum_min % 60;

    cout << x << "\n" << y;

    return 0;
}