## 이분 탐색 (Binary Search)

- 시간복잡도는 탐색할 범위를 절반으로 줄여서 탐색하므로 `O(logn)`

### 이분탐색 - 인덱스 구하기

```js
function solution(target, arr) {
  let answer;
  let start = 0;
  let end = arr.length - 1;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    if (target === arr[mid]) {
      answer = mid;
      break;
    } else if (target < arr[mid]) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }

  return answer;
}

let arr = [12, 23, 32, 57, 65, 81, 87, 99];
console.log(solution(32, arr)); // 2번 인덱스
```

<br>

## Lower Bound, Upper Bound

- 이분 탐색이 원하는 값 x를 찾는 과정이라면,
  - **Lower Bound**는 원하는 값 x이상이 처음 나오는 위치를 찾는 과정
  - **Upper Bound**는 원하는 값 x를 초과한 값이 처음 나오는 위치를 찾는 과정
- 만약 **target**이 모든 원소들보다 큰게 주어지면, 주어진 배열크기 만큼 리턴되어야 하기 때문에
  - `end = arr.length -1` 이 아니고 `end = arr.length`

### LowerBound : x이상이 처음나오는 위치

```js
function solution(target, arr) {
  let start = 0;
  let end = arr.length;

  while (start < end) {
    let mid = Math.floor((start + end) / 2);
    if (target <= arr[mid]) {
      end = mid;
    } else {
      start = mid + 1;
    }
  }
  return end;
}

let arr = [11, 22, 33, 44, 55, 66, 75, 88, 88, 99, 101, 102, 103];
console.log(solution(88, arr)); // 7번 인덱스
```

<br>

### UpperBound : x초과가 처음나오는 위치

- **LowerBound**의 **_arr[mid]_** 를 **_target_** 과 비교하는 부분에서 등호만 빼 주면 됨

```js
function solution(target, arr) {
  let start = 0;
  let end = arr.length;

  while (start < end) {
    let mid = Math.floor((start + end) / 2);
    if (target < arr[mid]) {
      end = mid;
    } else {
      start = mid + 1;
    }
  }
  return end;
}

let arr = [11, 22, 33, 44, 55, 66, 75, 88, 88, 99, 101, 102, 103];
console.log(solution(88, arr)); // 7번 인덱스
```
