// jackie.yee14@myhunter.cuny.edu
  // Jackie Yee

#include <iostream>
using namespace std;

int main() {
  float amount;
  cout << "Please enter starting amount: ";
  cin >> amount;
  float balance = amount;
  int x = 0;
  while (amount + 1000 > balance)
  {
    x += 1;
    balance = balance*1.03;
    cout << "Year " << x << " " << balance << "\n\n";
  }
}