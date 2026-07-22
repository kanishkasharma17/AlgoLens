int solve(int n){

    if(dp[n]!=-1)
        return dp[n];

    return dp[n]=solve(n-1)+solve(n-2);
}