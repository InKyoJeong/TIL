## 옵셔널 체이닝 (optional chaining)

- 옵셔널 체이닝 `?.`을 사용하면 프로퍼티가 없는 중첩 객체를 에러 없이 안전하게 접근할 수 있다.
- 만약 참초가 `null`이나 `undefined`라면 에러가 발생하는 대신 `undefined`를 리턴한다.

<br>

### 옵셔널 체이닝 필요한 이유

- 중첩된 객체에서 옵셔널 체이닝 없이 하위 속성을 찾으려면 아래처럼 해야한다.
  - first는 second에 접근하기 전에 `null` 또는 `undefined` 가 아니라는 것을 검증하여 에러를 방지한다.

```js
let nested = obj.first && obj.first.second;
```

- 옵셔널 체이닝을 사용하면 아래와 같이 간결해진다.

```js
let nested = obj.first?.second;
```

<br>

### 예시

```js
const user = {
  name: "Taeyeon",
  cat: {
    name: "Zero",
  },
};

console.log(user.dog.name);
// Uncaught TypeError: Cannot read property 'name' of undefined
console.log(user.dog?.name);
// undefined
```

<br>

### 요약

옵셔널 체이닝 문법 `?.`은 세 가지 형태로 사용할 수 있다.

1. `obj?.prop` – obj가 존재하면 `obj.prop`을 반환하고, 그렇지 않으면 `undefined`를 반환함
2. `obj?.[prop]` – obj가 존재하면 `obj[prop]`을 반환하고, 그렇지 않으면 `undefined`를 반환함
3. `obj?.method()` – obj가 존재하면 `obj.method()`를 호출하고, 그렇지 않으면 `undefined`를 반환함

- `?.`를 계속 연결해서 체인을 만들면 중첩 프로퍼티들에 안전하게 접근할 수 있음
- `?.`은 `?.`왼쪽 평가대상이 없어도 괜찮은 경우에만 선택적으로 사용해야 함
