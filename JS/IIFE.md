## IIFE란?

즉시 실행 함수 표현(IIFE, Immediately Invoked Function Expression)은 정의되자마자 즉시 실행되는 Javascript Function 를 말한다.

```java
(function() {
  statements
})()
```

<br>

IIFE 내부에서 정의된 변수는 외부 범위에서 접근이 불가능하다.

```js
(function() {
  var aName = "Mary";
})();

aName; // Uncaught ReferenceError: aName is not defined
```

<br>

IIFE를 변수에 할당하면 IIFE 자체는 저장되지 않고, 함수가 실행된 결과만 저장된다.

```js
var result = (function() {
  var name = "Mary";
  return name;
})();
// 즉시 결과를 생성
result; // "Mary"
```
