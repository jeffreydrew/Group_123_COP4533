from typing import List, Tuple

def greedy(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:

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
    return len(platforms), total_height, platforms, W - curr_width

def program2(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 2
    
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

    # Find the min index
    min_number = min(heights)  # unimodel -> one minimum
    min_index = heights.index(min_number)

    len1, height1, platforms1, rem_width1 = greedy(min_index, W, heights[0:min_index], widths[0:min_index])
    len2, height2, platforms2, rem_width2 = greedy(min_index, W, heights[n-1:min_index+1:-1], widths[n-1:min_index+1:-1])


    if (rem_width1 < widths[min_index] and rem_width2 < widths[min_index]):
        return len1+len2+1, height1+height2 + heights[min_index], platforms1.append(1).append(reversed(platforms2))
    elif (rem_width1 >= widths[min_index]):
        platforms1[-1] += 1
        return len1 + len2, height1+height2, platforms1.append(reversed(platforms2))
    else:
        platforms2[-1] += 1
        return len1 + len2, height1+height2, platforms1.append(reversed(platforms2))
    
    #return 0, 0, [] # replace with your code


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program2(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    
