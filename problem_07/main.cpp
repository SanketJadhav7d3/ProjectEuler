
#include <iostream>
#include <vector>
using namespace std;

#define MAX_VALUE 1000005

typedef long long ll;

vector<ll> getPrimes() {
    bool isPrime[MAX_VALUE];

    // fill the isPrime with all true values
    memset(isPrime, true, sizeof(isPrime));

    for (ll i = 2; i*i < MAX_VALUE; ++i) {
        if (isPrime[i] == true) {
            // multiples of prime are not prime
            for (ll j = i * i; j < MAX_VALUE; j += i) {
                isPrime[j] = false;
            } 
        }
    }

    vector<ll> primes;
    for (ll i = 2; i < MAX_VALUE; ++i) {
        if (isPrime[i]) {
            primes.push_back(i);
        }
    }

    return primes;
} 


int main() {
    vector<ll> primes = getPrimes();

    cout << primes[10000] << endl;
    return 0;
}
