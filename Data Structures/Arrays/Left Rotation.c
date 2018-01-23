#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
    int n,d;
    scanf("%d%d",&n,&d);
    int a[n];
    for(int i=0; i<n; i++)
    {
        scanf("%d",&a[i]);
    }
    for(int i=0; i<n; i++)
    {
        if(d>n-1)
        {
            d=d-n;
        }
        printf("%d ",a[d]);
        d++;
    }
    
    return 0;
}
