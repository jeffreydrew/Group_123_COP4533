import time
import random
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)


from src.program3 import program3
from src.program4 import program4
from src.program5A import program5A
from src.program5B import program5B

def compare_algorithms_different_ranges():
    plt.figure(figsize=(12, 8))
    W = 100  # Fixed platform width
    
    # Different ranges for each algorithm
    sizes_3 = range(2, 26)
    sizes_4 = range(2, 1001)
    sizes_5 = range(2, 1001)
    
    # Store times for each algorithm
    times_3 = []
    times_4 = []
    times_5a = []
    times_5b = []
    
    # # Test Program 3 (up to 25)
    # for n in tqdm(sizes_3, desc="Testing Program 3"):
    #     heights = [random.randint(1, 50) for _ in range(n)]
    #     widths = [random.randint(1, W//2) for _ in range(n)]
    #     start = time.time()
    #     program3(n, W, heights, widths)
    #     times_3.append(time.time() - start)
    
    # Test Program 4 (up to 100)
    for n in tqdm(sizes_4, desc="Testing Program 4"):
        heights = [random.randint(1, 50) for _ in range(n)]
        widths = [random.randint(1, W//2) for _ in range(n)]
        start = time.time()
        program4(n, W, heights, widths)
        times_4.append(time.time() - start)
    
    # Test Programs 5A and 5B (up to 1000)
    for n in tqdm(sizes_5, desc="Testing Programs 5A/5B"):
        heights = [random.randint(1, 50) for _ in range(n)]
        widths = [random.randint(1, W//2) for _ in range(n)]
        
        start = time.time()
        program5A(n, W, heights, widths)
        times_5a.append(time.time() - start)
        
        start = time.time()
        program5B(n, W, heights, widths)
        times_5b.append(time.time() - start)
    
    # Plot results
    # plt.plot(list(sizes_3), times_3, 'r-', label='Program 3', marker='o')
    plt.plot(list(sizes_4), times_4, 'b-', label='Program 4')
    plt.plot(list(sizes_5), times_5a, 'g-', label='Program 5A (DP top-down)')
    plt.plot(list(sizes_5), times_5b, 'y-', label='Program 5B (DP bottom-up)')
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Performance Comparison of Exact Algorithms')
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend()
    # plt.yscale('log')  # Use log scale for better visualization
    plt.tight_layout()
    plt.savefig('algorithm_comparison_different_ranges.png', dpi=300)
    plt.close()

if __name__ == "__main__":
    compare_algorithms_different_ranges()