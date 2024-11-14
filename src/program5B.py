from typing import List, Tuple

    
def program5B(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 5B
    
    Parameters:
    n (int): number of paintings
    W (int): width of the platform
    heights (List[int]): heights of the paintings
    widths (List[int]): widths of the paintings

    Returns:
    int: number of platforms used
    int: optimal total height
    List[int]: number of paintings on each platform
    """
    ############################
    # Add you code here
    ############################
    #Dp bottom-up approach: Dp[i] table keeps track of the minimum height (optimal height) to arrange the first i paintings. 
    # The algorithm loops over n paintings. In each ith painting, the loop will check over the first i paintings for optimal dp value. 
    # Thus, time complexity is 1+2+...+n, or O(n^2).
    dp = [float('inf')] * (n+1)  #Intialize dp
    dp[0] = 0    # Base case: No painting has been arranged.
    new_display = [-1] * (n+1)   # new_display table to keep track of indices where new display is used 
    # Starting the arrangement at the first painting to the nth paintign.
    for i in range(1, n+1):
        total_width = 0
        max_height = 0
        # Iterate to check all possible ways to put the ith paintings with the first j paintings (j <=i). Each possible case recursively calculates the min height for first j-1 paintings. 
        for j in range(i,0,-1):
            total_width += widths[j-1]
            max_height = max(max_height, heights[j-1])
            # Cannot add ith painting if it exceeds W constraint.
            if total_width > W:
                continue
            # If the optimal arrangement up to the j-1 th painting plus the painting from j to i results in smaller heihght,
            # In other words, as j-1th paintings are arranged in optimal way, we found a new optimal arrangement for jth-ith paintings. update dp[i] and store index j-1 as new_display needs.
            if dp[j-1] + max_height < dp[i]:
                dp[i] = dp[j-1] + max_height
                new_display[i] = j-1
    
    #Use new_display table to backtrack to find all displays used for optimal arranging all n paintings.
    displays = []
    current = n
    while current > 0:
        start = new_display[current]
        displays.append(current - start)
        current = start

    return len(displays), dp[n], displays[::-1] # revert the right order of backtracking displays used.


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program5B(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    
