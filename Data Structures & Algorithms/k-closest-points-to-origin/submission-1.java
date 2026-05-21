class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // Store [distance, index] pairs
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) ->
        (a[0] * a[0] + a[1] * a[1]) - (b[0] * b[0] + b[1] * b[1]));
        
        for (int i = 0; i < points.length; i++) {
            int dist = points[i][0] * points[i][0] + points[i][1] * points[i][1];
            minHeap.offer(new int[]{dist, i});  // Store distance and index
        }
        
        int[][] result = new int[k][2];
        for (int i = 0; i < k; i++) {
            int index = minHeap.poll()[1];  // Get the index
            result[i] = points[index];      // Use index to get the original point
        }
        
        return result;
    }
}
