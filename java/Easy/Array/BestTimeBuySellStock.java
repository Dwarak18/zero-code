
public class BestTimeBuySellStock {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int minPrice = Integer.MAX_VALUE;
        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
            }
        }
        return maxProfit;
    }

    public void testMaxProfit() {
        int[][] testCases = {
            {7,1,5,3,6,4},
            {7,6,4,3,1},
            {1,2,3,4,5},
            {2,4,1},
            {3,3,5,0,0,3,1,4},
            {1,2},
            {2,1,2,1,0,1,2},
            {1,2,4,2,5,7,2,4,9,0},
            {2,1,4},
            {1,2,3,4,5,6,7,8,9,10},
            {10,9,8,7,6,5,4,3,2,1},
            {1,1,1,1,1,1,1,1,1,1},
            {1,2,1,2,1,2,1,2,1,2},
            {2,4,1,7},
            {1,2,3,2,1,0,1,2,3,4},
            {3,2,6,5,0,3},
            {1,7,5,3,6,4,8,2,5},
            {2,1,2,0,1},
            {1,2,3,4,5,0,1,2,3,4},
            {1,2,3,4,5,6,7,8,9,10,1}
        };
        int[] expected = {5,0,4,2,4,1,2,8,3,9,0,0,1,6,4,4,7,1,4,9};
        int passed = 0;
        for (int i = 0; i < testCases.length; i++) {
            int result = maxProfit(testCases[i]);
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
        BestTimeBuySellStock solution = new BestTimeBuySellStock();
        solution.testMaxProfit();
        MeasurePerformance.run(() -> {
            int[] arr = new int[100000];
            for (int i = 0; i < arr.length; i++) arr[i] = (int)(Math.random() * 10000);
            for (int i = 0; i < 10; i++) solution.maxProfit(arr);
        }, "BestTimeBuySellStock.maxProfit");
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
