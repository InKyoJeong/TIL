# 시간복잡도와 점근적 분석

> 권오흠 교수님 - C로배우는 자료구조를 듣고 정리한 글입니다.

## 알고리즘의 분석

- 알고리즘의 자원(resource) 사용량을 분석
- 자원이란 실행시간, 메모리, 저장장치, 통신 등
- 여기서는 실행시간의 분석에 대해 다룸

## 시간복잡도(time complexity)

- 실행시간은 실행환경에 따라 달라짐
  - 하드웨어, 운영체제, 언어, 컴파일러 등
- 실행시간을 측정하는 대신 **연산의 실행 횟수**를 카운트
- 연산의 실행 횟수는 **입력 데이터의 크기에 관한 함수**로 표현
- 데이터의 크기가 같더라도 실제 데이터에 따라서 달라짐
  - 최악의 경우 시간복잡도 (worst-case analysis)
  - 평균 시간복잡도 (average-case analysis)

## 점근적 분석

- 점근적 표기법을 사용
  - 데이터의 개수 n->∞일때 수행시간이 증가하는 growth rate로 시간복잡도를 표현하는 기법(최고차항)
  - Order of, Big-Oh of 등을 사용
- 유일한 분석법도 아니고 가장 좋은 분석법도 아님
  - 다만 상대적으로 가장 간단하고
  - 알고리즘의 실행환경에 비의존적임
  - 그래서 가장 광범위하게 사용됨

### 점근적 분석의 예: 상수 시간복잡도

> 입력으로 n개의 데이터가 저장된 배열 data가 주어지고, 그 중 n/2번째 데이터를 반환한다.

```c
int sample(int data[], int n)
{
    int k = n/2;
    return data[k];
}
```

n에 관계없이 상수시간이 소요된다. 이 경우 알고리즘의 시간복잡도는 O(1)이다.

### 점근적 분석의 예: 선형 시간복잡도

> 입력으로 n개의 데이터가 저장된 배열 data가 주어지고, 그 합을 구하여 반환한다.

```c
int sum(int data[], int n)
{
    int sum = 0;
    for (int i=0; i < n; i++)
        sum = sum + data[i];
    return sum;
}
```

선형 시간복잡도를 가진다고 말하고 O(n)이라고 표기한다.

### 선형 시간복잡도: 순차탐색

> 배열 data에 정수 target이 있는지 검사한다.

```c
int search(int n, int data[], int target)
{
    for(int i=0; i<n; i++){
        if(data[i] == target)
            return i;
    }
    return -1;
}
```

최악의 경우 시간복잡도는 O(n)이다.

### Quadratic (2차)

> 배열 x에 중복된 원소가 있는지 검사한다.

```c
bool is_distinct(int n, int x[])
{
    for(int i=0; i<n-1; i++)
        for(int j=i+1; j<n; j++)
            if(x[i] == x[j])
                return false;
    return true;
}
```

최악의 경우 배열에 저장된 모든 원소 쌍을 비고하므로 비교연산의 횟수는 n(n-1)/2 이다. 최악의 경우 시간복잡도는 O(n²)으로 나타낸다.

## 점근적 표기법

- 알고리즘에 포함된 연산들의 실행 횟수를 표기하는 하나의 기법
- 최고차항의 차수만으로 표시
- 따라서 가장 자주 실행되는 연산 혹은 문장의 실행횟수를 고려하는 것으로 충분

<br>

## 이진검색(Binary Search)

> 배열에 데이터들이 오름차순으로 정렬되어 저장되어있다.

```c
int binarySearch(int n, char *data[], char *target){
    int begin = 0, end = n-1;
    while(begin <= end){
        int middle = (begin + end)/2;
        int result = strcmp(data[middle], target);
        if(result == 0)
            return middle;
        else if (result < 0)
            begin = middle + 1;
        else
            end = middle - 1;
    }
    return -1;
}
```

한번 비교할 때마다 남아있는 데이터가 절반으로 줄어든다. 따라서 시간복잡도는 O(log₂N)이다.

- 데이터가 연결리스트에 오름차순으로 정렬되어 있다면?
  - 연결리스트에서는 가운데 데이터를 O(1)시간에 읽을 수 없음
  - 따라서 이진 검색을 할 수 없다.
- 순차 검색의 시간복잡도는 O(N)이고 이진검색은 O(log₂N)이다. 둘의 차이는 매우크다.

## 버블 정렬(bubble sort)

```c
void bubbleSort(int data[], int n){
    for(int i=n-1; i>0; i--){
        for(int j=0; j<i; j++){
            if(data[j] > data[j+1]){
                int imp = data[j];
                data[j] = data[j+1];
                data[j+1] = tmp;
            }
        }
    }
}
```

시간복잡도는 n(n-1)/2 이므로 O(n²)이다.

## 삽입정렬(Insertion sort)

> data[i]를 data[0]~data[i-1] 중에 제자리를 찾아 삽입하는 일

```c
void insertion_sort(int n, int data[]) {
    for (int i=1; i<n; i++){
        int imp = data[i];
        int j = i-1;
        while (j>=0 && data[j] > tmp){
            data[j+1] = data[j];
            j--;
        }
        data[j+1] = tmp;
    }
}
```

시간복잡도는 최선은 O(n), 최악의경우 O(n²)이다.

## 다른 정렬 알고리즘

- 퀵소트(quicksort) 알고리즘
  - 최악의경우 O(n²), 하지만 평균 시간복잡도는 O(Nlog₂N)
- 최악의 경우 O(Nlog₂N) 시간복잡도를 가지는 정렬 알고리즘
  - 합병정렬(merge sort)
  - 힙 정렬(heap sort) 등
- 데이터가 배열이 아닌 연결리스트에 저장되어 있다면?
  - O(n²)의 시간복잡도를 벗어나기 어렵다.
