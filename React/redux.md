프로젝트에서 전역적으로 필요한 상태를 관리할때, 리액트 애플리케이션은 컴포넌트 간에 데이터를 _props_ 로 전달하기 때문에 컴포넌트에서 필요한 데이터가 있으면 주로 루트 컴포넌트인 **App**의 _state_ 에 넣어서 관리한다.

![Redux2](./images/whyredux.svg)

이러한 방식은 컴포넌트 A에서 B, C, D, E ... 까지 값을 전달하기 위해 여러 컴포넌트를 거쳐야 한다. Redux를 사용하면 상태값을 컴포넌트에 종속시키지 않고, 상태 관리를 컴포넌트의 바깥에서 관리할 수 있게 된다. 따라서 Redux 같은 상태 관리 라이브러리를 사용하면 전역 상태 관리 작업을 편하게 할 수 있다.

<br>

### <a name="what-redux"></a>Redux란?

<hr/>

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
