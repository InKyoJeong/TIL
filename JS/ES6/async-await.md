## async / await

**_async/await_** 문법은 기존의 비동기 처리 방식인 콜백 함수와 프로미스의 단점을 보완하고 코드를 더 깔끔하게 해준다. (따라서 async/await을 이해하기 전에 먼저 [비동기처리 및 콜백함수와 Promise](https://ingg.io/js-work/#async)에 대해 알아야할 필요가 있다.)

먼저 아래와 같은 코드가 있다고 하자.

```js
function makeRequest(company) {
  return new Promise((resolve, reject) => {
    console.log(`Making Request to ${company}`);
    if (company === "Google") {
      resolve("Google, Hi");
    } else {
      reject("It's not Google");
    }
  });
}

function processRequest(response) {
  return new Promise((resolve, reject) => {
    console.log("Processing response");
    resolve(`Extra Information + ${response}`);
  });
}

makeRequest("Google")
  .then(response => {
    console.log("Response Received");
    return processRequest(response);
  })
  .then(processedResponse => {
    console.log(processedResponse);
  })
  .catch(error => {
    console.log(error);
  });
```

```
Making Request to Google
Response Received
Processing response
Extra Information + Google, Hi
```

에러를 받기위해 `makeRequest('Google').then(...)` 이부분을 `makeRequest('Facebook').then(...)` 으로 바꿔보면 이렇게 출력된다.

```
Making Request to Facebook
It's not Google
```

<br>

이번에는 위의 코드를 **_async/await_** 으로 바꿔보자.

```js
function makeRequest(company) {
  return new Promise((resolve, reject) => {
    console.log(`Making Request to ${company}`);
    if (company === "Google") {
      resolve("Google, Hi");
    } else {
      reject("It's not Google");
    }
  });
}

function processRequest(response) {
  return new Promise((resolve, reject) => {
    console.log("Processing response");
    resolve(`Extra Information + ${response}`);
  });
}

async function testAsync() {
  const response = await makeRequest("Google");
  console.log("Response Received");
  const processedResponse = await processRequest(response);
  console.log(processedResponse);
}

testAsync();
```

```
Making Request to Google
Response Received
Processing response
Extra Information + Google, Hi
```

그렇다면 에러처리는 어떻게 할까?

예를들어, 여기서도 `makeRequest('Google');`을 `makeRequest('Facebook');` 으로 바꿔보자.

```
Making Request to Facebook
Uncaught (in promise) It's not Google
```

그러면 **_Uncaught Error_** 가 발생한다.

프로미스(_Promise_)의 `.catch` 와 같이 *async/await*에서는 `try/catch`문으로 이것을 해결할 수 있다. `try/catch` 문을 이용해서 에러를 처리해보자.

```js
async function testAsync() {
  try {
    const response = await makeRequest("Facebook");
    console.log("Response Received");
    const processedResponse = await processRequest(response);
    console.log(processedResponse);
  } catch (error) {
    console.log(error);
  }
}
```

```
Making Request to Facebook
It's not Google
```

이렇게하면 위의 _then/catch_ 와 같게 동작한다.

<!-- ---

// await은 promise가 resolve돼서 결과값이 넘어올때까지 기다린다.

```js
function delayP(sec) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(new Date().toISOString());
    }, sec * 1000);
  });
}

async function myAsync() {
  delayP(3).then(time => {
    console.log(time);
  });
  return "async";
}
myAsync().then(result => {
  console.log(result);
});

// async
// (3초뒤에)
// 2020-03-29T01:09:04
```

3초 동안 기다린 다음 async를 리턴하려면 await을 쓴다.
promise가 resolve될때까지 다음으로 넘어가지 않는다.
await으로 기다렸다가 나중에 리턴할수있다.

```js
function delayP(sec) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(new Date().toISOString());
    }, sec * 1000);
  });
}
async function myAsync() {
  await delayP(3);
  return "async";
}
myAsync().then(result => {
  console.log(result);
});

// (3초뒤에)
// async
```

```js
//이렇게 써보면 3초뒤에 시간이 찍히고 async가 찍힌다.
function delayP(sec) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(new Date().toISOString());
    }, sec * 1000);
  });
}
async function myAsync() {
  const time = await delayP(3);
  console.log(time);
  return "async";
}
myAsync().then(result => {
  console.log(result);
});

// (3초뒤에)
// 2020-03-29T01:21:31.994Z
// async
```

```js
//일반함수 앞에 await을 넣어도 된다.

function delayP(sec) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(new Date().toISOString());
    }, sec * 1000);
  });
}
function normalFun() {
  return "wow";
}

async function myAsync() {
  const result = await normalFun();
  console.log(result);

  return "async";
}

myAsync().then(result => {
  console.log(result);
});

//wow
//async
```

// 정리하면 await은 뒤의 함수를 기다리는데 그게 프로미스면 프로미스가 resolve되길 기다린다.
// 따라서 만약 normalFun()부분이 delayP()일경우엔 result값으로 Promise의 resolve하는 값이 오는 것이다. -->
