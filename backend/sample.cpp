void solve(int n){
    if(n<=1) return;
    solve(n-1);
    solve(n-2);
}