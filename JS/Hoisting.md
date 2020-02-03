### Hoisting

> 호이스팅(Hoisting)이란 변수나 함수를 선언했을때 코드 범위(scope)내의 최상단으로 끌어올리는 것

1. 함수표현식`Function Expression` : Hoisting 안됨

```js
a(); // Error

var a = function() {
  console.log("boo");
};

a();
```

a변수가 아직 할당을 못받은 상태에서 호출해서 에러발생

2. 함수선언식`Function Declaration` : Hoisting 됨

```js
say(); // Hello

function say() {
  console.log("Hello");
}

say();
```

3. `let`과 `const`변수 선언에서는 호이스팅이 발생하지 않는다.
