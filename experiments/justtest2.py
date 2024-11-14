import random
import time
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
import os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.program4 import program4
from src.program5A import program5A
from src.program5B import program5B
from src.program3 import program3  # Import Program 3
from src.program1 import program1  # Import Program 1

W = 10  # Keep W constant

def remove_outliers(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

# Configure different sizes for each program
program_configs = {
    'Program 4': {
        'func': program4,
        'sizes': list(range(100, 501, 20)),  # Smaller range for O(n²W)
        'runs': 1  # Fewer runs since it's more complex
    },
    'Program 5A': {
        'func': program5A,
        'sizes': list(range(500, 2501, 100)),  # Larger range for O(n²)
        'runs': 1
    },
    'Program 5B': {
        'func': program5B,
        'sizes': list(range(500, 2501, 100)),  # Same as 5A
        'runs': 1
    },
    'Program 3': {
        'func': program3,
        'sizes': list(range(5, 25, 2)),  # Adjust size range as needed
        'runs': 1
    }
}

# Create a new function to plot running times for all programs
def plot_running_times():
    plt.figure(figsize=(12, 8))
    
    for prog_name, config in program_configs.items():
        all_points_x = []
        all_points_y = []
        average_times = []
        
        for size in tqdm(config['sizes'], desc=f"Testing {prog_name}"):
            size_times = []
            for _ in range(config['runs']):
                heights = [random.randint(1, 100) for _ in range(size)]
                widths = [random.randint(1, W) for _ in range(size)]
                
                start_time = time.time()
                config['func'](size, W, heights, widths)
                end_time = time.time()
                execution_time = end_time - start_time
                
                size_times.append(execution_time)
            
            cleaned_times = remove_outliers(size_times)
            all_points_x.extend([size] * len(cleaned_times))
            all_points_y.extend(cleaned_times)
            average_times.append(np.mean(cleaned_times))
        
        # Plot individual run times as transparent blue dots
        plt.scatter(all_points_x, all_points_y, color='blue', alpha=0.3, label=f'{prog_name} Runs')  # Individual runs
        plt.plot(config['sizes'], average_times, label=prog_name)  # Plot average times
        # Add trendline
        z = np.polyfit(config['sizes'], average_times, 1)  # Linear trendline
        p = np.poly1d(z)
        plt.plot(config['sizes'], p(config['sizes']), linestyle='--', color='red', alpha=0.5)  # Trendline

    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Performance Comparison of All Programs')
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend()
    plt.tight_layout()
    plt.savefig('performance_comparison_all_programs.png', dpi=300)  # Save overlay plot
    plt.close()

# Overlay Plots 5 and 6
def overlay_programs_5A_5B():
    plt.figure(figsize=(12, 8))
    
    for prog_name in ['Program 5A', 'Program 5B']:
        config = program_configs[prog_name]
        average_times = []
        
        for size in tqdm(config['sizes'], desc=f"Testing {prog_name}"):
            size_times = []
            for _ in range(config['runs']):
                heights = [random.randint(1, 100) for _ in range(size)]
                widths = [random.randint(1, W) for _ in range(size)]
                
                start_time = time.time()
                config['func'](size, W, heights, widths)
                end_time = time.time()
                execution_time = end_time - start_time
                
                size_times.append(execution_time)
            
            cleaned_times = remove_outliers(size_times)
            average_times.append(np.mean(cleaned_times))
        
        # Plot individual run times as transparent blue dots
        plt.scatter(config['sizes'], average_times, color='blue', alpha=0.3, label=f'{prog_name} Runs')  # Individual runs
        plt.plot(config['sizes'], average_times, label=prog_name)  # Plot average times
        # Add trendline
        z = np.polyfit(config['sizes'], average_times, 1)  # Linear trendline
        p = np.poly1d(z)
        plt.plot(config['sizes'], p(config['sizes']), linestyle='--', color='red', alpha=0.5)  # Trendline

    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Performance Comparison of Programs 5A and 5B')
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend()
    plt.tight_layout()
    plt.savefig('performance_comparison_programs_5A_5B.png', dpi=300)  # Save overlay plot
    plt.close()

def plot_quality_comparison():
    plt.figure(figsize=(12, 8))
    
    # We'll use Program 5A for optimal solution
    sizes = list(range(10, 1001, 10))
    quality_ratios = []
    
    for size in tqdm(sizes, desc="Testing quality comparison"):
        size_ratios = []
        for _ in range(5):  # Run multiple times for each size
            # Generate random test data
            heights = [random.randint(1, 100) for _ in range(size)]
            widths = [random.randint(1, W) for _ in range(size)]
            
            # Get greedy solution (Program 1)
            _, h_greedy, _ = program1(size, W, heights, widths)
            
            # Get optimal solution (Program 5A)
            # Assuming program5A returns (height, other_values...)
            h_optimal, *_ = program5A(size, W, heights, widths)
            
            # Calculate quality ratio (hg - ho)/ho
            quality_ratio = (h_greedy - h_optimal) / h_optimal
            size_ratios.append(quality_ratio)
        
        # Average the ratios for this size
        quality_ratios.append(np.mean(size_ratios))
    
    # Plot the quality comparison
    plt.plot(sizes, quality_ratios, 'b-', label='Quality Ratio')
    plt.scatter(sizes, quality_ratios, color='blue', alpha=0.5)
    
    # Add trendline
    z = np.polyfit(sizes, quality_ratios, 1)
    p = np.poly1d(z)
    plt.plot(sizes, p(sizes), 'r--', alpha=0.5, label='Trend')
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Quality Ratio (hg - ho)/ho')
    plt.title('Quality Comparison: Greedy vs Optimal Solution')
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend()
    plt.tight_layout()
    plt.savefig('quality_comparison.png', dpi=300)
    plt.close()

# Call the function to plot running times
# plot_running_times()  # This will save individual plots for each program

# # Call the function to overlay Programs 5A and 5B
# overlay_programs_5A_5B()  # This will save 'performance_comparison_programs_5A_5B.png'

# Call the function to overlay all programs
# overlay_all_programs()  # This will save 'performance_comparison_all_programs.png'

# Call the function to plot quality comparison
plot_quality_comparison()