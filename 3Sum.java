class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int num1;
        ArrayList<List<Integer>> lists = new ArrayList<>();
        for(int i=0;i<nums.length-2;i++){
            for(int j=i+1;j<nums.length-1;j++){
                num1 = 0 - nums[i]-nums[j];
                for(int z=j+1;z<nums.length;z++){
                    if(nums[z] == num1){
                        if(nums[z] == num1){
                        ArrayList<Integer> list = new ArrayList<>();
                        list.add(nums[i]);
                        list.add(nums[j]);
                        list.add(nums[z]);
                        Collections.sort(list);
                        if(lists.contains(list)){
                            continue;
                        }
                        lists.add(list);
                    }
                    }
                }
            }
        }
        return lists;
    }
}
