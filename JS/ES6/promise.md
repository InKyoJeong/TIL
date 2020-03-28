## 프로미스(Promise)

```js
function say(callback) {
  setTimeout(function() {
    callback();
  }, 3000);
}
say(function() {
  console.log("A");
  say(function() {
    console.log("B");
    say(function() {
      console.log("C");
    });
  });
});

// A
// B
// C
// 3초후에 "A"를 표시하고, 3초후에 "B"를 표시하고, 마지막으로 3초후에 "C"를 표시한다.
```

이렇게 콜백함수를 여러 개 중첩하면 작업내용을 이해하기 어려워진다. 이것을 콜백 지옥(Callback Hell)이라고도 한다. `Promise`를 이용하면 콜백 헬을 극복하고 비동기 처리도 간결하게 작성할 수 있다.

Promise를 사용하려면 먼저 **Promise객체**를 생성해야 한다.

```js
const promise = new Promise(function(resolve, reject){
    ...
});

// Arrow Function
const promise = new Promise((resolve, reject) => {
    ...
});
```

- **_resolve_** : 함수 안의 처리가 끝났을 때 호출해야하는 콜백함수. 어떠한 값도 인수로 넘길 수 있다. 다음 처리를 실행하는 함수에 전달된다.
- **_reject_** : 함수 안의 처리가 실패했을 때 호출해야하는 콜백함수. 어떠한 값도 인수로 넘길수 있다. 주로 오류 메시지 문자열을 인수로 사용한다.

<br>

### then/catch 메서드

```js
promise.then(ouFulfilled);
```

```js
promise.catch(onRejected);
```

프로미스(promise) 내부에서 _resolve_ 가 호출되면 _then_ 이 실행되고, _reject_ 가 호출되면 _catch_ 가 실행된다. _resolve_ 와 _reject_ 에 넣어준 인자는 각각 _then_ 과 _catch_ 의 매개변수에서 받을 수 있다.

```js
// 2의 거듭제곱을 구하는 예시

const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    const input = parseInt(prompt("10미만 숫자를 입력하시오"));
    if (input < 10) {
      resolve(input);
    } else {
      reject(`오류: ${input}은 10 이상이거나 숫자가 아닙니다.`);
    }
  }, 2000);
});

promise
  .then(num => {
    console.log(`2^${num} = ${Math.pow(2, num)}`);
  })
  .catch(error => {
    console.log(error);
  });

//Promise {<pending>}
// 2^7(입력) = 128
```

코드를 입력하면 2초뒤 "10미만 숫자를 입력하시오"라는 입력창이 뜬다. 입력한 숫자가 10미만이면 _then_ 으로 넘긴 함수가 실행되고, 그렇지 않으면 _catch_ 에 넘긴 함수가 실행된다.

<br>

### then의 두번째 인수

```js
promise.then(onFulfilled, onRejected);
```

_then_ 메서드에 두 번째 인수로 실패 콜백함수를 지정할 수 있다. 그러면 _then_ 메서드에서 처리할 내용과 _catch_ 메서드에서 처리할 내용을 _then_ 메서드 하나로 담을 수 있다.

위의 **_then/catch_** 예시를 아래와 같이 수정할 수 있다.

```js
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    const input = parseInt(prompt("10미만 숫자를 입력하시오"));
    if (input < 10) {
      resolve(input);
    } else {
      reject(`오류: ${input}은 10 이상이거나 숫자가 아닙니다.`);
    }
  }, 2000);
});

promise.then(
  num => {
    console.log(`2^${num} = ${Math.pow(2, num)}`);
  }, // 처리가 성공으로 끝날때 호출
  error => {
    console.log(error);
  } //처리가 실패로 끝날때 호출
);
```

<br>

### Promise가 실행하는 콜백함수에 인수 넘기기

_buySomething_ 함수에 넘긴 인수를 **Promise** 객체가 실행하는 익명 함수 안에서 사용하는 예제이다.

```js
function buySomething(nowMoney) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const pay = parseInt(prompt("금액 입력"));
      const remain = nowMoney - pay;
      if (remain >= 0) {
        console.log(`${pay}원 지불`);
        resolve(remain);
      } else {
        reject(`잔액부족: 현재 잔액${nowMoney}원`);
      }
    }, 2000);
  });
}

buySomething(1000)
  .then(remain => {
    console.log(`잔액: ${remain}원`);
  })
  .catch(error => {
    console.log(error);
  });

// 금액 입력: 200(입력)
// 200원 지불
// 잔액: 800원
```

현재금액(_nowMoney_)을 인수로 넘겨 실행하면 지불할 금액을 2초후 입력할 수 있다. 차액이 0이상이면 _then_ 에 넘긴 함수가 **"잔액"을 표시**, 0미만으로 부족하면 _catch_ 에 넘긴 함수가 **"잔액부족" 오류 메세지를 표시**한다.

<br>

### Promise로 비동기 처리 연결하기

_then_ 이나 _catch_ 에서 다시 다른 _then_ 이나 _catch_ 를 붙일 수 있다. 이전 _then_ 의 return값을 다음 _then_ 의 매개변수로 넘긴다. 프로미스를 return한 경우 프로미스가 수행된 후 다음 _then_ 또는 _catch_ 가 호출된다.

```js
function buySomething(nowMoney) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const pay = parseInt(prompt("금액 입력"));
      const remain = nowMoney - pay;
      if (remain >= 0) {
        console.log(`${pay}원 지불`);
        resolve(remain);
      } else {
        reject(`잔액부족: 현재 잔액${nowMoney}원`);
      }
    }, 2000);
  });
}

buySomething(1000)
  .then(remain => {
    console.log(`잔액: ${remain}원`);
    return buySomething(remain);
  })
  .then(remain => {
    console.log(`잔액: ${remain}원`);
    return buySomething(remain);
  })
  .then(remain => {
    console.log(`잔액: ${remain}원`);
    return buySomething(remain);
  })
  .catch(error => {
    console.log(error);
  });
```

금액 입력을 여러번 받게 수정했다.

```
100원 지불
잔액: 900원
200원 지불
잔액: 700원
400원 지불
잔액: 300원
100원 지불
```

> #### 위에서는 then이 모두 같은 Promise객체를 반환하지만, then마다 다른 Promise객체를 반환해서 다른 비동기 처리를 연결하여 순차적으로 실행하게 할 수도 있다.

<br>

### Promise.all

프로미스 여러 개를 한번에 실행할 수 있는 방법이 있다. 지금까지는 비동기 처리 여러 개를 직렬로 연결해서 순차적으로 실행 했지만 **Promise**객체의 **all** 메서드를 이용하면 비동기 처리 여러 개를 병렬로 할 수 있다.

```js
Promise.all(iterable);
```

- **_iterable_** : Array와 같이 순회(반복) 가능한(iterable) 객체. 예를 들어 **Promise**객체가 요소로 들어있는 배열을 넘기면 **Promise.all** 메서드는 그 안의 요소로 들어있는 모든 **Promise** 객체를 병렬로 실행한다.

```js
function buySomething(name, nowMoney) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const pay = parseInt(prompt(`${name} : 금액 입력`));
      const remain = nowMoney - pay;
      if (remain >= 0) {
        console.log(`${name} : ${pay}원 지불`);
        resolve(remain);
      } else {
        reject(`${name} : 잔액부족: 현재 잔액${nowMoney}원`);
      }
    }, 2000);
  });
}

Promise.all([
  buySomething("John", 500),
  buySomething("Mary", 1000),
  buySomething("Bill", 1500)
])
  .then(remain => {
    console.log(remain);
  })
  .catch(error => {
    console.log(error);
  });
```

```
John : 200원 지불
Mary : 600원 지불
Bill : 1000원 지불
▶︎(3) [300, 400, 500]
```
