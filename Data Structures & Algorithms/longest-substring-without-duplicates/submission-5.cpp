class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int window = 0;
        unordered_set<int> chars;
        int l = 0;
        
        for (int r = 0; r < s.size(); r++) {
            while (chars.find(s[r]) != chars.end()) {
                chars.erase(s[l]);
                l++;
            }

            chars.insert(s[r]);
            window = max(window, r - l + 1);
        }

        return window;
    }
};
