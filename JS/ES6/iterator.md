## 이터레이션

- 반복 처리. 데이터 안의 요소를 연속적으로 꺼내는 행위

## 이터레이터

- **반복 처리(iteration)** 가 가능한 객체
- `Symbol.iterator` 메서드를 가진 객체를 반복 가능(이터러블, iterable)한 객체라고 한다.
- 이터레이터 객체는 `next` 메서드를 가진다.
- `forEach` 메서드의 경우 배열요소를 꺼내 그 값을 함수 인수로 넘기고 다음요소를 꺼내 넘기고를 반복하는데, 개발자가 각 처리 단계를 제어할 수 없다. `이터레이터`는 개발자가 반복 처리를 단계별로 제어할 수 있다.

이터레이터는 일반적으로 두 가지 항목을 만족하는 객체이다.

1. `next`메서드를 가진다.
2. `next`메서드의 반환값은 `value`프로퍼티와 `done`프로퍼티를 가진 객체인데, `value`에는 꺼낸 값이 저장되고 `done`에는 반복이 끝났는지 뜻하는 논리값이 저장된다.

```js
// 배열의 이터레이터 예시
const a = [5, 6, 7];
const iter = a[Symbol.iterator]();
console.log(iter.next()); // {value: 5, done: false}
console.log(iter.next()); // {value: 6, done: false}
console.log(iter.next()); // {value: 7, done: false}
console.log(iter.next()); // {value: undefined, done: true}
```

iter의 `next`메서드를 호출할때마다, `value`와 `done`프로퍼티를 갖는 **이터레이터 리절트(result)** 라는 객체가 반환된다.

<br>

## 반복 가능 객체와 for/of

- `for/of`문을 사용하면 이터레이터의 반복 처리를 간결하게 표현할 수 있다.

```js
// 배열 요소를 이터레이터를 사용해서 목록으로 바꾸는 예시
const a = [5, 6, 7];
const iter = a[Symbol.iterator]();
while (true) {
  const iteratorResult = iter.next();
  if (iteratorResult.done == true) break;
  const v = iteratorResult.value;
  console.log(v);
}
//5
//6
//7
```

```js
// for/of문을 사용한 예시
const a = [5, 6, 7];
for (const v of a) console.log(v);
//5
//6
//7
```

`for/of` 는 두가지 조건을 만족하는 객체를 반복처리 한다.

1. `Symbol.iterator` 메서드를 가지고 있다.
2. `Symbol.iterator` 메서드는 반환값으로 이터레이터를 반환한다.

다음 생성자로 생성한 내장 객체는 `Symbol.iterator` 메서드를 내장하고 있다.

```
Array, String, TypedArray, Map, Set
```

```js
//String 예시
for (const v of "ABC") console.log(v);
//A
//B
//C
```
