void solve(int n){
    if(n<=1) return;

    solve(n/2);
    solve(n/2);
}