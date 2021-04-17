## 명시적 타입 변환

- [숫자 👉 문자열](#toString)
  - **숫자 + 문자열**
  - **Number** 객체 메서드 활용
  - **String** 함수 활용
- [문자열 👉 숫자](#toNum)
  - **수식 안에서** 묵시적 변환
  - **parseInt / parseFloat** 함수 사용
  - **Number** 함수 활용
- 논리값으로 변환

<br>

## <a name="toString"></a>숫자를 문자열로 변환

1. 숫자 + 문자열

- 숫자와 문자열을 `+` 연산자로 연결하면 **숫자 -> 문자열**

```js
11 + "clock"; //"11clock"
```

2. Number 객체 메서드 활용

- `toString` : 숫자를 문자열로 변환
- `toLocaleString` : 숫자를 지역화된 문자열로 변환. 인수로 옵션 지정가능
- `toFixed` : 숫자의 소수점 아래 자릿수를 문자열로 변환

```js
const n = 234;
n.toString(); //"234"
n.toString(2); //"11101010" (인수로 숫자 넘기면 진법을 바꿈)

const n2 = 234.567;
n2.toFixed(2); //"234.57"
```

3. String 함수 활용

- `String` 함수는 모든 데이터 타입을 문자열 타입으로 바꿈

```js
String(27); //"27"
String(true); //"true"
String([1, 2, 3]); //"1,2,3"
```

<br>

## <a name="toNum"></a>문자열을 숫자로 변환

1. 수식 안에서 묵시적 변환

```js
const a = "22";
console.log(a - 3); // 19

const b = "77";
console.log(b - 0); // 77

const c = "99";
console.log(+c); // 99
```

2. **_parseInt_** 와 **_parseFloat_** 함수 사용

- 문자열을 해석(parse)해서 숫자로 바꾸는 함수.
- `parseInt`는 문자열을 정수로 바꿈
- `parseFloat`는 문자열을 부동소수점으로 바꿈

```js
parseInt("1.56"); // 1
parseFloat("1.56"); // 1.56

// 이후에 나오는 문자열을 무시됨
parseInt("1.56 abcd"); // 1
parseFloat("1.56 abcd"); // 1.56

// 해석불가능하면 NaN 반환
parseInt("abc"); // NaN
parseInt(".56"); // NaN
```

3. Number 함수 사용

- `Number` 함수는 모든 데이터 타입을 숫자 타입으로 바꿈

```js
Number("2.567"); // 2.567
Number(true); // 1
Number([1, 2, 3]); // NaN
Number(null); //0
```

<br>

#### parseInt / Number 차이

```js
Number("1000원"); // 숫자아니면 NaN
NaN;
parseInt("1000원"); // 숫자 끝날때까지 형변환
1000;
```

<br>

## 논리값으로 변환

모든 값을 논리값으로 바꾸는 방법 두가지

```js
!!x;
Boolean(x);
```

- `!!`로 값의 타입을 논리타입으로 바꿀 수 있음
  - !연산자는 논리타입이 아닌 값의 타입을 논리타입으로 바꾸고, 그다음에 !를 더붙여 참과 거짓을 바꾼다.
