import random
import time
#might have to comment next two lines out if on windows
import matplotlib #this 
matplotlib.use('Agg') #and this

import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from scipy.stats import linregress

#this might also have to be changed if on windows, it just adds the project root to the system path but uses ubuntu path format
import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
#end here

from src.program1 import program1
from src.program2 import program2
from src.program3 import program3
from src.program4 import program4   
from src.program5A import program5A
from src.program5B import program5B

def generate_random_input(n, max_width, max_height):
    W = random.randint(max_width // 2, max_width)
    heights = [random.randint(1, max_height) for _ in range(n)]
    widths = [random.randint(1, W) for _ in range(n)]
    return W, heights, widths

def run_experiment(program, n, max_width, max_height, num_runs=25):
    print(f"\nRunning experiment with n={n}")
    times = []
    all_results = []
    for run in range(num_runs):
        print(f"  Run {run + 1}/{num_runs}", end='\r')
        W, heights, widths = generate_random_input(n, max_width, max_height)
        start_time = time.time()
        result = program(n, W, heights, widths)
        end_time = time.time()
        run_time = end_time - start_time
        times.append(run_time)
        all_results.append((run + 1, n, W, result, run_time))
    print()  # New line after progress
    return times, all_results

def plot_running_times(program, program_name, input_sizes):
    print(f"\n{'='*50}")
    print(f"Starting experiments for {program_name}")
    print(f"{'='*50}")
    
    all_times = []
    all_sizes = []
    all_results = []
    
    if program_name != 'Program3':
        for n in input_sizes:
            times, results = run_experiment(program, n, 1000, 1000)
            avg_time = sum(times) / len(times)
            print(f"Average time for n={n}: {avg_time:.6f} seconds")
            all_times.extend(times)
            all_sizes.extend([n] * len(times))
            all_results.extend(results)
    else:
        for n in input_sizes:
            adjusted_n = n//500
            print(f"Note: Using adjusted n={adjusted_n} for Program3")
            times, results = run_experiment(program, adjusted_n, 1000, 1000)
            avg_time = sum(times) / len(times)
            print(f"Average time for n={n} (adjusted={adjusted_n}): {avg_time:.6f} seconds")
            all_times.extend(times)
            all_sizes.extend([n] * len(times))
            all_results.extend(results)

    print(f"\nGenerating plot for {program_name}...")
    
    plt.figure(figsize=(12, 8))
    plt.scatter(all_sizes, all_times, alpha=0.5, label='Individual runs')
    
    # Add trend line
    z = np.polyfit(all_sizes, all_times, 2)
    p = np.poly1d(z)
    x_trend = np.linspace(min(all_sizes), max(all_sizes), 100)
    y_trend = p(x_trend)
    plt.plot(x_trend, y_trend, 'r-', label='Trend line')
    
    plt.title(f'Running Times of {program_name} (25 runs per input size)')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Running Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'experiments/{program_name.lower()}_plot.png')
    plt.close()
    
    return all_results

def write_results_to_file(results, program_name):
    with open(f'experiments/{program_name.lower()}_results.txt', 'w') as f:
        for n_group in np.unique([r[1] for r in results]):
            n_results = [r for r in results if r[1] == n_group]
            f.write(f"Results for n = {n_group}:\n")
            headers = ["Run", "n", "W", "Result", "Time (s)"]
            table = tabulate(n_results, headers=headers, floatfmt=".6f")
            f.write(table + "\n\n")
            f.write("-" * 80 + "\n\n")

def main():
    input_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    
    print("\nStarting experimental runs...")
    print(f"Input sizes: {input_sizes}")
    print(f"Number of runs per input size: 25")
    
    # Plot1 and results for Program1
    results1 = plot_running_times(program1, 'Program1', input_sizes)
    write_results_to_file(results1, 'Program1')
    
    # Plot2 and results for Program2
    results2 = plot_running_times(program2, 'Program2', input_sizes)
    write_results_to_file(results2, 'Program2')

    # Plot3 and results for Program3
    results3 = plot_running_times(program3, 'Program3', input_sizes)
    write_results_to_file(results3, 'Program3')

    # Plot4 and results for Program4
    results4 = plot_running_times(program4, 'Program4', input_sizes)
    write_results_to_file(results4, 'Program4')

    # Plot5A and results for Program5A
    results5A = plot_running_times(program5A, 'Program5A', input_sizes)
    write_results_to_file(results5A, 'Program5A')

    # Plot5B and results for Program5B
    results5B = plot_running_times(program5B, 'Program5B', input_sizes)
    write_results_to_file(results5B, 'Program5B')

if __name__ == '__main__':
    main()
