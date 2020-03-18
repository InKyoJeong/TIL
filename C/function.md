## 함수

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
