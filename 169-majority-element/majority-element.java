class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> map= new HashMap<>();
        int n = nums.length;
        for (int a: nums){
            if (map.containsKey(a)){
                map.put(a,map.get(a)+1);
            }
            else{
                map.put(a,1);
            }
        }
        for (int a:map.keySet()){
            if (map.get(a)>n/2){
                return a;
            }
        }
        return -1;
    }
}