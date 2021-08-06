#include <bits/stdc++.h>
#include <math.h>
using namespace std;
#define ll long long

ll N = 10000000;
bool prime[10000001];
void SieveOfEratosthenes(){
int n = N;memset(prime, true, sizeof(prime));prime[0]=false;prime[1]=false;
for(int p=2;p*p<=n;p++){if(prime[p]==true){for(int i=p*p;i<=n;i+=p)prime[i]=false;}}}


int main()
{	
    SieveOfEratosthenes();
    ll x;
    bool flag = false;
    for(int i =5;i<10000;i+=2){
    	x = i;
    	if(!prime[x]){
    		int p1 = 2;
    		// x = p1 + 2*t*t
    		for(int pp = 0;p1+pp<=x;pp++){
    			if(prime[p1+pp]){
    				for(int t=1;2*t*t<=x;t++){
    					// cout<<x<<" "<<p1+pp<<" "<<t<<endl;
    					if(x == (p1+pp+ (2*t*t))){
    						flag = true;
						}
					}
				}
			}
			if(flag == false){
				cout<<x<<endl;
				return 0;
			}
			flag = false;
		}
	}
	return 0;
}
