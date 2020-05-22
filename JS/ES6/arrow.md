## 화살표 함수 (Arrow Functions)

ES6문법인 화살표함수를 이용하면 `function`키워드를 사용해서 함수를 만드는 것보다 간단히 함수를 표현할 수 있다.

```js
function sayHello(name) {
  return "Hello " + name;
}
const mary = sayHello("Mary");
console.log(mary); // Hello Mary
```

이를 화살표 함수 표현식으로 작성하면 다음과 같다.

```js
const sayHello = name => "Hello " + name; // 중괄호를 하지않는다면 return한다는 것이 함축되어있다.
const mary = sayHello("Mary");
console.log(mary); // Hello Mary
```

<br>

이렇게 default값을 넣을 수도 있다.

```js
function sayHello(name = "John") {
  return "Hello " + name;
}
const human = sayHello();
console.log(human); // Hello John
```

- Arrow Function

```js
const sayHello = (name = "John") => "Hello " + name;
const human = sayHello();
console.log(human); // Hello John
```

<br>

### 함수 리터럴과 화살표 함수의 차이점

화살표 함수 표현은 함수 리터럴(익명 함수)의 단축 표현이다. 그러나 두가지 표현이 완전히 같은 것은 아니다. 몇가지 차이점이 있다.

#### 1. this의 값이 함수를 정의할 때 결정된다

함수 리터럴로 정의한 함수의 `this`값은 함수를 **호출**할 때 결정된다. 그러나 화살표 함수의 `this`는 함수를 **정의**할 때 결정된다. 즉, 화살표 함수 바깥의 `this`값이 화살표 함수의 `this`값이 된다.

```js
const obj = {
  test: function() {
    console.log(this); //{test: ƒ}
    const f1 = function() {
      console.log(this); // Window {parent: Window, opener: null, top: Window, length: 0, frames: Window, …}
    };
    f1();
    const f2 = () => console.log(this); //{test: ƒ}
    f2();
  }
};
obj.test();
```

함수 `f1`은 test라는 함수의 중첩함수고 `this`의 값은 `전역객체`를 가리킨다. 반면 화살표함수 `f2`의 `this`값은 함수 `f2`를 정의한 익명함수의 `this`값인 객체 `obj`를 가리킨다.

화살표함수는 `call`이나 `apply`메서드를 사용해서 `this`를 바꿔 호출해도 `this`값이 바뀌지않는다.

```js
const mary = { name: "Mary" };
const f1 = function() {
  console.log(this.name);
};
const f2 = () => console.log(this.name);

f1.call(mary); //"Mary"
f2.call(mary); //""
```

#### 2. arguments 변수가 없다

화살표 함수 안에는 `arguments` 변수가 정의되어 있지 않으므로 사용할 수 없다.

```js
const f1 = () => console.log(arguments);
f1(); //Uncaught ReferenceError: arguments is not defined
```

#### 3. 생성자로 사용할 수 없다

화살표 함수 앞에 `new`연산자를 붙여 호출할 수 없다.

```js
const Person = (name, age) => {
  this.name = name;
  this.age = age;
};
const mary = new Person("Mary", 25); //Uncaught TypeError: Person is not a constructor
```

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
}
const mary = new Person("Mary", 25);

console.log(mary); //Person {name: "Mary", age: 25}
```

<!-- #### 4. yield 키워드를 사용할 수 없다.  -->
