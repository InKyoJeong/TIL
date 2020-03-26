## const, let

**var**은 이제 **let**과 **const**가 대체한다. `let`과 `const`는 ES6부터 추가된 변수 선언자로 '블록 유효 범위'를 갖는 변수를 선언한다. 블록 유효 범위를 가진 변수는 중괄호`{}`안에서만 유효하다. 즉, 블록 스코프를 가지므로 블록 밖에서는 변수에 접근할 수 없다.

### var와 let의 scope 비교

- var

```js
function varScope() {
  var test = 11;
  if (true) {
    var test = 22;
    console.log(test); // 22
  }
  console.log(test); // 22
}
//scope가 전체 외부함수까지이다.
```

- let

```js
function letScope() {
  let test = 33;
  if (true) {
    let test = 44;
    console.log(test); //44
  }
  console.log(test); //33
}
//scope가 내부, 하위블록에서 유효하다.
```

가장 큰 차이는 하위 블록에서 재선언을 했을 때 var는 상위 블록과 같은 변수 취급, let은 다른 변수로 취급한다는 것이다.

- var

```js
function varScope() {
  if (true) {
    var test = 50;
    console.log(test); // 50
  }
  console.log(test); // 50
}
```

- let

```js
function letScope1() {
  if (true) {
    let test = 50;
    console.log(test); // 50
  }
  console.log(test); //Uncaught ReferenceError: test is not defined
} //test는 블록 안에서 유효범위를 가지므로 블록 밖에서 변수에 접근할 수 없다.

function letScope2() {
  let test = 50;
  if (true) {
    console.log(test); //50
  }
  console.log(test); //50
} // 바깥에 있는 변수 test의 유효범위는 전체이므로 밖에서도 접근할 수 있다.
```

var의 유효범위는 상위블록을 포함하고, let은 포함하지 않는다.

### const와 let비교

- `let`과 `const`의 **공통점**은 `var`와 다르게 **변수 재선언 불가능**이다.
- `let`과 `const`의 **차이점**은 변수의 _immutable_ 여부이다.
- `let`은 **변수에 재할당이 가능**하지만, `const`는 **변수 재선언, 재할당 모두 불가능**하다.

```js
//let : 블록유효범위를 갖는 지역변수 선언
let a = "test";
let a = "test2"; // Uncaught SyntaxError: Identifier 'a' has already been declared
a = "test3"; // 가능
```

```js
// const : 블록유효범위를 가지면서 한번만 할당할 수 있는 변수(상수)선언
// 반드시 초기화해야 한다.
const b = "test";
const b = "test2"; // Uncaught SyntaxError: Identifier 'b' has already been declared
b = "test3"; // 불가능 (Uncaught TypeError)
```

> 자바스크립트에서 한 번 초기화했던 변수에 다른 값을 대입하는 경우는 의외로 적다. 따라서 기본적으로는 변수 선언 시 **const**를 사용하고, 값을 변경해야하는 상황이 있으면 **let**을 사용하면 된다.
