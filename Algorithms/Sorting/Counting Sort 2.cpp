{
    answer[arr[i]]++ ;
}
return answer ;
}

int main()
{
int n;
cin >> n ;
int arr[n] ;
for(int i = 0 ; i < n ; i++)
{
   cin >> arr[i] ;
}
int* result = countingSort(arr, n) ;
for (int i = 0 ; i < 100 ; i++)
{
    while(result[i] > 0)
    {
        cout << i << " " ;
        result[i]-- ;
    }
}
return 0;
}
