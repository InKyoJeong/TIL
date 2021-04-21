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
