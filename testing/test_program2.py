import random
import io
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.program2 import program2  # Import the main function

def generate_test_case(n, W):
    n = random.randint(1, min(n, 10**5 - 1))
    W = random.randint(1, min(W, 10**5 - 1))

    # Generate heights
    heights = [random.randint(1, 10**5 - 1) for _ in range(n)]
    heights.sort(reverse=True)

    # Generate widths
    widths = [random.randint(1, 10**5 - 1) for _ in range(n)]

    # Format the test case
    test_case = f"{n} {W}\n"
    test_case += " ".join(map(str, heights)) + "\n"
    test_case += " ".join(map(str, widths)) + "\n"

    return test_case

def run_test():
    # Generate a test case
    #test_input = generate_test_case(10, 100)

    # Use given test case
    test_input = "7 10\n12 10 9 7 8 10 11\n3 2 3 4 3 2 3\n"
    
    # Store the original stdin
    original_stdin = sys.stdin
    
    # Replace sys.stdin with our string buffer
    sys.stdin = io.StringIO(test_input)
    
    # Capture stdout
    original_stdout = sys.stdout
    sys.stdout = io.StringIO()

    # Run the main program
    if __name__ == '__main__':
        n, W = map(int, input().split())
        heights = list(map(int, input().split()))
        widths = list(map(int, input().split()))

        m, total_height, num_paintings = program2(n, W, heights, widths)

        print(m)
        print(total_height)
        for i in num_paintings:
            print(i)

    # Get the output
    output = sys.stdout.getvalue()
    
    # Restore original stdin and stdout
    sys.stdin = original_stdin
    sys.stdout = original_stdout

    # Print the test input and output
    print("Test Input:")
    print(test_input)
    print("Test Output:")
    print(output)

if __name__ == "__main__":
    run_test()