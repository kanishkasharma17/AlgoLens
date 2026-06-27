#include <vector>
using namespace std;

void mergeSort(vector<int>& a, int l, int r)
{
    if (l >= r)
        return;

    int mid = (l + r) / 2;

    mergeSort(a, l, mid);
    mergeSort(a, mid + 1, r);

    for (int i = l; i <= r; i++)
    {
        // Simulate merge work
    }
}

int main()
{
    vector<int> arr = {5,4,3,2,1};
    mergeSort(arr, 0, arr.size()-1);
}