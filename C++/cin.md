> cin, cin.get, cin.getline, getline

## cin

- cin은 공백, 개행을 무시.

```cpp
#include <iostream>
using namespace std;
int main(){
    char str1[100];
    cin>>str1;

    cout<<str1<<endl;

    return 0;
}
// abc def (입력)
// abc (결과)
```

<br>

## cin.get()

- cin.get()은 공백,개행을 포함
- 문자만 입력받음

```cpp
#include <iostream>
using namespace std;
int main(){
    char a,b,c;
    a = cin.get();
    b = cin.get();
    c = cin.get();

    cout<< "a :"<< a << '\n';
    cout<< "b :"<< b << '\n';
    cout<< "c :"<< c << '\n';

    return 0;
}
// p         (p입력후 엔터입력 o입력)
// o

// a :p      (결과)
// b :
//
// c :o
```

<br>

## getline()

- `std::getline()` 은 `<string>`에 정의되어있음
- `string`형에 문자열을 저장할때 사용
- 두번째 매개변수는 문자열을 저장할 string형 변수명,
- 세번째 매개변수는 어떤문자까지 입력받을지 결정. 디폴트는 개행

```cpp
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string a;

    getline(cin, a);  // getline(cin, a, '\n')과 같음

    cout<<a<<'\n';
    return 0;
}
// ii ooo pppp (입력)
// ii ooo pppp (결과)
```

<br>

## cin.getline()

- 첫번째 매개변수는 문자열을 저장할 `char`배열명, 두번째 매개변수는 저장할 문자 최대개수

```cpp
#include <iostream>
#include <string>
using namespace std;
int main()
{
    char s[100];
    cin.getline(s, 5);

    cout<<s<<'\n';
    return 0;
}

// a bcdefg (입력)
// a bc (결과)
// 배열 마지막값에는 null문자가 들어가있으므로 'a bcd'가 아니라 'a bc'가출력됨
```
