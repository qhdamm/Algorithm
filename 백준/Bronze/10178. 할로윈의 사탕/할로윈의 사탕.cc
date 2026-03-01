# include <iostream>
using namespace std;

int main() {
    int N, c, v;
    cin >> N;
    for (int i=0; i<N; ++i)
    {
        cin >> c >> v;
        int youN, dadN;
        youN = (int)c/v;
        dadN = (int)c%v;
        cout << "You get " << youN << " piece(s) and your dad gets " << dadN << " piece(s).\n";
    }
    return 0;
}