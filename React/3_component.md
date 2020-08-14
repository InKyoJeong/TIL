## 함수형 컴포넌트

- 공식 문서에서는 **함수형 컴포넌트와 Hooks**를 사용권장

```jsx
import React from "react";
import "./App.css";

function App() {
  const greet = "world";
  return (
    <>
      <h2 className="react">hello {greet}</h2>
    </>
  );
}
export default App;
```

- 장점: 클래스형 컴포넌트보다 선언이 편하며 메모리자원도 덜 사용한다.
- 단점: `state`와 라이프사이클 API 사용이 불가능 하다 => v16.8 이후 **Hooks** 도입으로 해결됨

<br>

## 클래스형 컴포넌트

```jsx
import React, { Component } from "react";

class App extends Component {
  render() {
    const greet = "world";
    return <div className="react">{greet}</div>;
  }
}

export default App;
```

- 클래스형 컴포넌트에는 `render`함수가 꼭 있어야 한다.

<br>

## 모듈 export/import

- **_export_**

```js
// NewComponent.js
export default NewComponent;
```

- **_import_**

```js
// App.js
import React from "react";
import NewComponent from "./NewComponent";

const App = () => {
  return <NewComponent />;
};

export default App;
```

<br>

## props

- `props`는 컴포넌트 속성을 설정할때 사용하는 요소
- 해당 컴포넌트를 불러와서 사용하는 부모컴포넌트에서 설정함

```js
// NewComponent.js
import React from "react";

const NewComponent = (props) => {
  return <div>my new component is {props.name}</div>;
};

export default NewComponent;
```

```js
// App.js
import React from "react";
import NewComponent from "./NewComponent";

const App = () => {
  return <NewComponent name="React!!" />;
};

export default App;
//실행결과 : my new component is React!!
```

<br>

### defaultProps

- `props`의 **기본값**을 설정할 수 있음

```js
// NewComponent.js
import React from "react";

const NewComponent = (props) => {
  return <div>my new component is {props.name}</div>;
};

NewComponent.defaultProps = {
  name: "디폴트",
};
export default NewComponent;
```

```js
// App.js
//...
const App = () => {
  return <NewComponent />;
};
//실행결과 : my new component is 디폴트
```

<br>

### children

- `props.children`은 컴포넌트 태그 사이의 내용을 보여줌

```js
// NewComponent.js
const NewComponent = (props) => {
  return (
    <div>
      my new component is {props.name} <br />
      children is {props.children}
    </div>
  );
};

NewComponent.defaultProps = {
  name: "디폴트",
};
export default NewComponent;
```

```js
//App.js
//...
const App = () => {
  return <NewComponent>태그사이</NewComponent>;
};
//실행결과
//my new component is 디폴트
//children is 태그사이
```
