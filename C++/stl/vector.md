## vector

> vector 컨테이너는 자동으로 메모리가 할당되는 배열이다. 스택과 비슷하다.

### vector 사용

- 헤더파일 : `<vector>`
- 선언 : `vector<[data type]> [변수이름]`
  - ex) `vector<int> x;`

```cpp
#include <iostream>
#include <vector>

int main()
{
    //int 자료형을 저장하는 동적배열
	vector<int> v;

    //벡터의 초기 크기를 n으로 설정
    vector<int> v(n);

    //벡터의 초기 크기를 n으로 설정하고 1로 초기화
	vector<int> v(n, 1);

    //벡터의 맨 뒤에 원소(5) 추가
	v.push_back(5);

    //벡터의 맨 뒤 원소 삭제
	vec1.pop_back();

    //벡터의 크기 출력(원소의 개수)
    v.size();

    //벡터의 크기를 n으로 재설정
    v.resize(n);

    //벡터의 모든 원소 삭제
    v.clear();

    //벡터의 첫원소의 주소 리턴
    v.begin();

    //벡터의 마지막 원소의 '다음' 주소 리턴
    v.end();

    return 0;
}
```

- 예시 1

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main(){

    vector<int> v;

    v.push_back(5);
    v.push_back(11);
    v.push_back(99);

    v.pop_back();

    for(int i=0; i<v.size(); i++)
        cout<< v[i] <<'\n';

    return 0;
}
//5
//11
```

<br>

- 예시 2

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main()
{
int n;
cin>>n;
vector<int> a(n);

    for(int i=0; i<n; i++){
        cin>> a[i];
    }

    for(int i=0; i<n; i++){
        cout<< a[i];
    }

    return 0;

}
//4 (입력)
//6 7 8 9 (입력)
//6789 (출력)

```

<br>

- 예시 3

```cpp
#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<string> a(n);
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }

    for (int i=0; i<n; i++) {
        cout<< a[i][0]<<'\n';
    }
    return 0;
}
//2       (n 입력)
//abbb    (a[0] 입력)
//cbbb    (a[1] 입력)
//a       a[0][0]
//c       a[1][0]
```

<br>

- `vector<자료형> 변수명 = { 변수1, 변수2, 변수3... }`
  - 백터 생성 후 오른쪽 변수 값으로 초기화

```cpp
#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<int>v = { 7, 8, 9};

    cout<<v[0]<<'\n';   //7
    cout<<v[1]<<'\n';   //8
    cout<<v[2]<<'\n';   //9

    return 0;
}
```

<br>

### 이차원 vector

- 사용 예시

```cpp
#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<vector<int>> Vec2D;

    vector<int> v1;
    v1.push_back(11);
    v1.push_back(22);
    v1.push_back(33);
    Vec2D.push_back(v1);

    cout<< "Vec2D[0].size() : "<< Vec2D[0].size() <<'\n';


    vector<int> v2;
    for(int i=0; i<5; i++){
        v2.push_back(i);
    }
    Vec2D.push_back(v2);

    cout<< "Vec2D[1].size() : "<< Vec2D[1].size() <<'\n';

     cout<< "Vec2D.size() : "<< Vec2D.size() <<'\n';

    for(int i=0; i<Vec2D.size(); i++){
        cout<< "Vec2D["<< i << "] : ";
        for(int j=0; j<Vec2D[i].size(); j++){
            cout<< Vec2D[i][j] << " ";
        }
        cout<<'\n';
    }
    return 0;
}
//Vec2D[0].size() : 3
//Vec2D[1].size() : 5
//Vec2D.size() : 2

//Vec2D[0] : 11 22 33
//Vec2D[1] : 0 1 2 3 4
```
