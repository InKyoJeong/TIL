## printf, scanf, if

```c
#include <stdio.h>

int main(void)
{
    //형식지정자
    printf("%d는 정수이다.\n", 10);
    printf("%f는 실수이다. 기본적으로 소숫점 6자리까지표시된다.\n", 3.14);
    printf("%c는 문자이다. 작은따옴표로 표기한다.\n", 'a');
    printf("%s는 문자열이다. 큰따옴표로 표기한다.\n", "ABC");

    //여러개의 형식지정자 받기
    printf("사과 %d개의 가격은 %d원입니다.\n", 10, 9000);
    printf("%c다음은 %c입니다.\n", 'A', 'B');

    //구구단 출력하기
    printf("%d곱하기 %d는 %d입니다.\n", 2, 3, 6);

    //이스케이프 시퀀스
    printf("따옴표를 출력하기: \" 백슬래시 출력하기: \\ ");

    return 0;
}

// 10는 정수이다.
// 3.140000는 실수이다. 기본적으로 소숫점 6자리까지표시된다.
// a는 문자이다. 작은따옴표로 표기한다.
// ABC는 문자열이다. 큰따옴표로 표기한다.
// 사과 10개의 가격은 9000원입니다.
// A다음은 B입니다.
// 2곱하기 3는 6입니다.
// 따옴표를 출력하기: " 백슬래시 출력하기: \
```

```c
#include <stdio.h>
int main(void)
{
    int number;  //정수형 변수선언
    float grade; //실수형 변수선언

    number = 10;
    grade = 13.2343;

    printf("%d %f\n", number, grade); //10 13.234300
    //형식지정자와 변수의 자료형은 일치해야한다.

    number = 20;            // 변수에 새로운 값을 대입하면 기존의 값이 지워지고 새로운 값이 저장된다.
    printf("%d\n", number); //20
    return 0;
}
```

```c
//원의면적 구하기
#include <stdio.h>
int main(void)
{
    float radius;
    float area;

    printf("원의 반지름을 입력하세요: ");
    scanf("%f", &radius);

    area = 3.141592 * radius * radius;
    printf("원의 면적은 %f입니다.", area);

    return 0;
}
//원의 반지름을 입력하세요: 11
//원의 면적은 380.132629입니다.
```

```c
//기호상수
#include <stdio.h>
#define PI 3.141592

int main(void)
{
    float radius;
    float area;

    printf("반지름을 입력: ");
    scanf("%f", &radius);

    area = PI * radius * radius;
    printf("원의면적은 %f이다.", area);
}
//반지름을 입력: 10
//원의면적은 314.159210이다.
```

```c
//두수의 합 구하기
#include <stdio.h>

int main(void)
{
    int x = 100;
    int y = 200;
    int sum;
    sum = x + y;

    printf("두수의 합은 %d이다\n", sum);
}
```

### 형식지정자 , scanf함수

- 실수는 `float`와 `double`형이 있다. double형이 더 넓은 범위의실수를 표현한다.
- double형을 입력받는경우 형식지정자를 `%lf`로 한다.

````c
#include <stdio.h>

int main(void)
{


    double score;

    printf("학점을 입력하세요: ");
    scanf("%lf", &score);

    printf("학점은 %f입니다.", score);
    return 0;
}
//학점을 입력하세요: 4.3
//학점은 4.300000입니다.

```c
//입력받은 정수 합계 구하기
#include <stdio.h>
int main(void)
{
    int x;
    int y;
    int sum;

    printf("첫번째 정수를 입력하세요: ");
    scanf("%d", &x);

    printf("두번째 정수를 입력하세요: ");
    scanf("%d", &y);

    sum = x + y;

    printf("두 수의 합은 %d이다.", sum);
}
````

```c
//세 수의 평균 구하기
#include <stdio.h>
int main(void)
{
    int x, y, z, sum, avg;

    printf("첫번째 정수를 입력하세요: ");
    scanf("%d", &x);

    printf("두번째 정수를 입력하세요: ");
    scanf("%d", &y);

    printf("두번째 정수를 입력하세요: ");
    scanf("%d", &z);

    sum = x + y + z;
    avg = sum / 3;
    printf("세 수의 평균은 %d이다.", avg);
}
//첫번째 정수를 입력하세요: 10
//두번째 정수를 입력하세요: 20
//두번째 정수를 입력하세요: 100
//세 수의 평균은 43이다.
```

### 부호없는 정수

- `unsigned`키워드가 정수형 앞에 붙으면 변수가 0과 **양의정수**만 나타낸다.
- `unsigned`변수를 출력할 경우 형식지정자는 `%u`사용.

```c
#include <stdio.h>
int main(void)
{
unsigned short value;
value = 65535;
printf("%u", value);
return 0;

}
```

### 문자 입출력

```c
#include <stdio.h>
int main(void)
{
char initial;
char grade;

    printf("이니셜 입력: ");
    scanf(" %c", &initial);

    printf("학점을 A~F중에 입력하세요: ");
    scanf(" %c", &grade);

    printf("%c의 성적은 %c이다.", initial, grade);

    return 0;

    // %c앞에 공백이 없으면 엔터키도 문자로 인식한다.

}
```

### 나머지연산자

```c
#include <stdio.h>
int main(void)
{
int remain;
int num;

    printf("정수를 입력하세요: ");
    scanf("%d", &num);

    remain = num % 2;
    printf("이것을 2로 나눈 나머지는 %d이다.", remain);
    return 0;

}
// 정수를 입력하세요: 11
// 이것을 2로 나눈 나머지는 1이다
```

```c
// 거스름돈 구하기
#include <stdio.h>
int main(void)
{
int remain;
int money;
int price;

    printf("받은 돈: ");
    scanf("%d", &money);

    printf("물건 가격: ");
    scanf("%d", &price);

    remain = (money - price);
    printf("오천원: %d \n", remain / 5000);
    printf("천원: %d \n", (remain % 5000) / 1000);
    printf("오백원: %d \n", (remain % 5000 % 1000) / 500);
    printf("백원: %d \n", (remain % 5000 % 1000 % 500) / 100);
    return 0;

}
// 받은 돈: 10000
// 물건 가격: 3400
// 오천원: 1
// 천원: 1
// 오백원: 1
// 백원: 1
```

### 명시적인형변환

```c
#include <stdio.h>
int main(void)
{
int i;
printf("%d \n", 3 / 2); //1
printf("%f \n", 3.0 / 2); //1.500000
printf("%f \n", (double)3 / 2); //1.500000

    i = (int)1.4 + (int)1.3;
    printf("%d\n", i); //2
    return 0;

}
```

#### 실수부와 정수부 나눠보기

```c
// 실수를입력하세요 : 3.13
// 정수부값은 3이고 소수부값은 0.13입니다.

#include <stdio.h>
int main()
{
    double x;
    int y;


    printf("실수를입력하세요 : ");
    scanf("%lf", &x);
      y = (int)x;
    printf("정수부값은 %d이고 소수부값은 %.2f입니다.", y , x - y);
    return 0;
}
```

### 홀짝 구분하기

```c
#include <stdio.h>
int main(void)
{
int i;
printf("정수를 입력하세요: ");
scanf("%d", &i);

    if (i % 2 == 0)
    {
        printf("짝수입니다.");
    }
    else
    {
        printf("홀수입니다.");
    }
    return 0;

}
```

### 큰 수 판별하기

```c
#include <stdio.h>
int main(void)
{
int x, y;
printf("첫번째 정수: ");
scanf("%d", &x);

    printf("두번째 정수: ");
    scanf("%d", &y);

    if (x > y)
    {
        printf("%d가 더 큰수다.", x);
    }
    else
    {
        printf("%d가 더 큰수다.", y);
    }
    return 0;

}
```

```c
// 윤년 판별하기
#include <stdio.h>
int main(void)
{
int year;

    printf("년도를 입력하세요 : ");
    scanf("%d", &year);

    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
    {
        printf("%d는 윤년이다.", year);
    }
    else
    {
        printf("%d는 윤년이 아니다", year);
    }
    return 0;

}
```

```c
//성적에따라 학점 매기기
#include <stdio.h>
int main(void)
{
int score;
printf("점수를 입력하세요 : ");
scanf("%d", &score);

    if (score >= 90)
    {
        printf("학점 A");
    }
    else if (score >= 80)
    {
        printf("학점 B");
    }
    else if (score >= 70)
    {
        printf("학점 C");
    }
    else if (score >= 60)
    {
        printf("학점 D");
    }
    else
    {
        printf("학점 F");
    }
    return 0;

}
```

```c
//계산기 만들기
#include <stdio.h>
int main(void)
{
int x, y, result;
char cal;
printf("수식을 입력하세요 <예시: 5 / 2> :");
scanf("%d %c %d", &x, &cal, &y);

    if (cal == '+')
    {
        result = x + y;
    }
    else if (cal == '-')
    {
        result = x - y;
    }
    else if (cal == '/')
    {
        result = x / y;
    }
    else if (cal == '*')
    {
        result = x * y;
    }
    else
    {
        printf("계산불가");
    }

    printf("결과: %d \n", result);
    return 0;

}
```

## 아스키코드

> 숫자입력해서 바꾸기

```c
#include <stdio.h>
int main()
{
    int x;
    printf("ASCII CODE: ");
    scanf("%d", &x);
    printf("The Character : %c \n", x);

    return 0;
}

//ASCII CODE: 67
//The Character : C
```

## 8진수와 16진수 출력하기

```c
#include <stdio.h>
int main()
{
    char ch = 'a';

     printf("%c     %d      0%o     0x%x \n", ch, ch, ch, ch);
     printf("%c     %d      0%o     0x%x \n", ch +1, ch +1,ch +1,ch +1);
     printf("%c     %d      0%o     0x%x \n", ch+2, ch+2, ch+2, ch+2);
     printf("%c     %d      0%o     0x%x \n", ch+3, ch+3, ch+3, ch+3);

return 0;
}
// a     97      0141     0x61
// b     98      0142     0x62
// c     99      0143     0x63
// d     100      0144     0x64
```

<br>

## 최댓값과 최솟값 표현

- `limits.h` 헤더 파일에는 부호 있는 정수와 부호 없는 정수의 최솟값과 최댓값이 정의되어 있다.

```cpp
#include <iostream>
#include <limits.h>

using namespace std;

int main() {

    cout<< INT_MAX <<'\n';  // 2147483647
    cout<< INT_MIN <<'\n';  // -2147483648

    cout<< CHAR_MAX <<'\n'; // 127
    cout<< LONG_MAX <<'\n'; // 9223372036854775807
    return 0;
}
```
