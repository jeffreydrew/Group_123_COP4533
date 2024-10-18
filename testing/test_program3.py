import random
import io
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
from generate_tests import generate_test_case

from src.program1 import program1
from src.program2 import program2 
from src.program3 import program3 
from src.program4 import program4
from src.program5A import program5A
from src.program5B import program5B

programs = {
    "program1": program1,
    "program2": program2,
    "program3": program3,
    "program4": program4,
    "program5A": program5A,
    "program5B": program5B
}

def run_test(test_case=None, random_test=False):
    if random_test:
        # Generate a test case
        test_input = generate_test_case(10, 100, test_case)
    else:
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

        m, total_height, num_paintings = programs.get(test_case)(n, W, heights, widths)

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
    run_test('program2', random_test=True)