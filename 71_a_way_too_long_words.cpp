#include <iostream>

using namespace std;

string abbrev(string s){
    
    if( s.length() > 10){
    
        string abbreviated = to_string(s.length() - 2);
        abbreviated = s[0] + abbreviated + s[s.length() - 1];
        return abbreviated;
    }
    
    return s;
    
}
int main(){
    
    
    int n;
    cin >> n;
    string s;
    for (int i = 0; i < n; i++){
        cin >> s;
        cout << abbrev(s) << endl;
    }
    
    return 0;
    
}
