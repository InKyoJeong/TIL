## 함수형 컴포넌트

- 공식 문서에서는 함수형 컴포넌트와 Hooks를 사용권장

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
