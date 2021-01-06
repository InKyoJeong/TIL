## useEffect

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
