## unordered_map

- 일반적으로 데이터 양이 많은 경우 `map` 보다 `unordered_map` 성능이 더 좋음. 데이터가 N 개일 때
  - `map` 은 이진 탐색 트리 기반으로 **O(logN)** 의 탐색 속도 (자동으로 정렬되는 컨테이너)
  - `unordered_map`은 해쉬 테이블 기반으로 **O(1)** 의 탐색 속도를 가짐 (자동으로 정렬되지 않는 컨테이너)

```cpp
#include <unordered_map>
unordered_map<string, int> d;

cout << d["leo"] << endl;
// key에 의한 value의 접근

d["leo"] = 3;
// 특정 key에 의한 value 업데이트
```

- 존재하지않는 키에대한 값은 기본값으로 간주함
- value의 (여기서는 int) 기본값은 0
  - 문자열의 기본값은 빈 문자열

```cpp
for(auto&i : d)
	cout << i.first << "-" << i.second << endl;
			//key 			  //value
```

<br>

### 프로그래머스 - 완주하지 못한 선수

```cpp
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
	unordered_map<string, int>d;
	for(auto& i : participant)
		d[i]++;
	for(auto& i: completion)
		d[i]--;
	for(auto& i: d){
		if(i.second > 0){
			answer = i.first;
			break;
		}
	}

	return answer;
}
// unordered_map은 해시테이블 구조로 되어있어서,
// 키를 통한 각 원소의 접근이 상수시간에 이루어질 수 있음
```
