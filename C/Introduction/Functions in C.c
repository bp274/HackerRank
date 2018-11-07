#include <stdio.h>

int max_of_four(int a, int b, int c, int d)
{
    int max_of_two = a >= b ? a : b;
    int max_of_three = max_of_two >= c ? max_of_two : c;
    int max_of_four = max_of_three >= d ? max_of_three : d;

    return max_of_four;
}

int main()
{
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);

    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);

    return 0;
}
