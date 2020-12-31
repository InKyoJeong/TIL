## This

1. 전역공간에서 : window(브라우저) / global(노드js)

2. 함수 호출시 : window / global

- **함수는 전역객체의 메소드다!** 라고 보면 편함

3. 메서드 호출시 : 메소드 호출 주체 (메소드명 앞)

```js
var a = {
  b: function () {
    console.log(this);
  },
};
a.b(); //{b: ƒ}
// 점(.)앞의 a가 this
```

```js
var a = {
  b: {
    c: function () {
      console.log(this);
    },
  },
};
a.b.c(); //{c: ƒ}
// 점(.)앞의 a.b가 this
```

<br>

```js
var a = 10;
var obj = {
  a: 20,
  b: function () {
    console.log(this.a); // 20 (this=obj이므로)

    function c() {
      console.log(this.a); //10 (함수로 호출해서)
    }
    c();
  },
};
obj.b();
```

- 위의 코드를 내부함수에서 우회하려면
  - `this`를 다른 변수에 담아서 내부에서 쓴다

```js
var a = 10;
var obj = {
  a: 20,
  b: function () {
    var self = this;
    console.log(this.a); //20

    function c() {
      console.log(self.a); //20
    }
    c();
  },
};
obj.b();
```

- ES6의 화살표함수 나오기전에 이 방법말고 없었음
- ES5에서 bind가 나왔지만 이게 더 많이쓰였음

<br>

4. callback 호출시 : 기본적으로는 함수내부와 동일

- 콜백을 받아서 어떻게 처리하느냐에 따라 다름
  - 제어권을 가진 함수가 `callback`의 `this`를 명시한 경우 그에따름
  - 개발자가 `this`를 바인딩해서 `callback`을 넘기면 그에 따름
- 참고: `call, apply` 는 즉시호출, `bind`는 새로운 함수 생성 (currying)

```js
var callback = function () {
  console.dir(this); //Window
};
var obj = {
  a: 1,
};
setTimeout(callback, 100);
```

- `this`에대한 처리를 `setTimeout`은 별도로하지않아서 전역객체가 나옴

```js
var callback = function () {
  console.dir(this); //Object a:1
};
var obj = {
  a: 1,
};
setTimeout(callback.bind(obj), 100);
```

- `bind`로 바꿀 수 있다.
  - `callback` 함수가 실행될때 `this`는 `obj`로 한다는 의미

<br>

5. 생성자함수 호출시 : 인스턴스

```js
function Person(n, a) {
  this.name = n;
  this.age = a;
}

var dankookie = new Person("단쿠키", 12);
console.log(dankookie); // Person {name: "단쿠키", age: 12}
```

- 새로 생성될 인스턴스 자체가 `this`가 됨
