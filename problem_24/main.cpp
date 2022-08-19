

#include <iostream>
#include <algorithm>

using namespace std;

// used cpp because stl has next_permutation function which gives the next permutation of a sequence in lexicographic order

int main() {
    string s = "0123456789";

    long int i = 1;
    long int n = 1000000;

    do {
        cout << s << endl;
        if (i == n)
            break;
        i++;
    } while (next_permutation(s.begin(), s.end()));

    cout << "Answer: " << s << endl;


    return 0;
}


