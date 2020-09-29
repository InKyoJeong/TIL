## algorithm

- algorithm
  - [max_element(), min_element()](#element)
  - [minmax_element()](#minmax)
  - [sort()](#sort)
  - [next_permutation, prev_permutation](#permutation)
  <!-- - stable_sort() -->

<br>

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

### <a name="minmax"></a>minmax_element()

- `minmax_element` 함수는 최대와 최소값을 동시에 구할 수 있다.

```cpp
#include <iostream>
#include <algorithm>    // std::minmax_element
#include <vector>
using namespace std;

int main () {
    vector<int> v;
    v.push_back(1);
    v.push_back(9);
    v.push_back(3);
    v.push_back(7);

    auto result = minmax_element(v.begin(), v.end());

    cout << "최소 값: " << *result.first;
    cout<<'\n';
    cout << "최대 값: " << *result.second;
    cout<<'\n';

    return 0;
}
//최소 값: 1
//최대 값: 9
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
- 모든 경우에 대해서 정렬을 할 필요가 있을 경우에는 원본 container를 미리 `sort` 해 둘 필요가 있다.

### 예시

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

### 예시 2

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int n;
    cin>>n;

    vector<int> d(n);
    for (int i=0; i<n; i++) {
        d[i] = i;
    }

    if(next_permutation(d.begin(), d.end())){
        for (int i=0; i<n; i++) {
            cout<<d[i]<<' ';
        }
    };
    return 0;
}

// 4            (d크기 입력)
// 0 1 3 2      (출력 : 0 1 2 3의 다음순열 출력됨!)
```

<br>

### 직접 구현

```cpp
// 다음순열
// a[i-1] < a[i] 인 가장 큰 i를 찾는다
// j>=i 면서 a[j] > a[i-1]를 만족하는 가장 큰 j를 찾는다
// a[i-1]과 a[j]를 swap한다
// a[i]부터 순열을 뒤집는다

#include <iostream>
#include <vector>

using namespace std;

void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

bool next_permutation(vector<int> &a, int n){
    int i = n-1;
    while(i > 0 && a[i-1] >= a[i]){         // a[i-1] < a[i] 인 가장 큰 i를 찾는다
         i -= 1;                            // a[i-1]이 더 크면 계속 i를 왼쪽으로
    }
    if(i <= 0){
        return false;       // 제일끝까지 왼쪽으로 가면, 다음순열이 없음. 마지막 순열
    }
    int j = n-1;            //j>=i 면서 a[j] > a[i-1]를 만족하는 가장 큰 j를 찾는다
    while(a[j] <= a[i-1]){
        j -= 1;
    }
    swap(a[i-1], a[j]);     //a[i-1]과 a[j]를 swap한다

    // a[i]부터 순열을 뒤집는다
    j = n-1;
    while(i < j){
        swap(a[i], a[j]);
        i += 1;
        j -= 1;
    }
    return true;
}

int main(){
    int n;
    cin>>n;
    vector<int> a(n);
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    if(next_permutation(a, n)){
        for(int i=0; i<n; i++){
            cout<<a[i]<<" ";
        }
    }else{
        cout<<"-1";
    }
    cout<<'\n';
    return 0;
}

// 4 (n크기 입력)
// 1 2 3 4 (배열 입력)
// 1 2 4 3 (다음순열 출력)
```
