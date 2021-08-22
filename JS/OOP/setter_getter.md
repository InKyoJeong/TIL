## 접근자 프로퍼티

- 데이터 프로퍼티 : 지금까지 사용한 모든 프로퍼티. 값을 저장하기 위한 프로퍼티
- 접근자 프로퍼티 : 값이 없음. 프로퍼티를 읽거나 쓸때 호출하는 함수를 값 대신 지정할 수 있는 프로퍼티

#### 접근자란?

- 접근자 : 객체지향 프로그래밍에서 객체가 가진 프로퍼티 값을 **객체 바깥에서 읽거나 쓸 수 있도록 제공하는 메서드**

<!-- - 접근자 프로퍼티는 부적절한 데이터 변경 막고, 외부에서 데이터를 숨기거나, 외부에서 읽으려고 할때 적절한 값으로 가공해서 넘길 수 있음
  - 객체 프로퍼티를 객체 바깥에서 직접 조작하는 것은 유지 보수성을 해치는 원인
  - 접근자 프로퍼티를 사용해 프로퍼티를 읽고 쓸 수 있게하면 유지 보수성을 높일 수 있음 -->

## getter와 setter

접근자 프로퍼티는 객체 리터럴 안에서 getter와 setter는 `get`과 `set`으로 나타낼 수 있음

```js
let obj = {
  get propName() {
    // getter // obj.propName을 실행할때 실행되는 코드
  },

  set propName(value) {
    // setter // obj.propName = value를 실행할때 실행되는 코드
  },
};
```

`getter` 메서드는 `obj.propName`으로 프로퍼티를 읽으려고 할 때 실행되고

`setter` 메서드는 `obj.propName = value` 으로 프로퍼티에 값을 할당하려 할 때 실행됨

#### 예시

```js
let user = {
  lastName: "Kim",
  firstName: "Taeyeon",

  get fullName() {
    return `${this.lastName} ${this.firstName}`;
  },
};

console.log(user.fullName); // Kim Taeyeon
```

일반 프로퍼티에서 값에 접근하는 것처럼 user.fullName 으로 프로퍼티 값을 얻음

<br>

<!-- ```js
let user = {
  get fullName() {
    return `FULL NAME!!!`;
  },
};

console.log(user.fullName = "FULL NAME");
```
`getter` 메서드만 있어서, `user.fullName=`으로 값을 할당하려고 하면 에러 발생 -->

```js
let user = {
  lastName: "Kim",
  firstName: "Taeyeon",

  get fullName() {
    return `${this.lastName} ${this.firstName}`;
  },

  set fullName(value) {
    [this.lastName, this.firstName] = value.split(" ");
  },
};

user.fullName = "Baek Yerin";
console.log(user.fullName); // Baek Yerin
```

이렇게 getter와 setter 메서드를 구현하면 객체엔 `fullName`이라는 읽고 쓸 순 있지만 실제로는 존재하지 않는 가상의 프로퍼티가 생김

<br>

## class에서 setter와 getter

- setter와 getter는 **_data validation_** 에 유용하다.

```js
class PersonCl {
  constructor(fullName, birthYear) {
    this.fullName = fullName;
    this.birthYear = birthYear;
  }

  calcAge() {
    console.log(2021 - this.birthYear);
  }

  get age() {
    return 2021 - this.birthYear;
  }

  set fullName(name) {
    if (name.includes(" ")) {
      this._fullName = name; // 이름 충돌이 발생하므로 _fullName으로 변경
    } else {
      alert(`${name} is not a full name.`);
    }
  }
}

const nancy = new PersonCl("Nancy McDonie", 1991);
console.log(nancy);
// PersonCl {_fullName: "Nancy McDonie", birthYear: 1991}
// 		birthYear: 1991
// 		_fullName: "Nancy McDonie"
// 		age: (...)
// 		[[Prototype]]: Object
```

이제 더이상 nancy.fullName이 존재하지않아서 접근할수없다.

```js
console.log(nancy.fullName); // undefined
```

<br>

- 이걸 고치기위해 getter를 생성

```js
class PersonCl {
  constructor(fullName, birthYear) {
    this.fullName = fullName;
    this.birthYear = birthYear;
  }

  calcAge() {
    console.log(2021 - this.birthYear);
  }

  get age() {
    return 2021 - this.birthYear;
  }

  // Set a property that already exist
  set fullName(name) {
    if (name.includes(" ")) {
      this._fullName = name;
    } else {
      alert(`${name} is not a full name.`);
    }
  }

  get fullName() {
    return this._fullName;
  }
}
const nancy = new PersonCl("Nancy McDonie", 1991);

console.log(nancy.fullName); // "Nancy McDonie"
console.log(nancy);
// PersonCl {_fullName: "Nancy McDonie", birthYear: 1991}
//	 birthYear: 1991
//	 _fullName: "Nancy McDonie"
// 	age: 30
// 	fullName: "Nancy McDonie"
// 	[[Prototype]]: Object
```

<br>

- 유효하지않은 객체를 만든경우

```js
const will = new PersonCl("Will", 1963);
// alert발생 ('Will is not a full name.')
console.log(will); // PersonCl {birthYear: 1963}
```
