## Contents

[선택 정렬 알고리즘](#선택-정렬-알고리즘)<br/>
[삽입 정렬 알고리즘](#삽입-정렬-알고리즘)<br/>
[버블 정렬 알고리즘](#버블-정렬-알고리즘)<br/>

<br>

## 선택 정렬 알고리즘

> 데이터의 처음부터 끝까지 훑으면서 가장 작은 값을 찾아 첫번째 데이터와 자리를 바꾸고, 두번째로 작은 값을 찾아 두번째의 데이터와 자리를 바꾸며 구현하는 알고리즘

```cpp
#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int a[100];
    int index, temp;

    for(int i=0; i<n; i++){
           cin >> a[i];
    }

    for(int i=0; i<n-1; i++){
        index = i;
        for(int j=i+1; j<n; j++){
            if(a[j] < a[index]){
                index = j;
            }
        }

        temp = a[i];
        a[i] = a[index];
        a[index] = temp;
    }
    for(int i=0; i<n; i++){
        cout << a[i] <<' ';
    }
    return 0;
}
```

```bash
# 입력
7
13 5 11 7 23 15
# 출력
5 7 11 13 15 23
```

### 분석

- 2개의 반복문으로 **N²/2**회 비교한다. 선택정렬 알고리즘은 실제 정렬에 사용되는 데이터의 수가 많은 경우 유용하다.
- 시간복잡도 : `O(n²)`

<br>

## 삽입 정렬 알고리즘

> 삽입 정렬 알고리즘은 데이터를 순차적으로 정렬하면서 현재 값을 정렬되어있는 값들과 비교해 적합한 위치로 삽입하는 방식이다.

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int a[100];
    int i, j, temp;
    for(int i=0; i<n; i++) {
        cin >> a[i];
    }

    for(i=1; i<n; i++){
        temp = a[i];
        for(j=i-1; j>=0; j--){
            if(a[j] > temp){
                a[j+1] = a[j];
            }else{
                break;
            }

        }
        a[j+1] = temp;
    }

    for(i=0; i<n; i++){
        cout << a[i] <<" ";
    }

    return 0;
}
```

```bash
# 입력
6
11 7 5 6 10 9
# 출력
5 6 7 9 10 11
```

### 분석

- 시간복잡도 : `O(n²)`
- 선택 정렬 알고리즘이 비교 횟수가 많고 데이터의 이동 횟수는 적은 반면,
- 삽입 정렬 알고리즘은 비교 횟수가 적고 상대적으로 데이터의 이동 횟수는 많은 편이다.

<br>

## 버블 정렬 알고리즘

> 순차적으로 바로 옆의 데이터와 비교해서 옆의 데이터가 더 크면 자신과 위치를 바꾼다. 즉, 첫번째 데이터가 만약 가장크면 계속해서 비교해서 맨 끝으로 이동한다.

```cpp
for(int i=0; i<n; i++){
    for(int j=0; j<n-i-1; j++){
        if(a[j] > a[j+1]){
            temp = a[j];
            a[j] = a[j+1];
            a[j+1] = temp;
        }
    }
}
```

### 분석

- 시간복잡도 : `O(n²)`
- 최선의 경우 데이터가 정렬된 상황이므로 이동횟수는 0이지만 비교횟수는 `N*N / 2`이다.
- 최악의 경우는 비교횟수와 이동횟수 모두 `N*N / 2`이다. 최악의 경우를 가정하면 성능이 다른 정렬 알고리즘보다 많이 나쁘다.
