class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int daily = 0;
        int l = 0;
        int r = 1;

        while (r < prices.size()) {
            if (prices[r] > prices[l]) {
                daily = prices[r] - prices[l];
                if (daily > profit) {
                    profit = daily;
                }
            } else {
                l = r;
            }

            r++;
        }

        return profit;
    }
};
