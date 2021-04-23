## 프로토타입이란

- 자바스크립트의 모든 객체는 자신의 부모 역할을 하는 객체와 연결되어 있다.
- 부모 객체를 **프로토타입 객체** (짧게 **프로토타입**) 이라고 한다.
- 자바스크립트의 모든 객체는 자신의 프로토타입을 가리키는 `[[Prototype]]` 라는 숨겨진 프로퍼티를 가진다.
  - 크롬에서는 `__proto__`가 `[Prototype]]` 이다.

```js
const test = {
  name: "aa",
  number: 123,
};
console.log(test.toString());
// [object Object]
console.dir(test);
// ▼Object
//   name: "aa"
//   number: 123
//   ▼__proto__: Object
//        ►constructor: ƒ Object()
//        ►hasOwnProperty: ƒ hasOwnProperty()
//        ►isPrototypeOf: ƒ isPrototypeOf()
//        ►propertyIsEnumerable: ƒ
//        ►propertyIsEnumerable()
//        ►toLocaleString: ƒ toLocaleString()
//        ►toString: ƒ toString()
```

`test.toString()` 이 오류나지 않는이유는 test 객체의 프로토타입에 `toString()` 메서드가 정의되어 있기 때문

<br>

## 프로토타입 체이닝

<hr>

```js
var obj = {
  name: "foo",
};

obj.hasOwnProperty("name"); // true
obj.hasOwnProperty("age"); // false
```

- 객체 리터럴로 생성한 객체함수 객체이므로 **prototype 프로퍼티**가 **Object.prototype 객체**를 자신의 프로토타입으로 연결함
- **프로토타입 체이닝** : 이렇게 특정 객체의 프로퍼티나 메서드에 접근할 때, 접근하려는 프로퍼티나 메서드가 없으면 `[[Prototype]]` 링크를 따라 부모 역할을 하는 프로토타입 객체의 프로퍼티를 차례대로 검색하는 것
