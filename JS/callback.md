## 콜백함수

- **제어권**을 맡긴다.
  - 실행시점에 대한 제어권
  - 인자
  - this

```js
setInterval(function () {
  console.log("1초마다 실행됨");
}, 1000);
```

cb로 다시 쓰면

```js
var cb = function () {
  console.log("1초마다 실행됨");
};

setInterval(cb, 1000);
```

첫 번째 인자로 콜백함수가 넘어감, 두 번째 인자가 주기

제어권을 `setInterval`에게 넘겨준 것

<br>

- 인자

```js
var arr = [1, 2, 3, 4, 5];
var entries = [];
arr.forEach(
  function (v, i) {
    entries.push([i, v, this[i]]);
  },
  [10, 20, 30, 40, 50]
);
console.log(entries);
// (5) [Array(3), Array(3), Array(3), Array(3), Array(3)]
// 0: (3) [0, 1, 10]
// 1: (3) [1, 2, 20]
// 2: (3) [2, 3, 30]
// 3: (3) [3, 4, 40]
// 4: (3) [4, 5, 50]
```

```js
arr.forEach(callback(currentvalue[, index[, array]])[, thisArg])
```

`forEach`는 콜백함수 인자가 `value`, `index`, `array` 순서

- forEach가 정해놓은 규칙에 따라야 동작을 제대로함
- 아래와 같이 _index, value_ 순서로 써도 이름이 _index인 value_ 일 뿐임

```js
var arr = [99, 55, 44, 22, 11];
arr.forEach(function (index, value) {
  console.log(index, value);
});

// 99 0
// 55 1
// 44 2
// 22 3
// 11 4
```

<br>

### 정리

- 다른 함수(A)의 인자로 콜백함수(B)를 전달하면, A가 B의 제어권을 받게됨
- 특별한 요청(bind)이 없는한 A에 미리 정해놓은 방식에 따라 B를 호출함
  - 미리 정해놓은 방식:
    - 어떤 시점에 콜백을 호출할지
    - 인자에는 어떤값을 지정할지
    - this에 무엇을 바인딩할지

<br>

### 주의 - 콜백은 함수다

```js
var arr = [1, 2, 3, 4, 5];
var obj = {
  vals: [1, 2, 3],
  logValues: function (v, i) {
    if (this.vals) {
      console.log(this.vals, v, i);
    } else {
      console.log(this, v, i);
    }
  },
};
obj.logValues(1, 2);
// 메소드로서 호출했으므로

//(3) [1, 2, 3] 1 2
```

```js
var arr = [99, 55, 44, 22, 11];
var obj = {
  vals: [1, 2, 3],
  logValues: function (v, i) {
    if (this.vals) {
      console.log(this.vals, v, i);
    } else {
      console.log(this, v, i);
    }
  },
};
arr.forEach(obj.logValues);
// 콜백함수로 전달
// 호출한게 아니라 그냥 콜백으로 obj.logValues가 가리키는 함수만 넘겨준것

//Window {0: global, window: Window, self: Window, document: document, name: "", location: Location, …} 99 0
//Window {0: global, window: Window, self: Window, document: document, name: "", location: Location, …} 55 1
//Window {0: global, window: Window, self: Window, document: document, name: "", location: Location, …} 44 2
//Window {0: global, window: Window, self: Window, document: document, name: "", location: Location, …} 22 3
//Window {0: global, window: Window, self: Window, document: document, name: "", location: Location, …} 11 4
```

- `obj`를 지정하고 싶으면 `forEach`의 두번째 인자로 `thisArg`넣어주거나 `bind`메서드사용
