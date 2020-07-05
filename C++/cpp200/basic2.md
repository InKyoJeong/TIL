> 문자열, 명시적변환, 순환문, floor/ceil, abs/pow/sqrt, static_cast, 문자열함수

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
#include <random>
#include <algorithm>
#include <ctime>

using namespace std;

int main()
{
    string str1 = "1a2b3c4d5e6f7g8h9i";
    string str2 = "republick of korea";
    int data1[10] = {1,2,3,4,5,6,7,8,9,10};

    srand(static_cast<unsigned int>(time(NULL)));

    random_shuffle(str1.begin(), str1.end());
    random_shuffle(str2.begin(), str2.end());
    random_shuffle(data1, data1 + 4);


    cout<<"str1 :"<<endl;
    for(auto i : str1)
        cout<<i<<", ";

    cout<<endl<<"str2 :"<<endl;
    for(auto i : str2)
        cout<<i<<", ";

    cout<<endl<<"data1 :"<<endl;
    for(auto i : data1)
        cout<<i<<", ";

    return 0;
}
```

```
str1 :
8, g, i, 5, c, h, 2, 6, a, b, 7, f, 9, 1, d, e, 4, 3,

str2 :
o, o, u, k, f, e, a, r, k, l,  , e, c,  , p, r, b, i,

data1 :
3, 4, 1, 2, 5, 6, 7, 8, 9, 10,
```

- string의 `begin`은 첫위치, `end`는 마지막위치를 나타냄
- `data1+4`는 data1의 인덱스 0~3까지 무작위 재배치를 나타냄

<br>

## 문자열 비교하기 (string.compare)

```cpp
#include <iostream>
using namespace std;

int main()
{
    string seven_war = "임진왜란";
    string korea_war = "한국전쟁";

    if(seven_war.compare(korea_war) == 0)
        cout<<"같은 문자열입니다."<<'\n';
    else
        cout<<"다른 문자열입니다."<<'\n';

    return 0;
}


// 다른 문자열입니다.
```

- `compare`함수는 서로같으면 0, 다르면 -1이 리턴된다.

<br>

## 문자열 조회(find)

```cpp
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string something = "가나다라마바사 아자";
    int rtn = something.find("아자");

    if(rtn > 0)
        cout<<"문자열을 찾았습니다. 위치는 "<<rtn<<"입니다."<<endl;
    else
        cout<<"문자열을 찾을 수 없습니다."<<endl;
    return 0;
}

// 문자열을 찾았습니다. 위치는 22입니다.
```

<br>

## 문자열 길이 구하기(length)

```cpp
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string kor_name = "김태연";
    string eng_name = "taeyeon";

    cout<<"한국이름 길이: "<<kor_name.length()<<endl;
    cout<<"영어이름 길이: "<<eng_name.length()<<endl;
    return 0;
}

//한국이름 길이: 6
//영어이름 길이: 7
```

<br>

## 문자 대소문자 변환하기 (toupper, tolower)

```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    string ty = "taeyeon";
    char lower_ch = 'g';
    char upper_ch = 'A';

    lower_ch = toupper(lower_ch);
    upper_ch = tolower(upper_ch);

    cout<<lower_ch<<endl;
    cout<<upper_ch<<endl;

    return 0;
}

//G
//a
```

<br>

## 문자열 합치기

```cpp
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string last = "김";
    string first = "태연";

    string info = "";

    info += last;
    info += first;
    info.append("은 ");
    info.append("가수입니다.");

    cout<<info<<endl;

    return 0;
}

//김태연은 가수입니다.
```

- 문자열을 합치려면 C에서는 char배열, strcat, 메모리 재할당을 이용하지만 C++에서는 `+`연산자로 쉽게 합칠 수 있다.

- `append()`는 추가한다는 의미로 `+=`와 같은 의미다.

<br>

## 문자열 중간에 삽입하기 (insert)

```cpp
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string sentence = "I conding";
    sentence.insert(2, "like ");
    cout <<sentence<<endl;

    return 0;
}
//I like conding
```

<br>

## 문자열 일부 지우기(erase)

```cpp
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string sentence = "i like coding";

    sentence.erase(0, 7);

    cout<<sentence<<endl;

    return 0;
}
//coding
```

<br>

## 문자열 이동하기(move)

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    string str1 = "i like coding";
    string str2 = move(str1);

    cout<<"str1: "<<str1<<endl;
    cout<<"str2: "<<str2<<endl;

    vector<int> v1 = {1,2,3,};
    vector<int> v2 = move(v1);

    cout<<"v1 size: "<<v1.size()<<endl;
    cout<<"v2 size: "<<v2.size()<<endl;

    return 0;
}

//str1:
//str2: i like coding
//v1 size: 0
//v2 size: 3
```

<br>

## 특정 문자만 제거하기(erase, remove)

```cpp
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string sentence = "i like coding";

    sentence.erase(remove(sentence.begin(), sentence.end(), ' '), sentence.end());

    cout<<sentence<<endl;

    return 0;
}

//ilikecoding
```

- 특정 문자만 제거할때는 `erase`와 `remove`를 함께사용

<br>

## 문자열 일부 교체하기 (replace)

```cpp
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string sentence = "i like coding";
    string find_str = "coding";
    string replace_str = "soccer";

    sentence.replace(sentence.find(find_str), find_str.length(), replace_str);

    cout<<sentence<<endl;

    return 0;
}
//i like soccer
```

<br>

## 문자열을 정수로 변환 (stoi)

```cpp
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string str1 = "10";
    string str2 = "2.345";
    string str3 = "789 가나다";

    int num1 = stoi(str1);
    int num2 = stoi(str2);
    int num3 = stoi(str3);

    cout<<num1<<endl;
    cout<<num2<<endl;
    cout<<num3<<endl;
    return 0;
}

//10
//2
//789
```

### 문자열을 숫자로 변환 (stringsteam)

```cpp
#include <iostream>
#include <sstream>

using namespace std;

int main()
{
    stringstream ss;

    double number1 = 0.0;

    ss<<"1.2,3.4-4.2!2.6=9.9";

    cout<<"string to double"<<endl;

    while(!ss.eof())
    {
        ss>>number1;
        ss.ignore();

        cout<<number1<<", ";
    }
    return 0;
}
//string to double
//1.2, 3.4, 4.2, 2.6, 9.9,
```

- stringstream을 include하고 변수를 선언한다.
- stringstream변수에 실수와 특수문자로된 문자열을 추가한다.
- while문은 stringstream을 다 읽지않았으면 반복한다.
- `ignore()`은 첫 데이터를 계속읽는 것을 막고 다음데이터를 읽을수 있게한다.

<br>

## 문자열 정렬하기(sort)

```cpp
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string str1 = "taeyeon";
    string str2 = "AaBbCcDdEe";

    sort(str1.begin(), str1.end());
    sort(str2.begin(), str2.end());

    cout<<str1<<endl;
    cout<<str2<<endl;

    return 0;
}

//aeenoty
//ABCDEabcde
```

- 문자열을 알파벳 순서에따라 정렬
- 대소문자가 섞여있으면 대문자가 앞으로

<br>

## 문자열 뒤집기(reverse)

```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    string str = "noeyeat";

    reverse(str.begin(), str.end());

    cout<<str<<endl;

    return 0;
}

//taeyeon
```

- `reverse`함수가 정의된 `algorithm`을 include

<br>

## 숫자를 문자열로 변환(to_string)

```cpp
#include <iostream>
#include <string>

using namespace std;

int main()
{
    int num1 = 10;
    double num2 = 34.65;

    string no_str1 = to_string(num1);
    string no_str2 = to_string(num2);

    cout<<"num1: "<<num1<<endl;
    cout<<"num2: "<<num2<<endl;

    return 0;
}

//num1: 10
//num2: 34.65
```

<br>

## 정수와 문자의 최대/최소값 (min, max)

```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    auto result1 = min(1,5);
    auto result2 = max('a', 'z');

    cout<<result1<<endl;
    cout<<result2<<endl;

    auto result3 = minmax({'a', 'n', 'z'});
    auto result4 = minmax({1,2,3});

    cout<<result3.first<<", "<<result3.second<<endl;
    cout<<result4.first<<", "<<result4.second<<endl;
    return 0;
}

//1
//z
//a, z
//1, 3
```

- 자료형 `auto`는 반환형이 무엇인지 모를때 유용한 키워드
- `max`함수에 a와 z를 넘기고, 아스키 코드 값을 기준으로 반환됨(a=97, z=122)
- `auto`키워드로 받은 결과의 `first`는 최소, `second`는 최대값

<br>

## 포인터

```cpp
#include <iostream>

using namespace std;

int main()
{
    int num1 = 10;
    int *pointer1 = &num1;

    double num2 = 23.4;
    double *pointer2 = &num2;

    cout<<"num1: "<<num1<<endl;
    cout<<"pointer1: "<<pointer1<<endl;

    cout<<"num2: "<<num2<<endl;
    cout<<"pointer2: "<<pointer2<<endl;
    return 0;
}
//num1: 10
//pointer1: 0x7ffeefbff588
//num2: 23.4
//pointer2: 0x7ffeefbff578
```
