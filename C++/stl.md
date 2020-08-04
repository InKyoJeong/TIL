## C++ STL, 헤더파일 정리

> PS를 할때 사용하는 stl 정리하는 파일

- [vector](#vector)
- [algorithm](#algorithm)
  - [max_element(), min_element()](#element)
  - [sort()](#sort)
  - [next_permutation, prev_permutation](#permutation)
  <!-- - stable_sort() -->
- [stack](#stack)
- [queue](#queue)
- [deque](#deque)

---

<br>

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
//c       a[0][1]
```

<br>

## algorithm

### <a name="element"></a>max_element(), min_element()

`max_element()`, `min_element()` 함수 : `begin(), end()`를 이용해서 배열이나 벡터 등에서 최대, 최소값을 구할 수 있다. 값을 참조하려면 `*` 연산자를 붙여야 한다.

### 예시

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> v;

    v.push_back(1);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);
    v.push_back(2);

    cout << *min_element(v.begin(), v.end()) << '\n';
    cout << *max_element(v.begin(), v.end()) << '\n';

    return 0;
}
// 1
// 5
```

- 반드시 시작부터 끝까지 찾을 필요는 없다. 만약 `max_element(v.begin()+2, v.begin()+5)`라고 사용했다면 `v[2]`부터 `v[4]`까지 중 최대값을 찾는다.

<br>

#### 문자열도 가능

```cpp
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
    string str = "algorithm";
    cout << *min_element(str.begin(), str.end()) << '\n';
    cout << *max_element(str.begin(), str.end()) << '\n';
    return 0;
}
//a
//t
```

<br>

### <a name="sort"></a>sort()

- `sort()`는 기본적으로 **오름차순으로 정렬**을 해준다.
- 첫 원소의 주소와 마지막 원소의 다음 주소를 인자로 넘겨준다.
  - `sort(arr, arr+n)`
  - `sort(v.begin(), v.end())`
- 비교 함수도 만들어서 같이 넘겨줄 수 있다.
  - `sort(arr1, arr1+n, cmp);`

### 예시 - vector

```cpp
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main (){
    int n;
    cin>>n;
    vector<int> v(n);


    for(int i=0; i<n; i++){
        cin>>v[i];
    }

    sort(v.begin(), v.end());

    cout<<"sort후 결과: ";
    for(int i=0; i<n; i++){
        cout<<v[i]<<' ';
    }

    return 0;
}
//4 (n입력)
//8 9 1 2 (v입력)
//sort후 결과: 1 2 8 9
```

### 예시 - 배열

```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int main (){

    int a[5];
    for(int i=0; i<5; i++){
           cin>>a[i];
    }

    sort(a, a+5);

    cout<<"sort후 결과: ";
    for(int i=0; i<5; i++){
        cout<<a[i]<<' ';
    }
    return 0;
}
//9 8 7 2 1
//sort후 결과: 1 2 7 8 9
```

#### 비교함수 예시

```cpp
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool cmp(const int a, const int b){
    return a>b;
}

int main (){
    int n;
    cin>>n;
    vector<int> v(n);


    for(int i=0; i<n; i++){
        cin>>v[i];
    }

    sort(v.begin(), v.end(), cmp);

    cout<<"sort후 결과: ";
    for(int i=0; i<n; i++){
        cout<<v[i]<<' ';
    }

    return 0;
}
//4
//8 9 1 2
//sort후 결과: 9 8 2 1 (내림차순)
```

<!-- <br>

### stable_sort()

- `sort`와 사용법은 같지만 다른점은 **정렬하는 원소값이 같은 경우**이다.
- 원소가 같은경우 `sort`는 랜덤, `stable_sort`는 순서를 보존함 -->
<br>

### <a name="permutation"></a>next_permutation, prev_permutation

- 순열을 생성해 주는 함수. algorithm 헤더 파일에 정의되어 있다.
- `next_permutation` 은 오름차순으로 순열을 생성해 주고,
- `perv_permutation` 은 내림차순으로 순열을 생성해 준다.

```cpp
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){

    vector<int> v;

    for(int i=0 ; i<3 ; i++){
        v.push_back(i);
    }

    do{
        for(int i=0 ; i<(int)v.size() ; i++){
            cout<<v[i]<<" ";
        }
        cout<<'\n';
    }while(next_permutation(v.begin(),v.end()));

    return 0;
}

// 0 1 2
// 0 2 1
// 1 0 2
// 1 2 0
// 2 0 1
// 2 1 0
```

<br>

## stack

> 스택 자료구조

- `stack<int> s;` : int 자료형을 저장하는 스택 s 생성

- `push(element);` : top에 원소(element) 삽입

- `pop();` : top에 있는 원소 삭제

- `top();` top에 있는 원소 반환

- `empty();` : 스택이 비어있으면 **true(1)** 아니면 **false(0)** 반환

- `size();` : 스택 사이즈 반환(저장된 원소의 수)

<br>

### 예시

```cpp
#include <iostream>
#include <stack>

using namespace std;

int main()
{

    // 스택 생성
    stack<int> s;

    // 33, 22, 11 순서로 push
    s.push(33);
    s.push(22);
    s.push(11);

    cout<< s.top() <<'\n';      //top은 마지막에넣은 11

    s.pop();    //top원소 한개 빼냄
    s.pop();    //top원소 한개 빼냄

    cout<< s.top() <<'\n';      //top은 이제 33

    cout<< s.size() <<'\n';     //원소 한개남았으므로 size는 1

    return 0;
}
```

<br>

## queue

> 큐 자료구조

- `push(element)` : 큐에 원소(element)를 (뒤에)추가

- `pop()` : 큐에 있는 원소를 삭제(앞에)

- `front()` : 큐 제일 앞의 원소 반환

- `back()` : 큐 제일 뒤의 원소 반환

- `empty()` : 큐가 비어있으면 **true(1)**, 비어있지않으면 **false(0)** 반환

- `size()` : 큐 사이즈를 반환

<br>

### 예시

```cpp
#include <iostream>
#include <queue>

using namespace std;

int main()
{
    //큐 생성
    queue<int> q;

    //7,5,99 순서로 push
    q.push(7);
    q.push(5);
    q.push(99);

    cout << q.front() <<'\n';       //제일앞 원소는 7 (처음에 넣은)
    cout << q.back() <<'\n';        //제일뒤 원소는 99 (마지막에 넣은)

    q.pop();
    q.pop();
    q.pop();

    cout<< q.size() <<'\n';         //모두빼냈으므로 0

    cout<< "Is Queue Empty? "<< (q.empty() ? "Yes" : "No") <<'\n';
    //큐가 비었으므로 Yes

    return 0;
}
```

<br>

## deque

> 양쪽끝에서만 자료를 넣고 양 끝에서 뺄 수 있는 자료구조. vector 컨테이너와 기능과 동작이 비슷한 컨테이너로, vector의 단점을 보완

```cpp
#include <iostream>
#include <deque>

using namespace std;

int main()
{
    //int자료형 저장하는 동적배열 생성
    deque<int> dq;

    //배열 맨 앞에 원소(5)추가
    dq.push_front(5);

    //배열 맨 뒤에 원소(8)추가
    dq.push_back(8);

    //배열 맨 앞의 원소 삭제
    dq.pop_front();

    //배열 맨 뒤의 원소 삭제
    dq.pop_back();

    return 0;
}
```
