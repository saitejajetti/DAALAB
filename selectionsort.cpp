#include <iostream>
#include <chrono>   // for execution time
using namespace std;
using namespace std::chrono;

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

    // Selection Sort logic directly in main
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        int temp = arr[minIndex];
        arr[minIndex] = arr[i];
        arr[i] = temp;
    }

    // Stop measuring execution time
    auto stop = high_resolution_clock::now();

    // Print sorted array
    cout << "Sorted Array (Selection Sort): ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    // Calculate execution time
    auto duration = duration_cast<nanoseconds>(stop - start);
    cout << "\nExecution Time: " << duration.count() << " ns\n";

    // Complexity notes (for examiner)
    cout << "\n--- Complexity Analysis ---\n";
    cout << "Best Case Time Complexity: O(n^2)\n";
    cout << "Average Case Time Complexity: O(n^2)\n";
    cout << "Worst Case Time Complexity: O(n^2)\n";
    cout << "Space Complexity: O(1) (in-place sorting)\n";

    return 0;
}
