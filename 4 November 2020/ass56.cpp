//jackie.yee14@myhunter.cuny.edu
//Jackie Yee

#include <iostream>
using namespace std;

int main() {
  int number;
  cout << "Enter a number: ";
  cin >> number;
  for (int x = 0; x < number;)
  {
    for (int i = 0; i < number; i++)
   {
      cout << "* ";
    }
    cout << "\n";
    number -= 1;
  }
  return 0;
}