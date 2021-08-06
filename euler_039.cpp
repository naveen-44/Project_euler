#include<iostream>
#include<math.h>
#define ll long long
using namespace std;

int main(){
	ll answer = 0;
	ll pans = 0;
	int plen[1001] = {0};
	for(int p = 10;p <= 1000;p++){
		for(int a = 1;a <= 500;a++){
			for(int b = 1;b <= 500;b++){
				if(sqrt((a*a)+(b*b)) == p-(a+b)){
					plen[p]++;
				}
			}
		}
	}
	
	for (int i = 0;i<1001;i++){
		if(plen[i]>0){
			cout<<plen[i]<<endl;
			if(plen[i]>pans){
				pans = plen[i];
				answer = i;
			}
		}
	}
	cout<<pans<<" "<<answer<<endl;
}
