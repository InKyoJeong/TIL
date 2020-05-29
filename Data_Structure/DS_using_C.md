# C 자료구조

📌 Content

0. [Intro](#Intro)<br/>
1. [재귀](#재귀)<br/>

---

## Intro

### 순차 탐색(Linear Search) 알고리즘

```c
#include <stdio.h>

int LSearch(int ar[], int len, int target)
{
    int i;
    for(i=0; i<len; i++)
    {
        if(ar[i] == target)
            return i;           //찾은 대상의 인덱스반환
    }
    return -1;                  //찾지 못함
}

int main(void)
{
    int arr[] = {3, 5, 2, 4, 9};
    int idx;

    idx = LSearch(arr, sizeof(arr)/sizeof(int), 4);
    if(idx == -1)
        printf("탐색 실패\n");
    else
        printf("타겟 저장 인덱스: %d \n", idx);

    idx = LSearch(arr, sizeof(arr)/sizeof(int), 7);
    if(idx == -1)
        printf("탐색 실패\n");
    else
        printf("타겟 저장 인덱스: %d \n", idx);

    return 0;
}
```

```
// 실행결과
타겟 저장 인덱스: 3
탐색 실패
```

순차 탐색알고리즘은 맨 앞에서부터 순서대로 탐색한다. 데이터 수가 n개일때 최악의 경우 연산횟수는 n이다. 시간복잡도는 n이다.

<br>

### 이진 탐색(Binary Search) 알고리즘

이진 탐색 알고리즘은 정렬된 데이터에 적용할 수 있다. 탐색의 대상을 반씩 줄이는 알고리즘이다.

```c
#include <stdio.h>

int BSearch(int ar[], int len, int target)
{
    int first = 0;
    int last = len - 1;
    int mid;

    while(first <= last)
    {
        mid = (first+last) / 2;

        if(target == ar[mid])
        {
            return mid;
        }
        else
        {
            if(target < ar[mid])
                last = mid-1;
            else
                first = mid+1;
        }
    }
    return -1;
}

int main(void)
{
    int arr[] = {1,3,5,7,9};
    int idx;

    idx = BSearch(arr, sizof(arr)/sizeof(int), 7);
    if(idx == -1)
        printf("탐색 실패 \n");
    else
        printf("타겟 저장 인덱스: %d \n", idx);

    idx = BSearch(arr, sizof(arr)/sizeof(int), 4);
    if(idx == -1)
        printf("탐색 실패 \n");
    else
        printf("타겟 저장 인덱스: %d \n", idx);

    return 0;
}
```

- last와 first에 값을 1씩 빼서 저장한 이유는 mid에 저장된 인덱스 값의 배열요소를 새로운 탐색 범위에 포함할 필요가 없기때문이다.

- 시간복잡도는 log₂n 이다.

<br>

## 재귀

### 재귀함수 이해

> 함수 내에서 자신을 다시 호출하는 함수

```c
void Recur(void)
{
    printf("Recursive call\n");
    Recur();
}
```

### 탈출 조건을 추가한 재귀함수

```c
#include <stdio.h>

void Recur(int num)
{
    if(num < 0)
        return;
    printf("Recursive call %d \n", num);
    Recur(num-1);
}

int main(void)
{
    Recur(3);
    return 0;
}
```

```
// 실행결과
Recursive call 3
Recursive call 2
Recursive call 1
```

<br>

### 팩토리얼 값을 반환하는 재귀함수

정수 팩토리얼은

```
n! = n * (n-1) * (n-2) * (n-3) * ... * 2 * 1
```

이고 `(n-1) * (n-2) * (n-3) * ... * 2 * 1` 은 `(n-1)!`과 같으므로 재귀적 특성을 보인다.

따라서 **n>=1**일 경우에는 `f(n) = n * f(n-1)` 이고 0!은 값이 1이므로 **n=0**일 경우는 f(0) = 1이다.

```c
if (n == 0)
    return 1;
else
    return n * Factorial(n-1);
```

#### 예시

```c
#include <stdio.h>

int Factorial(int n)
{
    if(n == 0)
        return 1;
    else
        return n * Factorial(n-1);
}

int main(void)
{
    printf("1! = %d\n", Factorial(1));
    printf("2! = %d\n", Factorial(2));
    printf("3! = %d\n", Factorial(3));
    printf("4! = %d\n", Factorial(4));
    printf("10! =%d\n", Factorial(10));
}
```

```
// 실행결과
1! = 1
2! = 2
3! = 6
4! = 24
10! =3628800
```

<br>

### 피보나치수열

피보나치 수열도 재귀적인 형태를 띤다. 피보나치 수열은 `0, 1, 1, 2, 3, 5, 8, 13, 21 ...`와 같이 처음 두 수를 더해서 현재 수를 만들어가는 수열이다.

`수열의 n번째 값 = 수열의 n-1번째 값 + 수열의 n-2번째 값`

```c
#include <stdio.h>

int Fibo(int n)
{
    if(n == 1)
        return 0;
    else if(n == 2)
        return 1;
    else
        return Fibo(n-1) + Fibo(n-2);
}

int main(void)
{
    int i;
    for(i=1; i<15; i++)
        printf("%d ", Fibo(i));

    return 0;
}
```

```
// 실행결과
0 1 1 2 3 5 8 13 21 34 55 89 144 233
```

### 하노이 타워

> 하나의 막대에 쌓인 원반을 다른 원반에 그대로 옮기는 방법

막대 A에 꽂힌 원반 n개를 막대 C로 옮기는 흐름

1. 작은 원반 n-1개를 A에서 B로이동
2. 큰 원반 1개를 A에서 C로 이동
3. 작은 원반 n-1개를 B에서 C로 이동

```c
//from에 꽂힌 num개 원반을 by를 거쳐 to로 이동
void Hanoi(int num, char from, char by, char to)
{
    ...
}
```

재귀 탈출 조건은 **이동할 원반 수가 1개**인 경우이다.

```c
#include <stdio.h>

void Hanoi(int num, char from, char by, char to)
{
    if(num == 1)        //이동할 원반 수가 1개일 경우
    {
        printf("원반 1을 %c에서 %c로 이동 \n", from, to);
    }
    else
    {
        Hanoi(num-1, from, to, by);
        printf("원반 %d를 %c에서 %c로 이동 \n", num, from, to);
        Hanoi(num-1, by, from, to);
    }
}

int main(void)
{
    Hanoi(3, 'A', 'B', 'C');
    return 0;
}
```

```
//실행결과
원반 1을 A에서 C로 이동
원반 2를 A에서 B로 이동
원반 1을 C에서 B로 이동
원반 3를 A에서 C로 이동
원반 1을 B에서 A로 이동
원반 2를 B에서 C로 이동
원반 1을 A에서 C로 이동
```

<br>

<!-- ## 연결리스트

### 추상자료형 (Abstract Data Type) -->
