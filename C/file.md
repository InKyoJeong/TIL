## 파일 입출력

### 파일이란?

- 파일(file) : 보조기억장치에서 문서/소리/그림/동영상 같은 자료를 모아 놓은것
- 파일안에는 바이트들이 순차적으로 저장되어 있고 끝에는 `EOF(end-of-file)`마커가 있음
- 모든 파일은 입출력 동작이 발생하는 위치를 나타내는 위치표시자를 가지고 있고 위치표시자는 파일의 내용을 읽거나 쓸때 자동으로 업데이트됨

### 파일 종류

- 텍스트 파일(text file) : 사람이 읽을 수 있는 텍스트 파일 (ex: 메모장 등)
- 이진 파일(binary file) : 사람이 읽을 수 없으나 컴퓨터는 읽을 수 있는 파일 (ex: 사운드/이미지 파일 등)

### 스트림

- 스트림(stream) : 입출력 장치와 프로그램을 연결하는 통신 채널
- 스트림은 기본적으로 버퍼(buffer)를 사용한다. 버퍼는 입력속도에 비해 출력속도가 느린경우 데이터를 임시 저장하는 공간을 말하며, 임시저장장치라고도 함

### fopen() 함수

> 파일에서 데이터를 읽거나, 쓸 수 있도록 파일과 연결된 스트림을 만들어서 반환한다.

```
FILE *fopen(const char *name, const char *mode);
```

```c
FILE *fp;
fp = fopen("test.txt", "r");
if(fp == NULL){
    오류출력
}
...
fclose(fp);
```

### 파일모드

`fopen()`의 두번째 매개변수 `mode`는 파일모드를 의미한다. `"r"`, `"w"`, `"a"`가 있다.

- "r" : 읽기모드. 파일의 처음부터 읽는다.
- "w" : 쓰기모드. 파일의 처음부터 쓴다. 파일이 없으면 생성된다.
- "a" : 추가모드. 파일의 끝에 쓴다. 파일이 없으면 생성된다.

파일모드에 `"t"`나 `"b"`를 붙일 수 있다.

- "t" : 파일을 텍스트모드로 연다.
- "b" : 파일을 이진모드로 연다.

### 문자 단위 입출력

- `fgetc()`함수는 파일에서 하나의 문자를 읽어 반환한다. 문자를 반환하지만 반환형이 `char`가 아니고 `int`이다. (파일의 끝을 나타내는 `EOF`가 `-1`로 정의되기때문)

```c
int fgetc(FILE *fp);
```

- `fputc()`함수는 `fp`로 지정된 파일로 하나의 문자를 쓰는 함수인다.

```c
int fputc(int c, FILE *fp);
```

#### 파일 생성하고 글자 쓰기

> text.txt 파일을 쓰기모드로 열어서 a b c 저장하기

```c
#include <stdio.h>

int main(void)
{
    FILE *fp = NULL;         // FILE포인터 변수 fp 를 정의하고 fopen()의 반환값 저장
    fp = fopen("text.txt", "w");
    if( fp == NULL){         // fopen()이 반환하는 FILE포인터는 NULL인지 아닌지 검사해야한다.
        printf("파일 열기 실패 \n");
        return 1;
    }
    fputc('a', fp);
    fputc('b', fp);
    fputc('c', fp);

    fclose(fp);
    return 0;
}
// text.txt
// --------
// abc
```

#### 파일 오픈하고 글자 읽기

> 위에서 생성한 text.txt 파일을 읽기

```c
#include <stdio.h>
int main(void)
{
    FILE *fp;
    int c;

    fp = fopen("sample.txt", "r");

    if(fp == NULL){
        printf("파일 열기 실패 \n");
        return 1;
    }

    while((c = fgetc(fp)) != EOF)
        putchar(c);

    fclose(fp);
    return 0;
}
```

### 문자열 단위 입출력

파일에서 문자열을 읽으려면 `fgets()`를 사용한다.

```c
char *fgets( char *s, int n, FILE *fp );
```

`fputs()`는 문자열을 fp에 저장한다.

```c
int fputs( char *s, FILE *fp );
```

#### 파일 생성하고 문자열 쓰기

```c
#include <stdio.h>
int main(void){
    FILE *fp;

    fp = fopen("text.txt", "w");

    if( fp == NULL ){
        printf("파일 열기 실패 \n");
        return 1;
    }

    fputs("This is a test. \n", fp);
    fputs("This is a sample. \n", fp);

    fclose(fp);
    return 0;
}
```
