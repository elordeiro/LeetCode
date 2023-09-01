import java.util.HashMap;

public class MaxPointsOnALine {
    public int maxPoints(int[][] points) {
        int n = points.length;
        if (n < 3) return n;

        
        HashMap<Double, Integer> slopeMap = new HashMap<>(n, 0.75f);
        int longestLine = 0;
        int maxLength = n;
        double slope;
        
        for (int i = 0; i < n; ++i) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for (int j = i + 1; j < n; ++j) {
                int x2 = points[j][0];
                int y2 = points[j][1];
                if (x1 == x2)
                    slope = Float.POSITIVE_INFINITY;
                else if (y1 == y2)
                    slope = 0f;
                else
                    slope = (float) (y1 - y2) / (x1 - x2);
                
                int count = slopeMap.getOrDefault(slope, 1) + 1;
                slopeMap.put(slope, count);
                longestLine = Math.max(longestLine, count);
            }
            if (longestLine == maxLength--)
                return longestLine;
            slopeMap.clear();
        }
        return longestLine;
    }
    
    public static void main (String[] args) {
        MaxPointsOnALine sol = new MaxPointsOnALine();
        // int[][] points = {{1,1},{3,2},{5,3},{4,1},{2,3},{1,4}};
        // int[][] points = {{9,-25},{-4,1},{-1,5},{-7,7}};
        // int[][] points = {{2,3},{3,3},{-5,3}};
        int[][] points = {{1,1},{3,2},{5,3},{4,1},{2,3},{1,4}};
        System.out.println(sol.maxPoints(points));
    }
}