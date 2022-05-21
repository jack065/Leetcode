class Solution {
    public int nearestValidPoint(int x, int y, int[][] points) {
        int length = points.length;
        int i = -1;
        int distance = 10000000;
        for (int r = 0; r < length; r++){
            if ((x == points[r][0]) || (y == points[r][1])){
                if (distance > Math.abs(x - points[r][0]) + Math.abs(y - points[r][1])){
                    distance = Math.abs(x - points[r][0]) + Math.abs(y - points[r][1]);
                    i = r;
                }
                
            }
        }
        return i;
    }
}