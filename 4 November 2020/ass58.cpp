//jackie.yee14@myhunter.cuny.edu
//Jackie Yee
// assignment 58

#include <iostream>
using namespace std;


int main() {
  int num;
  cout << "Please enter an odd number:";
  cin >> num;

  while (num % 2 == 0)
  {
    cout << "You entered an even number.\n";
    cout << "Please enter an odd number:";
    cin >> num;
  }
  if (num % 2 == 1)
  {
    cout << "Your odd number is: " << num << "\n\n";
  }
  
}