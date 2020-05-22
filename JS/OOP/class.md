## 클래스(Class)

> 클래스구문을 사용하면 다양한 생성자 정의문과 생성자 상속 방법을 통일된 문법으로 표현할 수 있다.

```js
class Person {}

const kim = new Person();
console.log(kim); // Person{}
```

`Person`이라는 객체가 생성된 것을 볼 수 있다. 클래스는 객체를 만드는 공장이다.

### class constructor

```js
class Person {
  constructor(name, first, second) {
    this.name = name;
    this.first = first;
    this.second = second;
  }
}

const kim = new Person("kim", 10, 20);

console.log(kim); // Person { name: 'kim', first: 10, second: 20 }
```

객체가 생성될때 자동으로 생성되기전에 실행되도록 약속된 함수인 `constructor`를 `class`내에서 구현했다.

### class에서 객체의 method 구현

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
const lee = new Person("lee", 30, 40);
console.log(kim.sum()); //prototype 30
```

기존방식에서 `constructor`함수의 `prototype`이라는 객체에 `sum`이라는 프로퍼티를 함수로 지정해서<br>`Person`이라는 `constructor`를 통해 만들어진 모든 객체가 공유하는 함수를 만들 수 있었다.

```js
class Person {
  constructor(name, first, second) {
    this.name = name;
    this.first = first;
    this.second = second;
  }
}

Person.prototype.sum = function() {
  return "prototype " + (this.first + this.second);
};

const kim = new Person("kim", 10, 20);
console.log(kim.sum()); //prototype 30
```

그대로 복사해도 클래스에서도 잘 동작한다.

```js
class Person {
  constructor(name, first, second) {
    this.name = name;
    this.first = first;
    this.second = second;
  }
  sum() {
    return "prototype " + (this.first + this.second);
  }
}

const kim = new Person("kim", 10, 20);
console.log(kim.sum()); //prototype 30
```

다음으로, `class`안에 넣어도 의미가 같기 때문에 똑같이 동작한다. 즉 `sum`이라는 메소드는 같은 클래스에 속해있는 모든 객체가 공유하는 함수가 된다.<br>
`kim`이라는 객체만큼은 다르게 동작하는 함수를 정의할 수도 있다.

```js
class Person {
  constructor(name, first, second) {
    this.name = name;
    this.first = first;
    this.second = second;
  }
  sum() {
    return "prototype " + (this.first + this.second);
  }
}

const kim = new Person("kim", 10, 20);
kim.sum = function() {
  return "this " + (this.first + this.second);
};
const lee = new Person("lee", 30, 40);

console.log(kim.sum()); //this 30
console.log(lee.sum()); //prototype 70
```

이제 `kim`은 같은 클래스에 속해있는 다른 객체들과는 다른 메소드를 가지고있는 상태가 된다.

## Class 상속(Inheritance)

```js
class Person {
  constructor(name, first, second) {
    this.name = name;
    this.first = first;
    this.second = second;
  }
  sum() {
    return this.first + this.second;
  }
  // avg(){
  // 	return (this.first+this.second)/2;
  // }
}
```

예를들어, sum외에도 평균을 구하고 싶다고 하자. `class`내에서 `avg(){...}`를 추가할 수도 있지만 그것이 불가능한 경우(다른사람의 코드, 가져다쓰는 라이브러리 등의 경우)가 있을 수 있다. 코드를 수정하지 않고 클래스를 하나 더 만들어보자.

```js
class PersonPlus {
  constructor(name, first, second) {
    this.name = name;
    this.first = first;
  }
  sum() {
    return this.first + this.second;
  }
  avg() {
    return (this.first + this.second) / 2;
  }
}

const kim = new PersonPlus("kim", 10, 20);
```

기존의 `Person`과 코드중복이 생긴다. 이를 해결하기 위해 상속을 이용한다. 중복되는 부분을 지운다.<br>

`extends` 키워드는 `Person`이라는 클래스를 확장하고 요소들을 그대로 상속받을 수 있게 한다.

```js
class PersonPlus extends Person {
  avg() {
    return (this.first + this.second) / 2;
  }
}

const kim = new PersonPlus("kim", 10, 20);

console.log(kim.sum()); // 30
console.log(kim.avg()); // 15
```

## super

`PersonPlus`클래스에서 `Person`을 수정하지 않고 10 20 외에 30 이라는 세번째 값을 갖고싶다면 `super`를 사용할 수 있다.

```js
class Person {
  constructor(name, first, second) {
    this.name = name;
    this.first = first;
    this.second = second;
  }
  sum() {
    return this.first + this.second;
  }
}
class PersonPlus extends Person {
  constructor(name, first, second, third) {
    super(name, first, second);
    this.third = third;
  }
  sum() {
    return super.sum() + this.third;
  }
  avg() {
    return (this.first + this.second + this.third) / 3;
  }
}

const kim = new PersonPlus("kim", 10, 20, 30);

console.log(kim.sum()); // 60
console.log(kim.avg()); // 20
```

`super()`는 부모클래스의 constructor(생성자)이다. 따라서 `super(name,first, second)`를 전달하게 되면 `PersonPlus`의 부모 클래스(`Person`)의 생성자가 호출이 되고 그 안에서 프로퍼티들이 셋팅되기 때문에 자식은 `this.third = third;`만 추가하면 된다.<br>

`super.sum()`이라고하면 부모클래스의 `sum(){...}`이 호출되고 그 결과가 리턴되어 `super.sum()+this.third`와 같이 중복을 없앨수 있다.
<br>

## 객체 간의 상속

### `__proto__`를 이용한 상속 구현

객체의 `__proto__` 프로퍼티는 그 객체에게 상속을 해 준 부모 객체를 가르킨다. 따라서 객체는 `__proto__`가 가리키는 부모 객체의 프로퍼티를 사용할 수 있다.

```js
const objA = {
  attrA: "aaa"
};

const objB = {
  attrB: "bbb"
};
```

`objA`와 `obB`라는 객체가 있다고 하자. 지금은 `objB`가 `objA`의 `attrA`속성에 접근할 수 없지만 `objB`객체에서도 `objA`의 `attrA`를 소유한 것처럼 사용하려면 `프로토타입 체인(__proto__)`을 사용한다.

```js
const objA = {
  attrA: "aaa"
};

const objB = {
  attrB: "bbb"
};

objB.__proto__ = objA;

console.log(objB.attrA); // aaa
```

자신이 갖고있지 않은 프로퍼티를 `__proto__` 프로퍼티가 가리키는 객체를 차례대로 거슬러 올라가며 검색한다. 이렇게 객체와 객체의 연결을 통한 단방향 공유 관계를 프로토타입 체인이라고 한다.

### Object.create를 이용해서 `__proto__`를 대체

실제로 프로그래밍을 할때는 직접적으로 `__proto__`에 접근하여 상속하지는 않기 때문에 다른 방법으로 상속한다.

```js
const objA = {
  attrA: "aaa"
};

const objB = Object.create(objA);

console.log(objB.attrA); // aaa
```

`__proto__`를 사용하는 것보다는 이렇게 `Object.create`를 사용해서 객체와 객체간의 상속 관계 프로토링크를 지정해주는 것이 더 좋은 방법이라고 할 수 있다.
<br>

## 객체와 함수

### call 메서드

> call을 통해 실행할 때마다 this의 값을 변경할 수 있다.

아래 예제에서 현재 `sum`은 어떤 객체에도 속해있지 않다. `sum.call()`은 `sum`이라는 객체를 실행시킨다. 역할은 `sum();`과 같다.

```js
const kim = { name: "kim", first: 10, second: 20 };
const lee = { name: "lee", first: 30, second: 40 };

function sum() {
  return this.first + this.second;
}

sum.call(kim);
```

사실 모든함수는 `call`이라는 메소드를 가지고있다. 자바스크립트에서는 함수도 일종의 객체이기 때문이다.<br>

`call`이라는 함수의 메소드를 호출할 때 첫번째 인자로 `kim`을 주면 `sum`함수에서 내부적으로 `this`는 `kim`이된다. 따라서 `this.first`는 `kim.first`이고 `10`, `second`도 마찬가지로 `20`이 된다.

```js
console.log(sum.call(kim)); // 30
```

`sum`이라는 함수는 `kim`이라는 객체의 멤버가 아니였지만, `call`이라는 특이한 함수를 호출할때 첫번째 인자로 `sum`이 내부적으로 사용할 `this`의 값을 `kim`으로 지정했더니 `sum`이라는 함수가 `kim`의 멤버인 메소드가 된 것이다.

```js
console.log(sum.call(lee)); // 70
```

마찬가지로 `lee`를 인자로 주면 `sum`안에서 `this`는 이제 `lee`이다. 따라서 결과는 `70`이다.

call은 첫번째 인자로는 그함수의 내부적으로 this를 무엇으로 할 것인가, 두번째 인자는 호출할 함수의 파라미터에 들어갈 인자값들이 들어간다.

```js
const kim = { name: "kim", first: 10, second: 20 };
const lee = { name: "lee", first: 30, second: 40 };

function sum(prefix) {
  return prefix + (this.first + this.second);
}

console.log(sum.call(kim, "Number ")); //Number 30
```

### apply 메서드

`apply`는 `call`과 본질적으로는 같은 동작을 한다. 차이점은 함수에 인수를 넘기는 방법이다. `apply`의 인수는 **배열**이고 `call`의 인수는 **쉼표**로 구분한 값의 목록이다.

```js
const lee = { name: "lee", first: 30, second: 40 };

function say(a, b) {
  return a + b + (this.first + this.second);
}
console.log(say.apply(lee, ["Value ", "is.."])); //Value is..70
```

`apply`는 `call`과 마찬가지로 **첫 번째 인수**는 함수의 **this값**이고, **두 번째 인수**는 함수의 인수를 순서대로 담은 **배열**이다.

### bind 메서드

> bind는 객체에 함수를 바인드한다(=묶는다).

```js
const kim = { name: "kim", first: 10, second: 20 };

function sum(a, b) {
  return a + b + (this.first + this.second);
}

const sumKim = sum.bind(kim);

console.log(sumKim("Value ", "is..")); // Value is..30
```

이렇게 `sum.bind(kim)`은 `kim`객체를 함수 `sum`의 `this`로 설정한 **새로운 함수를 만들어서 반환**한다.
