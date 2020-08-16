## 데이터 배열을 컴포넌트 배열로

- `map`을 이용한 반복

```js
// Iteration.js
import React from "react";

const Iteration = () => {
  const names = ["AA", "BB", "CC", "DD"];
  const nameList = names.map((name) => <li>{name}</li>);
  return <ul>{nameList}</ul>;
};

export default Iteration;
```

```js
// App.js
import React, { Component } from "react";
import Iteration from "./Iteration";

class App extends Component {
  render() {
    return (
      <div>
        <Iteration />
      </div>
    );
  }
}

export default App;
```

![iter](./images/iteration.png)

<br>

### key

- 리액트에서 `key`는 컴포넌트 배열을 렌더링했을때 어떤 원소에 변동이 있는지 알아내려고 사용함
- `key`가 있다면 어떤 변화가 일어났는지 빠르게 알아냄
- `map`함수 인자로 전달되는 함수 내부에서 `props`처럼 설정하면 됨
- `key`값을 유일해야함
- 고유한 값이 없을때만 `index` 값을 `key`로 사용해야함

```js
//...
const nameList = names.map((name, index) => <li key={index}>{name}</li>);
```

<br>

## 데이터 추가하기

```js
import React, { useState } from "react";

const Iteration = () => {
  const [names, setNames] = useState([
    { id: 1, text: "사과" },
    { id: 2, text: "딸기" },
    { id: 3, text: "포도" },
  ]);
  const [inputText, setInputText] = useState("");
  const [nextId, setNextId] = useState(4);

  const onChange = (e) => setInputText(e.target.value);
  const onClick = () => {
    const nextNames = names.concat({
      id: nextId,
      text: inputText,
    });
    setNextId(nextId + 1);
    setNames(nextNames);
    setInputText("");
  };

  const nameLists = names.map((name) => <li key={name.id}>{name.text}</li>);
  return (
    <>
      <input value={inputText} onChange={onChange} />
      <button onClick={onClick}>추가하기</button>
      <ul>{nameLists}</ul>
    </>
  );
};

export default Iteration;
```

- 배열에 추가할때 `push`대신 `concat`을 사용
  - `push`는 기존 배열 자체를 변경, `concat`은 새로운 배열생성
  - 리액트에서 상태 업데이트시에는 기존 상태를 그대로 두고 새로운 값을 상태로 설정해야함 (불변성 유지)
  - 불변성 유지해야 컴포넌트의 성능 최적화

<br>

## 데이터 제거하기

- 불변성 유지하며 배열의 항목을 지울때는 `filter` 사용

```js
const numbers = [1, 2, 3, 4, 5];
const upThree = numbers.filter((num) => num > 3);

console.log(upThree);
// [4, 5]
```

- 이벤트 `onDoubleClick`을 이용하여 더블클릭하면 제거

```js
import React, { useState } from "react";

const Iteration = () => {
  const [names, setNames] = useState([
    { id: 1, text: "사과" },
    { id: 2, text: "딸기" },
    { id: 3, text: "포도" },
  ]);
  const [inputText, setInputText] = useState("");
  const [nextId, setNextId] = useState(4);

  const onChange = (e) => setInputText(e.target.value);
  const onClick = () => {
    const nextNames = names.concat({
      id: nextId,
      text: inputText,
    });
    setNextId(nextId + 1);
    setNames(nextNames);
    setInputText("");
  };
  const onRemove = (id) => {
    const nextNames = names.filter((name) => name.id !== id);
    setNames(nextNames);
  };

  const nameLists = names.map((name) => (
    <li key={name.id} onDoubleClick={() => onRemove(name.id)}>
      {name.text}
    </li>
  ));

  return (
    <>
      <input value={inputText} onChange={onChange} />
      <button onClick={onClick}>추가하기</button>
      <ul>{nameLists}</ul>
    </>
  );
};

export default Iteration;
```
