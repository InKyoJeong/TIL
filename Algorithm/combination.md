## 조합

- **nCr**
- 순서 상관없이 뽑기
  - ex) `[1,2,3] = [3,2,1]` 은 같으므로 하나의 조합으로 취급

```
  1을 고정하고 -> 나머지 [2, 3, 4] 중에서 2개씩 조합을 구한다.
  [1, 2, 3] [1, 2, 4] [1, 3, 4]
  2를 고정하고 -> 나머지 [3, 4] 중에서 2개씩 조합을 구한다.
  [2, 3, 4]
  3을 고정하고 -> 나머지 [4] 중에서 2개씩 조합을 구한다.
  []
  4을 고정하고 -> 나머지 [] 중에서 2개씩 조합을 구한다.
  []
```

## 순열

- **nPr = nCr \* r!**
- 순열은 순서가 중요
  - ex) `[1,2]` 와 `[2,1]` 은 다르다.
- 조합을 구한후 선택하려는 수의 팩토리얼을 곱하면 순열
  - ex) 1234 에서 3개씩 뽑는다고 하면 `[1,2,3],[1,2,4],[1,3,4],[2,3,4]` 가있고 각각 조합에서 순서를 바꾸는 경우 `3!`을 곱한다.

```
1(고정) => permutation([2, 3, 4]) => 2(고정) => permutation([3, 4]) => ...
2(고정) => permutation([1, 3, 4])
3(고정) => permutation([1, 2, 4])
4(고정) => permutation([1, 2, 3])
```

<br>

## DFS로 구하기

#### m개를 뽑는 조합 수

```js
function solution(arr, m) {
  let answer = [];
  let n = arr.length;
  let temp = Array.from({ length: m }, () => 0);

  function DFS(L, p) {
    if (L === m) {
      answer.push(temp.slice());
    } else {
      for (let i = p; i < n; i++) {
        temp[L] = arr[i];
        DFS(L + 1, i + 1);
      }
    }
  }
  DFS(0, 0);

  return answer;
}

let arr = [1, 2, 3, 4];
console.log(solution(arr, 3));
// [
//  [ 1, 2, 3 ], [ 1, 2, 4 ],
//  [ 1, 3, 4 ], [ 2, 3, 4 ]
// ]
```

<br>

#### m개 뽑는 순열

```js
function solution(arr, m) {
  let answer = [];
  let n = arr.length;
  let ch = Array.from({ length: n }, () => 0);
  let temp = Array.from({ length: m }, () => 0);

  function DFS(L) {
    if (L === m) {
      answer.push(temp.slice());
    } else {
      for (let i = 0; i < n; i++) {
        if (ch[i] === 0) {
          ch[i] = 1;
          temp[L] = arr[i];
          DFS(L + 1);
          ch[i] = 0;
        }
      }
    }
  }
  DFS(0);
  return answer;
}

let arr = [1, 2, 3, 4];
console.log(solution(arr, 3));
// [
//   [ 1, 2, 3 ], [ 1, 2, 4 ],
//   [ 1, 3, 2 ], [ 1, 3, 4 ],
//   [ 1, 4, 2 ], [ 1, 4, 3 ],
//   [ 2, 1, 3 ], [ 2, 1, 4 ],
//   [ 2, 3, 1 ], [ 2, 3, 4 ],
//   [ 2, 4, 1 ], [ 2, 4, 3 ],
//   [ 3, 1, 2 ], [ 3, 1, 4 ],
//   [ 3, 2, 1 ], [ 3, 2, 4 ],
//   [ 3, 4, 1 ], [ 3, 4, 2 ],
//   [ 4, 1, 2 ], [ 4, 1, 3 ],
//   [ 4, 2, 1 ], [ 4, 2, 3 ],
//   [ 4, 3, 1 ], [ 4, 3, 2 ]
// ]
```

<br>

## 중복 순열

- 순열을 구할때 체크를 안하면 됨

```js
function solution(arr, m) {
  let answer = [];
  let n = arr.length;
  let temp = Array.from({ length: m }, () => 0);

  function DFS(L) {
    if (L === m) {
      answer.push(temp.slice());
    } else {
      for (let i = 0; i < n; i++) {
        temp[L] = arr[i];
        DFS(L + 1);
      }
    }
  }
  DFS(0);
  return answer;
}

let arr = [1, 2, 3, 4];
console.log(solution(arr, 3));
// [ [1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 1, 4],
//   [1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 2, 4]
//   [1, 3, 1], [1, 3, 2], [1, 3, 3], [1, 3, 4],
//   [1, 4, 1], [1, 4, 2], [1, 4, 3], [1, 4, 4],
//   [2, 1, 1], ...생략 ]
```

<br>

## 참고

<br>

#### 조합 구현

```js
function combination(arr, count) {
  let result = [];
  if (count === 1) {
    return arr.map((v) => [v]);
  }

  arr.forEach((fixed, index, origin) => {
    let rest = origin.slice(index + 1); //fixed 제외 나머지 뒤
    let combine = combination(rest, count - 1); // 나머지에 대해 조합 구하기
    let attached = combine.map((comb) => [fixed, ...comb]); // fixed랑 합치기
    result.push(...attached);
  });

  return result;
}

let answer = combination([1, 2, 3, 4], 3);
console.log(answer);
// [
//  [ 1, 2, 3 ], [ 1, 2, 4 ],
//  [ 1, 3, 4 ], [ 2, 3, 4 ]
// ]
```

<br>

#### 순열 구현

- 나머지를 구하는 코드만 다르다.
- 자신을 제외한 원소에 대해 순열을 구한다.

```js
function permutation(arr, count) {
  const result = [];
  if (count === 1) return arr.map((value) => [value]); // 1개씩 택할 때, 바로 모든 배열의 원소 return

  arr.forEach((fixed, index, origin) => {
    let rest = [...origin.slice(0, index), ...origin.slice(index + 1)]; // fixed를 제외한 나머지 배열
    let permute = permutation(rest, count - 1);
    let attached = permute.map((per) => [fixed, ...per]);
    result.push(...attached);
  });

  return result;
}

const answer = permutation([1, 2, 3, 4], 3);
console.log(answer);
// [
//   [ 1, 2, 3 ], [ 1, 2, 4 ],
//   [ 1, 3, 2 ], [ 1, 3, 4 ],
//   [ 1, 4, 2 ], [ 1, 4, 3 ],
//   [ 2, 1, 3 ], [ 2, 1, 4 ],
//   [ 2, 3, 1 ], [ 2, 3, 4 ],
//   [ 2, 4, 1 ], [ 2, 4, 3 ],
//   [ 3, 1, 2 ], [ 3, 1, 4 ],
//   [ 3, 2, 1 ], [ 3, 2, 4 ],
//   [ 3, 4, 1 ], [ 3, 4, 2 ],
//   [ 4, 1, 2 ], [ 4, 1, 3 ],
//   [ 4, 2, 1 ], [ 4, 2, 3 ],
//   [ 4, 3, 1 ], [ 4, 3, 2 ]
// ]
```
