## to_string

- **_<string>_** 헤더에 포함됨
- `to_string` 함수는 숫자타입의 데이터를 안전하게 **스트링타입으로** 변경한다.

```cpp
#include <iostream>
#include <string>

using namespace std;

int main ()
{
  int number = 123;
  string str = "Hi, I'm" + to_string(number);

  cout << str << '\n';

  return 0;
}
//Hi, I'm123
```

<br>

## stoi

- **_<string>_** 헤더에 포함됨
- `stoi` 함수는 스트링을 **정수로** 바꾼다.

```cpp
#include <iostream>
#include <string>

using namespace std;

int main ()
{
  string str = "12";
  int num = stoi(str);

  printf("%d\n", num);

  return 0;
}
//12
```

<br>

## substr

- 문자열의 일부분을 문자열로 반환
  - `(시작위치)` : 시작 위치부터 끝까지
  - `(시작위치, 개수)` : 시작 위치부터 개수까지

```cpp
#include <string>
//...
string s = "ABCDEF";
string test = s.substr(3);    //DEF
string test2 = s.substr(1,4);   //BCDE
//...
```
