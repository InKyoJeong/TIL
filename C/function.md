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
