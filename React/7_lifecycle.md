## 컴포넌트의 라이프사이클 메서드

- 모든 컴포넌트에는 라이프사이클(수명 주기)가 존재
- 수명은 페이지에 렌더링되기전 준비과정에서 시작, 페이지에서 사라질때 끝
- 리액트 프로젝트를 하다보면 가끔 컴포넌트를 처음으로 렌더링할때 어떤 작업을 처리하거나, 업데이트 하기 전후로 작업을 하거나, 불필요한 업데이트를 방지해야할 때도 있음
- 이럴때 컴포넌트의 라이프사이클 메서드를 사용함
- 클래스형 컴포넌트에서만 사용할 수 있지만, 함수형 컴포넌트에서는 대신 Hooks를 이용하여 비슷하게 가능

<br>

## 라이프사이클 메서드 이해

- 라이프사이클 메서드의 종류는 총 9가지
- **_Will_** 접두사 : 어떤 작업을 작동하기 **전에** 실행됨
- **_Did_** 접두사 : 어떤 작업을 작동한 **후에** 실행됨
- 라이프사이클은 총 3가지 카테고리로 나눔
  - **마운트**
  - **업데이트**
  - **언마운트**

### 마운트

- 마운트(mount) : DOM이 생성되고 웹브라우저에 나타나는것
- 이때 호출하는 메서드
  - `constructor` : 컴포넌트를 새로 만들때마다 호출되는 클래스 생성자 메서드
  - `getDerivedStateFromProps` :**_props_** 에 있는 값을 **_state_** 에 넣을때 사용하는 메서드
  - `render` : 준비한 UI를 렌더링하는 메서드
  - `componentDidMount` : 컴포넌트가 웹 브라우저상에 나타난후 호출하는 메서드

<br>

### 업데이트

- 컴포넌트는 다음의 경우 업데이트함
  - `props`가 바뀔때
  - `state`가 바뀔때
  - 부모 컴포넌트가 리렌더링될때
  - `this.forceUpdate`로 강제 렌더링을 트리거할때
- 컴포넌트를 업데이트할때 호출하는 메서드
  - `getDerivedStateFromProps` : **_props_** 의 변화에 따라 **_state_** 값에도 변화를 주고 싶을때 사용
    - 이 메서드는 마운트 과정에서도 호출됨. 업데이트가 시작하기 전에도 호출됨.
  - `shouldComponentUpdate` : 컴포넌트가 리렌더링을 해야할지 말아야할지 결정하는 메서드
    - 이 메서드에서는 _true_ 혹은 _false_ 를 반환해야함.
    - _true_ 를 반환하면 다음 라이프사이클 메서드를 계속실행, _false_ 를 반환하면 작업을 중지 (컴포넌트가 리렌더링되지 않음)
    - 만약 특정 함수에서 `this.forceUpdate()`함수를 호출하면 이 과정은 생략됨
  - `render` : 컴포넌트를 리렌더링
  - `getSnapshotBeforeUpdate` : 컴포넌트 변화를 DOM에 반영하기 바로 직전에 호출하는 메서드
  - `componentDidUpdate` : 컴포넌트의 업데이트 작업이 끝난 후 호출하는 메서드

<br>

### 언마운트

- 언마운트(unmount) : 마운트의 반대. 컴포넌트를 DOM에서 제거하는 것
  - `componentWillUnmount` : 컴포넌트가 웹 브라우저상에서 사라지기 전에 호출하는 메서드

<br>

## 라이프 사이클 메서드 정리

### render() 함수

```js
render() {...}
```

- 컴포넌트 모양새를 정의
- 라이프 사이클 메서드 중 유일한 필수 메서드
- 이 메서드 안에서 `this.props`와 `this.state`에 접근가능
- DOM 정보를 가져오거나 `state`에 변화를 줄때는 `componentDidMount`에서 해야함

<br>

### constructor 메서드

```js
constructor(props) {...}
```

- 컴포넌트의 생성자 메서드로 컴포넌트를 만들때 처음으로 실행됨
- 이 메서드에서 초기 `state`를 정할 수 있음

<br>

### getDerivedStateFromProps 메서드

- 리액트 v16.3 이후에 새로만든 라이프사이클 메서드
- `props`로 받아온 값을 `state`에 동기화시키는 용도로 사용

<br>

### componentDidMount 메서드

```js
componentDidMount() {...}
```

- 컴포넌트를 만들고, 첫 렌더링을 다 마치고 실행
- 이 안에서 다른 자바스크립트 라이브러리나 프레임워크 함수를 호출가능
- 이벤트 등록, _setTimeout_, _setInterval_, 네트워크 요청 등 비동기 작업 처리가능

<br>

### shouldComponentUpdate 메서드

```js
shouldComponentUpdate(nextProps, nextState) {...}
```

- `props` 또는 `state`를 변경했을때, 리렌더링을 시작할지 여부를 지정
- 반드시 _false_ 나 _true_ 를 반환해야함
  - 이 메서드를 따로 생성하지않으면 디폴트는 _true_
  - _false_ 를 반환하면 업데이트 과정은 여기서 중지됨
- 이 메서드 안에서 현재 `props`와 `state`는 `this.props`와 `this.state`로 접근하고, 새로 설정될 `props`또는 `state`는 `nextProps`와 `nextState`로 접근가능

<br>

### getSnapshotBeforeUpdate 메서드

- 리액트 v16.3이후 만든 메서드
- `render`에서 만들어진 결과물이 브라우저에 실제로 반영되기 직전에 호출됨
- 이 메서드에서 반환하는 값은 `ComponentDidUpdate`에서 세번째 매개변수 `snapshot`으로 전달받을 수 있음
- 주로 업데이트하기 직전 값을 참고할일이 있을때 활용

<br>

### ComponentDidUpdate 메서드

```js
ComponentDidUpdate(prevProps, prevState, snapshot) {...}
```

- 리렌더링 완료한 후 실행
- `prevProps`또는 `prevState`를 사용해 컴포넌트가 이전에 가졌던 데이터에 접근가능

<br>

### componentWillUnmount 메서드

```js
componentWillUnmount() {...}
```

- 컴포넌트를 DOM에서 제거할 때 실행
- `componentDidMount` 에서 등록한 이벤트, 타이머, 직접 생성한 DOM이 있으면 여기서 제거작업을 해야함

<br>

### componentDidCatch 메서드

- 리액트 v16에서 새로 도입
- 컴포넌트 렌더링 도중 에러가 발생하면 오류 UI를 보여주게 함
