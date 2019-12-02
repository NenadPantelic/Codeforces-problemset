#include <iostream>

using namespace std;
int main(){
    
    
    int n,val = 0;
    cin >> n;
    string op;
    for(int i = 0; i < n; i++){

	cin >> op;
	if (op == "X++") val++;
	if (op == "++X") ++val;
	if (op == "X--") val--;
	if (op == "--X") --val;
		

    }
    cout << val << endl;;
    
    return 0;
    
}
