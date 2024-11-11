from typing import List, Tuple

    
def program3(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 3
    
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
    min_height = float('inf')    # minimum height 
    num_paintings = []        # number of paintings in each display
    m = 0      # Number of displays

    # Naive approach: recursively explore all possible cases and backtrack to compute the optimal value at each explored cases.
    # Parameters:
    # i: Index of the current painting.
    # current_width: total width of the paintings on the current display
    # current_height: tallest painting in the current display
    # total_height: the total height of all displays currently.
    # num_per_display: number of paintings in each display currently. 
    def recurse(i, current_width, current_height, total_height, num_per_display):
        nonlocal min_height, m, num_paintings   # make the parameters global for recursion.

        # Base case:There is no more paintings to arrange, so we compare with the last optimal height and make conclusions. 
        if i == n:
            final_height = total_height + current_height  
            if final_height < min_height:       # final height after arranging the last painting is less than current optimal height => Update all return outputs for new optimal choice.
                min_height = final_height
                m = len(num_per_display)
                num_paintings = num_per_display[:]
            return
        # Case 1: If the current painting can be added to the display
        # => Update current number of paintings in this display. 
        # And call recurse for the next painting with updated width and max_height after considering adding this painting.
        if current_width + widths[i] <= W:
            num_per_display[-1] += 1
            recurse(i+1, current_width + widths[i],max(current_height, heights[i]), total_height, num_per_display)
            num_per_display[-1] -= 1  # reverse adding this painting to this display, allow backtracking
        # Case 2: Cannot add this painting to the display. 
        # => Assign a new display for the current painting.
        # Call recurse for the next painting after updating the height cost for the current painting.
        num_per_display.append(1)
        recurse(i+1, widths[i], heights[i], total_height + current_height, num_per_display)
        num_per_display.pop()  # revert of not assigning new display, allow backtracking.
    
    recurse(0,0,0,0, [0])  # Initial call for first painting => no display or height has been assigned yet.
    return m, min_height, num_paintings 


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program3(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    
