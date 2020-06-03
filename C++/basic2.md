> bool, 참조자(reference)

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
