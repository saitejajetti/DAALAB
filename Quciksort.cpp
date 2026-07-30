#include <iostream>
#include <chrono>   // for execution time
using namespace std;
using namespace std::chrono;

// Partition Function
int partition(int arr[], int low, int high) {
    int pivot = arr[high];   // Last element as pivot
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;

            // Swap arr[i] and arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    // Place pivot in correct position
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return i + 1;
}

// Quick Sort Function
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pivotIndex = partition(arr, low, high);

        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);
    }
}

int main() {
    int n;

    cout << "Enter number of elements: ";
    cin >> n;

    int arr[n];

    cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Start measuring execution time
    auto start = high_resolution_clock::now();

    // Quick Sort
    quickSort(arr, 0, n - 1);

    // Stop measuring execution time
    auto stop = high_resolution_clock::now();

    // Print sorted array
    cout << "Sorted Array (Quick Sort): ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    // Calculate execution time
    auto duration = duration_cast<nanoseconds>(stop - start);

    cout << "\nExecution Time: " << duration.count() << " ns\n";

    // Complexity Analysis
    cout << "\n--- Complexity Analysis ---\n";
    cout << "Best Case Time Complexity: O(n log n)\n";
    cout << "Average Case Time Complexity: O(n log n)\n";
    cout << "Worst Case Time Complexity: O(n^2)\n";
    cout << "Space Complexity: O(log n)\n";

    return 0;
}