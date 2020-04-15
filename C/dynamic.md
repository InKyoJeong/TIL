## 동적 메모리 할당

> 프로그램이 실행 도중 동적으로 메모리를 할당받는 것

```c
int score_s[100];
```

위 같은 배열은 30개정도가 입력됐다고 하면 70개를 저장할 공간이 낭비된다.

```c
int *score;
score = (int *) malloc(100*sizeof(int));
```

동적 메모리 할당을 이용하면 프로그램에서 필요한 만큼만 메모리를 할당받아 사용하고, 사용이 끝나면 메모리를 반납한다.

### 동적 메모리 절차

```c
int *score;
score = (int *) malloc(100*sizeof(int));    // 동적메모리를 할당한다. malloc()으로 인수크기를 결정한다.

score[0] = 90;  // 동적메모리를 사용한다.
score[1] = 80;
...

free(score);    // free()를 호출하고 동적메모리를 반납한다.
```

### malloc()

`malloc()`은 바이트 단위로 메모리를 할당한다.

```c
score = (int *) malloc(100);    //100 바이트 만큼 메모리를 동적 할당한다.
```

아래 코드는 정수하나가 sizeof(int)만큼의 바이트이므로 100개의 정수를 저장할 공간을 할당할 수 있다.

```c
score = (int *) mallic(100*sizeof(int));
```

### 동적 메모리 사용

1. `*`연산자 사용

```c
*score = 100;
*(score+1) = 200;
*(score+2) = 300;
...
```

2. `[]`연산자 사용

```c
score[0] = 100;
score[1] = 200;
score[2] = 300;
...
```

동적 메모리를 동적 배열처럼 생각하고 두 번째 방법처럼 사용하는 것이 보다 일반적이다.

### 동적 메모리 반납

> 동적 메모리는 반드시 사용후 반납해야한다.

```c
free(score);
```

동적 메모리 반납이 안되어서 사용가능한 메모리가 점점 줄어드는 것을 **메모리 누수**라고 한다.

### 평균 점수 계산하기

```c
#include <stdio.h>
#include <stdlib.h>

int main(void){
    int n, i, *score;
    int sum = 0;

    printf("전체학생수 입력: ");
    scanf("%d", &n);

    score = (int*)malloc(n*sizeof(int));

    if(score == NULL)
    {
        printf("동적메모리 할당 오류");
        exit(0);        // exit()은 프로그램을 종료시킴
    }
    for(i = 0; i < n; i++)
    {
        printf("점수를 입력: ");
        scanf("%d", &score[i]);
        sum += score[i];
    }
    printf("평균 = %d \n", sum / n);
    free(score);

    return 0;
}
//전체학생수 입력: 3
//점수를 입력: 10
//점수를 입력: 20
//점수를 입력: 30
//평균 = 20
```

### 구조체 배열

구조체를 저장할 수 있는 공간도 할당받을 수 있다. 구조체의 크기에 필요한 개수를 곱한다.

```c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Book{
    int number;
    char title[50];
};

int main(void){
    struct Book *p;     //구조체를 가리키는 포인터 변수 선언
    p = (struct Book *)malloc(2* sizeof(struct Book));      // malloc()으로 구조체 2개분량 메모리를 동적으로 할당받음. 이 메모리블록의 시작주소를 p에 대입

    if(p == NULL){
        printf("메모리 할당 오류\n");
        exit(1);
    }


    p[0].number = 1;        // 동적으로 할당받은 첫 번째 구조체 배열 원소에 데이터를 대입
    strcpy(p[0].title, "C program");

    p[1].number = 2;
    strcpy(p[1].title, "Data Structure");

    free(p);
    return 0;
}
```

### realloc() 함수

`malloc()`으로 할당받은 메모리가 부족해질때 할당했던 메모리 블록의 크기를 변경한다.

```c
void *realloc(void *p, size_t szie);
```

```c
//예시
int *p;

p = (int *)mallic(5*sizeof(int));
realloc(p, 7*sizeof(int));
```

5개 정수를 저장하는 동적 메모리를 할당하고 다시 7개의 정수를 저장할 수 있도록 할당하였다. 기존 값은 유지된다.
