#include<iostream>
#include<math.h>
#define ll long long
using namespace std;

ll m = 10000000000;

ll selfpower(ll n){
	ll x = 1;
	for (int i =1;i<=n;i++){
		x = x * n;
		x = x % m;
	}
	return x;
}


int main(){
	ll s = 0;
	for (int i =1;i<1000;i++){
		s += selfpower(i);
		s = s%m;
	}
	cout<<s<<endl;
	
	return 0;
}
