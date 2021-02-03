- [useEffect](#useeffect)
- [useMemo, useCallback](#usememo)

<br>

## <a name="useeffect"></a>useEffect

> 리액트 컴포넌트가 렌더링 될때마다 특정 작업수행

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

- 두번째 파라미터로 배열안에 검사하고 싶은 값 추가

```js
useEffect(() => {
  console.log(name);
}, [name]);
```

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

- 함수 자체를 기억. 함수 생성 자체가 오래걸리거나 비용이 클때 사용
- **두번째 파라미터**에는 배열을 넣음
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
