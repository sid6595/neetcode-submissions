public class Solution {

    public int minEatingSpeed(int[] piles, int h) {
        int start = 1;
        int end = Arrays.stream(piles).max().getAsInt(); // Max bananas in any pile

        while (start < end) {
            int mid = start + (end - start) / 2;
            int hours = countHours(piles, mid);

            if (hours <= h) {
                end = mid; // Try slower speed
            } else {
                start = mid + 1; // Too slow, need faster speed
            }
        }

        return start; // The smallest speed that allows finishing in ≤ h hours
    }

    private int countHours(int[] piles, int speed) {
        int hours = 0;
        for (int pile : piles) {
            hours += (pile + speed - 1) / speed; // Ceiling division
        }
        return hours;
    }
}

