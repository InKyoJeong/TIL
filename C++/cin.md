> cin, cin.get, cin.getline, getline, cin.ignore()

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

### cin.ignore()

> cin과 getline을 같이 사용할때 cin.ignore()이 필요한 이유

- `cin`은 '\n'를 변수에 담지 않는다. (입력버퍼에 남겨둔다)
- `getline`은 '\n'를 변수에 담는다.

```cpp
#include <iostream>
using namespace std;
int main(void)
{
    string s1,s2;

    cin >> s1;
    cout << s1 << endl;

    getline(cin,s2);
    cout << s2 << endl;


    return 0;
}
//aa (입력)
//aa (출력)
```

이렇게하면 s1만 출력되고 종료됨

```cpp
#include <iostream>
using namespace std;
int main(void)
{
    string s1,s2;

    cin >> s1;
    cout << s1 << endl;

    cin.ignore();

    getline(cin,s2);
    cout << s2 << endl;


    return 0;
}
//aa (입력)
//aa (출력)
//bbbb (입력)
//bbbb (출력)
```

- `cin.ignore();`는 버퍼 전체를 비우는것이 아니라 맨 앞의 문자하나를 지운다

- `getline(읽어올 입력스트림, 저장할 문자열변수)`

```cpp
#include <iostream>
using namespace std;
int main(void)
{
    string s;

    for(int i=0;i<3;i++)
    {
        cin.ignore();
        getline(cin,s);
        cout << s << endl;
    }
    return 0;
}
//abcd  (입력)
//bcd   (출력)
//abcd  (입력)
//bcd   (출력)
//poooo (입력)
//oooo  (출력)
```
