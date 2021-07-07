프로젝트에서 전역적으로 필요한 상태를 관리할때, 리액트 애플리케이션은 컴포넌트 간에 데이터를 _props_ 로 전달하기 때문에 컴포넌트에서 필요한 데이터가 있으면 주로 루트 컴포넌트인 **App**의 _state_ 에 넣어서 관리한다.

![Redux2](./images/whyredux.svg)

이러한 방식은 컴포넌트 A에서 B, C, D, E ... 까지 값을 전달하기 위해 여러 컴포넌트를 거쳐야 한다. Redux를 사용하면 상태값을 컴포넌트에 종속시키지 않고, 상태 관리를 컴포넌트의 바깥에서 관리할 수 있게 된다. 따라서 Redux 같은 상태 관리 라이브러리를 사용하면 전역 상태 관리 작업을 편하게 할 수 있다.

<br>

## Redux란?

![redux](./images/redux.jpg)

상태를 조작하려는 컴포넌트가 있을때, 미리 정의된 정보 패키지인 액션(**action**)을 디스패치(**dispatch**)한다. 디스패치는 액션을 발생시키는 것이라고 생각하면 된다. 그러면 이 액션은 변화를 일으키는 함수인 리듀서(**reducer**)라는 것에 도달하고, 리듀서는 스토어(**store**)의 상태를 업데이트한다.

그리고 해당 스토어의 상태가 변경되면, 다른 컴포넌트들로부터 해당 스토어에 대한 구독(**subscription**)을 가질 수 있고, 구독은 스토어에서 트리거된다.

이제 만약 업데이트에 관심있는 컴포넌트가 있으면 구독을 설정할 수 있고 업데이트에 대한 정보를 받아서 새로운 상태를 얻을 수 있다.

짧게 요약하면, 다음과 같은 흐름이다.

`dispatch(action) -> Reducer 작동 -> store의 state변경 -> 변경된 state가 state를 구독(subscribe)하고 있는 컴포넌트에게 전달`

<br>

### action

#### 매번 액션 쓰지않고 동적으로 만들기

```js
const changeNickname = {
  type: "CHANGE_NICKNAME",
  data: "AAA",
};

const changeNickname = {
  type: "CHANGE_NICKNAME",
  data: "BBB",
};
```

- 매번 위와같이 액션을 만들지 않고 **action creator** 를 만들기

```js
const changeNickname = (data) => {
  return {
    type: "CHANGE_NICKNAME",
    data,
  };
};

changeNickname("바꿀 닉네임");
```

<br>

### 리듀서의 기본 꼴

```js
const initialState = {
  //...
};

const reducer = (state = initialState, action) => {
  switch (action.type) {
    default:
      return state;
  }
};

export default reducer;
```

<br>

## redux-thunk

- 하나의 액션에서 _dispatch_ 를 여러번 가능
- 하나의 비동기 액션안에 여러개의 동기 액션을 넣을 수 있음

```js
const INCREMENT_COUNTER = "INCREMENT_COUNTER";

function increment() {
  return {
    type: INCREMENT_COUNTER,
  };
}

function incrementAsync() {
  return (dispatch) => {
    setTimeout(() => {
      // Yay! Can invoke sync or async actions with `dispatch`
      dispatch(increment());
    }, 1000);
  };
}
```

## redux-saga

- _thunk_ 는 위처럼 딜레이를 직접 구현해야 하지만, _saga_ 는 그러한 기능들이 내장됨
  - 또다른 장점은, 예를들어 _thunk_ 에서는 실수로 클릭을 두번한다면 요청이 두번간다.
  - 그러나 _saga_ 는 _takeLatest_ 로 마지막것만 요청보내는 기능, 몇초에 몇번까지 허용하는 _throttle_ 등의 기능이 있음

#### generator

```js
function* genFunction() {
  while (true) {
    yield "무한";
  }
}

const g = genFunction();
g.next(); //{value: "무한", done: false}
g.next(); //{value: "무한", done: false}
```

- 제네레이터에서는 이게 무한 반복이 안된다

#### call

- `call` 은 동기
- `put`은 *dispatch*라고 생각

```js
function loginAPI(data) {
  return axios.post("/api/login", data);
}

function* logIn(action) {
  try {
    const result = yield call(loginAPI, action.data); // loginAPI가 리턴할때까지 기다려서 result에 넣는다
    yield put({
      type: "LOG_IN_SUCCESS",
      data: result.data,
    });
//...
```

- then을 하는것과 마찬가지

```js
function* logIn(action) {
  try {
    const result = yield call(loginAPI, action.data);
    axios.post("/api/login");
      .then((result)=>{
        yield put({
        type: "LOG_IN_SUCCESS",
        data: result.data,
        });
      })
  }
```

- **call** 을 쓰면 _loginAPI(action.data)_ 이런식이 아니라 펼쳐줘야 한다.
  - _call(loginAPI, action.data)_

<br>

#### fork

- `fork`는 비동기함수 호출. 요청보내고 바로 다음 실행. 블로킹을 하지않음

```js
function* logIn() {
  try {
    const result = yield fork(loginAPI);  // 기다리지 않고 바로 다음이 실행되버린다.
    yield put({
      type: "LOG_IN_SUCCESS",
      data: result.data,
    });
//...
```

이렇게 하는것과 같다.

```js
function* logIn() {
  try {
    axios.post("/api/login");
    yield put({
      type: "LOG_IN_SUCCESS",
      data: result.data,
    });
//...
```

<br>

#### take

- 비동기 액션들이 saga에서는 이벤트리스너 비슷한 역할
  - **LOG_IN** 액션이 들어오면 _logIn_ 제네레이터 함수를 실행

```js
function* watchLogin() {
  yield take("LOG_IN", logIn);
}
```

- 문제는 딱 한번 실행되므로 while로 감싸서 이벤트리스터 같은 역할을 하게 할 수 있다.

```js
function* watchLogin() {
  while (true) {
    yield take("LOG_IN", logIn);
  }
}
```

<br>

#### takeEvery

- 그러나 직관적이지 않으므로 보통 `takeEvery` 사용
- *while take*는 동기적으로 동작하지만 _takeEvery_ 는 비동기로 동작한다.

```js
function* watchLogin() {
  yield takeEvery("LOG_IN_REQUEST", logIn);
}
```

<br>

#### takeLatest

- 여러 액션이 중첩되어 디스패치되면 기존 것들은 무시하고 가장 **마지막** 액션만 처리.
  - 가끔가다 실수로 두번 눌렀을때. ex)로그인, 글쓰기 등 (_takeEvery_ 는 두번 실행됨)
  - **이미 완료된 작업을 취소하는게 아니라**, 완료되지 않은것을 없애는것임. ex) 동시에 로딩중이거나..
  - 첫번째것만 하고싶으면 _takeLeading_ 도 있다.

```js
function* watchAddPost() {
  yield takeLatest("ADD_POST_REQUEST", addPost);
}
```

- 주의할 점은 : 응답을 취소하는것. 요청까진 취소를 못해서 서버에는 데이터가 두번 저장됨
- 서버에서 검사해서 첫번째 요청은 등록하고, 두번째는 취소하는 등의 검증을 해도된다.

<br>

#### throttle

- `throttle`을 쓰면 요청 보내는것까지 제한을 둘 수 있다.
- 아래처럼 2초 설정해놓으면 2초 동안은 request를 한번만 실행가능

```js
function* watchAddPost() {
  yield throttle(2000, "ADD_POST_REQUEST", addPost);
}
```

- 쓰로틀 vs 디바운싱
  - **쓰로틀**은 마지막 함수가 호출된 후 일정 시간이 지나기 전에 다시 호출되지 않도록 하는것
  - **디바운싱**은 연이어 호출되는 함수들중 마지막 함수만 호출하는 것
