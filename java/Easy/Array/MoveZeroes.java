import java.util.Arrays;

public class MoveZeroes {
    public void moveZeroes(int[] nums) {
        int zeroIndex = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[zeroIndex] = nums[i];
                zeroIndex++;
            }
        }
        for (int i = zeroIndex; i < nums.length; i++) {
            nums[i] = 0;
        }
    }

    public void testMoveZeroes() {
        int[][] testCases = {
            {0,1,0,3,12},
            {0,0,1},
            {1,0,1},
            {0,0,0,0},
            {1,2,3,4},
            {0,1,2,0,3,0,4},
            {1,0,0,2,0,3},
            {0,0,1,0,0,2,0,0,3},
            {1,2,0,0,3,4,0,5},
            {0,1,0,2,0,3,0,4,0,5},
            {1,0,2,0,3,0,4,0,5,0},
            {0,0,0,1},
            {1,0,0,0},
            {0,1,0,0},
            {1,0,0,0,0},
            {0,0,0,0,1},
            {1,2,0,0,0,3,4,0,5},
            {0,0,0,0,0,0,0,0,0,1},
            {1,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0}
        };
        int[][] expected = {
            {1,3,12,0,0},
            {1,0,0},
            {1,1,0},
            {0,0,0,0},
            {1,2,3,4},
            {1,2,3,4,0,0,0},
            {1,2,3,0,0,0},
            {1,2,3,0,0,0,0,0,0},
            {1,2,3,4,5,0,0,0},
            {1,2,3,4,5,0,0,0,0,0},
            {1,2,3,4,5,0,0,0,0,0},
            {1,0,0,0},
            {1,0,0,0},
            {1,0,0,0},
            {1,0,0,0,0},
            {1,0,0,0,0},
            {1,2,3,4,5,0,0,0,0},
            {1,0,0,0,0,0,0,0,0,0},
            {1,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0}
        };
        int passed = 0;
        for (int i = 0; i < testCases.length; i++) {
            int[] arr = Arrays.copyOf(testCases[i], testCases[i].length);
            moveZeroes(arr);
            if (Arrays.equals(arr, expected[i])) {
                System.out.println("Test case " + (i + 1) + " passed.");
                passed++;
            } else {
                System.out.println("Test case " + (i + 1) + " failed: got " + Arrays.toString(arr) + ", expected " + Arrays.toString(expected[i]));
            }
        }
        System.out.println("Passed " + passed + "/" + testCases.length + " test cases.");
    }

    public static void main(String[] args) {
        MoveZeroes solution = new MoveZeroes();
        solution.testMoveZeroes();
        MeasurePerformance.run(() -> {
            int[] arr = new int[100000];
            for (int i = 0; i < arr.length; i++) arr[i] = (i % 5 == 0) ? 0 : (int)(Math.random() * 10000);
            for (int i = 0; i < 10; i++) solution.moveZeroes(arr);
        }, "MoveZeroes.moveZeroes");
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
