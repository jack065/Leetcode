bool isPalindrome(int x){
    if (x < 0){
        return false;
    }
    
    int temp = x;
    
    //Long to prevent overloading
    long int save = 0;
    
    while (x != 0){
        save = ((save * 10) + (x % 10));
        x /= 10;
    }
    
    return (save == temp);
    
}