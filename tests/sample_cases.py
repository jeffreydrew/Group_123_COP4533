from program1 import program1


def run_tests():
    # Example 1
    n = 7
    W = 10
    heights = [21, 19, 17, 16, 11, 5, 1]
    widths = [7, 1, 2, 3, 5, 8, 1]
    expected = (3, 42, [3, 2, 2])
    result = program1(n, W, heights, widths)
    print(f"Example 1: {'Solution Passed' if result == expected else ' :( '}")

    # Example 2
    n = 4
    W = 10
    heights = [8, 10, 9, 7]
    widths = [8, 1, 2, 2]
    expected = (2, 18, [1, 3])
    result = program1(n, W, heights, widths)
    print(f"Example 2: {'Solution Passed' if result == expected else ' :( '}")

    # Example 3
    n = 7
    W = 10
    heights = [12, 10, 9, 7, 8, 10, 11]
    widths = [3, 2, 3, 4, 3, 2, 3]
    expected = (3, 30, [3, 1, 3])
    result = program1(n, W, heights, widths)
    print(f"Example 3: {'Solution Passed' if result == expected else ' :( '}")

if __name__ == '__main__':
    run_tests()
