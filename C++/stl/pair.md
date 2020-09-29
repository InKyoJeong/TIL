## pair

- 이름이 `first`, `second`인 두 개의 변수를 저장할 수 있는 struct
- `#include <utility>` 헤더 파일에 존재하는 STL
- 하지만, `algorithm`, `vector` 같은 헤더파일에서 이미 include하고 있기에 따로 utility를 include해 줄 필요는 없음
- 비교 연산시 1순위 **_first_** 2순위 **_second_** 로 판별함

```cpp
#include <iostream>
#include <utility>

using namespace std;

pair<int, char> p;

int main()
{
    p.first = 1;
    p.second = 'a';

    cout<< p.first << p.second <<'\n';
    return 0;
}
// 1a
```

<br>

- `make_pair` : pair를 만들어 주는 함수
  - `p = make_pair(x, y);`로 대입 가능

```cpp
#include <iostream>
#include <utility>

using namespace std;

pair<int, char> p;

int main()
{
    p = make_pair(2, 'b');

    cout<< p.first << p.second <<'\n';
    return 0;
}
// 2b
```

<br>

- `vector`에 넣을 때는 vector의 형식은 `vector<pair<int, char>>` 같은 형식

```cpp
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

vector<pair<int, char>> vc;

int main()
{
    vc.push_back(make_pair(3, 'c'));

    cout<< vc[0].first << vc[0].second <<'\n';
    return 0;
}

// 3c
```

```cpp
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

vector<pair<int, int>> e;

int main()
{
    e.push_back({0,1});
    e.push_back({1,2});
    e.push_back({2,3});

    cout<< e[0].first <<" "<< e[0].second <<'\n';
    cout<< e[1].first <<" "<< e[1].second <<'\n';
    cout<< e[2].first <<" "<< e[2].second <<'\n';

    return 0;
}

// 0 1
// 1 2
// 2 3
```
