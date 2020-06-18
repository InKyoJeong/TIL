## Contents

[선택 정렬 알고리즘](#선택-정렬-알고리즘)<br/>
[삽입 정렬 알고리즘](#삽입-정렬-알고리즘)<br/>
[버블 정렬 알고리즘](#버블-정렬-알고리즘)<br/>

<br>

## 선택 정렬 알고리즘

> 데이터의 처음부터 끝까지 훑으면서 가장 작은 값을 찾아 첫번째 데이터와 자리를 바꾸고, 두번째로 작은 값을 찾아 두번째의 데이터와 자리를 바꾸며 구현하는 알고리즘이다.

```c
void MakeRandomNum(void)
{
    int i = 1;
    int Num;
    Buf[0] = 100;

    while(i < MAX){
        Num = rand() % MAX;

        if(!IsNumExit(Num, i)){
            Buf[i] = Num;
            i++;
        }
    }
}
```

최댓값 **100**을 **Buf[0]** 에 저장하고 이미 생성된 값과 중복되지 않게 `IsNumExit()` 함수를 이용한다.
`IsNumExit`이 **TRUE**면 이미 존재하는 값이므로 다시 **while**을 실행하고 **FALSE**면 존재하지 않는 값이므로 **Buf**에 저장한다.

<br>

```c
int IsNumExit(int number, int index)
{
    int i;
    for(i = 0; i < index; i++){
        if(Buf[i] == number)
            return TRUE;
    }
    return FALSE;
}
```

`IsNumExit`함수는 `rand()`으로 생성한 변수와 배열의 인덱스를 받는다.

<br>

```c
void SelectionSort(void)
{
    int i, j, min, dummy;
    for(i = 0; i < MAX; i++){
        min = i;

        for(j = i + 1; j < MAX; j++)
            if(Buf[j] < Buf[min])
                min = j;

        dummy = Buf[min];           //swap한다.
        Buf[min] = Buf[i];
        Buf[i] = dummy;
    }
}
```

첫번째 for문은 현재 **i**를 배열 `Buf`의 최솟값의 인덱스라고 가정하고, 두번째 for문에서 **j**는 **i**보다 **1** 더 큰 인덱스부터 **MAX-1** 까지 반복실행한다. `Buf[j]`가 `Buf[min]`보다 더 작으면 **j**를 **min**으로 저장한다.

<br>

### 전체 코드

```c
#include <stdio.h>
#include <stdlib.h>
#define MAX 100
#define TRUE 1
#define FALSE 0

void MakeRandomNum(void);
void SelectionSort(void);
void DisplayBuffer(void);
int IsNumExit(int, int);
int Buf[MAX];

void MakeRandomNum(void)
{
    int i = 1;
    int Num;
    Buf[0] = 100;

    while(i < MAX){
        Num = rand() % MAX;

        if(!IsNumExit(Num, i)){
            Buf[i] = Num;
            i++;
        }
    }
}

void SelectionSort(void)
{
    int i, j, min, dummy;
    for(i = 0; i < MAX; i++){
        min = i;

        for(j = i + 1; j < MAX; j++)
            if(Buf[j] < Buf[min])
                min = j;

        dummy = Buf[min];
        Buf[min] = Buf[i];
        Buf[i] = dummy;
    }
}

void DisplayBuffer(void)
{
    int i;
    for(i = 0; i < MAX; i++){
        if((i % 10) == 0)
            printf("\n");

        printf("%3d ", Buf[i]);
    }
    printf("\n");
}

int IsNumExit(int number, int index)
{
    int i;
    for(i = 0; i < index; i++){
        if(Buf[i] == number)
            return TRUE;
    }
    return FALSE;
}

void main()
{
    printf("정렬할 데이터 초기화 :");
    MakeRandomNum();
    DisplayBuffer();
    printf("\n");

    printf("정렬 후 데이터 :");
    SelectionSort();
    DisplayBuffer();
    printf("\n");
}
```

```
정렬할 데이터 초기화 :
100   7  49  73  58  30  72  44  78  23
  9  40  65  92  42  87   3  27  29  12
 69  57  60  33  99  16  35  97  26  67
 10  79  21  93  36  85  45  28  91  94
  1  53   8  68  90  24  96  22  66  77
 98  81  13  14  63  25  15  17  95   5
  4  51  88  82  52  37  38  71  31  75
  6  62  19  54  89  70  20  34  50  59
 47  39  11  18  61  76  74  56  84  55
 80   2   0  64  48  83  46  43  32  41

정렬 후 데이터 :
  0   1   2   3   4   5   6   7   8   9
 10  11  12  13  14  15  16  17  18  19
 20  21  22  23  24  25  26  27  28  29
 30  31  32  33  34  35  36  37  38  39
 40  41  42  43  44  45  46  47  48  49
 50  51  52  53  54  55  56  57  58  59
 60  61  62  63  64  65  66  67  68  69
 70  71  72  73  74  75  76  77  78  79
 80  81  82  83  84  85  87  88  89  90
 91  92  93  94  95  96  97  98  99 100
```

### 분석

2개의 반복문으로 **N²/2**회 비교한다. 선택정렬 알고리즘은 실제 정렬에 사용되는 데이터의 수가 많은 경우 유용하다.

<br>

## 삽입 정렬 알고리즘

> 삽입 정렬 알고리즘은 데이터를 순차적으로 정렬하면서 현재 값을 정렬되어있는 값들과 비교해 적합한 위치로 삽입하는 방식이다.

```c
void InsertSort(void)
{
    int i, j, dummy;
    for(i = 0; i < MAX; i++){
        dummy = Buf[i];
        j = i;

        while(Buf[j-1] > dummy && j > 0){
            Buf[j] = Buf[j-1];
            j--;
        }

        Buf[j] = dummy;
    }
}
```

for문을 한번실행하면 j>0 이 아니므로 while로 들어가지않고 두번째 실행할때 (i가 1이되는 경우)부터 while문으로 들어간다. while로 들어가면 `Buf[j-1]`의 값을 `Buf[j]`에 저장하고 j를 하나 감소시킨다. 그리고 다시 while로 간다. j가 0되면 빠져나온다.

즉 for문은 정렬할 데이터를 처음부터 끝까지 반복해서 찾는 부분, while문은 이미 정렬된 데이터 중에서 dummy에 저장한 값이 들어갈 위치를 찾는 부분이다.

### 분석

삽입 정렬 알고리즘 성능은 빅오표기법으로 **O(N²)** 이다. 선택 정렬 알고리즘이 비교횟수가 많고 데이터의 이동 횟수는 적은 반면, 삽입 정렬 알고리즘은 비교 횟수가 적고 상대적으로 데이터의 이동 횟수는 많은 편이다.

<br>

## 버블 정렬 알고리즘

> 순차적으로 바로 옆의 데이터와 비교해서 옆의 데이터가 더 크면 자신과 위치를 바꾼다. 즉, 첫번째 데이터가 만약 가장크면 계속해서 비교해서 맨 끝으로 이동한다.

```c
void BubbleSort(void)
{
    int i, j, dummy;

    for(i = MAX-1; i >= 0; i--){
        for(j = 1; j <= i; j++){
            if(Buf[j-1] > Buf[j]){
                dummy = Buf[j-1];
                Buf[j-1] = Buf[j];
                Buf[j] = dummy;
            }
        }
    }
}
```

첫번째 for문은 마지막 위치에서부터 한 칸씩 줄어들며 반복실행한다. 두번째 for문은 i값과 같거나 작을때까지 증가하면서 반복실행한다. if문은 `Buf[j-1]`이 `Buf[j]`보다 크면 두 값을 바꾼다.

### 분석

버블 정렬 알고리즘 성능도 빅오표기법으로 **O(N²)** 이다. 최선의 경우 데이터가 정렬된 상황이므로 이동횟수는 0이지만 비교횟수는 `N*N / 2`이다. 최악의 경우는 비교횟수와 이동횟수 모두 `N*N / 2`이다. 최악의 경우를 가정하면 성능이 다른 정렬 알고리즘보다 많이 나쁘다.

<br>
