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
