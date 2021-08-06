#include<iostream>
#include<math.h>
#define ll long long
using namespace std;

ll fact(int n){
	if(n<=1){
		return 1;
	}
	return fact(n-1)*n;
}

int main(){
	ll answer = 0;
	for(ll i=3;i<10000000;i++){
		int n = i, sum = 0;
		while(n>0){
			int d = n%10;
			sum+=fact(d);
			n = n/10;
		}
		if(sum == i){
			answer += i;
		}
	}
	cout<<answer<<endl;
	
	
	return 0;
}
