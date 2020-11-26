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

> 이 코드는 **_1,2,3, ... 9_** 를 **0.1초**마다 출력하는 것이 목표였는데 결과로 `10`이 9번 출력됨

- `timer`는 클로저로 언제 어디서 어떻게 호출되던지 항상 상위 스코프인 `count`에게 `i`를 알려달라고 요청함
- 그리고 `timer`는 **0.1초** 후 호출됨
- 그런데 첫 **0.1초**가 지날동안 이미 `i`는 `10`이 되었음
- 그리고 `timer`는 **0.1**초 주기로 호출될 때마다 항상 `count`에서 `i`를 찾음
- 결국, `timer`는 이미 `10`이 되어버린 `i`만 출력하게 됨

<!-- ```js
for (var i = 1; i <= 5; i++) {
  setTimeout(() => {
    console.log(i);
  }, i * 1000);
}
```
- 1초 간격으로 6을 5번 출력 -->

- `var`로 선언한 변수는 함수 스코프를 따르기 때문에 전역에 선언하는 것과 같다.
  - setTimeout의 콜백 함수가 콜스택에 올라왔을 당시에 참조하는 `i`의 값은 `10`인 것
  <!-- - `setTimeout`의 콜백 함수가 콜스택에 올라왔을 당시에 참조하는 `i`의 값은 `6` -->

### 그럼 의도한대로 1~9를 출력하려면?

### 1. 새로운 스코프를 추가하여 반복 시마다 그곳에 각각 따로 값을 저장

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

- 중간에 IIFE를 덧붙여 `setTimeout()`에 걸린 함수를 클로저로 만들기
- 클로저는 만들어진 환경을 기억함
- `i`는 IIFE내에 `countingNumber`라는 형태로 주입되고, 클로저에 의해 각기 다른 환경속에 포함됨
- 반복문은 10회 반복되므로 10개의 환경이 생길 것이고, 10개의 서로 다른 환경에 10개의 서로 다른 `countingNumber`가 생김

#### cf) IIFE 매개변수로 i를 넘기지 않으면?

- **인자로 i를 넘기지 않는다면** 클로저가 참조하는 IIFE의 함수 스코프에서도 i값이 없으므로 생성 당시의 외부 스코프인 글로벌을 탐색하게 되고
  - 결국 모두 같은 i를 참조하게 된다.
- 반면에, **인자로 i를 넘기게 되면** IIFE로 만든 10개의 스코프에 모두 i라는 변수가 다른 값으로 생기므로
  - 정상적으로 동작할 수 있는 것이다.

#### cf) 콜백으로 넘기는 함수 자체를 IIFE로 만들면 되지 않나?

```js
function count() {
  var i;
  for (i = 1; i < 10; i += 1) {
    setTimeout(
      (function timer() {
        console.log(i);
      })(),
      i * 100
    );
  }
}
count();
```

- 이렇게 하면 1-9까지 출력은 되지만
- 함수 내부가 즉시 실행되어 버리므로 `setTimeout()`의 **0.1**초 딜레이가 작동하지 않게 된다.

<br>

### 2. ES6에서 추가된 블록 스코프를 이용

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

- for 반복문 안에서 let으로 선언하면 매번 반복할 때마다 변수가 선언
- 블록 스코프에서 존재하는 변수를 만드는 방법

<!-- var로 선언한거는 호이스팅되서 최상단으로 끌어올려지고, 바깥을 참조하지만 for문에서 let로 선언하면 스코프를 블록내에 가지므로 반복할때마다 변수가 선언돼서? -->

<br>

```js
function count() {
  for (let i = 1; i < 10; i += 1) {
    setTimeout(function timer() {
      console.log(i);
    }, i * 100);
  }
}
count();

// 즉, 위 코드는 이거랑 같다.
function count() {
  for (var i = 1; i < 10; i += 1) {
    let x = i;
    setTimeout(function timer() {
      console.log(x);
    }, i * 100);
  }
}
count();
```

- let은 블록 유효범위를 가지고 있다.
- for문의 초기화 식에서 선언한 변수를
- `반복문이 실행될 때마다 새롭게 선언해서 값을 대입`한다.
- 반복횟수별로 일종의 클로저 영역이 생성
- `setTimeout`에 전달된 콜백은 자신이 `setTimeout`으로 호출될 당시의 `for`반복문의 클로저의 `i`에 접근하게 되는 것
