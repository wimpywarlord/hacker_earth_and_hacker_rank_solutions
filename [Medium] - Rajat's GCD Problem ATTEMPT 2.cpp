#include<stdio.h>
#include<conio.h>
#include<math.h>
int gcd(int a, int b)
{

    if(b == 0) 
    {
            return a;
    }
    else 
    {
        return gcd(b, a % b);
    }
}
int main()
{   
    int t,i;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
    	int a,b,n;
    	scanf("%d %d %d",&a,&b,&n);
    	int res1=pow(a,n)+pow(b,n);
    	int res2;
    	if (a>=b)
    	{
    	    res2=a-b;
    	}
    	else
    	{
    	    res2=b-a;
    	}
    	//printf("%d\n",res1);
    	//printf("%d\n",res2);
    	printf("%d",gcd(res1,res2)%(1000000007));
	}
	getch();
    return 0;
    
}
