#include<iostream>
#include<cmath>
using namespace std;
#define ll long long

ll digitpowersum(ll a, int n){
	ll sum = 0;
	int i = 0;
	while(a>0){
		sum+=pow(a%10,n);
		a = a/10;
		i++;
	}
	return sum;
}

int main(){
	ll answer = 0;
	for (int i =10;i<10000000;i++){
		if(i==digitpowersum(i,5)){
			answer+=i;
		}
	}
	cout<<answer<<endl;
	
	return 0;
}
