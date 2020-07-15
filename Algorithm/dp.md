## DP와 분할정복 차이

- DP : 중복 O
- 분할 정복 : 중복 X

## 동적프로그래밍 조건 두가지

- **_Overlapping Subproblem_** : 겹치는 부분(작은)문제
  - 큰문제를 여러개의 작은문제로 쪼갤 수 있다.
  - 큰문제와 작은문제를 같은 방법으로 풀 수 있다.
  - 주로 재귀 사용 ex) 피보나치 수
- **_Optimal Substructrue_** : 최적 부분 구조
  - 문제의 정답을 작은 문제의 정답을 통해 구할 수 있다.
  - Optimal Substructrue를 만족하면, 문제의 크기에 상관없이 어떤 한 문제의 정답은 일정함
  - ex) 10번째 피보나치수를 구하면서 구한 4번째 피보나치수, 9번째 피보나치 구하면서 구한 4번째 , ...
  - 정답을 구했으면 메모(배열에 저장)해놓음

## 구현 방식

> 다이나믹의 구현 방식에는 두가지 방법이 있음

- Top-down : 재귀 사용
  - 큰 문제부터 문제를 쪼개가면서
  - 작은 문제를 만들고 합쳐가면서 원래 문제를 푼다.
- Bottom-up : 반복문 사용
  - 문제를 크기가 작은 문제부터 차례대로 푼다.
  - 문제의 크기를 조금씩 크게 만든다.
  - 작은문제를 풀면서 왔기때문에 큰문제는 항상 풀수있다.
  - 계속 반복하면 큰 문제를 풀 수 있다.

### Top-down 예시

```cpp
int memo[100];
int fibonacci(int n){
  if(n <= 1){
    return n;
  } else{
    if(memo[n] > 0){    //메모된 값이 있는지 없는지 비교
      return memo[n];
    }
    memo[n] = fibonacci(n-1) + fibonacci(n-2);
    return memo[n];
  }
}
```

### Bottom-up 예시

```cpp
int d[100];
int fibonacci(int n){
  d[0] = 0;
  d[1] = 1;
  for(int i=2; i<=n; i++){
    d[i] = d[i-1] + d[i-2];
  }
  return d[n];
}
```

작은문제 두개 풀어두고, 그다음 작은문제는 2니까 2부터 n까지 증가
