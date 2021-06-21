## global

```js
console.log(global === this); // false
console.log(this); // {}
console.log(this === module.exports); //true

function a() {
  console.log(global === this); // true
}
a();
```

- 전역 스코프의 `this` 는 빈 객체다
- 빈 객체가 나오는 이유는 `this === module.exports`
- _function_ 안의 `this`는 `global` 이다.

<br>

## 타이머 (setTimeout, setImmediate, process.nextTick)

- `process.nextTick()`, `resolve된 Promise` 순서고, 그다음이 `setTimeout`이나 `setImmediate`이다.

- 태스크 큐에 들어가는건 똑같은데, `process.nextTick()`, `Promise` 는 `setTimeout` 보다 호출스택에 먼저 들어간다(새치기를 한다). 정확히는 마이크로 태스크큐로 따로 구분짓는다.

```js
setImmediate(() => {
  console.log("immediate");
});
process.nextTick(() => {
  console.log("nextTick");
});
setTimeout(() => {
  console.log("timeout");
}, 0);
Promise.resolve().then(() => console.log("promise"));

// nextTick
// promise
// timeout
// immediate
```

#### setTimeout vs setImmediate

- `setTimeout`, `setImmediate` 얘네둘은 뭐가 먼저일지 모른다. 정확히는 환경에 따라 다르다. 프로세스 성능에 영향을 받는다.

```js
setTimeout(() => {
  console.log("timeout");
}, 0);

setImmediate(() => {
  console.log("immediate");
});

// $ node test.js
// timeout
// immediate

// $ node test.js
// immediate
// timeout
```

- 그러나 I/O 주기에서 호출하면 `immediate`콜백이 항상 먼저 실행된다.

```js
const fs = require("fs");

fs.readFile(__filename, () => {
  setTimeout(() => {
    console.log("timeout");
  }, 0);
  seetImmediate(() => {
    console.log("immediate");
  });
});

// $ node test.js
// immediate
// timeout
```

<br>

## module, exports

- 모듈이란 특정한 기능을하는 함수나 변수들의 집합

```js
// var.js
const odd = "홀";
const even = "짝";

module.exports = {
  odd,
  even,
};
```

```js
// func.js
const { odd, even } = require("/var");

function checkNum(num) {
  if (num % 2 === 0) {
    return even;
  } else {
    return odd;
  }
}

module.exports = checkNum;
```

- `exports` 객체로도 모듈을 만들수 있다.

```js
// var.js
exports.odd = "홀";
exports.even = "짝";
```

<br>

## filename, dirname

- 현재 파일명, 파일경로에 대한 정보제공
- 경로 처리는 보통 `path` 모듈 사용

```js
// test.js
console.log(__filename);
console.log(__dirname);

// $ node test.js
// /Users/ingg/Documents/TIL/test.js
// /Users/ingg/Documents/TIL
```
