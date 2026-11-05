class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] frequency = new int[2001];

        // Count frequency
        for (int n : nums) {
            frequency[n + 1000]++;
        }

        // Initialize result with first k indices
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = i;
        }

        // Iterate through the rest of frequency array
        for (int i = k; i < frequency.length; i++) {
            for (int j = 0; j < k; j++) {
                // If current frequency is bigger than result[j] frequency, insert here
                if (frequency[i] > frequency[result[j]]) {
                    // Shift elements to the right to make room for i
                    for (int shift = k - 1; shift > j; shift--) {
                        result[shift] = result[shift - 1];
                    }
                    result[j] = i;
                    break;  // Insert done, move on
                }
            }
        }

        // Convert indices back to original numbers
        for (int i = 0; i < k; i++) {
            result[i] -= 1000;
        }

        return result;
    }
}
