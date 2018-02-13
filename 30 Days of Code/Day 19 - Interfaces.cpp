class Calculator : public AdvancedArithmetic
{
    public :
        int divisorSum(int) ;
};

int Calculator :: divisorSum(int n)
{
    int i = 1, sum = 0 ;
    while(i*i < n)
    {
        if(n % i == 0)
        {
            sum = sum + i + n/i ;
        }
        i = i + 1 ;
    }
    if(i*i == n && n % i == 0)
    {
        sum = sum + i ;
    }
    return sum ;
}
