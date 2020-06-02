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
