## 선택 정렬 알고리즘

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

최댓값 **100**을 **Buf[0]**에 저장하고 이미 생성된 값과 중복되지 않게 `IsNumExit()` 함수를 이용한다.
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

IsNumExit함수는 rand()으로 생성한 변수와 배열의 인덱스를 받는다.

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

첫번째 for문은 현재 i를 배열 `Buf`의 최솟값의 인덱스라고 가정하고 두번째 for문에서 j는 i보다 1 더 큰 인덱스부터 **MAX-1** 까지 반복실행한다. `Buf[j]`가 `Buf[min]`보다 더 작으면 j를 min으로 저장한다.

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

2개의 반복문으로 N²/2회 비교한다. 선택정렬 알고리즘은 실제 정렬에 사용되는 데이터의 수가 많은 경우 유용하다.
