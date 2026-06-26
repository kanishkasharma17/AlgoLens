void mergeSort(int n)
{
    if(n<=1)
        return;

    mergeSort(n/2);
    mergeSort(n/2);

    for(int i=0;i<n;i++)
    {
    }
}