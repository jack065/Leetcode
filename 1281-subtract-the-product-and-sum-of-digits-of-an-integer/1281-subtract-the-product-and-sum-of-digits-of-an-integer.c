int subtractProductAndSum(int n){
    int sum = 0, result = 0;
    int product = 1;
    while (n != 0)
    {
        product *= (n % 10);
        sum += (n % 10);
        n = n / 10;
    }
    result = product - sum;
    return result;
}