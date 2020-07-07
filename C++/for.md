## 범위 기반 for 문 (range-based for statement)

배열 등의 모든 요소를 반복한다.

```cpp
for (element_declaration : array)
    statement;
```

루프는 각 `array`의 요소를 반복하여 `element_declaration`에 선언된 변수에 현재 배열 요소의 값을 할당한다. 최상의 결과를 얻으려면 `element_declaration`이 배열 요소와 같은 자료형이어야 한다. 그렇지 않으면 형 변환이 발생한다.

```cpp
for (char ch : str) {
}
```

위는 아래와 같음

```cpp
for (int i=0; i<str.length(); i++) {
    char ch = str[i];
}
```

#### 범위 기반 for 문을 사용해서 fibonacci 배열의 모든 요소를 출력하는 예제

```cpp
#include <iostream>
using namespace std;
int main()
{
    int fibonacci[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 };
    for (int number : fibonacci)
       cout << number << ' ';
    return 0;
}

// 0 1 1 2 3 5 8 13 21 34 55 89
```
