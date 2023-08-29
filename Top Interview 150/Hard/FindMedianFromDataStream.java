import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;

public class FindMedianFromDataStream {
    PriorityQueue<Integer> smallHeap = new PriorityQueue<>(Collections.reverseOrder());;
    PriorityQueue<Integer> largeHeap = new PriorityQueue<>();;
    boolean isEven = true;
    
    public void addNum(int num) {
        if (isEven) {
            smallHeap.offer(num);
            largeHeap.offer(smallHeap.poll());
        } else {
            largeHeap.offer(num);
            smallHeap.offer(largeHeap.poll());
        }
        isEven = !isEven;
    }

    public double findMedian() {
        if (isEven) {
            return (smallHeap.peek() + largeHeap.peek()) / 2.0;
        }
        return largeHeap.peek();
    }

    public static void main (String[] args) {
        FindMedianFromDataStream sol = new FindMedianFromDataStream();
        List<Double> res = new ArrayList<>();
        sol.addNum(-1);
        res.add(sol.findMedian());
        sol.addNum(-2);
        res.add(sol.findMedian());
        sol.addNum(-3);
        res.add(sol.findMedian());
        sol.addNum(-4);
        res.add(sol.findMedian());
        sol.addNum(-5);
        res.add(sol.findMedian());
        System.out.println(res);
    }
}
