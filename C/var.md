## 정적변수 (static)

```c
#include <stdio.h>

void increaseNum()
{
    int num = 0;
    printf("%d\n", num);
    num++;
}

int main()
{
    increaseNum();
    increaseNum();
    increaseNum();
    return 0;
}
```

- 실행결과

```
0
0
0
```

실행결과를 보면 0이 계속 출력된다. num이 지역 변수라서 increaseNum함수를 벗어나면 값이 사라지기 때문이다.

정적 변수는 변수가 사라지지 않게 한다. 변수선언시 변수 앞에 `static`을 선언하면 된다.

```c
#include <stdio.h>

void increaseNum()
{
    static int num = 0;
    printf("%d\n", num);
    num++;
}

int main()
{
    increaseNum();
    increaseNum();
    increaseNum();
    return 0;
}
```

- 실행결과

```
0
1
2
```

### 정적변수는 다른 파일에서 `extern`으로 참조할 수 없다.

```c
#include <stdio.h>

extern int num;
int main()
{
    printf("%d\n", num);    //에러

    return 0;
}
```

### 정적변수는 매개변수로 사용할 수 없다.

```c
void increaseNum(static int num)
{                                       // warning C4042: 'num'
    printf("%d\n", num);
    num++;
}
```

<br>

### 정적변수, 지역변수, 전역변수로 프로그램만들기

```
    [은행 자동 업무 시스템]
1. 입금
2. 출금
3. 조회
4. 종료
[선택(1-4)] 1
입금액 : 2000
    [은행 자동 업무 시스템]
1. 입금
2. 출금
3. 조회
4. 종료
[선택(1-4)] 2
출금액 : 400
    [은행 자동 업무 시스템]
1. 입금
2. 출금
3. 조회
4. 종료
[선택(1-4)] 3
총금액 :1600
    [은행 자동 업무 시스템]
1. 입금
2. 출금
3. 조회
4. 종료
[선택(1-4)] 4
```

```c
#include <stdio.h>

int input;      //전역변수

int main()
{
    while(1)
    {
        printf("    [은행 자동 업무 시스템]  \n");
        printf("1. 입금\n");
        printf("2. 출금\n");
        printf("3. 조회\n");
        printf("4. 종료\n");
        printf("[선택(1-4)] ");

        scanf("%d", &input);

        static int num = 0;     //정적변수

        if(input == 1)
        {
            int in;             //지역변수
            printf("입금액 : ");
            scanf("%d", &in);
            num += in;

        }
        else if(input == 2)
        {
            int out;            //지역변수
            printf("출금액 : ");
            scanf("%d", &out);
            num -= out;
        }
        else if(input == 3)
             printf("총금액 :%d\n", num);
        else
            break;
    }

    return 0;
}
```
