import random
import time
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
import os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.program4 import program4
from src.program5A import program5A
from src.program5B import program5B

W = 1000  # Larger W to force more combinations

def generate_worst_case_input(size):
    # Create inputs that force more combinations to be tested
    heights = [size - i for i in range(size)]  # Decreasing heights
    widths = [W//(size//10)] * size  # Small enough widths to prevent early breaks
    return heights, widths

program_configs = {
    'Program 5A': {
        'func': program5A,
        'sizes': list(range(1000, 10001, 500)),  # 1000 to 10000
        'runs': 3
    },
    'Program 5B': {
        'func': program5B,
        'sizes': list(range(1000, 10001, 500)),  # Same range
        'runs': 3
    }
}

for prog_name, config in program_configs.items():
    all_points_x = []
    all_points_y = []
    average_times = []
    
    for size in tqdm(config['sizes'], desc=f"Testing {prog_name}"):
        size_times = []
        for _ in range(config['runs']):
            heights, widths = generate_worst_case_input(size)
            
            start_time = time.time()
            config['func'](size, W, heights, widths)
            end_time = time.time()
            execution_time = end_time - start_time
            
            size_times.append(execution_time)
        
        average_times.append(np.mean(size_times))
        all_points_x.extend([size] * len(size_times))
        all_points_y.extend(size_times)

    plt.figure(figsize=(12, 8))
    plt.scatter(all_points_x, all_points_y, alpha=0.1, color='blue', label='Individual runs')
    plt.plot(config['sizes'], average_times, 'r-', linewidth=2, label='Average time')
    
    coeffs = np.polyfit(config['sizes'], average_times, 2)
    quad_fit = np.poly1d(coeffs)
    plt.plot(config['sizes'], quad_fit(config['sizes']), 'g--', 
             label=f'Quadratic fit: {coeffs[0]:.2e}x² + {coeffs[1]:.2e}x + {coeffs[2]:.2e}')

    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title(f'{prog_name}: Input Size vs Execution Time (Quadratic Growth)')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(f'{prog_name.lower().replace(" ", "_")}_performance.png', dpi=300)
    plt.close()