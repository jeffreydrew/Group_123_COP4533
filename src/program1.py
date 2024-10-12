from typing import List, Tuple

def program1(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 1
    
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
    curr_width = 0
    curr_height = 0
    curr_platform_len = 0
    total_height = 0
    platforms = []

    for i in range(n):
        if curr_width + widths[i] <= W:
            curr_width += widths[i]
            curr_height = max(curr_height, heights[i])
            curr_platform_len += 1
        else:
            platforms.append(curr_platform_len)
            total_height += curr_height
            curr_width = widths[i]
            curr_height = heights[i]
            curr_platform_len = 1

    platforms.append(curr_platform_len)
    total_height += curr_height
    return len(platforms), total_height, platforms


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program1(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    