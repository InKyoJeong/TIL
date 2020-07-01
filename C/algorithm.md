## 수를 입력받아 오름차순만들기

### 병합정렬

```c
//입력 예
//3 (테스트 케이스 수)
//2
//5
//1

//출력
//1
//2
//5

#include <stdio.h>
#include <stdlib.h>


void MergeTwoArea(int arr[], int left, int mid, int right)
{
    int frontIdx = left;
    int rearIdx = mid+1;
    int i;

    int * sortArr = (int *)malloc(sizeof(int)*(right+1));
    int sortIdx = left;

    while(frontIdx<=mid && rearIdx<=right)
    {
        if(arr[frontIdx] <= arr[rearIdx])
            sortArr[sortIdx] = arr[frontIdx++];
        else
            sortArr[sortIdx] = arr[rearIdx++];

        sortIdx++;
    }

    if(frontIdx > mid)
    {
        for(i=rearIdx; i<=right; i++, sortIdx++)
            sortArr[sortIdx] = arr[i];
    }
    else
    {
        for(i=frontIdx; i<=mid; i++, sortIdx++)
            sortArr[sortIdx] = arr[i];
    }

    for(i=left; i<=right; i++)
        arr[i] = sortArr[i];

    free(sortArr);
}

void MergeSort(int arr[], int left, int right)
{
    int mid;

    if(left < right)
    {
        mid = (left + right) / 2;

        MergeSort(arr, left, mid);
        MergeSort(arr, mid+1, right);

        MergeTwoArea(arr, left, mid, right);
    }
}

int main(void)
{
    int T;
    scanf("%d", &T);
    int *arr = (int *)malloc(sizeof(int) * T);

    for(int i=0; i<T; i++){
        scanf("%d", &arr[i]);
    }

    int i;

    MergeSort(arr, 0, T-1);

    for(i=0; i<T; i++)
        printf("%d\n", arr[i]);
    free(arr);
    return 0;
}
```

### 퀵정렬

```c
//입력 예
//3 (테스트 케이스 수)
//2
//5
//1

//출력
//1
//2
//5

//백준에서 시간초과. 퀵정렬은 사용하지않는게좋다. 병합/힙/기수정렬 사용하기
```

```c
#include <stdio.h>
#include <stdlib.h>

void Swap(int arr[], int idx1, int idx2)
{
int temp = arr[idx1];
arr[idx1] = arr[idx2];
arr[idx2] = temp;
}

int Partition(int arr[], int left, int right)
{
int pivot = arr[left];
int low = left+1;
int high = right;

    while(low <= high)
    {
        while(pivot >= arr[low] && low <= right)
            low++;

        while(pivot <= arr[high] && high >= (left+1))
            high--;

        if(low <= high)
            Swap(arr, low, high);
    }

    Swap(arr, left, high);
    return high;

}

void QuickSort(int arr[], int left, int right)
{
if(left <= right)
{
int pivot = Partition(arr, left, right);
QuickSort(arr, left, pivot-1);
QuickSort(arr, pivot+1, right);
}
}

int main()
{
int T=0;
scanf("%d", &T);
int *arr = (int *)malloc(sizeof(int) * T);

    for(int i=0; i<T; i++){
        scanf("%d", &arr[i]);
    }
    int i;

    QuickSort(arr, 0, T-1);

    for(i=0; i<T; i++)
        printf("%d\n", arr[i]);

    free(arr);
    return 0;

}
```
