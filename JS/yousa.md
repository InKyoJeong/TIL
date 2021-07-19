## 유사 배열 객체

- 배열은 아니지만 배열로 처리할 수 있는 객체
- 프로퍼티 이름이 `0` 이상의 정수이고 `length` 프로퍼티가 있는 객체
- 유사 배열 객체는 `Array.prototype`의 메서드를 직접 사용 불가능

```js
let yousa = {
  0: "aa",
  1: "bb",
  2: "cc",
  3: "dd",
  length: 4,
};

yousa[0]; // "aa"
yousa.length; // 4
```

<br>

#### 배열과 유사배열을 구분해야 하는 이유는, 유사배열의 경우 배열 메서드를 쓸 수 없기 때문

```js
// 배열
let array = [1, 2, 3];
array.forEach(function (e) {
  console.log(e);
});
// 1
// 2
// 3

// 유사 배열
yousa.forEach(function (e) {
  console.log(e);
});
// Uncaught TypeError: yousa.forEach is not a function
```

<br>

#### Function.prototype.call 메서드를 간접 호출하면 사용 가능

```js
let yousa = {
  0: "aa",
  1: "bb",
  2: "cc",
  3: "dd",
  length: 4,
};

Array.prototype.forEach.call(yousa, function (e) {
  console.log(e);
});
// aa
// bb
// cc
// dd

Array.prototype.join.call(yousa, ",");
// "aa,bb,cc,dd"

// 이렇게 해도 같은 결과
[].forEach.call(yousa, function (e) {
  console.log(e);
});
// aa
// bb
// cc
// dd
```

<br>

#### Array.from 으로 더 간단하게 가능

```js
Array.from(yousa).forEach(function (e) {
  console.log(e);
});
// aa
// bb
// cc
// dd
```
