/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int high = n;
        int low = 1;
        while (low <= high){
            int middle = (low + (high - low) / 2);
            int g = guess(middle);
            if (g == -1){
                high = middle - 1;
            }
            else if (g == 1){
                low = middle + 1;
            }
            else if (g == 0){
                return middle;
            }
        }
        return 0;
    }
}