class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            int[] frequency = new int[26];
            
            for (int i = 0; i < s.length(); i++) {
                frequency[s.charAt(i) - 'a']++;
            }
            
            String key = Arrays.toString(frequency);
            
            if (map.containsKey(key)) {
                map.get(key).add(s);
            }
            else {
                List<String> list = new LinkedList<>();
                list.add(s);
                map.put(key, list);
            }
        }
        return new ArrayList<List<String>>(map.values());
    }
}

