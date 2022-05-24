class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        if (s1.equals(s2)){
            return true;
        }
        int counter = 0;
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < s1.length(); i++){
            if (s1.charAt(i) != s2.charAt(i)){
                counter++;
                list.add(i);
            }
        }
        if (counter == 2){
            if ((s1.charAt(list.get(0)) == s2.charAt(list.get(1))) && (s1.charAt(list.get(1)) == s2.charAt(list.get(0)))){
                return true;
            }
        }
        return false;
    }
}