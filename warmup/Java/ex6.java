import java.util.HashMap;
import java.util.Map;

class Ex6 {

    public static void longestSubBinaryArray (int[] nums) {
        // Given a binary array, find the longest subarray where number of 0 === number of 1
        Map<Integer, Integer> d = new HashMap<>();
        d.put(0, -1);
        int maxLen = 0;
        int endInd = 0;
        int addSum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {addSum--;}
            else {addSum++;}
            if (d.containsKey(addSum)) {
                if (i - d.get(addSum) > maxLen) {
                    maxLen = i - d.get(addSum);
                    endInd = i;
                }
            }
            d.put(addSum, i);
        }
        
    }
    public static void main (String[] args) {
        int[] num = {0, 0, 1, 0, 1, 0, 0};
    }

}