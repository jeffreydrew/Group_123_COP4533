import random
import io
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.program1 import program1  # Import the main function

tests = [
    "7 10\n21 19 17 16 11 5 1\n7 1 2 3 5 8 1\n",
    "10 5\n10 9 8 7 6\n1 2 1 3 2\n",
    "20 6\n30 25 20 15 10 5\n3 4 2 5 3 2\n",
    "10 4\n40 30 20 10\n10 10 10 10\n",
    "5 3\n15 10 5\n5 5 5\n",
    "15 5\n100 20 15 10 5\n10 3 4 2 1\n",
    "20 6\n200 30 25 20 15 10\n15 4 3 5 2 1\n",
    "10 5\n20 19 18 17 16\n2 3 2 2 1\n",
    "15 7\n30 29 28 27 26 25 24\n3 4 2 3 2 1 2\n",
    "12 6\n100 99 5 4 3 2\n3 4 2 1 3 2\n",
    "20 8\n200 195 190 50 45 40 10 5\n5 4 3 2 3 4 2 1\n",
    "10 5\n20 18 15 12 10\n3 3 4 5 5\n",
    "15 7\n30 25 20 18 15 12 10\n5 5 5 7 4 4 7\n",
    "11 5\n20 18 15 12 10\n3 5 4 2 6\n",
    "17 6\n30 25 20 15 12 10\n5 7 3 4 6 9\n",
    "10 5\n1 2 3 4 5\n2 3 2 2 1\n",
    "15 6\n5 10 15 20 25 30\n3 4 2 3 2 1\n",
    "10 5\n20 15 10 5 1\n2 3 2 2 1\n",
    "15 6\n30 25 20 15 10 5\n3 4 2 3 2 1\n",
    "10 5\n10 5 1 5 10\n2 3 2 2 1\n",
    "15 7\n20 15 10 5 10 15 20\n3 2 3 2 3 2 3\n",
    "12 7\n10 5 1 1 1 5 10\n2 3 1 2 1 2 3\n",
    "20 9\n30 20 10 5 5 5 10 20 30\n3 4 2 3 2 1 2 3 4\n",
    "15 7\n20 15 10 5 6 8 10\n3 2 3 2 3 2 3\n",
    "20 9\n30 20 10 5 6 8 11 15 20\n3 4 2 3 2 1 2 3 4\n",
    "10 5\n10 5 1 5 10\n3 2 10 2 3\n",
    "15 7\n20 15 10 5 10 15 20\n3 4 2 15 2 3 4\n",
    "12 7\n10 5 5 5 5 5 10\n2 1 3 4 2 3 2\n",
    "20 9\n30 20 10 10 10 10 10 20 30\n3 4 2 5 1 3 4 3 4\n",
    "50 20\n50 45 40 35 30 25 20 15 10 5 6 7 8 9 10 15 20 25 30 35\n2 3 4 2 3 4 2 3 4 2 3 4 2 3 4 2 3 4 2 3\n",
    "100 30\n100 90 80 70 60 50 40 30 20 10 5 6 7 8 9 10 20 30 40 50 60 70 80 90 100 110 120 130 140 150\n3 4 5 3 4 5 3 4 5 3 4 5 3 4 5 3 4 5 3 4 5 3 4 5 3 4 5 3 4 5\n"
]

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

def run_test(test_input):
    # Generate a test case
    #test_input = generate_test_case(10, 100)

    # Use given test case
    
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

        m, total_height, num_paintings = program1(n, W, heights, widths)

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
    for test_input in tests:
        run_test(test_input)
