#### reference

> [https://dmitripavlutin.com/use-react-memo-wisely](https://dmitripavlutin.com/use-react-memo-wisely)<br/>https://ui.toast.com/weekly-pick/ko_20190731

<br>

- UI 성능을 증가 시키기 위해 React는 고차 컴포넌트 `React.memo()` 제공
- 렌더링 결과를 메모이징 함으로써, 불필요한 리렌더링을 건너뜀

## React.memo() 란?

- React는 컴포넌트를 렌더링한뒤, 이전 렌더링 결과와 비교해서 DOM 업데이트를 결정함
  - 렌더 결과가 이전과 다르면 DOM을 업데이트함
- 컴포넌트가 `React.memo()`로 래핑 될때, React는 컴포넌트를 렌더링 하고 그 결과를 메모이징(memoizing)함
  - **그 다음 렌더링이 일어날때 `props`가 같다면, 메모이징된 내용을 재사용**

```jsx
export function Movie({ title, releaseDate }) {
  return (
    <div>
      <div>Movie title: {title}</div>
      <div>Release date: {releaseDate}</div>
    </div>
  );
}

export const MemoizedMovie = React.memo(Movie);
```

- 위 코드에서 _MemoizedMovie_ 의 렌더링 결과는 메모이징 되어있음
- 만약 `props` 가 변경 되지 않는다면 (여기선 _title, releaseData_ ) 다음 렌더링 때 메모이징 된 내용을 그대로 사용함

```jsx
// 첫 렌더이다. React는 MemoizedMovie 함수를 호출
<MemoizedMovie
  movieTitle="Heat"
  releaseDate="December 15, 1995"
/>

// 다시 렌더링 할 때 React는 MemoizedMovie 함수를 호출하지 않음
// 리렌더링을 막는다.
<MemoizedMovie
  movieTitle="Heat"
  releaseDate="December 15, 1995"
/>
```

- 메모이징 한 결과를 재사용 함으로써, React에서 리렌더링을 할 때 가상 DOM에서 달라진 부분을 확인하지 않아 성능상의 이점을 누릴 수 있다.

<br>

## React.memo()를 써야할 때

#### 같은 props로 렌더링이 자주 일어나는 컴포넌트

```js
function MovieViewsRealtime({ title, releaseDate, views }) {
  return (
    <div>
      <Movie title={title} releaseDate={releaseDate} />
      Movie views: {views}
    </div>
  );
}
```

```js
// Initial render
<MovieViewsRealtime
  views={0}
  title="Forrest Gump"
  releaseDate="June 23, 1994"
/>

// After 1 second, views is 10
<MovieViewsRealtime
  views={10}
  title="Forrest Gump"
  releaseDate="June 23, 1994"
/>

// After 2 seconds, views is 25
<MovieViewsRealtime
  views={25}
  title="Forrest Gump"
  releaseDate="June 23, 1994"
/>
```

- 위에서는 _views_ 가 새로 업데이트 될때마다 `MoviewViewsRealtime` 컴포넌트도 리렌더링됨
- `Movie` 컴퍼넌트도 _title_ 이나 _releaseData_ 가 같은데도 리렌더링 됨
  - 따라서 `Movie` 컴포넌트에 메모이제이션을 적용하기 좋음

```js
export function Movie({ title, releaseDate }) {
  return (
    <div>
      <div>Movie title: {title}</div>
      <div>Release date: {releaseDate}</div>
    </div>
  );
}

export const MemoizedMovie = React.memo(Movie);
```

```js
function MovieViewsRealtime({ title, releaseDate, views }) {
  return (
    <div>
      <MemoizedMovie title={title} releaseDate={releaseDate} />
      Movie views: {views}
    </div>
  );
}
```

<br>

## React.memo()를 쓰지 말아야 할 때

- 렌더링될 때 _props_ 가 다른 경우가 대부분인 컴포넌트의 경우 메모이제이션 기법의 이점을 얻기 힘들다.

<br>

## React.memo()와 콜백함수

- **함수객체는 일반객체와 동일한 비교 원칙**을 따름
- 아래와 같이 _sum1_ 과 _sum2_ 는 다른 함수

```js
function sum() {
  return (a, b) => a + b;
}

const sum1 = sum();
const sum2 = sum();

console.log(sum1 === sum2); // false

console.log(sum1 === sum1); // true
console.log(sum2 === sum2); // true
```

<br>

#### 메모이제이션을 적용할 때는 콜백을 받는 컴퍼넌트 관리에 주의

- 부모 컴퍼넌트가 자식 컴퍼넌트의 콜백 함수를 정의한다면, 새 함수가 암시적으로 생성될 수 있음

```js
function MyApp({ store, cookies }) {
  return (
    <div className="main">
      <header>
        <MemoizedLogout
          username={store.username}
          onLogout={() => cookies.clear()}
        />
      </header>
      {store.content}
    </div>
  );
}
```

```js
function Logout({ username, onLogout }) {
  return <div onClick={onLogout}>Logout {username}</div>;
}

const MemoizedLogout = React.memo(Logout);
```

- 동일한 `username` 값이 전달되더라도, `MemoizedLogout`은 새로운 `onLogout` 콜백 때문에 리렌더링을 하게 됨
  - 따라서 메모이제이션이 중단됨
  - 이 문제를 해결하려면 `onLogout` `props` 의 값을 매번 동일한 콜백 인스턴스로 설정하면됨
  - `useCallback()을 이용` 해서 콜백 인스턴스를 보존시키기

```js
function MyApp({ store, cookies }) {
  const onLogout = useCallback(() => {
    cookies.clear();
  }, []);

  return (
    <div className="main">
      <header>
        <MemoizedLogout username={store.username} onLogout={onLogout} />
      </header>
      {store.content}
    </div>
  );
}
```

- `useCallback` 으로 감싸서 항상 같은 함수 인스턴스를 반환하게 함
- 따라서 이제 `MemoizedLogout` 의 메모이제이션이 정상적으로 동작한다.
