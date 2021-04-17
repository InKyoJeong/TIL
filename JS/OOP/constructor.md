## 생성자와 new

> 객체지향 프로그래밍을 간단히 말하면 서로 연관된 변수와 서로연관된 메소드를 하나의 객체라는 그릇에 넣는것이다. 서로 연관되지않은 것들은 별도의 객체에 분리시키는 것이다. (연관된것들을 그룹핑한다)

`객체`란 서로 연관된 변수와 함수를 그룹핑한 그릇이라고 할 수 있다. 객체 내의 변수를 `프로퍼티(property)`, 함수를 `메소드(method)`라고 부른다.

```js
const person1 = {
  name: "John",
  introduce: function() {
    return "My name is " + this.name;
  }
};
const person2 = {
  name: "Mary",
  introduce: function() {
    return "My name is " + this.name;
  }
};
```

객체를 여러개 만든다고 하면 `introduce`라는 메소드를 정의하는 부분이 중복 되고 있다. 이런 메소드의 동작 방법을 바꾼다고 하면 그 객체들이 가지고 있는 메소드 전체를 찾아서 똑같이 바꿔야하는 이슈가 생긴다( = 중복이 생긴다). 따라서 객체의 구조를 재활용할 수 있는 방법이 필요하다. 이 중복을 해결하기 위한 것이 `생성자, new`이다.

### 생성자

> 생성자(constructor)는 객체를 만드는 역할을 하는 함수이다. 자바스크립트에서 함수는 재사용 가능한 로직의 묶음이 아니라 객체를 만드는 창조자라고 할 수 있다.

```js
function Person() {}
const p = new Person();

p; // Person{}
```

함수에 `new`를 붙이면 그 리턴값은 객체가 된다.

```js
function Person(name) {
  this.name = name;
  this.introduce = function() {
    return "My name is " + this.name;
  };
}
const p1 = new Person("John");

console.log(p1); // -> Person {name: "John", introduce: ƒ}
```

생성자 내에서 이 객체의 프로퍼티를 정의하고 있다. 이렇게 생성자는 객체를 생성하고 **초기화**하는 역할을 한다. 생성자 함수는 일반함수와 구분하기 위해 첫글자를 대문자로 표시한다.

#### constructor 사용의 장점

```js
function Person(name, first, second) {
  this.name = name;
  this.first = first;
  this.second = second;
  this.sum = function() {
    return this.first + this.second;
  };
}

const kim = new Person("kim", 10, 20);
const lee = new Person("lee", 30, 40);
console.log(kim.sum()); //30
console.log(lee.sum()); //70
```

이전에는 객체를 만들때마다 객체를 다시 정의해야하는데 생성자 함수를 만들면 앞에 `new`를 사용하므로써 실행할때마다 객체가 양산된다. 또한 생성자 함수의 내용을 바꾸면 이 생성자 함수에 의해 만들어진 모든 객체가 한번에 바뀐다.

## Prototype

> 프로토타입을 이용해서 성능을 향상시키고 메모리를 절약할 수 있다.

위에서 생성자 `Person`의 메소드로 추가했던 코드를 바꾸어보자.

```js
function Person(name, first, second) {
  this.name = name;
  this.first = first;
  this.second = second;
}

//객체들 모두가 공통적으로 사용하는 속성을 만든다.
Person.prototype.sum = function() {
  return "prototype " + (this.first + this.second);
};

const kim = new Person("kim", 10, 20);
const lee = new Person("lee", 30, 40);
console.log(kim.sum()); //prototype 30
console.log(lee.sum()); //prototype 70
```

`kim` 이라는 변수가 가르키는 객체의 `sum`메소드 만큼은 다르게 동작하게 하고싶다면

```js
function Person(name, first, second) {
  this.name = name;
  this.first = first;
  this.second = second;
}

Person.prototype.sum = function() {
  return "prototype " + (this.first + this.second);
};

const kim = new Person("kim", 10, 20);
kim.sum = function() {
  return "this " + (this.first + this.second);
};

const lee = new Person("lee", 30, 40);
console.log(kim.sum()); //this 30
console.log(lee.sum()); //prototype 70
```

자바스크립트는 `kim`이라는 객체의 `sum`이라는 메소드를 표출할때 객체 자신이 `sum`이라는 속성을 가지고 있는지를 찾는다. 그 속성은 `kim.sum = function(){...}`함수이므로 이걸 실행시키고 거기서 끝난다. 그러나 `lee`라는 객체는 `sum`이라는 메소드를 정의한 적이 없기 때문에 이 객체의 생성자인 `Person`의 `prototype`의 `sum`이라는 메소드가 정의되어있는지를 찾고 그걸 실행한다.
