#include <bits/stdc++.h>

using namespace std;

void addNumber(int num,
               priority_queue <int> &maxHeap,
               priority_queue <int, vector<int>, greater<int> > &minHeap)
{
    if (maxHeap.empty() || num < maxHeap.top())
    {
        maxHeap.push(num);
    }
    else
    {
        minHeap.push(num);
    }
}

void reBalance(priority_queue <int> &maxHeap,
               priority_queue <int, vector<int>, greater<int> > &minHeap)
{
    if (minHeap.size() > maxHeap.size() + 1)
    {
        maxHeap.push(minHeap.top());
        minHeap.pop();
    }

    if (maxHeap.size() > minHeap.size() + 1)
    {
        minHeap.push(maxHeap.top());
        maxHeap.pop();
    }
}

double getMedian(priority_queue <int> &maxHeap,
                 priority_queue <int, vector<int>, greater<int> > &minHeap)
{
    double median;
    if (minHeap.size() == maxHeap.size())
    {
        median = (double) (minHeap.top() + maxHeap.top()) / 2;
    }
    else if (minHeap.size() > maxHeap.size())
    {
        median = (double)minHeap.top();
    }
    else if (minHeap.size() < maxHeap.size())
    {
        median = (double)maxHeap.top();
    }

    return median;
}


vector<double> runningMedian(vector<int> a)
{
    vector<double> medians;

    priority_queue <int> maxHeap;
    priority_queue <int, vector<int>, greater<int> > minHeap;

    for (int i = 0; i < a.size(); i++)
    {
        int num = a[i];

        addNumber(num, maxHeap, minHeap);
        reBalance(maxHeap, minHeap);

        double median = getMedian(maxHeap, minHeap);
        medians.push_back(median);
    }

    return medians;
}

int main()
{
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    vector<double> result = runningMedian(a);
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << endl;
    }

    return 0;
}
