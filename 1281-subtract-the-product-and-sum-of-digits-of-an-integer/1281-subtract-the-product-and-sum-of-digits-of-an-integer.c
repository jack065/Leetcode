int subtractProductAndSum(int n){
    int product = 1, sum = 0;
    int result = 0;
    while (n > 0)
    {
        product *= (n % 10);
        sum += (n % 10);
        n = n / 10;
    }
    result = product - sum;
    return result;
}