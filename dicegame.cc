#include <iostream>
using namespace std;

int main() {
  int a1, a2, a3, a4;
  int b1, b2, b3, b4;
  cin >> a1 >> b1 >> a2 >> b2;
  cin >> a3 >> b3 >> a4 >> b4;
  
  int ea = a1 + a2;
  int eb = b1 + b2;
  int ga = a3 + a4;
  int gb = b3 + b4;
  
  if (ga > eb) {
    cout << "Gunnar\n";
  } else if (ea > gb) {
    cout << "Emma\n";
  } else {
    int l = ea - ga;
    int r = gb - eb;
    
    if (r == l) {
      cout << "Tie\n";
    } else if ((r >= 0 && r > l) || (r < 0 && r < l)) {
      cout << (max(gb, eb) == eb ? "Gunnar\n" : "Emma\n");
    } else {
      cout << (max(gb, eb) == gb ? "Gunnar\n" : "Emma\n");
    }
  }
  
  return 0;
} 
