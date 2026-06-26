void foo(int n){
    int x=n/2;
    foo(n-1);
    foo(n-2);
}