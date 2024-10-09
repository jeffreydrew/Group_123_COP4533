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

    # this basically iterates through each painting and tracks the platforms W & H

    plat = []
    newPlat = []
    newWidth = 0
    newHeight = 0
    finalHeight = 0

    for i in range(n):
        if newWidth + widths[i] <= W: # adds painting
            newPlat.append(i)
            newWidth += widths[i]
            newHeight = max(newHeight, heights[i])
        else:
            plat.append(newPlat)
            finalHeight += newHeight

            newPlat = [i] # new platform starts
            newWidth = widths[i]
            newHeight = heights[i]

    if newPlat:
        plat.append(newPlat)
        finalHeight += newHeight

    return len(plat), finalHeight, [len(p) for p in plat]

    ############################

    ##return 0, 0, [] # replace with your code


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program1(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
