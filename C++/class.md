## 클래스

- 클래스는 정의하는 과정에서 각각 변수 및 함수의 접근 허용범위를 별도로 선언해야함
- 접근제어 지시자
  - public : 어디서든 접근허용
  - protected : 상속관계에 놓였을때, 유도클래스에서의 접근허용
  - private : 클래스 내(클래스 내에 정의된 함수)에서만 접근허용

### 좋은 클래스 조건 : 정보은닉

- 멤버변수를 private로 선언하고 해당변수에 접근하는 함수를 별도로 정의, 안정한 형태로 멤버변수의 접근을 유도하는 것

### const

이 함수 내에서는 멤버변수에 저장된 값을 변경하지 않음

```cpp
class SimpleClass
{
  private:
    int num;

  public:
    void InitNum(int n)
    {
      num = 0;
    }
    int GetNum()            //const 선언이 추가돼야 에러 소멸
    {
      return num;
    }
    void ShowNum() const
    {
      cout<<GetNum()<<endl;   //에러 발생
    }
}
```

- **_ShowNum()_** 함수는 `const`함수로 선언되었지만 에러가 발생함
- `const`함수 내에서는 `const`가 아닌 함수의 호출이 제한됨

### 좋은 클래스 조건 : 캡슐화

- 관련있는 함수와 변수를 하나의 클래스안에 묶는것

### 생성자(Constructor)

```cpp
class SimpleClass
{
  private:
    int num;
  public:
    SimpleClass(int n)    //생성자(Constructor)
    {
      num = n;
    }
    int GetNum() const
    {
      return num;
    }
};
```

- 클래스의 이름과 함수이름이 동일
- 반환형이 선언되어있지 않고, 실제로 반환하지 않음
- 객체 생성시 딱 한번 호출됨

```cpp
#include <iostream>
using namespace std;

class SimpleClass
{
private:
    int num1;
    int num2;
public:
    SimpleClass()
    {
        num1 = 0;
        num2 = 0;
    }
    SimpleClass(int n)
    {
        num1 = n;
        num2 = 0;
    }
    SimpleClass(int n1, int n2)
    {
        num1 = n1;
        num2 = n2;
    }
    void ShowData() const
    {
        cout<<num1<<' '<<num2<<endl;
    }
};

int main(void)
{
    SimpleClass sc1;
    sc1.ShowData();

    SimpleClass sc2(100);
    sc2.ShowData();

    SimpleClass sc3(100, 200);
    sc3.ShowData();

    return 0;
}

//0 0
//100 0
//100 200
```

- 생성자도 함수의 일종이니 오버로딩이 가능
- 매개변수에 디폴트값 설정 가능
