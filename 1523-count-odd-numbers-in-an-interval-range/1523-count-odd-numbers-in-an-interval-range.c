

int countOdds(int low, int high){
    int counter = 0;
    if ((low%2 == 0) && (high%2 == 0)){
        counter = (high-low)/2;
    }
    else{
        counter = ((high-low)/2)+1;
    }
    return counter;
}