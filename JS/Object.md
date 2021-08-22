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
const obj1 = {
  a: "somestring",
  b: 42,
  c: false,
};

console.log(Object.keys(obj1)); // ["a", "b", "c"]
```

## Object.values()

> 속성의 값들로 이루어진 배열을 리턴

```js
const obj1 = {
  a: "kkk",
  b: 123,
  c: false,
};

console.log(Object.values(obj1)); // ["kkk", 123, false]
```

<br>

## 객체의 복사

### 얕은 복사(Shallow copy)

- 객체가 담겨있는 변수를 다른 변수에 할당하면 call by reference (데이터 복사가 아닌 참조)가 일어남
  - 한 변수의 데이터를 변경하면 다른 변수의 데이터도 함께 변경됨

```js
const dog1 = { name: "zero" };
const dog2 = dog1;

dog1.name = "ginger";

dog2.name; // ginger
dog1 === dog2; // true (같은 데이터 주소를 바라보고 있는 두 변수)
```

- 데이터가 그대로 하나 더 생성된 것이 아니라, 해당 데이터의 메모리 주소를 전달하게 됨
  - 결국 한 데이터를 공유하게 되는 것

<br>

### 깊은 복사(Depth copy)

- 한 데이터의 공유가 아닌, 똑같은 구조의 객체를 하나 더 생성

### Object.assign()

```js
const originObj = { a: 1 };

const newObj = Object.assign({}, originObj); //빈 Object에 originObj를 병합

newObj; //  { a: 1 }
originObj === newObj; // false
```

### 전개 연산자

```js
const Obj1 = { a: 1, b: 2 };

const Obj2 = { ...Obj1 };

Obj2; // {a:1, b:2}
Obj1 === Obj2; // false
```

#### 하지만, 현재의 Depth 이상으로는 깊은 복사를 하지 않음

```js
const Obj1 = { a: { b: 1 } };

const Obj2 = { ...Obj1 };

Obj1 === Obj2; // false
Obj1.a === Obj2.a; // true
```

- `Obj1 === Obj2`는 `false`이지만 `Obj1.a === Obj2.a`가 `true`가 나옴
  - 즉, 깊은 복사가 된 것은 제일 바깥의 Depth뿐임
  - 두 번째 Depth 이상의 요소들은 **얕은 복사(Shallow copy)** 를 하게 됨
- `Object.assign()` 도 마찬가지

<br>

### 완벽한 깊은 복사하기

1. 재귀적으로 깊은 복사를 수행

<br>

2. Lodash의 `cloneDeep` 함수사용

```js
var objects = [{ a: 1 }, { b: 2 }];

var deep = _.cloneDeep(objects);
console.log(deep[0] === objects[0]); // false
```

<br>

3. JSON.parse()와 JSON.stringify()함수 사용

```js
const Obj1 = { a: { b: 1 } };
const Obj2 = { ...Obj1 };

const Obj3 = JSON.parse(JSON.stringify(Obj1));

Obj3; // {a: {…}}
// 전개 연산자의 경우,
Obj1 === Obj2; //false
Obj1.a === Obj2.a; //true

//JSON.parse(JSON.stringify())의 경우
Obj1 === Obj3; //false
Obj1.a === Obj3.a; //false
```

<br>

## Map

- Map 객체는 키-값 쌍을 저장하며 각 쌍의 삽입 순서도 기억하는 콜렉션
- 아무 값(객체와 원시 값)이라도 키와 값으로 사용가능

#### 속성

- `Map.prototype.size` : Map 객체에 들어있는 key/value pair의 수를 반환

#### 메서드

- `Map.prototype.get(key)` : 주어진 키(Key)에 해당되는 값(value)을 반환하고, 만약 없으면 undefined를 반환한다.
- `Map.prototype.has(key)` : Map 객체 안에 주어진 key/value pair가 있는지 검사하고 Boolean 값을 반환한다.
- `Map.prototype.set(key, value)` : Map 객체에 주어진 키(Key)에 값(Value)를 집어넣고, Map 객체를 반환한다.
- `Map.prototype.delete(key)` : 주어진 키(Key)와 해당되는 값(Value)를 제거

#### for ... of

- **Map**은 `for..of` 반복문을 사용해 순회 가능
  - `for...of` 반복문은 각 순회에서 `[key, value]`로 이루어진 배열을 반환

<br>

## Set

- Set 객체는 자료형에 관계 없이 원시 값과 객체 참조 모두 **유일한 값을 저장**

```js
const set1 = new Set([1, 2, 3, 4, 5]);
set1.has(1); // true

const mySet = new Set();
mySet.add(1); // Set { 1 }
mySet.add(5); // Set { 1, 5 }
mySet.add(5); // Set { 1, 5 }
```

- `Set.prototype.has(value)` : Set 객체 내 주어진 값을 갖는 요소가 있는가, _boolean_ 리턴
- `Set.prototype.add(value)` : Set 객체에 주어진 값을 갖는 **새로운 요소를 추가**
