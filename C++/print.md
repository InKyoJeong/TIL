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
