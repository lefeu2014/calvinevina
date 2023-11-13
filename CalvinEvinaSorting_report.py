
import random
import time
import cProfile
import matplotlib.pyplot as plt


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]


def profile_sorting_algorithm(size):
    arr = generate_random_array(size)
    cProfile.run("quicksort(arr)")


def main():
    sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    execution_times = []

    for size in sizes:
        start_time = time.time()
        profile_sorting_algorithm(size)
        end_time = time.time()
        execution_times.append(end_time - start_time)

    plt.plot(sizes, execution_times, marker='o')
    plt.xlabel('Array Size')
    plt.ylabel('Time Taken (s)')
    plt.title('Sorting Time vs. Array Size')
    plt.show()


if __name__ == "__main__":
    main()
