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

### typeof

- 데이터 타입을 조사함

```js
const ex = "ABC";
console.log(typeof ex); //string
```
