### Hoisting

> 호이스팅(Hoisting)이란 변수나 함수를 선언했을때 코드 범위(scope)내의 최상단으로 끌어올리는 것

프로그램은 작성한 순서에 따라 윗줄부터 차례로 실행된다. 그러나 변수 선언은 이 원칙을 따르지 않는다.

```js
console.log(x); // undefined
var x;
```

이 코드에서 첫번째 줄은 아직 변수 `x`가 선언되지 않았기 때문에 오류가 발생할 것 같지만, `undefined`가 출력된다.

프로그램 중간에서 변수나 함수를 선언하더라도 프로그램 첫 머리에 선언된 것처럼 다른 문장앞에 생성되기 때문이다. 이를 변수 선언의 `끌어올림(Hoisting)`이라고 한다.

단, 선언과 동시에 대입하는 코드는 끌어올리지 않는다.

```js
console.log(x); // undefined
var x = 5;
console.log(x); /// 5
```

첫번째 줄은 `undefined`가 출력되고 3번째는 5가 출력된다. 변수 선언부 `var x`는 끌어올리지만 대입부 `x = 5`는 끌어올리지 않기 때문이다.

---

1. 함수표현식`Function Expression` : Hoisting 안됨

```js
a(); // Uncaught TypeError: a is not a function

var a = function() {
  console.log("boo");
};

a();
```

a변수가 아직 할당을 못받은 상태에서 호출하여 에러가 발생한다.

2. 함수선언식`Function Declaration` : Hoisting 됨

```js
say(); // Hello

function say() {
  console.log("Hello");
}

say();
```

함수를 작성하기 전에 함수를 호출하였지만, 코드는 여전히 동작한다.

3. `let`과 `const`변수 선언에서는 Hoisting이 발생하지 않는다.

```js
console.log(b); //Uncaught ReferenceError: Cannot access 'b' before initialization

let b = 1;

console.log(b);
```
