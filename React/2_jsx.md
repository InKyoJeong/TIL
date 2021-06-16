## JSX란

- 자바스크립트의 확장 문법이고 XML과 비슷함
- 브라우저에서 실행되기전에 코드가 번들링되면서 바벨을 이용해 일반 자바스크립트 형태로 변환됨

### JSX 장점

- 가독성, 활용도가 높다.

### JSX 문법

#### 컴포넌트는 반드시 부모요소 하나로 감싸야한다.

예를 들어, 아래와 같은 코드처럼 요소들을 `div`로 감싼다.

```jsx
import React from "react";

function App() {
  return (
    <div>
      <h1>hello</h1>
      <h2>react</h2>
    </div>
  );
}
export default App;
```

<br>

- `div`가 아닌 리액트 v16부터 도입된 `Fragment`를 이용해 감싸도 된다.
- `import`에 `Fragment` 컴포넌트를 추가한다.

```jsx
import React, { Fragment } from "react";

function App() {
  return (
    <Fragment>
      <h1>hello</h1>
      <h2>react</h2>
    </Fragment>
  );
}
export default App;
```

- `Fragment` 대신 `<> </>`로 표현할 수 있다.

```jsx
import React from "react";

function App() {
  return (
    <>
      <h1>hello</h1>
      <h2>react</h2>
    </>
  );
}
export default App;
```

<br>

#### 자바스크립트 표현식을 쓸 수 있다.

```jsx
function App() {
  const greet = "world";
  return (
    <>
      <h1>hello</h1>
      <h2>react {greet}</h2>
    </>
  );
}
```

<br>

#### if문은 삼항 연산자로 대체

- JSX 내부에서 `if`문은 사용할 수 없다.
- JSX 밖에서 `if`문을 쓰거나 `{}`으로 삼항 연산자(조건부 연산자)를 사용한다.

```jsx
function App() {
  const greet = "world";
  return (
    <>
      <h1>hello</h1>
      <h2>
        {greet === "world" ? (
          <h3>nice to meet you!!</h3>
        ) : (
          <h3>bye react!!!!</h3>
        )}
      </h2>
    </>
  );
}
```

<br>

#### && 연산자

- 조건을 만족하지 않을때 아무것도 렌더링 하지 않으려면 `null`을 렌더링 한다.

```jsx
<>
  <h1>hello</h1>
  <h2>{greet === "world" ? <h3>nice to meet you!!</h3> : null}</h2>
</>
```

- 이때 `&&` 연산자를 사용하면 더 짧게 할 수 있다.

```jsx
<>
  <h1>hello</h1>
  <h2>{greet === "world" && <h3>nice to meet you!!</h3>}</h2>
</>
```

- `0` 은 예외로, 화면에 출력됨

```jsx
function App() {
  const num = 0;
  return (
    <>
      <h2>{num && <h3>nice to meet you!!</h3>}</h2>
    </>
  );
}
// 0
```

#### 스타일링

- 카멜 표기법으로 작성
  - ex) `background-color`가 아닌 `backgroundColor`

#### className

- `class` 대신 `className` 사용

<br>

## JSX In Depth

Fundamentally, JSX just provides syntactic sugar for the `React.createElement(component, props, ...children)` function. The JSX code:

```js
<MyButton color="blue" shadowSize={2}>
  Click Me
</MyButton>;

// compiles into:

React.createElement(MyButton, { color: "blue", shadowSize: 2 }, "Click Me");
```

## Spread Attributes

- 아래 두 컴포넌트는 동일

```js
function App1() {
  return <Greeting firstName="Ben" lastName="Hector" />;
}

function App2() {
  const props = { firstName: "Ben", lastName: "Hector" };
  return <Greeting {...props} />;
}
```
