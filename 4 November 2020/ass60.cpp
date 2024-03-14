// jackie.yee14@myhunter.cuny.edu
// Jackie Yee

#include <iostream>
using namespace std;

int main() {
  int n;
  cout << "Enter a number: ";
  cin >> n;
  int x;
  int b = 16;

  if (n < 0)
  {
    cout << 1;
    x = 32 + n;
  }
  else
  {
    cout << 0;
    x = n;
  }

  while (b > 0.5)
  {
    if (x >= b)
    {
      cout << 1;
    }
    else
    {
      cout << 0;
    }
    x = x % b;
    b = b/2;
  }
  cout << "\n";
}