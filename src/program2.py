from typing import List, Tuple

def greedy(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    #this entire function is just a duplicate of algorithm 1

    curr_width = 0
    curr_height = 0
    curr_platform_len = 0
    total_height = 0
    platforms = []
    if not heights:
        return 0, 0, 0,[], 0
    
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
    return len(platforms), total_height, curr_height, platforms, W - curr_width

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
    min_number = min(heights)  # unimodal -> one minimum
    min_index = heights.index(min_number)

    '''
    here is the cool part, we are spliting the input into two parts, the first is left of the minimum, so its monotonically non-increasing. the second is right of the minimum, so its monotonically increasing, but if we reverse it, it becomes monotonically non-decreasing! now we just run algorithm 1 on both parts and add the results together, after reversing the second part again to get the correct order. We also have to check if the minimum painting can be fit in either of the platforms on the left and right of it. If it does, we add it to one of the platforms, doesn't really matter which one because it will not be teh tallest on the platform anyways. If not, it is its own platform. 
    '''

    len1, height1, cur_height1, platforms1, rem_width1 = greedy(min_index, W, heights[0:min_index], widths[0:min_index]) #left part
    while min_index != n and rem_width1 - widths[min_index] >=0 :
        height1 = height1 - cur_height1 + max(cur_height1, heights[min_index])
        cur_height1 = max(cur_height1, heights[min_index])
        rem_width1 -= widths[min_index]
        platforms1[-1] += 1
        min_index += 1
    len2, height2, cur_height2, platforms2, rem_width2 = greedy(n-min_index, W, heights[min_index:n][::-1], widths[min_index:n][::-1]) #right part

    platforms2.reverse() #reverse the right part to get the correct order

    # if (rem_width1 < widths[min_index] and rem_width2 < widths[min_index]): #if the minimum painting can be fit in either of the platforms on the left and right of it
    #     platforms1.append(1)
    #     return len1+len2+1, height1+height2 + heights[min_index], platforms1 + platforms2
    # elif (rem_width1 >= widths[min_index]): #if the minimum painting can be fit in the platform on the left of it
    #     platforms1[-1] += 1 #add one to the last platform on the left
    #     rem_width1 -= widths[min_index]
        
    # else: #if the minimum painting can be fit in the platform on the right of it
    #     platforms2[0] += 1 #add one to the first platform on the right
    # else:    
    return len1 + len2, height1+height2, platforms1 + platforms2

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
    
