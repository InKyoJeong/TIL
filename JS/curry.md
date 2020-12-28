## Currying

- 커링패턴(Currying Pattern) : 함수가 일부인자를 먼저 받고 나머지 인자를 나중에 받을 수 있는 함수를 만드는 패턴

```js
const multiply = (a, b) => a * b;
const curriedMultiply = (a) => (b) => a * b;
curriedMultiply(5)(3); //15

const curriedMultiplyBy5 = curriedMultiply(5);
curriedMultiplyBy5(4); //20
```

<br>

- 커링패턴은 클로저를 사용한 일반적인 함수 사용법과 크게 다르지 않음

```js
const add = (x) => (y) => x + y;
add(1)(2); // 3
```

위를 es5로 작성해보면

```js
function add(x) {
  return function (y) {
    return x + y;
  };
}

var first = add(1); // first: ƒ (y) {...}
first(2); // 3
```

`add`함수가 반환하는 함수에서 `x`를 참조하고 있기 때문에, `add`함수의 호출이 끝난 이후에도 스코프가 유지되는 클로저를 사용한 패턴.

<!-- https://project42da.github.io/javascript/2019/02/06/js-curry.html -->
