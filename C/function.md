## 함수

- 매개변수 = 데이터를 받는 변수
- 매개변수가 없을 경우 `int get(void)`같이 매개변수 위치에 `void`를 쓰거나 그냥 비워놓는다.
- 반환값이 없으면 void main (int 변수이름)

```c
[반환형태][함수이름][입력형태]
int     main    (void){
    함수 몸체
}
// main이라는 함수는 반환값을 int형으로 반환하며 전달인자가 없다.(void는 존재하지않는다는 의미)
```

### 함수 호출 예제

```c
//두 개의 정수를 입력하시오 : 2 3
//2의 3승은 8입니다.

#include <stdio.h>
int power(int x, int y);

int main(void){
    int a, b, result;

    printf("두 개의 정수를 입력하시오 : ");
    scanf("%d %d", &a, &b);
    result = power(a , b);
    printf("%d의 %d승은 %d입니다.\n", a, b, result);
    return 0;
}

int power(int x, int y){
    int i;
    int value = 1;

    for(i=0; i<y; i++){
        value = value * x;
    }
    return value;
}
```

### 두 수 중에서 큰 수 찾기

```c
//두 수를 입력하시오: 4 18
//두 수 중에서 큰 수는 18이다.

#include <stdio.h>
int get_large(int x, int y);

int main(){
    int a, b;
    printf("두 수를 입력하시오: ");
    scanf("%d %d", &a, &b);
    printf("두 수 중에서 큰 수는 %d이다.\n", get_large(a, b));

    return 0;
}
int get_large(int x, int y){
    if(x > y){
        return (x);
    }else{
        return (y);
    }
}

```

### 소수 찾기

```c
// 정수를 입력하세요 :11
// 11는 소수입니다.

#include <stdio.h>

int get_integer(void);
int is_prime(int n);

int main(void){
    int n, result;

    n = get_integer();
    result = is_prime(n);

    if(result == 1){
        printf("%d는 소수입니다.\n", n);
    }
    else{
        printf("%d는 소수가 아닙니다.\n", n);
    }
    return 0;
}
int get_integer(void){
    int n;
    printf("정수를 입력하세요 :");
    scanf("%d", &n);
    return n;
}
int is_prime(int n){
    int i;
    for(i=2; i<n; i++){
        if(n%i == 0){
            return 0;
        }
    }
    return 1;
}
```

### 지역변수와 전역변수

```c
#include <stdio.h>

int x = 1;  // 전역변수

void sub(void){
    int y = 2 ;     // 지역변수
    printf("x = %d\n", x);
    printf("y = %d\n", y);
//  printf("z = %d\n", z);    //선언되지않은 식별자
}
int main(void){
    int z = 3;      // 지역변수
    printf("x = %d\n", x);
//  printf("y = %d\n", y);    //선언되지않은 식별자
    printf("z = %d\n", z);

    return 0;
}
```

- 전역변수는 컴파일러에 의해 자동적으로 0으로 초기화 된다.
- 지역변수는 자동으로 초기화되지않으며 초깃값을 정하지않으면 쓰레기값이 저장된다.
- 지역변수는 블록이 시작될때 생성되고 블록 끝에서 소멸된다.
