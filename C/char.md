## 문자열 함수

### 문자열 라이브러리 함수

- 문자열 입출력 함수 : 문자와 문자열을 입출력하는 함수

```
int getchar(void)       :    하나의 문자를 읽어서 반환
void putchar(int c)     :    변수 c에 저장된 문자를 출력
char *gets(char *s)     :    한 줄의 문자열을 읽어서 문자배열 s[]에 저장
int puts(const char *s) :    배열 s[]에 저장된 한 줄의 문자열 출력
```

- 문자열 처리 함수 : 문자열을 비교하거나 복사하는 함수

```
strlen(s)       :    문자열 s의 길이를 구함
strcpy(s1, s2)  :    s2를 s1에 복사
strcat(s1, s2)  :    s2를 s1의 끝에 붙임
strcmp(s1, s2)  :    s1과 s2를 비교
char *strtok( s, delimit)  :    분리자를 이용하여 문자열 s를 토큰으로 분리
```

### 문자열 입출력 함수

```c
#include <stdio.h>
int main(){

    char name[100];
    char address[100];

    printf("이름을 입력하세요: ");
    gets(name);     //배열의 이름이 배열의 주소이므로 &name과 같이 하지않는다.

    printf("현재 주소를 입력하세요: ");
    gets(address);

    puts(name);
    puts(address);

    return 0;
}
//이름을 입력하세요: In
//현재 주소를 입력하세요: seoul
//In
//seoul
```

### 문자열 처리 함수

문자열 함수들은 `string.h`에 선언되어 있다.

```c
#include <string.h>
```

`strlen()`은 문자열 길이를 계산한다.

```c
count = strlen("Hello");        //5를 반환한다.
```

```c
#include <stdio.h>
#include <string.h>
int main(){

    char name[20]="This is my..";
    int length;

    length = strlen(name);
    printf("문자열 길이 = %d\n", length);

    return 0;
}
//문자열 길이 = 12
```

### 문자열 복사 함수

문자열 복사하는 함수는 `strcpy()`이다.

```c
strcpy(s1, s2);
s1에 s2를 복사한다.
s1의 문자열 길이가 s2보다 길거나 같아야한다.
```

복사되는 문자열의 길이를 제한하려면 함수 `strncpy()`를 사용한다.

```c
char s1[6];
char s2[6] = "Hello";
strncpy(s1, s2, 3);

// s1은 "Hel"이 된다.
```

### 문자열 연결 함수

문자열을 연결하여 하나로 만드려면 `strcat()`함수를 사용한다.

```c
#include <string.h>
#include <stdio.h>

int main(void)
{
    char string[80];

    strcpy(string, "Hello my name ");
    strcat(string, "is ");
    strcat(string, "Inkyo");
    printf("%s \n", string);
    return 0;
}
// Hello my name is Inkyo
```

### 문자열 비교

```c
strcmp(s1, s2);

// -1: ASCII 코드 기준으로 문자열2(s2)가 클 때
// 0: ASCII 코드 기준으로 두 문자열이 같을 때
// 1: ASCII 코드 기준으로 문자열1(s1)이 클 때
```

두 개의 문자열을 비교할 때는 `strcmp()`함수를 사용한다. 주의할 점은 2개의 문자열이 **같으면** `1`이 아닌 **`0`을 반환한다.**

```c
#include <string.h>
#include <stdio.h>

int main(void)
{
    char a[100], b[100];

    printf("첫번째 문자를 입력하세요: ");
    gets(a);

    printf("두번째 문자를 입력하세요: ");
    gets(b);

    if(strcmp(a,b) == 0){
        printf("문자열이 일치\n");
    }else{
        printf("문자열이 다름\n");
    }
    return 0;
}
//첫번째 문자를 입력하세요: asdf
//두번째 문자를 입력하세요: asdf
//문자열이 일치
```

### 문자열 토큰 분리

`strtok()`를 사용하면 문장을 토큰으로 분리할 수 있다. 토큰이란 문법적으로 더 이상 나눌 수 없는 기본적인 언어 요소이다.

나머지 토큰들을 계속해서 읽으려면 `s` 대신 `NULL`을 넣는다. 즉 나머지 토큰들은 연속적으로 `strtok(NULL, " ")` 호출로 추출된다.

```c
char s [] = "your name is.";
char *t1, *t2, *t3, *t4;

t1 = strtok(s, " ");    //첫번째 토큰: "your" 반환  (분리자는 스페이스)
t2 = strtok(NULL, " "); //두번째 토큰: "name" 반환
t3 = strtok(NULL, " "); //세번째 토큰: "is." 반환
t4 = strtok(NULL, " "); //NULL반환
```

#### 토큰 분리 예제

```c
//토큰: Hi
//토큰: I
//토큰: like
//토큰: apples

#include <string.h>
#include <stdio.h>

char s[] = "Hi, I like apples";

char seps[] = " ,\t\n";     //분리자는 스페이스,쉼표,탭,줄바꿈
char *token;

int main(void){
    token = strtok(s, seps);

    while(token != NULL)
    {
        printf("토큰: %s\n", token);
        token = strtok(NULL, seps);
    }
    return 0;
}
```

### 문자열 수치변환

문자열을 수치값으로 바꿀때는 `sscanf()`와 `sprintf()`를 사용한다. `sscanf()`는 키보드대신 문자열에서 입력받는다. `sprintf()`는 모니터로 출력하는 대신 문자열로 출력한다.

```c
#include <stdio.h>
int main(void)
{
    char s1[] = "100";
    char s2[30];
    int value;

    sscanf(s1, "%d", &value);   // s1에서 "%d" 형식으로 읽어 value에 저장. 문자열->수치로 변환
    printf("%d\n", value);
    sprintf(s2, "%d", value);   // value에 저장된 값을 문자열로 변환해서 s2에 저장. 수치->문자열로 변환
    printf("%s\n", s2);
    return 0;
}
//100
//100

```
