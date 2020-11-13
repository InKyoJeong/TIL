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

<br>

## priority_queue

> 우선순위큐

- 기본 생성자 형식 `priority_queue< [Data Type] > [변수이름];`
  - ex) `priority_queue<int> pq;`
- 정렬 기준 변경하면
  - `priority_queue< [Data Type], [Container Type], [정렬기준] > [변수이름];`

```cpp
#include <cstdio>
#include <queue>
using namespace std;

priority_queue<int> pq;
//priority_queue<int , vector<int>, less<int>> pq; 와 동일

int main(){
    pq.push(3);
    pq.push(2);
    pq.push(1);
    pq.push(7);
    pq.push(3);
    pq.push(9);
    while (!pq.empty()) {
        printf("%d ",pq.top());
        pq.pop();
    }
}
// 9 7 3 3 2 1
```

`priority_queue<int , vector<int>, greater<int>> pq;` 이면
// 1 2 3 3 7 9
