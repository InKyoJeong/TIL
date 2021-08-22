## Static method

- `Array.from()`은 **_static method_** 를 이해할때 좋다
  - from()은 **_prototype property_** 내부에 할당되지 않고, Array 생성자 함수 객체에 직접 할당되어 있는 method이다.

```js
ƒ Array()
from: ƒ from()          //static methods
isArray: ƒ isArray()    //static methods
of: ƒ of()              //static methods
arguments: (...)    //static properties
length: 1           //static properties
name: "Array"       //static properties
caller: (...)
  prototype: Array(0)
	at: ƒ at()
	concat: ƒ concat()
	constructor: ƒ Array()
	copyWithin: ƒ copyWithin()
	entries: ƒ entries()
	every: ƒ every()
	fill: ƒ fill()
	filter: ƒ filter()
	find: ƒ find()
	findIndex: ƒ findIndex()
	//...생략
```

<br>

#### 예시

```js
class PersonCl {
  constructor(fullName, birthYear) {
    this.fullName = fullName;
    this.birthYear = birthYear;
  }

  // Instance method: .prototype property에 더해진다.
  calcAge() {
    console.log(2021 - this.birthYear);
  }

  // Static method
  static hey() {
    console.log("Hey there!");
  }
}
```

- _static method_ 는 **클래스가 인스턴스화되면 호출할 수 없다.**

```js
const nancy = new Person("Nancy", 2000);

nancy.calcAge(); // 21
nancy.hey(); // Uncaught TypeError: nancy.hey is not a function
```

<br>
