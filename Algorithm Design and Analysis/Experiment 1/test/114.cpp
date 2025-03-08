#include <bits/stdc++.h>
using namespace std;

void merge(vector<int> &a, vector<int> &temp, int left, int mid, int right) {
    int i = left;  
    int j = mid + 1; 
    int k = left;

    while (i <= mid && j <= right) {
        if (a[i] <= a[j]) {
            temp[k] = a[i];
            i++;
        } else {
            temp[k] = a[j];
            j++;
        }
        k++;
    }

    while (i <= mid) {
        temp[k] = a[i];
        i++;
        k++;
    }

    while (j <= right) {
        temp[k] = a[j];
        j++;
        k++;
    }

    for (int m = left; m <= right; m++) {
        a[m] = temp[m];
    }
}

void merge_sort(vector<int> &a, vector<int> &temp, int left, int right) {
    if (left >= right) {
        return;
    }

    int mid = left + (right - left) / 2;

    merge_sort(a, temp, left, mid);
    merge_sort(a, temp, mid + 1, right);
    merge(a, temp, left, mid, right);
}

void merge_sort(vector<int> &a, int n) {
    vector<int> temp(n + 1);
    merge_sort(a, temp, 1, n);
}

void quick_sort(vector<int> &a, int left, int right) {
    if (left >= right) {
        return;
    }

    int pivot = a[left]; 
    int i = left;
    int j = right;

    while (i < j) {
        while (i < j && a[j] > pivot) {
            j--;
        }

        while (i < j && a[i] <= pivot) {
            i++;
        }

        if (i < j) {
            swap(a[i], a[j]);
        }
    }

    swap(a[left], a[i]);

    quick_sort(a, left, i - 1);
    quick_sort(a, i + 1, right);
}

void quick_sort(vector<int> &a, int n) 
{
    quick_sort(a, 1, n);
}

signed main()
{
    int n;
    cin >> n;
    vector<int> a(n + 1);
    for(int i = 1;i<=n;i++) cin >> a[i];
    quick_sort(a,n);
    for(int i = 1;i<=n;i++) cout << a[i] << ' ';

    return 0;
}