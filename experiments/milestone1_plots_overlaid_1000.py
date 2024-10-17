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

def run_experiment(program, n, max_width, max_height):
    W, heights, widths = generate_random_input(n, max_width, max_height)
    start_time = time.time()
    result = program(n, W, heights, widths)
    end_time = time.time()
    run_time = end_time - start_time
    return run_time, result, W

def plot_running_times(program1, program2, num_runs=1000):
    sizes1, times1, results1 = [], [], []
    sizes2, times2, results2 = [], [], []
    
    for _ in range(num_runs):
        n = random.randint(1, 10000)
        
        time1, result1, W1 = run_experiment(program1, n, 1000, 1000)
        sizes1.append(n)
        times1.append(time1)
        results1.append((n, W1, result1, time1))
        
        time2, result2, W2 = run_experiment(program2, n, 1000, 1000)
        sizes2.append(n)
        times2.append(time2)
        results2.append((n, W2, result2, time2))
    
    # Remove top 10 outliers for each program
    def remove_outliers(sizes, times, results):
        sorted_indices = sorted(range(len(times)), key=lambda k: times[k], reverse=True)
        outlier_indices = sorted_indices[:10]
        
        sizes = [s for i, s in enumerate(sizes) if i not in outlier_indices]
        times = [t for i, t in enumerate(times) if i not in outlier_indices]
        results = [r for i, r in enumerate(results) if i not in outlier_indices]
        
        return sizes, times, results
    
    sizes1, times1, results1 = remove_outliers(sizes1, times1, results1)
    sizes2, times2, results2 = remove_outliers(sizes2, times2, results2)
    
    plt.figure(figsize=(12, 8))
    plt.scatter(sizes1, times1, alpha=0.5, color='blue', label='Program 1')
    plt.scatter(sizes2, times2, alpha=0.5, color='orange', label='Program 2')
    
    # Add trend lines
    for sizes, times, color, label in [(sizes1, times1, 'blue', 'Trend (Program 1)'),
                                       (sizes2, times2, 'orange', 'Trend (Program 2)')]:
        z = np.polyfit(sizes, times, 2)
        p = np.poly1d(z)
        x_trend = np.linspace(min(sizes), max(sizes), 100)
        y_trend = p(x_trend)
        plt.plot(x_trend, y_trend, color=color, linestyle='--', label=label)
    
    plt.title(f'Running Times Comparison (1000 runs each, top 10 outliers removed)')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Running Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('experiments/program_comparison_plot.png')
    plt.close()
    
    return results1, results2

def write_results_to_file(results, program_name):
    with open(f'experiments/{program_name.lower()}_results.txt', 'w') as f:
        headers = ["n", "W", "Result", "Time (s)"]
        table = tabulate(results, headers=headers, floatfmt=".6f")
        f.write(table)

def main():
    results1, results2 = plot_running_times(program1, program2)
    
    write_results_to_file(results1, 'Program1')
    write_results_to_file(results2, 'Program2')

if __name__ == '__main__':
    main()
