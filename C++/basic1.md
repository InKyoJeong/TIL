> 입/출력, 오버로딩, 매개변수, inline, namespace, bool, 참조자(reference)

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

<br>

## 자료형 bool

```cpp
#include <iostream>
using namespace std;

int main(void)
{
    int i = 0;
    cout<<"true: "<<true<<endl;
    cout<<"false: "<<false<<endl;

    cout<<"sizeof(true): "<<sizeof(true)<<endl;
    cout<<"sizeof(false): "<<sizeof(false)<<endl;

    while(true)
    {
        cout<<i++<<' ';
        if(i>5)
            break;
    }
    cout<<endl;
    return 0;
}
```

```
true: 1
false: 0
sizeof(true): 1
sizeof(false): 1
0 1 2 3 4 5
```

- bool형 변수나 함수반환형으로도 사용가능

```cpp
#include <iostream>
using namespace std;

bool IsPositive(int n)
{
    if(n<=0)
        return false;
    else
        return true;
}

int main(void)
{
    bool isPosi;
    int n;
    cout<<"숫자 입력: ";
    cin>>n;

    isPosi=IsPositive(n);

    if(isPosi)
        cout<<"양수"<<endl;
    else
        cout<<"음수"<<endl;
    return 0;
}
```

```
숫자 입력: -3
음수
```

<br>

## 참조자(Reference)

> 자신이 참조하는 변수를 대신할 수 있는 또하나의 이름

```cpp
#include <iostream>
using namespace std;

int main()
{
    int num1=1111;
    int &num2=num1;

    num2=2222;
    cout<<"Val: "<<num1<<endl;
    cout<<"Ref: "<<num2<<endl;

    cout<<"Val: "<<&num1<<endl;
    cout<<"Ref: "<<&num2<<endl;

    return 0;
}
```

```
Val: 2222
Ref: 2222

Val: 0x7ffeefbff588
Ref: 0x7ffeefbff588
```

- 변수만 선언이 가능하고 선언과 동시에 누군가를 참조해야함

#### 배열도 참조가능

```cpp
#include <iostream>
using namespace std;

int main()
{
    int arr[3] = {11,22,33};
    int &ref1=arr[0];
    int &ref2=arr[1];
    int &ref3=arr[2];

    cout<<ref1<<endl;
    cout<<ref2<<endl;
    cout<<ref3<<endl;
    return 0;
}
```

```
11
22
33
```

<br>

## new & delete

> malloc & free를 대신한다.

```cpp
#include <iostream>
#include <string.h>
#include <stdlib.h>

using namespace std;

char * MakeStrAdr(int len)
{
    // char * str = (char*)malloc(sizeof(char)*len);
    char * str = new char[len];
    return str;
}

int main(void)
{
    char * str = MakeStrAdr(20);
    strcpy(str, "I am student");
    cout<<str<<endl;
    // free(str);
    delete []str;
    return 0;
}
```

- int형 변수 할당 : `int * ptr1 = new int;`
- double형 변수 할당 : `double * ptr2 = new double;`
- 길이가5인 int형 배열할당 : `int * arr1 = new int[5];`

- int형 변수 소멸 : `delete ptr1;`
- double형 변수 소멸 : `delete ptr1;`
- int형 배열 소멸 : `delete []arr1;`

<br>

## C++ 헤더파일

C언어의 라이브러리의 함수들은 C++라이브러리에도 포함되어있다. 헤더파일의 .h를 빼고 c를 앞에 붙이면 된다.

```c
//C
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

//C++
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
```

---

<br>

## 입출력 문제

#### 사용자로부터 총5개 정수를 입력받아 그 합을 출력하기

```
0번째 정수 입력 : 1
1번째 정수 입력 : 2
2번째 정수 입력 : 2
3번째 정수 입력 : 2
4번째 정수 입력 : 2
합계: 9
```

```cpp
#include <iostream>
using namespace std;
int main(void)
{
    int x;
    int sum=0;
    for(int i =0; i<5; i++)
    {
        cout<<i<<"번째 정수 입력 : ";
        cin>>x;
        sum+=x;
    }

    cout<<"합계: "<<sum;
    return 0;
}
```

#### 숫자에 해당하는 구구단 출력하기

```
구구단을 출력할 숫자입력: 4
4*1=4
4*2=8
4*3=12
4*4=16
4*5=20
4*6=24
4*7=28
4*8=32
4*9=36
```

```cpp
#include <iostream>
using namespace std;

int main(){
    int input;
    int cal=1;
    cout<<"구구단을 출력할 숫자입력: ";
    cin>>input;

    for(int i=1; i<10; i++)
    {
        cal = input * i;
        cout<<input<<'*'<<i<<'='<<cal<<endl;
    }
    return 0;
}
```

#### 판매액을 입력하면 급여를 계산하기

> 어떤 회사는 판매액을 입력하면 50만원 + 판매액의 18%만큼 추가 급여를 준다. 이회사의 급여계산 프로그램 만들기 (-1을 입력하면 종료한다.)

```
판매금액 입력(단위:만원) :100
이번달 급여 : 68
판매금액 입력(단위:만원) :50
이번달 급여 : 59
판매금액 입력(단위:만원) :-1
프로그램종료
```

```cpp
#include <iostream>
using namespace std;

int CalFunc(int sale)
{
    int result = 50 + sale*0.18;
    return result;
}

int main(void)
{
    while(1)
    {
        int sale;
        cout<<"판매금액 입력(단위:만원) :";
        cin>>sale;
        if(sale == -1)
            break;
        cout<<"이번달 급여 : "<<CalFunc(sale)<<endl;
    }
    cout<<"프로그램종료"<<endl;

    return 0;
}

```
