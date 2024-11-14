import random
import time
from tqdm import tqdm
import seaborn

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from scipy.stats import linregress

import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.program1 import program1
from src.program2 import program2
from src.program3 import program3
from src.program4 import program4   
from src.program5A import program5A
from src.program5B import program5B

def generate_test_case(n: int, W: int = 1000):
    """Generate random test cases within the given constraints"""
    heights = [random.randint(1, 1000) for _ in range(n)]
    widths = [random.randint(1, min(W//2, 1000)) for _ in range(n)]
    return W, heights, widths

def measure_execution_time(func, n, W, heights, widths, num_runs=3):
    """Measure execution time of a given function with multiple runs"""
    times = []
    height = None
    for _ in range(num_runs):
        start_time = time.time()
        result = func(n, W, heights, widths)
        end_time = time.time()
        times.append(end_time - start_time)
        height = result[1]
    return min(times), height  # Return best time and height

def run_experiments():
    # Define more granular input sizes for different programs
    sizes_3 = list(range(2, 26))  # Program 3: 2-25 (every number)
    sizes_4 = list(range(10, 501, 20))  # Program 4: 10-500 (step of 20)
    
    # More granular steps for larger numbers
    sizes_5_small = list(range(10, 1000, 50))  # 10-1000 with step 50
    sizes_5_medium = list(range(1000, 3000, 100))  # 1000-3000 with step 100
    sizes_5_large = list(range(3000, 5001, 250))  # 3000-5000 with step 250
    sizes_5 = sizes_5_small + sizes_5_medium + sizes_5_large

    # Initialize results dictionaries
    results = {
        'program3': {'sizes': sizes_3, 'times': [], 'heights': []},
        'program4': {'sizes': sizes_4, 'times': [], 'heights': []},
        'program5A': {'sizes': sizes_5, 'times': [], 'heights': []},
        'program5B': {'sizes': sizes_5, 'times': [], 'heights': []},
        'program1': {'sizes': sizes_5, 'times': [], 'heights': []}
    }

    # Run experiments for each program
    for program_name, data in results.items():
        print(f"\nRunning experiments for {program_name}...")
        for n in tqdm(data['sizes']):
            W, heights, widths = generate_test_case(n)
            
            try:
                if program_name == 'program3':
                    time_taken, height = measure_execution_time(program3, n, W, heights, widths)
                elif program_name == 'program4':
                    time_taken, height = measure_execution_time(program4, n, W, heights, widths)
                elif program_name == 'program5A':
                    time_taken, height = measure_execution_time(program5A, n, W, heights, widths)
                elif program_name == 'program5B':
                    time_taken, height = measure_execution_time(program5B, n, W, heights, widths)
                elif program_name == 'program1':
                    time_taken, height = measure_execution_time(program1, n, W, heights, widths)
                
                data['times'].append(time_taken)
                data['heights'].append(height)
            except Exception as e:
                print(f"\nError in {program_name} with n={n}: {str(e)}")
                data['times'].append(None)
                data['heights'].append(None)

    return results

def create_plots(results):
    # Common plotting settings
    plt.style.use('default')
    markers = {'program1': 'o', 'program3': 's', 'program4': '^', 
               'program5A': 'D', 'program5B': 'v'}
    colors = {'program1': '#1f77b4', 'program3': '#2ca02c', 'program4': '#ff7f0e', 
              'program5A': '#d62728', 'program5B': '#9467bd'}

    def setup_plot(title, xlabel='Input Size (n)', ylabel='Time (seconds)'):
        plt.figure(figsize=(12, 8))
        plt.title(title, pad=20)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True, linestyle='--', alpha=0.7)

    # Individual plots (3-6)
    for prog in ['program3', 'program4', 'program5A', 'program5B']:
        setup_plot(f'Running Time of {prog}')
        plt.plot(results[prog]['sizes'], results[prog]['times'], 
                marker=markers[prog], color=colors[prog], 
                linewidth=2, markersize=6, alpha=0.7)
        plt.savefig(f'plot{prog[-1]}.png', dpi=300, bbox_inches='tight')
        plt.close()

    # Plot 7: Overlay of all programs
    setup_plot('Performance Comparison of All Programs')
    for prog, data in results.items():
        plt.plot(data['sizes'], data['times'], 
                marker=markers[prog], label=prog, color=colors[prog],
                linewidth=2, markersize=6, alpha=0.7)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('plot7.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Plot 8: Comparison of 5A and 5B
    setup_plot('Performance Comparison of Programs 5A and 5B')
    plt.plot(results['program5A']['sizes'], results['program5A']['times'], 
            marker=markers['program5A'], label='Program 5A', color=colors['program5A'],
            linewidth=2, markersize=6, alpha=0.7)
    plt.plot(results['program5B']['sizes'], results['program5B']['times'], 
            marker=markers['program5B'], label='Program 5B', color=colors['program5B'],
            linewidth=2, markersize=6, alpha=0.7)
    plt.legend()
    plt.savefig('plot8.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Plot 9: Quality comparison
    setup_plot('Output Quality Comparison (Program 1 vs Optimal)', 
              ylabel='(hg - ho)/ho')
    optimal_heights = results['program5B']['heights']
    greedy_heights = results['program1']['heights']
    quality_diff = [(hg - ho)/ho for hg, ho in zip(greedy_heights, optimal_heights)]
    plt.plot(results['program5B']['sizes'], quality_diff, 
            marker='o', color='#e377c2', linewidth=2, markersize=6, alpha=0.7)
    plt.savefig('plot9.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    results = run_experiments()
    create_plots(results)