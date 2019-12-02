#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int m,n,a;
    cin >> m >> n >> a;
    long long x = ceil( 1.0 * m / a);
    int y = ceil(1.0 * n / a);
    cout << x * y;
    return 0;
}
