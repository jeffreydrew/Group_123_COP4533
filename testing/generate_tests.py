import random

def generate_test_case(n, W, program):
    n = random.randint(1, min(n, 10**5 - 1))
    W = random.randint(1, min(W, 10**5 - 1))

    # Generate heights
    heights = [random.randint(1, 10**5 - 1) for _ in range(n)]

    if program == "program1":
        heights.sort(reverse=True)
    elif program == "program2":
        min_value = min(heights)
        min_index = heights.index(min_value)
        left = sorted([h for h in heights[:min_index] if h > min_value], reverse=True)
        right = sorted([h for h in heights[min_index+1:] if h > min_value])
        heights = left + [min_value] + right

    widths = [random.randint(1, 10**5 - 1) for _ in range(n)]

    # Format the test case
    test_case = f"{n} {W}\n"
    test_case += " ".join(map(str, heights)) + "\n"
    test_case += " ".join(map(str, widths)) + "\n"

    return test_case
