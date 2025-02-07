import random
import time

# Helper function to extract the median from a small sublist
def extract_sublist_median(sublist):
    """Sorts a small segment and retrieves its median value."""
    sublist.sort()
    return sublist[len(sublist) // 2]

# Deterministic Selection Algorithm 
def median_of_medians(data_list, index):
    """Determines the k-th smallest element using a refined deterministic approach."""

    # Base case: If the list is small, sort and return the desired element
    if len(data_list) <= 5:
        data_list.sort()
        return data_list[index]

    # Step 1: Break list into groups and gather medians
    medians_collected = []
    i = 0
    while i < len(data_list):
        subgroup = data_list[i: i + 5]
        medians_collected.append(extract_sublist_median(subgroup))
        i += 5

    # Step 2: Identify the median of the collected medians
    pivot = median_of_medians(medians_collected, len(medians_collected) // 2)

    # Step 3: Partition elements based on the pivot
    smaller_segment = [val for val in data_list if val < pivot]
    larger_segment = [val for val in data_list if val > pivot]
    pivot_repeats = len(data_list) - len(smaller_segment) - len(larger_segment)

    # Step 4: Recursively determine k-th smallest element
    if index < len(smaller_segment):
        return median_of_medians(smaller_segment, index)
    elif index < len(smaller_segment) + pivot_repeats:
        return pivot
    else:
        return median_of_medians(larger_segment, index - len(smaller_segment) - pivot_repeats)

# Randomized Selection Algorithm
def quickselect(data_list, index):
    """Determines the k-th smallest element using a randomized pivot-based method."""
    if len(data_list) == 1:
        return data_list[0]

    pivot = random.choice(data_list)

    # Partition data relative to pivot
    left_part = [item for item in data_list if item < pivot]
    right_part = [item for item in data_list if item > pivot]
    pivot_occurrences = data_list.count(pivot)

    if index < len(left_part):
        return quickselect(left_part, index)
    elif index < len(left_part) + pivot_occurrences:
        return pivot
    else:
        return quickselect(right_part, index - len(left_part) - pivot_occurrences)

# Functions for dataset generation
def generate_random_sequence(size):
    """Creates a randomly shuffled list of numbers."""
    return [random.randint(1, 100000) for _ in range(size)]

def generate_sequential_data(size):
    """Produces an ascending sequence of numbers."""
    return list(range(size))

def generate_descending_data(size):
    """Produces a descending sequence of numbers."""
    return list(range(size, 0, -1))

# Performance Analysis Function
def analyze_algorithm_efficiency():
    """Compares execution time of both selection algorithms on various datasets."""
    sample_sizes = [100, 500, 1000, 5000, 10000]
    dataset_variants = [
        ("Random", generate_random_sequence),
        ("Sorted", generate_sequential_data),
        ("Reverse sorted", generate_descending_data)
    ]

    # Print table headers
    print(f"\n{'Dataset Type':<15}{'Size':<12}{'Median of Medians (s)':<30}{'QuickSelect (s)':<30}")
    print("=" * 90)

    for dataset_name, dataset_generator in dataset_variants:
        for size in sample_sizes:
            dataset = dataset_generator(size)
            middle_index = size // 2  # Find the median position

            # Measure time for Median of Medians
            start_time = time.time()
            median_of_medians(dataset, middle_index)
            mom_duration = time.time() - start_time

            # Measure time for QuickSelect
            start_time = time.time()
            quickselect(dataset, middle_index)
            qs_duration = time.time() - start_time

            print(f"{dataset_name:<15}{size:<12}{mom_duration:<30.6f}{qs_duration:<30.6f}")

analyze_algorithm_efficiency()
