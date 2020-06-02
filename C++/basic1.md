> 입/출력, 오버로딩, 매개변수, inline, namespace

## 출력

- `#include <iostream>` 헤더파일 선언
- `std::cout`과 `<<`을 이용한 출력
- `std::endl`을 이용한 개행

```cpp
#include <iostream>

int main(void)
{
    int num = 22;
    std::cout<<"Hello World!"<<std::endl;
    std::cout<<"Hello"<<"World"<<std::endl;
    std::cout<<num<<' '<<'A';
    std::cout<<' '<<3.14<<std::endl;
    return 0;
}
```

```
Hello World!
HelloWorld
22 A 3.14
```

## 입력

- `std::cin`과 `>>`을 이용한 입력

```cpp
#include <iostream>

int main(void)
{
    int val1;
    std::cout<<"첫번째 숫자입력: ";
    std::cin>>val1;

    int val2;
    std::cout<<"두번째 숫자입력: ";
    std::cin>>val2;

    int result = val1 + val2;
    std::cout<<"덧셈 결과: "<<result<<std::endl;

    return 0;
}
```

```
첫번째 숫자입력: 12 (입력)
두번째 숫자입력: 8 (입력)
덧셈 결과: 20
```

### 정수 사이의 합구하기

```cpp
#include <iostream>

int main(void)
{
    int val1, val2;
    int result = 0;
    std::cout<<"두 개의 숫자 입력: ";
    std::cin>>val1>>val2;

    if(val1<val2)
    {
        for(int i = val1+1; i<val2; i++)
            result += i;
    }
    else
    {
        for(int i = val2+1; i<val1; i++)
            result += i;
    }

    std::cout<<"두 수 사이의 정수 합: "<<result<<std::endl;
    return 0;
}
```

```
두 개의 숫자 입력: 3 6 (입력)
두 수 사이의 정수 합: 9
```

`std::cin>>'변수1'>>'변수2';`와 같이 연속적인 데이터 입력이 가능

### 배열기반 문자열 입출력

```cpp
#include <iostream>
int main(void)
{
    char name[100];
    char lang[200];

    std::cout<<"이름을 입력하세요 ";
    std::cin>>name;

    std::cout<<"프로그래밍 언어를 입력하세요 ";
    std::cin>>lang;


    std::cout<<"내 이름은 "<<name<<"입니다.\n";
    std::cout<<"프로그래밍 언어는 "<<lang<<"입니다"<<std::endl;
    return 0;
}
```

```
이름을 입력하세요 inkyo
프로그래밍 언어를 입력하세요 c
내 이름은 inkyo입니다.
프로그래밍 언어는 c입니다
```

## 함수 오버로딩

> 함수호출시 전달되는 인자를 통해 구분이 가능해서, C++에서는 동일한 이름의 함수를 정의할 수 있다.

1. 매개변수의 선언이 달라야한다.

```cpp
int Func(char c)
{
    ...
}

int Func(int n)
{
    ...
}
```

2. 또는 개수가 달라야한다.

```cpp
int Func(int n)
{
    ...
}

int Func(int n1, int n2)
{
    ...
}
```

#### 예제

```cpp
#include <iostream>
void Func(void)
{
    std::cout<<"Func(void)"<<std::endl;
}
void Func(char c)
{
    std::cout<<"Func(char c)"<<std::endl;
}
void Func(int a, int b)
{
    std::cout<<"Func(int a, int b)"<<std::endl;
}

int main(void)
{
    Func();
    Func('A');
    Func(11,22);
    return 0;
}
```

- 실행결과

```
Func(void)
Func(char c)
Func(int a, int b)
```

#### 예제 2

```cpp
// swap함수를 오버로딩하여 구현하기

#include <iostream>

int main(void)
{
    int num1 = 11, num2 = 22;
    swap(&num1, &num2);
    std::cout<<num1<<' '<<num2<<std::endl;

    char c1 = 'A', c2 = 'B';
    swap(&c1, &c2);
    std::cout<<c1<<' '<<c2<<std::endl;

    double db1 = 1.11, db2 = 2.22;
    swap(&db1, &db2);
    std::cout<<db1<<' '<<db2<<std::endl;
    return 0;
}
```

```cpp
#include <iostream>
void swap(int * ptr1, int * ptr2)
{
    int temp = *ptr1;
    *ptr1 = *ptr2;
    *ptr2 = temp;
}

void swap(char * ptr1, char * ptr2)
{
    char temp = *ptr1;
    *ptr1 = *ptr2;
    *ptr2 = temp;
}

void swap(double * ptr1, double * ptr2)
{
    double temp = *ptr1;
    *ptr1 = *ptr2;
    *ptr2 = temp;
}

int main(void)
{
   ...(생략)
}
```

```
22 11
B A
2.22 1.11
```

## 매개변수의 디폴트

```cpp
int Func(int n = 1)
{
    return n+2;
}

int Func2(int n1 = 3, int n2 = 4)
{
    return n1 + n2;
}
```

#### 예제

```cpp
#include <iostream>
int AddFunc(int n1 = 3, int n2 = 5)
{
    return n1 + n2;
}

int main(void)
{
    std::cout<<AddFunc()<<std::endl;
    std::cout<<AddFunc(10)<<std::endl;
    std::cout<<AddFunc(7,5)<<std::endl;
    return 0;
}
```

```
8       //매개변수 디폴트값으로 3+5
15      //(10)하나만 전달하여 10은 첫번째 매개변수로 들어간다. 10+5
12      //(7,5)가 두개 다 전달되어 디폴트값이 의미가없다. 7+5
```

- 위와 같은 형태

```cpp
#include <iostream>
int AddFunc(int n1 = 3, int n2 = 5)

int main(void)
{
    std::cout<<AddFunc()<<std::endl;
    std::cout<<AddFunc(10)<<std::endl;
    std::cout<<AddFunc(7,5)<<std::endl;
    return 0;
}

int AddFunc(int n1, int n2)
{
    return n1 + n2;
}
```

- 매개변수 디폴트값은 왼쪽부터 채워지므로, 왼쪽만 채우고 오른쪽 매개변수 값을 비울수는 없다.

```cpp
ex)
int AddFunc(int n1 = 3, int n2, int n3)     //X 불가능
int AddFunc(int n1, int n2, int n3 = 10)    //O 가능
```

## inline 함수

> 매크로함수의 장점을 살리고 단점은 제거한 형태

```cpp
#include <iostream>

inline int SQUARE(int a)
{
    return a*a;
}

int main(void)
{
    std::cout<<SQUARE(4)<<std::endl;    //16
    std::cout<<SQUARE(4.5)<<std::endl;    //16

}
```

그러나 자료형이 다른걸 쓰면 소수부분이 무시됨. 따라서 템플릿을 사용하면 됨

```cpp
#include <iostream>

template <typename T>
inline T SQUARE(T a)
{
    return a*a;
}

int main(void)
{
    std::cout<<SQUARE(4)<<std::endl;    //16
    std::cout<<SQUARE(4.5)<<std::endl;    //20.25
}
```

## namespace (이름공간)

```cpp
#include <iostream>

namespace MaryFunc
{
    void TestFunc(void)
    {
        std::cout<<"Mary가 정의한 함수"<<std::endl;
    }
}

namespace JohnFunc
{
    void TestFunc(void)
    {
        std::cout<<"John이 정의한 함수"<<std::endl;
    }
}

int main(void)
{
    MaryFunc::TestFunc();
    JohnFunc::TestFunc();
    return 0;
}
```

```
Mary가 정의한 함수
John이 정의한 함수
```

이름공간을 지정할때 사용하는 `::`을 **범위지정 연산자**라고 한다.

- 함수 선언과 정의 분리

```cpp
#include <iostream>

namespace MaryFunc
{
    void TestFunc(void);
}

namespace JohnFunc
{
    void TestFunc(void);
}

int main(void)
{
    MaryFunc::TestFunc();
    JohnFunc::TestFunc();
    return 0;
}

void MaryFunc::TestFunc(void)
{
    std::cout<<"Mary가 정의한 함수"<<std::endl;
}

void JohnFunc::TestFunc(void)
{
    std::cout<<"John이 정의한 함수"<<std::endl;
}
```

```
Mary가 정의한 함수
John이 정의한 함수
```

#### 이름공간 중첩

```cpp
#include <iostream>

namespace Parent
{
    int n = 1;

    namespace ChildOne
    {
        int n = 2;
    }
    namespace ChildTwo
    {
        int n = 3;
    }

}

int main(void)
{
    std::cout<<Parent::n<<std::endl;
    std::cout<<Parent::ChildOne::n<<std::endl;
    std::cout<<Parent::ChildTwo::n<<std::endl;
    return 0;
}
```

```
1
2
3
```

#### using namespace

```cpp
#include <iostream>
using namespace std;

namespace AA
{
    namespace BB
    {
        namespace CC
        {
            int n1;
            int n2;
        }
    }
}

int main(void)
{
    AA::BB::CC::n1=11;
    AA::BB::CC::n2=22;

    namespace ABC=AA::BB::CC;
    cout<<ABC::n1<<endl;
    cout<<ABC::n2<<endl;
    return 0;
}
```

```
11
22
```

## 범위지정 연산자

지역변수/전역변수 접근하기

```cpp
int n1 = 10;        //전역변수

int Func(void)
{
    int n1 = 20;    //지역변수
    n1 += 4;        //20+4
}

//함수내에서 전역변수에 접근하기
int n2 = 10;        //전역변수

int Func(void)
{
    int n2 = 20;    //지역변수
    n2 += 4;        //20+4  (지역변수+4)
    ::n2 += 7;      //10+7  (전역변수+7)
}
```
