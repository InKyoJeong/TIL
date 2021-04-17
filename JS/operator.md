## + 연산자

- `+` 연산자는 더하기 연산과 문자열 연결 연산을 수행
- 모두 숫자일 경우에만 더하기 연산, 나머지는 문자열 연결 연산이 이뤄짐

```js
const add1 = 1 + 2;
const add2 = "hi" + "js";
const add3 = 1 + "js";
const add4 = 1 + "4";

console.log(add1); // 3
console.log(add2); // hijs
console.log(add3); // 1js
console.log(add4); // 12 (string)
```

<br>

## 논리 연산자

- a `&&` b : a와 b 모두 true면 true, 아니면 false
- a `||` b : a와 b 중 하나라도 true면 true, 모두 false면 false
- `!`a : a가 true면 false, false면 true

## 피연산자 평가

- 논리 연산자의 피연산자는 논리값이 아니여도 됨
- 피연산자가 논리값이 아니면 다음과같이 타입변환이 됨

**_0, -0, 빈문자열(""), NaN, null, undefined_** : `false` <br>
**_0을 제외한 숫자, 빈 문자열을 제외한 문자열, 모든 객체, 심벌_** : `true`

<br>

## 문자열 제어

> String 객체 메서드

### split()

> 첫 번째 인수로 문자열을 분할한 다음 배열에 담아서 반환한다. 첫 번째 인수를 생략하면 원본 문자열 전체를 배열에 담아 반환한다.

```js
const str = "The quick brown fox jumps over the lazy dog.";
undefined;
str.split(" ");
// (9) ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
```

### trim()

> trim() 메서드는 문자열 양 끝의 공백을 제거한다.

```js
const greeting = "   Hello world!   ";

console.log(greeting);
// "   Hello world!   ";
console.log(greeting.trim());
// "Hello world!";
```

<br>

## 기타 연산

### delete

- 객체의 프로퍼티나 배열 요소를 제거한다.

```js
const Person = {
  name: "John",
  job: "student",
};

console.log(Person.name); // John

delete Person.name;

console.log(Person.name); // undefined
console.log(Person); // {job: "student"}
```

<br>

### typeof

- 데이터 타입을 조사함

```js
const ex = "ABC";
console.log(typeof ex); //string
```

- 주의할 점은 **null과 배열**이 `object`, **함수**는 `funtion`

```js
typeof null; // "object";
typeof []; // "object";

const nullTest = null;
console.log(typeof nullTest === null); // false
```

<br>

## !! 연산자

- `!!`의 역할은 **피연산자를 불린값으로 변환**함
- 객체는 값이 빈 객체라도 `true`로 변환됨

```js
console.log(!!{}); // true

console.log(!!3); // true
console.log(!!0); // false
console.log(!!"string"); // true

console.log(!!null); // false
console.log(!!undefined); // false
```
