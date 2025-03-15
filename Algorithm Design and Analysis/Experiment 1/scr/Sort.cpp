#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <direct.h>
#include <chrono>
using namespace std;

void insert_sort(vector<int> &a,int n)
{
    for(int i = 2;i<=n;i++)
    {   
        int temp = a[i];
        int j = i - 1;
        while(j > 0 && a[j] > temp) 
        {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = temp;
    }
}

void bubble_sort(vector<int> &a,int n)
{
    for(int i = 1;i<n;i++)
    {   
        int cnt = 0;
        for(int j = 1;j<=n - i;j++)
        {
            if(a[j] > a[j + 1]) swap(a[j],a[j + 1]),cnt++;
        }
        if(cnt == 0) break;
    }
}

void select_sort(vector<int> &a,int n)
{
    for(int i = 1;i<n;i++)
    {
        int minn = a[i];
        int pos = i;
        for(int j = i + 1;j<=n;j++) 
        {
            if(a[j] < minn)
            {
                minn = a[j];
                pos = j;
            }
        }
        swap(a[i],a[pos]);
    }
}

void merge(vector<int> &a, vector<int> &temp, int left, int mid, int right) 
{
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

void merge_sort(vector<int> &a, vector<int> &temp, int left, int right) 
{
    if (left >= right) {
        return;
    }

    int mid = left + (right - left) / 2;

    merge_sort(a, temp, left, mid);
    merge_sort(a, temp, mid + 1, right);
    merge(a, temp, left, mid, right);
}

void merge_sort(vector<int> &a, int n) 
{
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

typedef void (*SortFuntion)(vector<int>&,int);

void data_reader(string path,vector<int> &v)
{
    int n;
    ifstream infile(path,ios::in);
    if(infile.is_open() == 0) 
    {   
        char buff[1004];
        _getcwd(buff,1004);
        cerr << string(buff) << endl;
        cerr << path << endl;
        cerr << "open infile failed" << endl;
        return;
    }

    infile >> n;
    v.resize(n + 1);
    for(int i = 1;i<=n;i++) infile >> v[i];
}

signed main()
{   
    string out_root = ".\\data\\";
    string in_root = ".\\resource\\";

    vector<SortFuntion> fun = {bubble_sort,insert_sort,select_sort,merge_sort,quick_sort};
    vector<string> name = {"bubble_sort","insert_sort","select_sort","merge_sort","quick_sort"};

    for(int idx = 0;idx<1;idx++)
    {
        SortFuntion f = fun[idx];

        for(int i = 0;i<5;i++)
        {
            int scale = (i + 1) * 100;
            string scale_path = to_string(scale) + "k\\";
            _mkdir((out_root + scale_path).c_str());
            string out_path = out_root + scale_path + "data.txt";
            ofstream outfile(out_path,ios::app);
            if(outfile.is_open() == 0)
            {
                cerr << "failed to open outfile" << endl;
                cerr << out_path << endl;
                return 0;
            }
            for(int j = 1;j<=20;j++)
            {
                string file_name = to_string(j) + ".txt";
                string in_path = in_root + scale_path + file_name;
                cerr << in_path << endl;
                vector<int> v;
                data_reader(in_path,v);

                cout << "Now " << name[idx] << " is Running in " << j << " " << scale << "k..." << endl; 
                auto st = chrono::high_resolution_clock::now();
                f(v,scale * 1000);
                auto ed = chrono::high_resolution_clock::now();
                auto duration = chrono::duration_cast<chrono::milliseconds>(ed - st);
                double cost = duration.count();
                outfile << cost << " ";
                outfile.flush();
                cout << cost << "ms\n";
            }
        }
    }


    return 0;
}