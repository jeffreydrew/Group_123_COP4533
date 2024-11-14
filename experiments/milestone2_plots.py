import random
import time
from tqdm import tqdm

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
    times = []
    all_results = []
    
    pbar = tqdm(total=num_runs, desc=f"n={n}", unit='runs')
    
    for run in range(num_runs):
        W, heights, widths = generate_random_input(n, max_width, max_height)
        start_time = time.time()
        result = program(n, W, heights, widths)
        run_time = time.time() - start_time
        
        times.append(run_time)
        all_results.append((run + 1, n, W, result, run_time))
        
        avg_time = sum(times) / len(times)
        pbar.set_postfix({'avg_time': f'{avg_time:.4f}s'})
        pbar.update(1)
    
    pbar.close()
    return times, all_results

def plot_running_times(program, program_name, input_sizes):
    print(f"\n{'='*50}")
    print(f"Starting experiments for {program_name}")
    print(f"{'='*50}")
    
    all_times = []
    all_sizes = []
    all_results = []
    
    batch_pbar = tqdm(input_sizes, desc=f"{program_name} batches", unit='batch')
    
    if program_name == 'Program3':
        for n in batch_pbar:
            adjusted_n = n//500
            batch_pbar.set_description(f"{program_name} batches (adjusted n={adjusted_n})")
            times, results = run_experiment(program, adjusted_n, 1000, 1000)
            avg_time = sum(times) / len(times)
            batch_pbar.set_postfix({'avg_time': f'{avg_time:.4f}s'})
            all_times.extend(times)
            all_sizes.extend([n] * len(times))
            all_results.extend(results)
    elif program_name == 'Program4':
        for n in batch_pbar:
            adjusted_n = n//20
            batch_pbar.set_description(f"{program_name} batches (adjusted n={adjusted_n})")
            times, results = run_experiment(program, adjusted_n, 1000, 1000)
            avg_time = sum(times) / len(times)
            batch_pbar.set_postfix({'avg_time': f'{avg_time:.4f}s'})
            all_times.extend(times)
            all_sizes.extend([n] * len(times))
            all_results.extend(results)
    else:
        for n in batch_pbar:
            
            times, results = run_experiment(program, n, 1000, 1000)
            avg_time = sum(times) / len(times)
            batch_pbar.set_postfix({'avg_time': f'{avg_time:.4f}s'})
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
    
    # Add theoretical O(n^2) curve for comparison
    c = np.mean(np.array(all_times) / (np.array(all_sizes)**2))  # scaling factor
    theoretical = c * x_trend**2
    plt.plot(x_trend, theoretical, 'g--', label='O(n²) theoretical')
    
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
    # Define start, end, and number of points
    start_size = 1000
    end_size = 10000
    num_points = 10  # This will give us 100 different input sizes
    
    # Generate more granular input sizes
    input_sizes = np.linspace(start_size, end_size, num_points, dtype=int)
    
    print("\nStarting experimental runs...")
    print(f"Testing input sizes from {start_size} to {end_size}")
    print(f"Number of points: {num_points}")
    print(f"Number of runs per input size: 25")
    
    # # Plot1 and results for Program1
    # results1 = plot_running_times(program1, 'Program1', input_sizes)
    # write_results_to_file(results1, 'Program1')
    
    # # Plot2 and results for Program2
    # results2 = plot_running_times(program2, 'Program2', input_sizes)
    # write_results_to_file(results2, 'Program2')

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
