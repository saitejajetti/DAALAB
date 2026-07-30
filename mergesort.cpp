#include <iostream>
#include <chrono>   // for execution time
using namespace std;
using namespace std::chrono;

// Merge function
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int L[n1], R[n2];

    // Copy data into temporary arrays
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];

    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;

    // Merge the temporary arrays
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy remaining elements of L[]
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy remaining elements of R[]
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// Merge Sort function
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
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

    // Merge Sort
    mergeSort(arr, 0, n - 1);

    // Stop measuring execution time
    auto stop = high_resolution_clock::now();

    // Print sorted array
    cout << "Sorted Array (Merge Sort): ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    // Calculate execution time
    auto duration = duration_cast<nanoseconds>(stop - start);

    cout << "\nExecution Time: " << duration.count() << " ns\n";

    // Complexity Notes
    cout << "\n--- Complexity Analysis ---\n";
    cout << "Best Case Time Complexity: O(n log n)\n";
    cout << "Average Case Time Complexity: O(n log n)\n";
    cout << "Worst Case Time Complexity: O(n log n)\n";
    cout << "Space Complexity: O(n)\n";

    return 0;
}