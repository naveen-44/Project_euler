#include<iostream>
#include<cmath>
using namespace std;
#define ll long long

int amicable(int a){
	int sum = -a;
	for(int i =1; i <= sqrt(a);i++){
		if(a%i == 0){
			// cout<<i<<" "<<a/i<<" "<<endl;
			sum = sum + i + a/i;
			if(i == sqrt(a)){
				sum-=i;
			}
		}
	}
	return sum;
}

int main(){
	int asum = 0;
	for(int i = 2;i < 10000;i++){
		ll a1 = amicable(i);
		if(i>a1 and amicable(a1) == i){
			asum = asum + a1 + i;
		}
	}
	cout<<asum<<endl;
	
	
	return 0;
}
