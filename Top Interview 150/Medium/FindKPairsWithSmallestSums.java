import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class FindKPairsWithSmallestSums {
    FindKPairsWithSmallestSums () {}

    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> sol = new ArrayList<>();
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        
        int len1 = nums1.length;
        int len2 = nums2.length;
        
        for (int i = 0; i < k && i < len1; i++) {
            heap.offer(new int[] {nums1[i] + nums2[0], i, 0});
        }
        
        while (k-- > 0 && !heap.isEmpty()) {
            int[] min = heap.poll();
            int i = min[1];
            int j = min[2];
            sol.add(List.of(nums1[i], nums2[j]));
            if (++j < len2) {
                heap.offer(new int[] {nums1[i] + nums2[j], i, j});
            }
        }
        return sol;
    }

    public static void main (String[] args) {
        FindKPairsWithSmallestSums sol = new FindKPairsWithSmallestSums();
        int[] nums1 = {1,2,4};
        int[] nums2 = {-1,1,2};
        int k = 100;
        long startTime = System.nanoTime();
        List<List<Integer>> res = sol.kSmallestPairs(nums1, nums2, k);
        long endTime = System.nanoTime();
        long elapsedTime = endTime - startTime;
        System.out.printf("Runtime: %.10fs%n", elapsedTime / 1_000_000_000.0);
        System.out.println(res);
    }
}

