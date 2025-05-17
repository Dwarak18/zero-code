import java.util.Arrays;

public class TwoSum {
    // Brute-force two sum
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return null;
    }

    public void testTwoSum() {
        int[][][] testCases = {
            {{2, 7, 11, 15}, {9}, {0, 1}},
            {{3, 2, 4}, {6}, {1, 2}},
            {{3, 3}, {6}, {0, 1}},
            {{1, 2, 3, 4, 5}, {9}, {3, 4}},
            {{0, 4, 3, 0}, {0}, {0, 3}},
            {{-1, -2, -3, -4, -5}, {-8}, {2, 4}},
            {{1, 5, 1, 5}, {10}, {1, 3}},
            {{1, 2}, {3}, {0, 1}},
            {{1, 2, 3}, {7}, null},
            {{2, 5, 5, 11}, {10}, {1, 2}},
            {{1, 3, 4, 2}, {6}, {2, 3}},
            {{1, 2, 3, 4, 4}, {8}, {3, 4}},
            {{1, 2, 3, 4, 5, 6}, {11}, {4, 5}},
            {{1, 2, 3, 4, 5, 6}, {7}, {0, 5}},
            {{1, 2, 3, 4, 5, 6}, {2}, null},
            {{1, 2, 3, 4, 5, 6}, {12}, null},
            {{1, 2, 3, 4, 5, 6}, {5}, {0, 3}},
            {{1, 2, 3, 4, 5, 6}, {9}, {2, 5}},
            {{1, 2, 3, 4, 5, 6}, {10}, {3, 5}},
            {{1, 2, 3, 4, 5, 6}, {8}, {1, 5}}
        };
        int passed = 0;
        for (int i = 0; i < testCases.length; i++) {
            int[] nums = testCases[i][0];
            int target = testCases[i][1][0];
            int[] expected = testCases[i].length > 2 ? testCases[i][2] : null;
            int[] result = twoSum(nums, target);
            if ((expected == null && result == null) ||
                (expected != null && result != null && Arrays.equals(result, expected))) {
                System.out.println("Test case " + (i + 1) + " passed.");
                passed++;
            } else {
                System.out.println("Test case " + (i + 1) + " failed: got " + Arrays.toString(result) + ", expected " + Arrays.toString(expected));
            }
        }
        System.out.println("Passed " + passed + "/" + testCases.length + " test cases.");
    }

    public static void main(String[] args) {
        TwoSum solution = new TwoSum();
        solution.testTwoSum();
        MeasurePerformance.run(() -> {
            int[] arr = new int[100000];
            for (int i = 0; i < arr.length; i++) arr[i] = (int)(Math.random() * 10000);
            for (int i = 0; i < 10; i++) solution.twoSum(arr, 12345);
        }, "TwoSum.twoSum");
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
