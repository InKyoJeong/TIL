## Rest Pattern

> spread가 unpack이라면, rest는 배열로 pack 하는 것

```js
const [a, b, ...others] = [1, 2, 3, 4, 5, 6, 7];

console.log(a); // 1
console.log(b); // 2
console.log(others); // [3, 4, 5, 6, 7]
```

<br>

## Rest Parameter

- Rest 파라미터는 **Spread 연산자(...)** 를 사용하여 **함수의 파라미터**를 작성한 형태
- Rest 파라미터를 사용하면 함수의 파라미터로 오는 값들을 `배열`로 전달받을 수 있다.

```js
const add = function (...numbers) {
  console.log(numbers);
};

add(2, 3); // [2, 3]
add(7, 8, 9, 10); // [7, 8, 9, 10]
```

<Br>

- **마지막 파라미터만** Rest 파라미터가 될 수 있다.

```js
function myFunc(a, b, ...others) {
  console.log(a);
  console.log(b);
  console.log(others);
}

myFunc("one", "two", "three", "four", "five");

// one
// two
// ["three", "four", "five"]
```
