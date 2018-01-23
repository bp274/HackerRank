#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
    int a[6][6],sum=0,max=-63;
    for(int i=0; i<6; i++)
    {
        for(int j=0; j<6; j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            sum=0;
            for(int k=0; k<3; k++)
            {
                for(int l=0; l<3; l++)
                {
                    if(k!=1)
                    {
                        sum+=a[i+k][j+l];
                    }
                    else if(l==1)
                    {
                        sum+=a[i+k][j+l];
                    }
                }
            }
            if(sum>max)
            {
                max=sum;
            }
        }
    }
    printf("%d",max);
    return 0;
}
