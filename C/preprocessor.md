## 전처리기

> 전처리기(preprocessor)는 컴파일하기에 앞서 소스파일을 처리하는 컴파일러의 한 부분이다.

- `#define` : 매크로 정의
- `#include` : 파일 포함
- `#undef` : 매크로 정의 해제
- `#if` : 조건이 참일 경우
- `#else` : 조건이 거짓일 경우
- `#endif` : 조건 처리 문장 종료
- `#ifdef` : 매크로가 정의되어 있는 경우
- `#ifndef` : 매크로가 정의되어 있지 않은 경우

### #include 지시자

`#include`지시자는 특정 헤더 파일을 포함시키기 위해 사용한다. `<>`로 묶은 파일은 C컴파일러가 제공하는 표준 라이브러리 헤더파일, `""`로 묶은 파일은 사용자가 만든 헤더파일.

```c
//mylib.h
int get_ integer(void);
...
```

```c
//main.c
#include "mylib.h"

int main(void)
{
    int a;
    a = get_integer();
}
...
```

### 단순매크로

`#define` 지시자를 이용하면 숫자 상수에 이름을 붙일 수 있다.

```c
#define N 100
```

### 함수매크로

함수매크로는 매크로가 함수처럼 매개변수를 가지는 것이다.

```c
#define SQUARE(x) ((x) * (x))
```

#### 함수매크로 예시

```c
#include <stdio.h>
#define SQUARE(x) ((x) * (x))

int main(void){
    int x = 2;

    printf("%d\n", SQUARE(x));      //4
    printf("%d\n", SQUARE(3));      //9
    printf("%f\n", SQUARE(1.2));    //1.440000
    printf("%d\n", SQUARE(x+3));    //25
    printf("%d\n", 100/SQUARE(x));  //25
    printf("%d\n", SQUARE(++x));    //16  ++x * ++x 이므로 9가아니라 16


    return 0;
}
```

#### 변수의 값을 교환하는 매크로

```c
// 정수 2개를 입력하세요: 11 22
// SWAP<> 실행결과: 22 11

#include <stdio.h>
#define SWAP(x, y, t) ( (t)=(x), (x)=(y), (y)=(t) )

int main(void){
    int x, y, t;

    printf("정수 2개를 입력하세요: ");
    scanf("%d %d", &x, &y);

    SWAP(x, y, t);

    printf("SWAP<> 실행결과: %d %d \n", x, y);

    return 0;
}
```

### #ifdef, #endif

`#ifdef`는 조건부 컴파일을 지시하는 전처리 지시자이다. (조건부 컴파일이란 어떤 조건이 만족하는 경우만 소스코드 블록을 컴파일하는 것)

```c
#include <stdio.h>
#define BETA

int main(){
    #ifdef BETA
        printf("베타버전입니다.\n");    //BETA가 정의된경우만 컴파일됨
    #endif

    return 0;
}
```
