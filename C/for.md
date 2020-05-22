## switch, while, do-while, for

### switch문으로 월의 날짜 구하기

```c
#include <stdio.h>
int main(void)
{
    int days, month;

    printf("달을입력하세요: ");
    scanf("%d", &month);

    switch (month)
    {
    case 2:
        days = 28;
        break;
    case 4:
    case 6:
    case 9:
    case 11:
        days = 30;
        break;
    default:
        days = 31;
        break;
    }

    printf("달의 일수는 %d이다.\n", days);
    return 0;
}
```

```c
// 0부터 9까지 출력하기
#include <stdio.h>
int main(void)
{
    int i = 0;
    while (i < 10)
    {

        printf("%d ", i);
        i++;
    }
    return 0;
}
```

```c
// 1부터 10까지 더하기
#include <stdio.h>
int main(void)
{
    int i = 0;
    int sum = 0;
    while (i <= 10)
    {
        sum += i;
        i++;
    }
    printf("%d", sum);
    return 0;
}
```

```c
// 팩토리얼 구하기
#include <stdio.h>
int main(void)
{
    int num;
    printf("팩토리얼을 구할 숫자입력: ");
    scanf("%d", &num);
    int i = 1;
    int result = 1;

    while (i <= num)
    {
        result *= i;
        i++;
    }
    printf("%d", result);
    return 0;
}
```

```c
// 구구단 3단 출력하기
#include <stdio.h>
int main(void)
{
    int i = 1;
    while (i <= 9)
    {
        printf("3*%d=%d\n", i, 3 * i);
        i++;
    }

    return 0;
}
```

```c
// 카운트다운
#include <stdio.h>
int main(void)
{
    int i;
    printf("숫자입력: ");
    scanf("%d", &i);

    while (i > 0)
    {
        printf("%d \n", i);
        i--;
    }

    printf("끝 \n");

    return 0;
}
```

```c
// 3의 배수의 합
#include <stdio.h>
int main(void)
{
    int num = 1;
    int result = 0;

    while (num <= 100)
    {
        if (num % 3 == 0)
        {
            result = result + num;
        }
        num++;
    }
    printf("1부터 100까지의 모든 3의 배수의 합은 %d이다.", result);

    return 0;
}
```

### do-while

```c
#include <stdio.h>
int main(void)
{
    char signal;
    do
    {
        printf("신호를 입력하세요<r,y,g> : ");
        scanf(" %c", &signal);
    } while (signal != 'r');

    printf("정지! \n");

    return 0;
}
```

```c
#include <stdio.h>
int main(void)
{
int n = 1;
int sum = 0;

    while (n)
    { //0이 아니면 계속반복
        printf("정수를 입력하세요: ");
        scanf("%d", &n);
        sum += n;
    }
    return 0;

}
```

### for문

```c
#include <stdio.h>
int main(void)
{
int i, limit;
int num = 0;

    printf("계산할 숫자를 입력하세요: ");
    scanf("%d", &limit);

    for (i = 0; i <= limit; i++)
    {
        num = num + i;
    }
    printf("정수의 합은 %d이다.\n", num);
    return 0;

}
```

```c
// 1^2 + 2^2 + 3^3 ... 수열 구하기
//숫자n의 값을 입력하라: 10
//결과는 385이다.
#include <stdio.h>
int main(void)
{
int i, n;
int result = 0;

    printf("숫자n의 값을 입력하라: ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        result = result + i * i;
    }
    printf("결과는 %d이다.\n", result);
    return 0;

}
```

```c
// 약수구하기
// 양의 정수를 입력: 100
// 1 2 4 5 10 20 25 50 100
#include <stdio.h>
int main(void)
{
int x, i;

    printf("양의 정수를 입력: ");
    scanf("%d", &x);

    for (i = 1; i <= x; i++)
    {
        if (x % i == 0)
        {
            printf("%d ", i);
        }
    }
    return 0;

}
```

### 중첩 for문

```c
//*********
//*********
//*********
//*********
//*********

#include <stdio.h>
int main(void)
{
    int i, j;
    for (i = 0; i < 5; i++){
        for (j = 0; j < 10; j++){
        printf("\*");
        }
    printf("\n");
    }
    return 0;
}
```

```c
// 구구단 전부출력하기
#include <stdio.h>
int main(void)
{
        int i, j;
        for (i = 2; i < 10; i++){
            for (j = 1; j < 10; j++){
            printf("%d*%d=%2d ", i, j, j * i); // %2d는 정수출력할때 2칸사용, 오른쪽정렬
            }
        printf("\n");
        }
        return 0;
}
```

```c
// 주사위의합이 7인경우구하기
// 주사위A 주사위B
// 1 6
// 2 5
// 3 4
// 4 3
// 5 2
// 6 1
#include <stdio.h>
int main(void)
{
    int i, j;
    printf("주사위A \t 주사위B \n");
    for (i = 1; i <= 6; i++){
        for (j = 1; j <= 6; j++){
            if (i + j == 7){
            printf("%d \t\t %d\n", i, j);
            }
        }
    }
    return 0;
}
```

```c
// continue문으로 3의배수 제외하고 출력하기
// 1 2 4 5 7 8
#include <stdio.h>
int main(void)
{
int i;

    for (i = 0; i < 10; i++)
    {
        if (i % 3 == 0)
        {
            continue; //continue문을 만나면 다음 반복을 즉시시작
        }
        printf("%d ", i);
    }
    return 0;

}
```

## 누적곱 (팩토리얼) 값 계속 입력받아서 출력하기

```c
//임의의 정수를 입력하시오: 5
//n      1부터 n까지의 곱
//1      1
//2      2
//3      6
//4      24
//5      120
//계속 하시겠습니까?(y/n) y
//임의의 정수를 입력하시오: 4
//n      1부터 n까지의 곱
//1      1
//2      2
//3      6
//4      24
//계속 하시겠습니까?(y/n)

#include <stdio.h>
int main(){

    char answer;

   while(1){
       int x;
       int i;
       int sum = 1;

       printf("임의의 정수를 입력하시오: ");
       scanf("%d", &x);
       printf("n \t 1부터 n까지의 곱\n");

       for(i=1; i<=x; i++){
       sum = sum * i;
       printf("%d \t %d \n", i, sum);
       }

    printf("계속 하시겠습니까?(y/n) ");
    scanf(" %c", &answer);

    if(answer == 'n') break;
   }
    return 0;
}
```

변수들을 while문 밖에서 선언해서 두번째 경우 누적값이 되는걸 해결하는데 오래걸렸다. while문 안에 선언해서 반복할때마다 초기화해서 해결함
