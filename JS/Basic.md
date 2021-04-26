## Variable

변수를 만들때는 기본적으로 이렇게 작동한다.

```
Create : 먼저 변수를 생성하고
Initialize : 다음으로 이걸 초기화하고
Use : 사용한다
```

필요에 따라 생성과 초기화를 동시에 할 수 있다.

```js
let a = 221;
let b = a - 5;
a = 4;
console.log(b, a); // 216 , 4
```

`const` (= constant)는 `상수` = stable (변하지 않는다)

```js
const a = 22;
a = 4;
console.log(b, a); // TypeError: Assignment to constant variable.
```

`const`는 변수를 바꿀 수 없다. 변수를 선언할 때는 기본적으로 `const`를 사용한다.

<br>

## comment (주석)

```js
// 한줄 처리
/* 
여러줄 처리
여러줄 처리
*/
```

## string

```js
const what = "Github";

console.log(what); //Github
```

만약 숫자를 넣어도 이건 텍스트다.

```js
const what = "1234567";
```

### Boolean : True or False

```js
const what = true;
```

true/false는 텍스트가 아니다. 소문자로 쓰고, `""` 없이 사용한다. 이진법에서 `true`는 `1`, `false`는 `0`이다.

### Float : 소숫점이 있는것

```js
const what = 55.1;
```

> Camel case: js에서는 변수명을 소문자로 시작해서 변수명 중간에는 스페이스 대신 대문자로 쓴다. ex) daysOfWeek

<br>

## for/in

`for/in`문은 객체 안의 프로퍼티를 순회하는 반복문이다.

```js
for (변수 in 객체 표현식) {...}
```

```js
const obj = { a: 1, b: 2, c: 3 };
for (const p in obj) {
  console.log(p);
}
// a
// b
// c
```

`for/in`문은 프로퍼티 이름만 꺼내서 변수에 할당한다. 따라서 반복문 안에서 프로퍼티 값을 가져오려면 괄호 연산자를 사용해야한다.

- 예시

```js
const obj = { a: 1, b: 2, c: 3 };

for (const p in obj) {
  console.log(`${p}: ${obj[p]}`);
}

// expected output:
// "a: 1"
// "b: 2"
// "c: 3"
```

<br>

## Array

```js
const monday = "Mon";
const tue = "Tue";
const wed = "Wed";
const thu = "Thu";
const fri = "Fri";

console.log(monday, tue, wed, thu, fri);
//이건 효과적이지 않다. 하나로 묶을 수 있다.
```

Array는 string을 하나로 묶는다.

```js
const daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", true];

console.log(daysOfWeek);
// ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', true];
```

Array는 0부터 시작하기때문에 3번째 요일을 알고싶다고 하면 2로 입력한다.

```js
console.log(daysOfWeek[2]); // Wed
```

<br>

## Object

Array와 Object의 다른점은 Object에는 각 `value`에 이름을 줄 수 있다는 것이다.

```js
const info = {
  name: "Nico",
  age: 33,
  gender: "Male",
  isHandsome: true,
};

console.log(info); // {name: "Nico", age: 33, gender: "Male", isHandsome: true}
```

gender에만 접근하려면 데이터의 이름만 사용한다.

```js
console.log(info.gender); //Male
```

객체안의 값은 바꿀 수도있다.

```js
const info = {
  name: "Nico",
  age: 33,
  gender: "Male",
  isHandsome: true,
};

console.log(info.gender); //Male

info.gender = "Female";

console.log(info.gender); //Female
```

데이터를 정렬하는데는 두가지 방법이 있는데 하나는 Array, 다른하나는 Object이다.
만약 DB에서 가져온 리스트 데이터라면 Array를 선택하고, 만약 데이터를 합쳐서 만들어야 한다면 Object를 선택한다.

Array와 Object는 서로를 안에 넣을 수도 있다.

```js
const info = {
  name: "Nico",
  age: 33,
  gender: "Male",
  isHandsome: true,
  favMovies: ["Inception", "Notebook"],
  favFood: [
    {
      name: "Kimchi",
      fatty: false,
    },
    {
      name: "Burger",
      fatty: true,
    },
  ],
};

console.log(info.favFood[0].fatty); //false
```

### console.log vs info.favFood

`console`은 info가 object인 것처럼 object다.
`console`이라는 object가 있고 `log`라는 키가 있다.

만약 console object를 `console.log`로 찍어보면?

```js
console.log(console);
// debug: ƒ debug()
// error: ƒ error()
// info: ƒ info()
// log: ƒ log()
// warn: ƒ warn()
// dir: ƒ dir()
// dirxml: ƒ dirxml()
// table: ƒ table()
// trace: ƒ trace()
// group: ƒ group()
// groupCollapsed: ƒ groupCollapsed()
// groupEnd: ƒ groupEnd()
// clear: ƒ clear()
// count: ƒ count()
// (...)
```

이런것들을 `내장함수(built-in function)`라고 한다.

<br>

## Function

```js
function sayHello() {
  console.log("Hello");
}

sayHello(); // Hello
```

함수는 `argument`를 받는다. argument는 변수같은 것이다. 함수는 인수를 여러개 받을 수 있다.

```js
function sayHello(apple) {
  console.log("Hello", apple);
}

sayHello("Nico"); // Hello Nico
```

- 자바스크립트에서는 `""`도 string이고 `''`도 string이다

### 백틱활용

```js
function sayHello(name, age) {
  console.log(`Hello ${name} you are ${age} years old`);
}

sayHello("Nico", 25); // Hello Nico you are 25 years old
```

### return (x) vs console.log

```js
function sayHello(name, age) {
  console.log(`Hello ${name} you are ${age} years old`);
}

const greetNico = sayHello("Nico", 12);

console.log(greetNico);

// Hello Nico you are 12 years old
// undefined
```

greetNico가 `정의되지않은(undefined)`게 아니려면 뭔가를 반환해보자.

```js
function sayHello(name, age) {
  return `Hello ${name} you are ${age} years old`;
}

const greetNico = sayHello("Nico", 12);

console.log(greetNico);

// Hello Nico you are 12 years old
```

sayHello함수는 어떤 값을 반환하지만 `console.log`로 찍어주진않기 때문에 여기선 하나의 console.log를 갖게 된다.

#### 계산 연습

```js
const calculator = {
  plus: function (a, b) {
    return a + b;
  },
};

const plusNumber = calculator.plus(5, 5);
console.log(plusNumber); // 10
```

<br>

## strict 모드

> 스크립트의 시작 혹은 함수의 시작 부분에 "use strict"(또는 'use strict')를 선언

#### 실수를 에러로 변환

- hasDriver에서 s를 빼고 콘솔에 출력한 결과

```js
"use strict";

let hasDriversLicense = false;
const passTest = true;

if (passTest) {
  hasDriverLicense = true;
}

if (hasDriversLicense) {
  console.log("I can drive!");
}
// Uncaught ReferenceError: hasDriverLicense is not defined
```

<br>

#### 예약된 키워드 등을 변수로 사용불가

```js
"use strict";

const interface = "dd";
// script.js:19 Uncaught SyntaxError: Unexpected strict mode reserved word
```
