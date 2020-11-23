## 반복문 클로저

```js
function count() {
  var i;
  for (i = 1; i < 10; i += 1) {
    setTimeout(function timer() {
      console.log(i);
    }, i * 100);
  }
}
count();
```

- 이 코드는 **_1,2,3, ... 9_** 를 **0.1초**마다 출력하는 것이 목표였는데 결과로 `10`이 9번 출력됨
- `timer`는 클로저로 언제 어디서 어떻게 호출되던지 항상 상위 스코프인 `count`에게 `i`를 알려달라고 요청함
- 그리고 `timer`는 **0.1초** 후 호출됨
- 그런데 첫 **0.1초**가 지날동안 이미 `i`는 `10`이 되었음
- 그리고 `timer`는 **0.1**초 주기로 호출될 때마다 항상 `count`에서 `i`를 찾음
- 결국, `timer`는 이미 `10`이 되어버린 `i`만 출력하게 됨

### 그럼 의도한대로 1~9를 출력하려면?

#### 1. 새로운 스코프를 추가하여 반복 시마다 그곳에 각각 따로 값을 저장

```js
function count() {
  var i;
  for (i = 1; i < 10; i += 1) {
    (function (countingNumber) {
      setTimeout(function timer() {
        console.log(countingNumber);
      }, i * 100);
    })(i);
  }
}
count();
```

#### 2. ES6에서 추가된 블록 스코프를 이용

```js
function count() {
  for (let i = 1; i < 10; i += 1) {
    setTimeout(function timer() {
      console.log(i);
    }, i * 100);
  }
}
count();
```
