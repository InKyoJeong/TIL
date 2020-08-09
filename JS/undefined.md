- **_null_** 은 **아무것도 없음**을 값으로 표현한 리터럴이다.
- **_undefined_** 는 **정의되지 않은 상태**를 뜻한다.

<br>

## undefined (정의되지 않음)

접근 가능한 스코프에 변수가 선언되었으나 현재 아무런 값도 할당되지 않은 상태.

```js
var test1;
console.log(test1); //undefined
console.log(typeof test1); //undefined
```

- 값이 `undefined`가 되는 경우들
  - 값을 아직 할당하지 않은 변수의 값
  - 없는 객체의 프로퍼티를 읽으려할때
  - 없는 배열의 요소를 읽으려할때
  - 아무것도 반환하지않는 함수가 반환하는 값
  - 함수를 호출했을때 전달받지 못한 인수의 값

### undeclared (선언되지 않음)

접근 가능한 스코프에 변수 선언조차 되어있지 않은 상태.

```js
console.log(test2);
//VM42:1 Uncaught ReferenceError: test2 is not defined
//    at <anonymous>:1:13
```

<br>

## null (아무것도 없음)

null은 주로 프로그램에서 뭔가 검색했는데 찾지 못했을때 아무것도 없음을 전달하기위한 값으로 사용된다.

```js
var test3;
test3 = null;
console.log(test3); //null
console.log(typeof test3); //object
```

null이라는 빈 값을 할당하면 해당 변수의 타입은 객체이다.

<br>

## undefined == null

```js
console.log(undefined == null); //true
```

`==`는 자료형이 다르면 자동 형변환을 하므로 참이지만

```js
console.log(undefined === null); //false
```

`===`는 거짓이다.
