- [useEffect](#useeffect)
- [useMemo, useCallback](#usememo)

<br>

## <a name="useeffect"></a>useEffect

- 리액트 컴포넌트가 렌더링 될때마다 특정 작업수행
- 서버 API호출, 이벤트 핸들러 등록/해제 등의 부수 효과(side effect)를 처리할 때 사용

#### 처음 렌더링 될때만 실행

- useEffect에서 설정한 함수를 컴포넌트가 화면에 **맨 처음 렌더링될때만 실행**하고, 업데이트시에는 실행하지 않으려면 두번째 파라미터로 **빈 배열** `[]`추가

```js
useEffect(() => {
  console.log("마운트 될때만 실행");
}, []);
```

- 두번째인자로 아무것도 안넣으면 **처음 렌더링 될때만 실행 + 리렌더링 될때마다 실행**

<br>

#### 특정 값이 업데이트될때만 실행

```js
useEffect(() => {
  console.log(name);
}, [name]);
```

- 두번째 파라미터로 배열안에 검사하고 싶은 값 추가
- 의존성배열(deps)에 여러개의 값이 전달되었을땐 그 중 하나라도 변경되면 이펙트가 실행됨
  - 이펙트 내부에서 사용되는 모든 변수는 deps에 명시를 해야한다.
  - 값이 변경되지 않는다는 것이 보장되는 함수는 예외적으로 의존성 배열에 입력하지 않아도 된다.

<br>

#### 조건안에 훅을 쓸수 없음

```js
const Example = () => {
  const [user, setUser] = useState(null);
  const [searchQuery, setSearchQuery] = useState("");

  if (searchQuery.length > 0) {
    useEffect(() => {
      const fetchFunc = async () => {
        const response = await fetch(`https://jsonplaceholder...`);
        const resJson = await response.json();
        setUser(resJson[0]);
      };
      fetchFunc();
    }, [searchQuery]);
  }
};
```

hook안에 넣어야함

```js
const Example = () => {
  const [searchQuery, setSearchQuery] = useState("");

  useEffect(() => {
    if (searchQuery.length > 0) {
      const fetchFunc = async () => {
        // ...
      };
      fetchFunc();
    }
  }, [searchQuery]);
};
```

<br>

#### Async

- 아래와 같이 `async` 사용 불가

```js
useEffect(async () => {
  await axios("adawgjwagaw");
}, [term]);
```

1. 방법1 : helper function을 만들기

```js
useEffect(() => {
  const search = async () => {
    await axios.get("adgfgagh");
  };
  search();
}, [term]);
```

2. 방법2 : 즉시실행함수 이용

```js
useEffect(() => {
  (async () => {
    await axios.get("adgfgagh");
  })();
}, [term]);
```

3. 방법3 : Promise 이용

```js
useEffect(() => {
  axios.get("agwagawhah").then((response) => {
    console.log(response.data);
  });
}, [term]);
```

<br>

### cleanup 함수

- 컴포넌트가 언마운트 되기 전이나 업데이트 되기 직전에 어떤 작업을 수행하고 싶을때 반환함

```js
useEffect(() => {
  console.log("Initial Render or term was changed");

  return () => {
    console.log("CLEAN UP");
  };
}, [term]);

// input value가 term이고 업데이트시
// CLEAN UP
// Initial Render or term was changed
```

<br>

## <a name="usememo"></a>useMemo

- 함수형 컴포넌트 내부에서 발생하는 연산을 최적화
- 함수의 리턴값을 기억함

## useCallback

- 함수도 객체이므로 변한다!!
- 함수 자체를 기억. 함수 생성 자체가 오래걸리거나 비용이 클때 사용
- **첫번째 피라미터**에 **생성하고 싶은함수**를, **두번째 피라미터**에 어떤 값이 바뀔때 함수를 새로 생성해야하는지 알려주는 **배열**을 넣음
  - useEffect처럼 얘가 바뀌면 실행
- 자식컴포넌트의 props로 넘길때는 부모로부터 받은 함수가 계속 같구나 라고 인식되게 함수를 useCallback으로 감싼다.

```js
// 그래야 최적화가 된다.
const onChangeId = useCallback((e) => {
  setId(e.target.value);
}, []);
```

#### useMemo, useCallback은 기억하는 함수

- 무조건 감싸는게 좋지는 않음
- 까먹어야할 필요도 있음
  - 두번째 배열 요소들이 바뀌었을때
  - ex) 로또 번호 추첨

<br>

## 의존 배열로 함수를 넘길때

- js의 함수 동등성을 판단하는 방식 때문에 무한루프가 발생
  - _fetchUser_ 는 함수라서, _userId_ 가 바뀌든 말든 컴포넌트가 렌더링될때마다 새로운 참조값으로 변경됨
  - `useEffect()` 함수가 호출되어 _user_ 상태값이 바뀜 -> 다시 렌더링 -> 다시 `useEffect()` 함수가 호출되는 무한루프

```js
import React, { useState, useEffect } from "react";

function Profile({ userId }) {
  const [user, setUser] = useState(null);

  const fetchUser = () =>
    fetch(`https://your-api.com/users/${userId}`)
      .then((response) => response.json())
      .then(({ user }) => user);

  useEffect(() => {
    fetchUser().then((user) => setUser(user));
  }, [fetchUser]);

  // ...
}
```

- `useCallback()` 함수를 이용하면 컴포넌트가 다시 랜더링되더라도 _fetchUser_ 함수의 참조값을 동일하게 유지할 수 있음
  - 따라서 `useEffect()` 에 넘어온 함수는 _userId_ 값이 변경되지 않는한 재호출되지 않음

```js
import React, { useState, useEffect } from "react";

function Profile({ userId }) {
  const [user, setUser] = useState(null);

  const fetchUser = useCallback(
    () =>
      fetch(`https://your-api.com/users/${userId}`)
        .then((response) => response.json())
        .then(({ user }) => user),
    [userId]
  );

  useEffect(() => {
    fetchUser().then((user) => setUser(user));
  }, [fetchUser]);

  // ...
}
```

<br>

### etc

> it is safe to omit dispatch function from the dependency array because its guaranteed to never change but still it won't do any harm if you add it as a dependency.

- 리액트에서 dispatch는 변하지 않는 값(항상 고정된 값)이므로 의존성 배열에서 제거할 수 있음
- 그러나 React hooks lint 규칙은 이걸 몰라서 dependency 배열에 dispatch를 추가해야한다고 경고함
- 아래와같이 추가하여 간단한 해결

```js
export const Todos() = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchTodos())
  // Safe to add dispatch to the dependencies array
  }, [dispatch])
}
```
