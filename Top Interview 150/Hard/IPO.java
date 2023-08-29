import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public class IPO {

    public int findMaxCapital(int[] capital, int[] profits, int k, int w) {
        List<int[]> toDo = new ArrayList<>();
        for (int i = 0; i < capital.length; i++) {
            toDo.add(new int[]{capital[i], profits[i]});
        }

        toDo.sort(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o2[0], o1[0]);
            }
        });

        PriorityQueue<Integer> heap = new PriorityQueue<>();

        for (int i = 0; i < k; i++) {
            while (!toDo.isEmpty() && toDo.get(toDo.size() - 1)[0] <= w) {
                heap.add(-toDo.remove(toDo.size() - 1)[1]);
            }
            if (heap.isEmpty()) {
                return w;
            }
            w += -heap.poll();
        }

        return w;
    }

    public static void main(String[] args) {
        int[] profits = {1, 2, 3};
        int[] capital = {0, 1, 2};
        int k = 10;
        int startingCapital = 0;

        IPO cp = new IPO();
        int result = cp.findMaxCapital(capital, profits, k, startingCapital);
        System.out.println("Maximum capital after investments: " + result);
    }
}
