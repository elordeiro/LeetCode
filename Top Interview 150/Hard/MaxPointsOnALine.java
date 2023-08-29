import java.util.HashMap;

public class MaxPointsOnALine {
    public int maxPoints(int[][] points) {
        if (points.length == 1) return 1;

        int n = points.length;
        int longestLine = 0;

        for (int i = 0; i < n; ++i) {
            HashMap<Float, Integer> slopeMap = new HashMap<>();
            for (int j = i + 1; j < n; ++j) {
                int x1 = points[i][0];
                int y1 = points[i][1];
                int x2 = points[j][0];
                int y2 = points[j][1];
                float slope;
                if (x1 == x2)
                    slope = Float.MAX_VALUE;
                else if (y1 == y2)
                    slope = 0f;
                else {
                    slope = (float) (y1 - y2) / (x1 - x2);
                }
                slopeMap.put(slope, slopeMap.getOrDefault(slope, 1) + 1);
            }
            if (!slopeMap.isEmpty()) {
                for (int count : slopeMap.values())
                    longestLine = Math.max(count, longestLine);
            }
        }
        return longestLine;
    }
    
    public static void main (String[] args) {
        MaxPointsOnALine sol = new MaxPointsOnALine();
        // int[][] points = {{1,1},{3,2},{5,3},{4,1},{2,3},{1,4}};
        // int[][] points = {{9,-25},{-4,1},{-1,5},{-7,7}};
        int[][] points = {{2,3},{3,3},{-5,3}};
        System.out.println(sol.maxPoints(points));
    }
}