
#include <iostream>
using namespace std;

int sumOfSquare(int n) {
    return (n * (n + 1) * (2 * n + 1)) / 6;
}

int squareOfSum(int n) {
    int sum = (n * (n + 1)) / 2;
    return sum * sum;
}

int main() {

    cout << "Square of the sum upto 100 natural numbers: " << squareOfSum(100) << endl;

    cout << "Sum of square of first 100 natural numbers: " << sumOfSquare(100) << endl;

    cout << (squareOfSum(100) - sumOfSquare(100)) << endl;

    return 0;
}
