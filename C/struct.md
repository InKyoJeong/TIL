## 구조체

> 변수를 하나로 묶어 한꺼번에 처리할 수 있다.

```c
struct point{
    int x;
    int y;
};
struct point p1;    // p1은 구조체 변수 이름
```

### 구조체 멤버 접근

```c
struct point{
    int x;
    int y;
};
struct point p1;

p1.x = 10;
p1.y = 11;

printf("%d", p1.x); // 10
printf("%d", p1.y); // 11
```

### 구조체 초기화

> 구조체도 선언과 동시에 초기화 할 수 있다. 초기값을 중괄호 안에 나열한다.

```c
struct point{
    int x;
    int y;
};
struct point p1 = {10, 11};
```

### 구조체 예제

문자배열에 문자열을 저장할 때는 `strcpy()`를 사용한다.

```c
#include <stdio.h>
#include <string.h>

struct student{
    int age;
    char name[10];
    double grade;
};

int main(void)
{
    struct student s;

    s.age = 25;
    strcpy(s.name, "아이유");
    s.grade = 4.3;

    printf("나이: %d\n", s.age);
    printf("이름: %s\n", s.name);
    printf("학번: %f\n", s.grade);

    return 0;
}
//나이: 25
//이름: 아이유
//학번: 4.300000
```

참고) 구조체 초기화에서 문자열을 저장할 때는 `strcpy()`를 사용하지 않는다. 배열에 바로 문자열이 저장된다.

```c
struct student{
    int age;
    char name[10];
    double grade;
};
struct student s = {25, "IU", 4.3};
```

### 구조체의 배열

> 구조체의 배열을 이용해서 학생 3명의 데이터를 저장하기

```c
struct student{
    int age;
    char name[10];
    double grade;
}
struct student list[3];
```

배열의 인덱스가 `0`인 요소에 값을 저장하기

```c
list[0].age = 25;
strcpy(list[0].name, "IU");
list[0].grade = 4.3;
```

구조체의 배열도 초기화가 가능하다.

```c
struct student list[3] = {
    {25, "IU", 4.3},
    {27, "Mary", 4.2},
    {29, "John", 4.1}
};
```

#### 학생 성적 저장하기

```c
//IU : 영어점수=30, 수학점수=60, 코딩점수=10
//Mary : 영어점수=50, 수학점수=90, 코딩점수=20
//John : 영어점수=80, 수학점수=40, 코딩점수=90

#include <stdio.h>
#define N 3

struct student{
    char name[10];
    int math;
    int eng;
    int coding;
};

struct student list[] = {
    {"IU", 30, 60, 10},
    {"Mary", 50, 90, 20},
    {"John", 80, 40, 90}
};

int main(void)
{
    int i;
    for(i = 0; i < N; i++){
        printf("%s : 영어점수=%d, 수학점수=%d, 코딩점수=%d\n", list[i].name, list[i].math, list[i].eng, list[i].coding);
    }
    return 0;
}
```

### 구조체의 포인터

구조체를 가리키는 포인터를 만들 수도 있다.

```c
struct point{
    int x;
    int y;
};
struct point p1 = {3,4};
struct point *ptr;  //구조체의 포인터 선언
ptr = &p1;  //구조체 주소를 포인터에 대입
```

#### 구조체 멤버에 접근하기

```
(*ptr).x = 10;
(*ptr).y = 11;
```

#### 간접 멤버 연산자

> 구조체 포인터를 이용해서 멤버에 접근하기

```
ptr->x = 10;    //포인터 ptr이 가리키는 구조체의 멤버 x
ptr->y = 11;
```

#### 구조체의 멤버를 출력하기

> 3가지 방법으로 출력해보기

```c
#include <stdio.h>

struct student{
    int age;
    char name[10];
    double grade;
};

int main(void)
{
    struct student s = {25, "아이유", 4.3};
    struct student *p;

    p = &s;

    printf("나이=%d 이름=%s 학점=%f\n", s.age, s.name, s.grade);
    printf("나이=%d 이름=%s 학점=%f\n", (*p).age, (*p).name, (*p).grade);
    printf("나이=%d 이름=%s 학점=%f\n", p->age, p->name, p->grade);

    return 0;
}
// 나이=25 이름=아이유 학점=4.300000
// 나이=25 이름=아이유 학점=4.300000
// 나이=25 이름=아이유 학점=4.300000
```

### 공용체

구조체는 각 멤버가 독립된 공간을 할당받는 반면 공용체는 메모리공간을 여러 멤버가 공유한다.

```c
union test2{
    char a;
    short b;
    int c;
}
```

공용체에서도 멤버를 참조하려면 `.`연산자를 사용한다.

### 열거형

열거형은 변수가 가질수 있는 값을 하나씩 나열해놓은 자료형이다.

```c
enum colors {white, red, blue, purple, yellow};
```

각 기호상수에 구체적 값을지정할 수도 있다. 일부만 지정해도 된다.

```c
enum colors {
    white=1, red=2, blue=3, purple=4, yellow=5
};
```

열거형도 구조체와 마찬가지로 어떤 틀만 정의한 것이다. 실제로 변수를 생성해야 값을 저장할 수 있다.

```c
enum colors { white, red, blue, purple, yellow};
enum colors c;
c = white;
```

#### 열거형 예제

```c
#include <stdio.h>

enum days {
    SUN=0, MON=1, TUE=2, WED=3, THU=4, FRI=5, SAT=6
};

char *days_name[] = {
    "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"
};

int main(void){
    enum days d;

    d = MON;
    printf("%d번째 요일은 %s입니다\n", d, days_name[d]);

    return 0;
}

//1번째 요일은 monday입니다
```

### typedef

자신이 필요한 자료형을 정의하여 사용할 수 있다.

```c
struct point{
    int x;
    int y;
}
```

구조체를 새로운 타임으로 정의할 수 있다.

```c
typedef struct point POINT;
```

구조체 선언과 `typedef`를 같이 사용할 수 있다.

```c
typedef struct point{
    int x;
    int y;
} POINT;
```

이제 point구조체 변수를 생성하려면 이렇게 할 수 있다.

```
POINT a, b;
```
