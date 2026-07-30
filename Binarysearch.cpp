#include <iostream>
#include <chrono>   // for execution time
using namespace std;
using namespace std::chrono;

int main() {
    int n, key;

    cout << "Enter number of elements: ";
    cin >> n;

    int arr[n];

    cout << "Enter " << n << " sorted elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << "Enter element to search: ";
    cin >> key;

    // Start measuring execution time
    auto start = high_resolution_clock::now();

    int low = 0, high = n - 1;
    int pos = -1;

    while (low <= high) {
        int mid = (low + high) / 2;

        if (arr[mid] == key) {
            pos = mid;
            break;
        }
        else if (arr[mid] < key) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }

    // Stop measuring execution time
    auto stop = high_resolution_clock::now();

    if (pos != -1)
        cout << "Element found at position: " << pos + 1 << endl;
    else
        cout << "Element not found." << endl;

    auto duration = duration_cast<nanoseconds>(stop - start);

    cout << "Execution Time: " << duration.count() << " ns\n";

    cout << "\n--- Complexity Analysis ---\n";
    cout << "Best Case Time Complexity: O(1)\n";
    cout << "Average Case Time Complexity: O(log n)\n";
    cout << "Worst Case Time Complexity: O(log n)\n";
    cout << "Space Complexity: O(1)\n";

    return 0;
}