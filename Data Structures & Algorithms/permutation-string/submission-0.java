class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int len1 = s1.length(), len2 = s2.length();
        if (len1 > len2) return false;

        for (int i = 0; i <= len2 - len1; i++) {
            String substr = s2.substring(i, i + len1);
            if (isPermutation(s1, substr)) return true;
        }

        return false;
    }

    private boolean isPermutation(String s1, String s2) {
        int[] count = new int[26];
        for (char c : s1.toCharArray()) count[c - 'a']++;
        for (char c : s2.toCharArray()) count[c - 'a']--;

        for (int c : count) {
            if (c != 0) return false;
        }

        return true;
    }
}

