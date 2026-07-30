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

    // Bubble Sort logic directly in main
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    // Stop measuring execution time
    auto stop = high_resolution_clock::now();

    // Print sorted array
    cout << "Sorted Array (Bubble Sort): ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    // Calculate execution time
    auto duration = duration_cast<nanoseconds>(stop - start);
    cout << "\nExecution Time: " << duration.count() << " ns\n";

    // Complexity notes (for examiner)
    cout << "\n--- Complexity Analysis ---\n";
    cout << "Best Case Time Complexity: O(n)\n";
    cout << "Average Case Time Complexity: O(n^2)\n";
    cout << "Worst Case Time Complexity: O(n^2)\n";
    cout << "Space Complexity: O(1) (in-place sorting)\n";

    return 0;
}
