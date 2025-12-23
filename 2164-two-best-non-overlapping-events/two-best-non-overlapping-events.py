class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x:x[1])
        arr = []
        max_val, ans = 0, 0
        for start, end, val in events:
            max_val = max(val, max_val)
            arr.append((end, max_val))
        for start, end, val in events:
            ans = max(ans, val)
            ind = bisect.bisect_left(arr, (start, 0))-1
            if ind>=0:
                ans = max(ans, val+arr[ind][1])
        return ans