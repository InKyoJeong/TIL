> 문자열, 명시적변환, 순환문, floor/ceil, abs/pow/sqrt, static_cast

## 문자형 변수(char)

- `char`의 범위는 **-127 ~ +127** 이다.
- `unsigned` 키워드를 붙일 경우 범위는 **0 ~ +255** 이다.
- 아스키코드 : 컴퓨터 문자 값
  - 아스키코드 숫자는 **48~57** 이다.
  - 아스키코드 대문자는 **65~90** 이다.
  - 아스키코드 소문자는 **97~122** 이다.

```cpp
#include <iostream>

using namespace std;

int main()
{
    char ch1 = 'c';
    char ch2 = 200;

    unsigned char ch3 = 'c';
    unsigned char ch4 = 200;

    printf("char ch1 = %c, %d\n", ch1, ch1);
    printf("char ch2 = %c, %d\n", ch2, ch2);
    printf("char ch3 = %c, %d\n", ch3, ch3);
    printf("char ch4 = %c, %d\n", ch4, ch4);

    return 0;
}
```

```
char ch1 = c, 99
char ch2 = ?, -56
char ch3 = c, 99
char ch4 = ?, 200
```

- ch2에서 200은 char변수 범위를 초과하고, 보수를 취한다. 128 - 200 = -72 이므로 최소범위 -127에서 72가 증가한 -56이 출력된다.

- ch4에서 unsigned char 범위에 속하는 200은 출력되고, 200에 해당하는 아스키값은 없어서 물음표가 출력된다.

<br>

### 문자열형 변수(string)

```cpp
#include <string>
#include <iostream>

using namespace std;

int main()
{
    string my_country = "korea";
    string my_job = "student";

    cout<<"Country : "<<my_country<<endl;
    cout<<"Job : "<<my_job<<endl;

    string my_info = my_country + ", " + my_job;

    cout<<"My Info : "<<my_info<<endl;

    return 0;
}
```

```
Country : korea
Job : student
My Info : korea, student
```

c에서는 문자열을 사용하기위해 `char []`을 사용하지만 c++에서는 `string`을 이용할 수 있다.

<br>

## 명시적 변환()

```cpp
#include <iostream>

using namespace std;

int main()
{
    int number1 = 65;
    double number2 = 23.5;

    int number3 = int(number2);
    double number4 = double(number1 / number2);

    char ch = char(number1);

    cout<<"number1 : "<<number1<<endl;
    cout<<"number2 : "<<number2<<endl;
    cout<<"number3 : "<<number3<<endl;
    cout<<"number1 : "<<number1<<endl;
    cout<<"ch : "<<ch<<endl;

    return 0;
}
```

```
number1 : 65
number2 : 23.5
number3 : 23
number4 : 2.76596
ch : A
```

<br>

## 중첩 순환문 (for~continue~break)

> 3의배수 빼고 출력하기

```cpp
#include <iostream>
using namespace std;
int main()
{
    int num=7;
    for(int i=0; i<10; i++)
    {
        if(i%3 ==0)
            continue;
        else if(i ==num)
            break;
        else
            cout<<i<<endl;
    }
    return 0;
}
```

```
1
2
4
5
```

<br>

### 순환문으로 특정문자 개수 구하기(for)

```cpp
#include <iostream>
#include <string>

using namespace std;
int main()
{
    string str = "The J State was formed in korea by the 3rd century BC";

    char find = 'a';

    int size = str.size();
    int count = 0;

    for(int i=0; i<size; i++)
    {
        if(str[i] == find)
            count ++;
    }
    cout<<"a의 개수는: "<<count<<"개"<<endl;

    return 0;
}
```

```
a의 개수는: 3개
```

<br>

### 순환문으로 홀수,짝수 찾기(for)

```cpp
#include <iostream>
using namespace std;

int main()
{
    int data[10] = {5, 19, 55, 76, 22, 19, 4, 16, 88, 43};

    for(int i=0; i<10; i++)
    {
        if(data[i] % 2 ==0)
            cout<<i<<":"<<data[i]<<"는 짝수"<<endl;
        else
            cout<<i<<":"<<data[i]<<"는 홀수"<<endl;
    }
    return 0;
}
```

```
0:5는 홀수
1:19는 홀수
2:55는 홀수
3:76는 짝수
4:22는 짝수
5:19는 홀수
6:4는 짝수
7:16는 짝수
8:88는 짝수
9:43는 홀수
```

<br>

## 실수 소수점 버리기 올리기(floor, ceil)

```cpp
#include <iostream>
using namespace std;

int main()
{
    cout<<"소수점 버리기"<<endl;
    cout<<"floor(1.1):"<<floor(1.1)<<endl;
    cout<<"floor(44.7):"<<floor(44.7)<<endl;

    cout<<"소수점 올리기"<<endl;
    cout<<"ceil(1.1):"<<ceil(1.1)<<endl;
    cout<<"ceil(44.7):"<<ceil(44.7)<<endl;

    return 0;
}
```

<br>

## 절댓값, 제곱수 구하기(abs, pow), 제곱근(sqrt)

```cpp
#include <iostream>
// #include <math.h>
using namespace std;

int main()
{
    cout<<"-101의 절대값: "<<abs(-101)<<endl;
    cout<<"-5.61의 절대값: "<<fabs(-5.61)<<endl;
    cout<<"2의 4승: "<<pow(2,4)<<endl;

    cout<<"16의 제곱근: "<<sqrt(16)<<endl;
    return 0;
}
```

```
-101의 절대값: 101
-5.61의 절대값: 5.61
2의 4승: 16
16의 제곱근: 4
```

<br>

## 나머지 구하기 (static_cast)

```cpp
#include <iostream>

using namespace std;

int main()
{
    double x = 5.7;
    int div1 = static_cast<int>(x / 5);
    double mod1 = x - 5 * static_cast<int>(x / 5);

    cout<<"5.7 / 5 = 몫: "<<div1<<", 나머지: "<<mod1<<endl;
    return 0;
}
```

```
5.7 / 5 = 몫: 1, 나머지: 0.7
```

<br>

## 난수 생성(srand, rand)

```cpp
#include <iostream>
#include <ctime>

using namespace std;

int main()
{
    srand(static_cast<unsigned int>(time(NULL)));

    for(int i=0; i<5; i++)
        cout<<"난수: "<<rand()<<endl;

    return 0;
}
```

- 난수를 구할때는 씨앗(seed)라 불리는 "어떤 값"이 필요한데 보통 시스템시간 이용
- `rand`함수를 이용해서 임의값을 얻으며 범위는 `0~32767`
- `rand`함수는`srand`함수를 통해 변경된 씨앗값을 이용해 무작위로 값 생성

```
// c++11에서 제공하는 난수엔진 템플릿
random_device
linear_congruential_engine
mersenne_twister_engine
subtract_with_carry_engine
```

<br>

## 무작위로 문자열과 배열섞기 (random_shuffle)

```cpp
#include <iostream>
#include
```
