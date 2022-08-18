
#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

int main() {
    ll n = 600851475143;
    ll c = 2;
    vector<ll> primes;

    while (n > 1) {
        if (n % c == 0) {
            primes.push_back(c);
            n /= c; 
        } else {
            c++;
        }
    }

    cout << primes.back() << endl;

    return 0;
}
