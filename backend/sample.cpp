void solve(int n){
    if(n<=1) return;
    int mid=n/2;
    int x=mid;
    solve(x);
}