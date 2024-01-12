class Solution
{
    public:
    
    // Function to reverse first k elements of a queue.
    queue<int> modifyQueue(queue<int> q, int k) {
        // add code here.
        queue<int> ans;
        stack<int> stk;

      //putting k elements into stack
        for(int i=0; i<k; i++){
            stk.push(q.front());
            q.pop();
        }    

      //pushing stack elements into final queue - reversed
        while(!stk.empty()){
            ans.push(stk.top());
            stk.pop();
        }    

      //pushing remaining elements
        while(!q.empty()){
            ans.push(q.front());
            q.pop();
        }
        
        return ans;
    }
};
