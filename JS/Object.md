## 객체 리터럴

- 프로퍼티 : 객체에 포함된 데이터 하나(이름과 값의 쌍)

```js
var card = {
  suit: "하트",
  rank: "A",
};
```

- 프로퍼티 값을 읽거나 쓸 때는 `.` 이나 `[]` 사용

```js
card.suit; //하트
card["rank"]; //A
```

<br>

## computed property name

> computed property name은 표현식(expression)을 이용해 객체의 key 값을 정의함

- 원래 코드
  - 먼저 객체를 만들고 값을 할당

```js
function objectify(key, value) {
  let obj = {};
  obj[key] = value;
  return obj;
}

objectify("name", "Kyo"); //{name: "Kyo"}
```

- computed property name 이용

```js
function objectify(key, value) {
  return {
    [key]: value,
  };
}
objectify("name", "Kyo"); //{name: "Kyo"}
```

<br>

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

<br>

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

<br>

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

<br>

<!-- ## 접근자 프로퍼티

- 객체의 프로퍼티는 두 종류로 나뉨
  - 첫번째는 **데이터 프로퍼티**: 지금까지 사용한 모든 프로퍼티. 값을 저장하기위함
  - 두번째는 **접근자 프로퍼티**: 값이 없음. 프로퍼티를 읽거나 쓸 때 호출하는 함수를 값 대신에 지정할 수 있는 프로퍼티

### getter와 setter

```js
let obj = {
  get propName() {
    // getter, obj.propName을 실행할 때 실행되는 코드
  },

  set propName(value) {
    // setter, obj.propName = value를 실행할 때 실행되는 코드
  },
};
````

- 위에서 `getter` 메서드는 `obj.propName`을 사용해 프로퍼티를 읽으려고 할 때 실행되고
- `setter` 메서드는 `obj.propName = value`으로 프로퍼티에 값을 할당하려 할 때 실행됨

<br>

```js
let user = {
  lastname: "Kim",
  name: "Taeyeon",

  get fullName() {
    return `${this.lastname} ${this.name}`;
  },
};

console.log(user.fullName); // Kim Taeyeon
```

- 바깥 코드에서 접근자 프로퍼티를 일반 프로퍼티처럼 사용할 수 있음

````js
let user = {
  lastname: "Kim",
  name: "Taeyeon",

  get fullName() {
    return `${this.lastname} ${this.name}`;
  },

  set fullName(value) {
    [this.lastname, this.name] = value.split(" ");
  },
};

user.fullName = "Kwon JinAh";

console.log(user.lastname); //Kwon
console.log(user.name); //JinAh
``` -->

```

```
