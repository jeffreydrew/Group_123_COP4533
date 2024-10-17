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

def generate_random_input(n, max_width, max_height):
    W = random.randint(max_width // 2, max_width)
    heights = [random.randint(1, max_height) for _ in range(n)]
    widths = [random.randint(1, W) for _ in range(n)]
    return W, heights, widths

def run_experiment(program, n, max_width, max_height, num_runs=25):
    times = []
    all_results = []
    for run in range(num_runs):
        W, heights, widths = generate_random_input(n, max_width, max_height)
        start_time = time.time()
        result = program(n, W, heights, widths)
        end_time = time.time()
        run_time = end_time - start_time
        times.append(run_time)
        all_results.append((run + 1, n, W, result, run_time))
    return times, all_results

def plot_running_times(program, program_name, input_sizes):
    all_times = []
    all_sizes = []
    all_results = []
    for n in input_sizes:
        times, results = run_experiment(program, n, 1000, 1000)
        all_times.extend(times)
        all_sizes.extend([n] * len(times))
        all_results.extend(results)
    
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
    
    # Plot1 and results for Program1
    results1 = plot_running_times(program1, 'Program1', input_sizes)
    write_results_to_file(results1, 'Program1')
    
    # Plot2 and results for Program2
    results2 = plot_running_times(program2, 'Program2', input_sizes)
    write_results_to_file(results2, 'Program2')

if __name__ == '__main__':
    main()
