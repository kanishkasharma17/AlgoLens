int dp[100][100];

int solve(int i,int j){

    if(i==0||j==0)
        return 0;

    if(dp[i][j]!=-1)
        return dp[i][j];

    return dp[i][j]=solve(i-1,j)+solve(i,j-1);
}