## 전개 연산자 (Spread Operator)

`...`은 **전개 연산자(spread operator)** 라고 한다. 반복가능한 객체를 반환하는 표현식 앞에 표기하며, 반복 가능한 객체를 배열 리터럴 또는 함수의 인수 목록으로 펼칠 수 있다.

```js
console.log([..."ABC"]); // (3) ["A", "B", "C"]
console.log([1, ...[2, 3, 4], 5]); //(5) [1, 2, 3, 4, 5]
```

예를들어 day1와 day2라는 배열이 있고 이 배열을 더한다고 하자.

```js
const day1 = ["Mon", "Tues", "Wed"];
const day2 = ["Thu", "Fri", "Sat"];

const allDays = day1 + day2;

console.log(allDays); //Mon,Tues,WedThu,Fri,Sat
```

모든게 `string`으로 바뀌었다. 따라서 더이상 배열이 아니게 된다. `+` 연산자가 숫자가 아니면 _WedThu_ 처럼 문자로 바꿔서 붙여버린다. 이번엔 아래와 같이 배열로 만들면 오직 하나의 item을 가진 배열이 된다.

```js
let allDays = [day1 + day2];

console.log(allDays); // ["Mon,Tues,WedThu,Fri,Sat"]
```

배열 전체가아니라 해당배열의 item들을 가지기 위해 이렇게 하면 두개의 배열을 만들 수 있다.

```js
const day1 = ["Mon", "Tues", "Wed"];
const day2 = ["Thu", "Fri", "Sat"];

const allDays = [day1, day2];

console.log(allDays); // ▶(2) [Array(3), Array(3)]
```

**_Spread Operator_** 는 배열로부터 아이템을 가져와서 `Unpack`한다. 따라서 배열을 없애고 콘텐츠만 얻으려면 다음과 같이 한다.

```js
const day1 = ["Mon", "Tues", "Wed"];
const day2 = ["Thu", "Fri", "Sat"];

const allDays = [...day1, ...day2];

console.log(allDays); //["Mon", "Tues", "Wed", "Thu", "Fri", "Sat"]
```

이러면 두배열의 콘텐츠를 한 배열에 가지게 된다. 이게바로 **_Spread Operator_** 이다.

#### push 메서드

배열 두 개를 연결할 때는 보통 `Array.prototype.concat`메서드를 사용하지만 전개 연산자를 활용하면 `Array.prototype.push`메서드로도 배열을 연결할 수 있다.

```js
const x = ["A", "B", "C"];
x.push(...["D", "E"]); //5

console.log(x); //(5) ["A", "B", "C", "D", "E"]
```

#### Math.max

배열 안의 최댓값을 `Math.max`로 구할 수 있다.

```js
const a = [5, 2, 6, 7, 8];

Math.max(a); //NaN
Math.max(...a); //8
```

#### Object에서도 작동한다.

```js
const a = {
  first: "name",
  second: "age"
};

const b = {
  thrid: "address"
};

const two = { a, b };

console.log(two); // ▶ {a: {…}, b: {…}}
```

이렇게 하면 **두개의 Object가 있는 하나의 Object**를 얻게된다. 따라서, 두개의 object를 합치는 _two_ 객체를 만들고 싶다면 **_Spread Operator_** 를 사용한다.

```js
const a = {
  first: "name",
  second: "age"
};

const b = {
  thrid: "address"
};

const two = { ...a, ...b };

console.log(two); // ▶ {first: "name", second: "age", thrid: "address"}
```

두개의 Object의 콘텐츠를 가지게 되었다.

#### 마찬가지로 Function에서도 작동한다.

```js
const info = (something, args) => console.log(...args);
```

이렇게 하면 누군가 제공한 *Argument*를 `console.log`할 수 있다.

> 전개 연산자는 React프로젝트에서 자주 사용한다. 두개의 Object를 병합하거나, 어떤 대상의 복사본을 만들거나, 어떤 한 콘텐츠를 다른 배열에 넣는 등의 상황에 사용한다.
