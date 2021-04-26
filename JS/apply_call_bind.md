### 📌Contents

- [call 메서드](#call)
- [apply 메서드](#apply)
- [bind 메서드](#bind)
- [화살표 함수의 예외](#arrow)

---

<br>

## 명시적으로 this를 바인딩하기

- `apply(), call()`메서드로 `this`에 별도의 대상을 바인딩할 수 있다.
- 모든 함수의 부모 객체인 `Function.prototype` 객체의 메서드 이므로 모든함수가 사용가능

<br>

### <a name="call"></a>call 메서드

```js
Function.prototype.call(thisArg[, arg1[, arg2[, ...]]])
```

`call`메서드는 메서드의 호출 주체인 함수를 즉시 실행한다. `call`메서드의 첫번째 인자를 `this`로 바인딩하고, 이후 인자들을 호출할 함수의 매개변수로 한다. 함수를 그냥 실행하면 `this`는 전역객체를 참조하지만 `call`메서드를 이용하면 임의의 객체를 `this`로 지정할 수 있다.

```js
var func = function (a, b, c) {
  console.log(this, a, b, c);
};

func(1, 2, 3); //Window {...} 1 2 3
func.call({ x: 1 }, 4, 5, 6); //{x: 1} 4 5 6
```

<br>

메서드에 대해서도 마찬가지로 임의의 객체를 `this`로 지정할 수 있다.

```js
var obj = {
  a: 1,
  method: function (x, y) {
    console.log(this.a, x, y);
  },
};

obj.method(2, 3); // 1 2 3
obj.method.call({ a: 4 }, 5, 6); // 4 5 6
```

<br>

### <a name="apply"></a>apply 메서드

```js
Function.prototype.apply(thisArg[, argsArray])
```

- 결국 `본질적인 기능은 함수 호출`이다.

`apply`메서드는 `call`메서드와 기능적으로 완전히 동일하다. 그러나 `call`메서드는 첫번째 인자를 제외한 나머지 인자들을 호출할 매개변수로 지정하고, `apply`메서드는 두번째 인자를 **배열**로 받아 그 배열의 요소들을 호출할 함수의 매개변수로 지정한다는 차이가 있다.

```js
var func = function (a, b, c) {
  console.log(this, a, b, c);
};
func.apply({ x: 1 }, [4, 5, 6]); // {x: 1} 4 5 6
```

```js
var obj = {
  a: 1,
  method: function (x, y) {
    console.log(this.a, x, y);
  },
};
obj.method.apply({ a: 4 }, [5, 6]); // 4 5 6
```

<br>

### <a name="bind"></a>bind 메서드

```js
Function.prototype.bind(thisArg[, arg1[, arg2[, ...]]])
```

`bind`는 `call`과 비슷하지만 넘겨 받은 `this` 및 인수들을 바탕으로 **새로운 함수를 반환**하는 메서드이다.

```js
name = "global context";

function hello() {
  console.log(this.name);
}

var obj = {
  name: "ingg",
};

hello(); //global context
hello.call(obj); //ingg
hello.apply(obj); //ingg
hello.bind(obj); //ƒ hello() { console.log(this.name); }

var test = hello.bind(obj);
test(); //ingg

hello.bind(obj)(); //ingg
```

`this` 값이나 인자와 함께 곧바로 함수를 호출하는 `call, apply`와 달리 `bind`는 메서드를 사용한 함수와 똑같은 생김새의 함수를 반환시킨 것을 볼 수 있다.

따라서 `bind` 메소드를 사용 후 다시 한번 호출을 해주어야 함수 속 `this`를 원하는 객체로 지정한 후 값을 얻을 수 있다.

<br>

```js
var func = function (a, b, c) {
  console.log(this, a, b, c);
};
func(1, 2, 3); //Window {...} 1, 2, 3

var bindFunc = func.bind({ x: 1 });
bindFunc(5, 6, 7); //{x: 1} 5 6 7

var bindFunc2 = func.bind({ x: 1 }, 3);
bindFunc2(4, 5); //{x: 1} 3 4 5
bindFunc2(8, 9); //{x: 1} 3 8 9
```

다시 새로운 함수를 호출할 때 인수를 넘기면 그 인수들은 기존 `bind`메서드를 호출할 때 전달했던 인수들의 뒤에 이어서 등록된다.

<br>

#### 상위 컨텍스트의 this를 내부함수나 콜백함수에 전달하기

메서드의 내부함수에서 메서드의 `this`를 그대로 바라보기 위해 **_self_** 등의 변수를 이용한 우회법 대신 `call, apply, bind`메서드를 이용하면 더 깔끔하게 처리할 수 있다.

```js
var obj = {
  outer: function () {
    console.log(this); //{outer: ƒ}
    var innerFunc = function () {
      console.log(this); //Window {...}
    };
    innerFunc();
  },
};
obj.outer();
```

- **_call_** 사용

```js
var obj = {
  outer: function () {
    console.log(this); //{outer: ƒ}
    var innerFunc = function () {
      console.log(this); //{outer: ƒ}
    };
    innerFunc.call(this);
  },
};
obj.outer();
```

- **_bind_** 사용

```js
var obj = {
  outer: function () {
    console.log(this); //{outer: ƒ}
    var innerFunc = function () {
      console.log(this); //{outer: ƒ}
    }.bind(this);
    innerFunc();
  },
};
obj.outer();
```

<br>

### <a name="arrow"></a>화살표 함수의 예외사항

ES6 화살표 함수는 실행 컨텍스트 생성시 `this`를 바인딩하는 과정이 제외되었다. 따라서 이 함수 내부에는 `this`가 없고, 접근하려면 스코프체인상 가장 가까운 `this`에 접근한다.

```js
const obj = {
  outer: function () {
    console.log(this); //{outer: ƒ}
    const innerFunc = () => {
      console.log(this); //{outer: ƒ}
    };
    innerFunc();
  },
};
obj.outer();
```

위의 예시에서 내부함수 부분을 화살표 함수로 바꿨다. 이렇게하면 별도의 변수로 `this`를 우회하거나, _call/apply/bind_ 를 적용할 필요가없어 간결하다.

<br>

## call, apply, bind 예제

```js
// 📌 call 메서드
const singer = {
  name: "Taeyeon",
  fanCode: "TY",
  age: 32,
  fans: [],
  // fan: function() {} 와 같음
  fan(fanNum, fanName) {
    console.log(`${fanName}'s number is ${fanNum}`);
    this.fans.push({ who: `${this.fanCode}${fanNum}`, fanName });
  },
};

singer.fan(229, "John");
singer.fan(252, "Mary");
console.log(singer); // {name: "Taeyeon", fanCode: "TY", age: 32, fans: Array(2), fan: ƒ}

const dancer = {
  name: "Jinah",
  fanCode: "JN",
  age: 29,
  fans: [],
};

const fan = singer.fan;
fan(99, "Zero"); // Uncaught TypeError: Cannot read property 'fans' of undefined
// 더이상 메서드가 아니고 함수로 호출했으므로 오류발생

fan.call(singer, 99, "Zero"); // Zero's number is 99
fan.call(dancer, 777, "Nero"); // 다른객체로 bind도 가능

// 📌 apply 메서드 : 배열 형태로 넣기
const applyFan = [888, "Kyo"];
fan.apply(dancer, applyFan);
fan.call(dander, ...applyFan); // (이렇게해도 동일)

// 📌 bind 메서드 : 곧바로 함수를 호출하지 않음. 새로운 함수리턴
const fanDancer = fan.bind(dancer);
fanDancer(999, "INGG");

// 인자를 미리 넣기가 가능
const fanSinger = fan.bind(singer, 11);
fanSinger("Anna");
fanSinger("Bona");
```

<br>

#### ▶︎ bind 메서드 : 이벤트리스너에서

```html
<html>
  <head>
    <title>test</title>
  </head>
  <body>
    <button class="buy">Buy new ticket</button>
    <script src="index.js"></script>
  </body>
</html>
```

```js
const singer = {
  name: "Taeyeon",
  fanCode: "TY",
  age: 32,
  fans: [],
  // fan: function() {} 와 같음
  fan(fanNum, fanName) {
    console.log(`${fanName}'s number is ${fanNum}`);
    this.fans.push({ who: `${this.fanCode}${fanNum}`, fanName });
  },
};

singer.tickets = 300;
singer.buyTicket = function () {
  console.log(this); // <button class="buy">Buy new ticket</button>

  this.tickets++;
  console.log(this.tickets); // NaN
};

document.querySelector(".buy").addEventListener("click", singer.buyTicket);

// NaN인 이유: singer.buyTicket 이 핸들러 함수가  document.querySelector(".buy") 이 요소에 묶인다.
// 그래서 this가 button element 를 가르킨다.

// 따라서 singer.buyTicket가 singer 객체를 가리키게 해야한다.
// bind를 이용해서 변경 해보면
document
  .querySelector(".buy")
  .addEventListener("click", singer.buyTicket.bind(singer));
// 이제 singer 객체가 this가 됐으므로, 버튼을 클릭하면 정상적으로 1씩 증가한다.
```

<Br>

#### ▶︎ bind 메서드 : Partial application (preset parameters)

```js
const addTax = (rate, value) => value + value * rate;
console.log(addTax(0.1, 200)); // 220
const addVAT = addTax.bind(null, 0.25); // (null은 인자를 쓰지않을때)
console.log(addVAT(100)); // 125

// 위의 bind를 쓰지않고 함수로 똑같이 만들면
const addTaxRate = function (rate) {
  return function (value) {
    return value + value * rate;
  };
};
const addVAT2 = addTaxRate(0.25);
console.log(addVAT2(100)); // 125
```

<br>

## 정리

- 명시적 _this_ 바인딩이 없는 한 성립하는 규칙
  - 전역공간에서 _this_ 는 전역객체를 참조
  - 어떤 함수를 메서드로서 호출하면 _this_ 는 메서드 호출 주체(메서드명 앞의 객체)를 참조
  - 어떤 함수를 함수로서 호출하면 _this_ 는 전역객체를 참조. 메서드의 내부함수에서도 같음
  - 콜백함수 내부에서의 _this_ 는 콜백함수의 제어권을 넘겨받은 함수가 정의한 바에 따름. 정의하지 않은경우 전역객체를 참조
  - 생성자 함수에서의 _this_ 는 생성될 인스턴스를 참조

* 명시적 _this_ 바인딩
  - _call_, _apply_ 메서드는 _this_ 를 명시적으로 지정하면서 함수나 메서드를 호출함
  - _bind_ 메서드는 _this_ 및 함수에 넘길 인수를 일부 지정해서 새로운 함수를 생성
