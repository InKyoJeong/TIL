## 불변성

기존의 값을 직접 수정하지 않으면서 새로운 값을 만들어 내는것을 **불변성을 지킨다**라고 함

<br>

- 배열 예시

```js
const array = [1, 2, 3, 4];
const badArray = array; // 배열을 복사하는것이 아니라 똑같은 배열을 가리킴

badArray[0] = 999;
console.log(array === badArray); //true
```

```js
const array = [1, 2, 3, 4];
const goodArray = [...array]; // 배열 내부의 값을 모두 복사

goodArray[0] = 777;
console.log(array === goodArray); //false
```

<br>

- 객체 예시

```js
const obj = {
  name: "zero",
  value: 22,
};

const badObj = obj; // 객체가 복사되지 않고, 똑같은 객체를 가리킴
badObj.value = badObj.value + 1;
console.log(obj === badObj); //true
```

`badObj`랑 `obj`는 둘다 `{name: "zero", value: 23}`가 됨

<br>

```js
const obj = {
  name: "zero",
  value: 22,
};

const goodObj = {
  ...obj,
  value: obj.value + 1,
};
console.log(obj === goodObj); //false
```

`obj`는 그대로 `{name: "zero", value: 22}` 이고 `goodObj`는 `{name: "zero", value: 23}`

<br>

### 얕은 복사

- **전개 연산자**를 사용해서 객체나 배열 내부 값을 복사할때는 **얕은 복사**가 됨
  - 내부 값이 완전히 새로 복사되는 것이 아닌, **가장 바깥쪽에 있는 값만 복사됨**
  - 즉, 내부 값이 객체나 배열이면 내부 값도 따로 복사해야함

```js
const todos = [
  { id: 1, checked: true },
  { id: 2, checked: true },
];
const nextTodos = [...todos];

nextTodos[0].checked = false;
console.log(todos[0] === nextTodos[0]); //true
```

- 여기서는 **아직 똑같은 객체를 가리키고 있어서** true임
  - **todos[0]** 와 **nextTodos[0]** 둘다 `{id: 1, checked: false}`

<br>

```js
const todos = [
  { id: 1, checked: true },
  { id: 2, checked: true },
];
const nextTodos = [...todos];

nextTodos[0] = {
  ...nextTodos[0],
  checked: false,
};
console.log(todos[0] === nextTodos[0]); //false
```

- 여기서는 새로운 객체를 할당해주어서 false
  - **todos[0]** 는 `{id: 1, checked: true}` 이지만 , **nextTodos[0]** 는 `{id: 1, checked: false}`

<br>

## immer

- 객체의 구조가 복잡해지면 불변성을 유지하면서 업데이트하기 어려워짐
- immer 라이브러리는 구조가 복잡한 객체도 쉽고 짧게 불변성을 유지하며 업데이트하게 해줌

```bash
$ npm i immer
또는 yarn add immer
```

<br>

### 사용 예시

- `produce`라는 함수는 **첫번째 파라미터로 수정하고 싶은 상태**, **두번째 파라미터로 상태를 어떻게 업데이트할지 정의하는 함수**를 받음
- 배열에 직접적인 변화를 일으키는 `push, splice`함수 사용해도됨

```js
import produce from "immer";

const initialState = [
  {
    id: 1,
    todo: "불변성 공부하기",
    checked: true,
  },
  {
    id: 2,
    todo: "immer 설치하기",
    checked: false,
  },
];

const nextState = produce(initialState, (draft) => {
  // id가 2인 항목의 checked를 true로 변경
  const todo = draft.find((t) => t.id === 2);
  todo.checked = true;

  // 배열에 새로운 데이터 추가
  draft.push({
    id: 3,
    todo: "실습해보기",
    checked: false,
  });

  // id가 1인 항목 제거
  draft.splice(
    draft.findIndex((t) => t.id === 1),
    1
  );
});
```
