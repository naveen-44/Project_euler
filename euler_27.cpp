#include <bits/stdc++.h>
#include <math.h>
using namespace std;
#define ll long long

ll N = 10000000;
bool prime[10000001];
 
void SieveOfEratosthenes()
{	int n = N;
    memset(prime, true, sizeof(prime));
    prime[0]=false;
    prime[1]=false;
    for (int p = 2; p * p <= n; p++)
    {
        if (prime[p] == true) 
        {
            for (int i = p * p; i <= n; i += p)
                prime[i] = false;
        }
    }
}

int nump(int a, int b){
	// n*n + a*n + b
	int count = 0;
	for(int i =0;i<10000;i++){
		ll x = i*i + a*i + b;
		if(!prime[x]){
			return count;
		}
		else{
			count++;
		}
	}
	return count;
}


int main()
{	
    SieveOfEratosthenes();
    int max = 0, ans = 1;
	for(int b = -1000; b <= 1000; b++){
		int gg = fabs(b);
		if(prime[gg]){
			for (int a = -999;a < 1000; a++){
				int n = nump(a,b);
				if(n>max){
					max = n;
					ans = a*b;
					//cout<<a<<" "<<b<<" "<<n<<endl;
				}
			}
		}
	}
	cout<<ans<<endl;
	return 0;
}
