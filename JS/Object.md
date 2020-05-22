## 전역 객체

전역객체는 특수한 객체다. 모든 객체는 이 전역객체의 프로퍼티다.

```js
function func() {
  alert("Hello?");
}

func();
window.func();
```

`func();`와 `window.func();`는 모두 실행이 된다. 모든 전역변수와 함수는 사실 `window` 객체의 프로퍼티다. 객체를 명시하지 않으면 암시적으로 window의 프로퍼티로 간주된다.

전역객체의 이름도 호스트환경에 따라서 다른데, 웹브라우저에서 전역객체는 `window`이지만 `node.js`에서는 `global`이다.

## JSON

> JSON(JavaScript Object Notation) : 자바스크립트 객체를 문자열로 표현하는 데이터 포맷<br>웹 애플리케이션에서는 서버와 웹 클라이언트가 데이터를 주고받을 때 JSON을 자주 사용한다.

### 자바스크립트 객체를 JSON문자열로 변환하기

> JSON.stringify 메서드는 인수로 받은 객체를 JSON문자로 바꾸어 반환한다.

```js
JSON.stringify(value[, replacer[, space]])
```

### JSON문자열을 자바스크립트 객체로 환원하기

> JSON.parse 메서드는 인수로 받은 문자열을 자바스크립트 객체로 환원해서 반환한다.

```js
JSON.parse(text[, reviver])
```

## Object.keys()

> 주어진 객체의 속성 이름의 배열을 반환한다.

```js
const object1 = {
  a: "somestring",
  b: 42,
  c: false,
};

console.log(Object.keys(object1));
// expected output: Array ["a", "b", "c"]
```
