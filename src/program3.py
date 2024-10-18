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
    def helper(n):
        if n == 1:
            return [[[0]]]
        groups = []
        subgroups = helper(n-1)

        for subplatform in subgroups:
            #add a new platform
            groups.append(subgroups + [[n-1]])
            #add to all existing platforms
            for i in range(len(subgroups)):
                groups.append(subgroups[i-1:]+[subgroups[i]+[n-1]]+subgroups[i+1:])
        return groups
    
    def get_cost(group):
        cost = 0
        for platform in group:
            cost += max(heights[painting] for painting in platform)
        return cost
    
    def check_valid(group):
        for platform in group:
            width = 0
            for painting in platform:
                width += widths[painting]
            if width > W:
                return False
        return True
    
    groups = helper(n)
    valid_groups = []
    for group in groups:
        if check_valid(group):
            valid_groups.append(group)
    
    min_cost = float('inf')
    for group in valid_groups:
        cost = get_cost(group)
        if cost < min_cost:
            min_cost = cost
            best_group = group
    
    return len(best_group), get_cost(best_group), [len(group) for group in best_group]



if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program3(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    