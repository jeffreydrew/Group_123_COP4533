from typing import List, Tuple

    
def program4(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 4
    
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
    # 
    # O(n^2*W) algorithm: Use dynamic programming approach. 
    # For each i_th painting, exploring all possible width within constraint W can compute optimal arrangement at each dp[i][w] state.
    dp = [[(float('inf'), float('inf'), []) for _ in range(W + 1)] for _ in range(n + 1)] # Initialize dp table with size (n+1,W+1)
    dp[0][0] = (0,0,[])  # Base case: No painting and no width. Each dp element stores its optimal output at that moment.
    # Iterate throguh all paintings
    for i in range(1,n+1):
        #For each painting, iterate through all possible width w up to W.
        for w in range(W+1):
            width_sum = 0  # current total width used for that display
            max_height = 0  # current max height of that dispaly
            # Iterate through all previously arranged painting to calculate the used width and max height
            for j in range(i, 0, -1):
                width_sum += widths[j-1]
                max_height = max(heights[j-1],max_height)
                # Stop if total width exceeds width constraint
                if width_sum > W:
                    break
                # Compute height after adding this painting. there are two possible cases:
                prev_rows, prev_height, prev_num_paintings = dp[j - 1][w]
                new_height = prev_height + max_height
                new_paintings_per_row = prev_num_paintings + [i - j + 1]  # New row with painting count
                # Case 1: The current height is smaller than the optimal height or same height but use fewer rows.Update the new optimal value.
                if new_height < dp[i][width_sum][1] or (new_height == dp[i][width_sum][1] and prev_rows+1 < dp[i][width_sum][0]):
                    dp[i][width_sum] = (prev_rows+1, new_height, new_paintings_per_row)
                # Case 2: Otherwise, we will not consider that painting as it is not optimal choice there. Continue considering other width choices. 
    min_rows, min_height, num_paintings = min((dp[n][w] for w in range(W+1)), key = lambda x: (x[0], x[1]))  # Find the smallest height and fewest rows in all possible arrangements in the dp table. It is the optimal value.
    return min_rows, min_height, num_paintings # replace with your code


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program4(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    
