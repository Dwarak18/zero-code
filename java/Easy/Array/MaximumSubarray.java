
public class MaximumSubarray {
    public int maxSubArray(int[] nums) {
        int currSum = nums[0];
        int maxSum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            currSum = Math.max(nums[i], currSum + nums[i]);
            maxSum = Math.max(maxSum, currSum);
        }
        return maxSum;
    }

    public void testMaxSubArray() {
        int[][] testCases = {
            {-2,1,-3,4,-1,2,1,-5,4},
            {1},
            {5,4,-1,7,8},
            {1,2,3,4,5},
            {-1,-2,-3,-4},
            {0,0,0,0},
            {1,-1,1,-1,1,-1,1},
            {2,-1,2,3,4,-5},
            {1,2,-1,2,1,-5,4},
            {3,-2,5,-1},
            {1,2,3,-2,5},
            {1,-2,3,10,-4,7,2,-5},
            {1,2,3,4,-10,5,6,7,8},
            {1,-1,1,-1,1,-1,1,-1,1},
            {1,2,3,-2,5,-3,2,2},
            {1,2,3,4,5,-15,10,10},
            {1,2,3,4,5,-15,10,10,-5,10},
            {1,2,3,4,5,-15,10,10,-5,10,10},
            {1,2,3,4,5,-15,10,10,-5,10,10,10},
            {1,2,3,4,5,-15,10,10,-5,10,10,10,10}
        };
        int[] expected = {6,1,23,15,-1,0,1,10,5,6,9,18,26,1,10,20,25,35,45,55};
        int passed = 0;
        for (int i = 0; i < testCases.length; i++) {
            int result = maxSubArray(testCases[i]);
            if (result == expected[i]) {
                System.out.println("Test case " + (i + 1) + " passed.");
                passed++;
            } else {
                System.out.println("Test case " + (i + 1) + " failed: got " + result + ", expected " + expected[i]);
            }
        }
        System.out.println("Passed " + passed + "/" + testCases.length + " test cases.");
    }

    public static void main(String[] args) {
        MaximumSubarray solution = new MaximumSubarray();
        solution.testMaxSubArray();
        MeasurePerformance.run(() -> {
            int[] arr = new int[100000];
            for (int i = 0; i < arr.length; i++) arr[i] = (int)(Math.random() * 20001) - 10000;
            for (int i = 0; i < 10; i++) solution.maxSubArray(arr);
        }, "MaximumSubarray.maxSubArray");
    }
}

// Decorator-like utility for measuring performance in Java
class MeasurePerformance {
    public static void run(Runnable func, String label) {
        Runtime runtime = Runtime.getRuntime();
        runtime.gc();
        long memBefore = runtime.totalMemory() - runtime.freeMemory();
        long startWall = System.nanoTime();
        long startCpu = System.currentTimeMillis();
        func.run();
        long endWall = System.nanoTime();
        long endCpu = System.currentTimeMillis();
        long memAfter = runtime.totalMemory() - runtime.freeMemory();
        System.out.printf("Performance test: %s\n", label);
        System.out.printf("Wall-clock time: %.6f seconds\n", (endWall - startWall) / 1e9);
        System.out.printf("CPU process time: %.6f seconds\n", (endCpu - startCpu) / 1000.0);
        System.out.printf("Memory usage before: %.2f MB\n", memBefore / (1024.0 * 1024.0));
        System.out.printf("Memory usage after: %.2f MB\n", memAfter / (1024.0 * 1024.0));
        System.out.println("--- End of measurement ---\n");
    }
}
