from typing import List, Tuple
import sys

    
def program5A(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 5A
    
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
    # Increase recursion limit to handle larger inputs
    sys.setrecursionlimit(max(1000, n*2))
    
    # DP with memoization (top_down). dp[i] table tracks the optimal minimum height of arranging the first i paintings
    # The top-down iterate through n paintings. As the minimum height is not recomputed, each paintings will only call recurse(i) i times. Thus time complexity is 1+2+...+n = O(n^2).
    dp = [-1] * (n+1)  # Initialize dp table. -1 means uncomputed at that ith painting.
    new_display = [-1] * (n+1) # for backtracking the optimal arrangement. It stores the index where new display is used
    # Recursion dp approach: explore all possible cases to arrange the ith painting and calculate min height at each case.
    # recurse() function returns the optimal arrangement at each ith state.
    def recurse(i):
        # base case: there is no painting to arrange. Return 0 as the height of zero painting.
        if i == 0: return 0
        # Memoization: The min height at the recursive ith painting has been computed. Return the min height at that state.
        if dp[i] != -1: 
            return dp[i]
        # Intialize width and height for the ith painting.
        width_sum = 0
        max_height = 0
        dp[i] = float('inf')
        #Iterate through all possible subset of paintings starting at j and ending at i. Update the width and height if possible
        for j  in range (i, 0, -1):
            width_sum += widths[j-1]
            max_height = max(max_height, heights[j-1])

            if width_sum > W:
                continue
            # curr_height is the heigiht if the subset from jth to ith painting forms a new row. Calculated by adding the minimum height requred to arrange the first j-1th paintings recursively.
            curr_height = recurse(j-1) + max_height
            # Recalculating min height at ith painting if necessary when considering all cases. 
            if curr_height < dp[i]:
                dp[i] = curr_height
                new_display[i] = j-1  # Keep track of where the new display starts
        return dp[i]
    
    min_height = recurse(n) # Start top-down dp from the nth paintings
    # Backtrack to identify number of paintings at each display for optimal arrangement using new_display tracking table.
    displays = []
    current = n
    while current > 0:
        start = new_display[current]
        displays.append(current - start)
        current = start

    return len(displays), min_height, displays[::-1] # revert to get the right order of the backtracking order of all displays. 


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program5A(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    
