class MinimumOperationstoHalveArraySum {
    public int halveArray(int[] nums) {
        PriorityQueue<Double> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        double sum = 0;
    
        for (int i = nums.length - 1; i >= 0; i--)
        {
            sum += (double)nums[i];
            maxHeap.add(Double.valueOf(nums[i]));
        }
        double halfSum = sum / 2;
        int count = 0;
        while(sum > halfSum)
        {
            count++;
            double a = maxHeap.poll() / 2;
            sum -= a;
            maxHeap.add(a);
        }
        return count;
    }
}
