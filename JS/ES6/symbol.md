### 자바스크립트 데이터 타입 분류

자바스크립트가 처리가능한 데이터 타입은 크게 **원시 타입**과 **객체 타입**으로 나뉜다.

- 데이터 타입
  - 원시 타입
    - 숫자 (Number)
    - 문자열 (String)
    - 논리값 (Boolean)
    - 특수한 값 (undefined, null)
    - 심벌 (ES6: Symbol)
  - 객체 타입

## 심볼(Symbol)

> 심볼(Symbol)은 ES6부터 추가된 데이터 타입(원시 값)이다. 심볼은 자기 자신을 제외한 그 어떤 값과도 다른 유일무이한 값이다.

### 심볼의 생성

심볼은 `Symbol()`을 사용해서 생성한다.

```js
var sym1 = Symbol();
```

`Symbol()`은 호출할 때마다 새로운 값을 만든다.

```js
var sym2 = Symbol();
```

sym1과 sym2의 값이 다른것을 확인할 수 있다.

```js
console.log(sym1 == sym2); // false
```

또한 `Symbol()`에 인수를 전달하면 생성된 심벌의 설명을 덧붙일 수 있다.

```js
var SYM = Symbol("심볼");
```

심볼의 설명은 `toString()`메서드를 사용해서 확인할 수 있다.

```js
console.log(SYM.toString()); // Symbol(심볼)
```

<br>

### 심볼과 문자열 연결

`Symbol.for()`을 이용하면 문자열과 연결된 심볼을 생성할 수 있다.

```js
var sym1 = Symbol.for("hello");
var sym2 = Symbol.for("hello");

console.log(sym1 == sym2); // true
```

심볼과 연결된 문자열은 `Symbol.keyFor()`로 구할 수 있다.

```js
var sym3 = Symbol.for("hi");
var sym4 = Symbol("hi");

console.log(Symbol.keyFor(sym3)); // hi
console.log(Symbol.keyFor(sym4)); // undefined
```
