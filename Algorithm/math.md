# 수학

- 나머지연산
- 최대공약수, 최소공배수
- 소수

<br>

## 나머지 연산

- 컴퓨터 정수는 저장할 수 있는 범위가 저장되어 있기때문에, 답을 M으로 나눈 나머지를 출력하라는 문제가 출제됨
- 이런 경우 정답을 다 구하고 나머지 연산을 하지 않고, 정답을 갱신할때마다 나머지 연산을 수행해야 한다.
- 덧셈, 곱셈
  - `(A+B) mod M = ((A mod M)+(B mod M)) mod M`
  - `(A*B) mod M = ((A mod M)*(B mod M)) mod M`
- 뺄셈 : 음수가 나올 수도 있기때문에 M을 한번더 더해준다.
  - `(A-B) mod M = ((A mod M)-(B mod M) +M) mod M`
- 나눗셈은 성립하지 않는다.

<br>

## 최대공약수(GCD)

- 2부터 계속 나누는 방법
- 유클리드 호제법
  - a를 b로 나눈 나머지를 r이라 하면
  - `GCD(a,b) = GCD(b,r)`
  - r이 0일때, b가 최대공약수이다.

```cpp
// 재귀를 이용한 유클리드 호제법
int gcd(int a, int b){
    if(b == 0)
        return a;
    else
        return gcd(b, a%b);
}
```

<br>

## 최소공배수(LCM)

- 어떤 수 A, B가 있을때
- `LCM = (A*B) / GCD` 이다.

<br>

## 소수

- 2부터 n-1까지 나누는방법 : O(N)
- 2부터 n/2까지 나누는방법 : O(N/2)
- 루트N까지 나누는방법 : O(루트N)

```cpp
//루트 N
bool prime(int n){
    if(n<2)
        return false;
    for(int i=2; i*i<=n; i++){
        if(n % i == 0){
            return false;
        }
    }
    return true;
}
```

<br>

## 에라토스테네스의 체

> 1부터 N까지 범위안에 들어가는 모든 소스를 구하기

- 2부터 N까지 모든 수를 써놓는다.
- 아직 지워지지 않은 수 중 가장 작은 수를 찾는다.
- 그 수는 소수임
- 이제 그 수의 **배수를 모두 지움**

```cpp
int prime[100]; //소수 저장
int pn = 0; //소수의 개수
bool check[101]; //지워졌으면 true
int n = 100; //100까지 소수
for(int i=2; i<=n; i++){
    if(check[i] == false){  //지워지지 않았으면
      prime[pn++] = i;
      for(int j=i*i; j<=n; j+=i){ //배수를 계속지우기
          check[j] = true;
      }
    }
} //이렇게 다 지우면 prime 배열에는 소수만 남음

//실제로 구현할때는 i*i 부분을 i*2 또는 i+i로 하는게 좋다. (백만^2 는 오버플로발생)
```
