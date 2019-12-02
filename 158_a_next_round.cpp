#include <iostream>
#include <vector>

using namespace std;

int main(){


	int n,k;
	cin >> n >> k;
	vector<int> ar(n);
	int i = 0;
	int pivot, count = 0;
	
	
	for(i = 0; i < n; i++)
		cin >> ar[i];
		
	pivot = ar[k-1];	
	for (i = 0; i < n; i++)
		if (ar[i] > 0 && ar[i] >= pivot) count++;


	cout << count << endl;  

	return 0;
	

}
