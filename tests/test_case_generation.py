import random

def generate_test_file(n, filename):
    # Set the range for painting dimensions and platform width
    min_width, max_width = 1, 100
    min_height, max_height = 1, 200
    platform_width = 1000  # W

    with open(filename, 'w') as f:
        # Write n and W
        f.write(f"{n} {platform_width}\n")
        
        # Generate n paintings
        for _ in range(n):
            width = random.randint(min_width, max_width)
            height = random.randint(min_height, max_height)
            f.write(f"{width} {height}\n")

def main():
    sizes = [1000, 2000, 3000, 4000, 5000]
    
    for size in sizes:
        filename = f"tests/cases/art_exhibition_n{size}.txt"
        generate_test_file(size, filename)
        print(f"Generated test file: {filename}")

if __name__ == "__main__":
    main()