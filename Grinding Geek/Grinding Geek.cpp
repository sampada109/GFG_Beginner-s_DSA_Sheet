vector<int> curr(total + 1);
        for(int ind = n - 1; ind >= 0; ind--){
            for(int tot = total; tot >= 0; tot--){
                if(tot >= cost[ind])
                    curr[tot] = max(curr[tot], 1 + curr[tot - 0.1 * cost[ind]]);
            }
        }
        return curr[total];
