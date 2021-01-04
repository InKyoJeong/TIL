## 제네레이터

- 함수를 작성할 때 함수를 특정 구간에 멈춰 놓을 수 있고, 원할때 다시 돌아가게 할 수 있음
- 제네레이터는 `function*` 문으로 정의한 함수이고, 하나이상의 `yield`표현식을 포함

```js
function* gen() {
  yield 1;
  yield 2;
  yield 3;
}

const g = gen();
console.log(g.next()); // {value: 1, done: false}
console.log(g.next()); // {value: 2, done: false}
console.log(g.next()); // {value: 3, done: false}
console.log(g.next()); // {value: undefined, done: true}
```

- `yield`는 프로그램이 일시적으로 정지하는 위치
- `next`메서드는 제네레이터 함수의 상태를 정지상태에서 실행상태로 바꿈

```js
function* gen(i) {
  yield i;
  yield i + 10;
  return 22;
}

const g = gen(5);

g.next(); //{value: 5, done: false}
g.next(); //{value: 15, done: false}
g.next(); //{value: 22, done: true}
g.next(); //{value: undefined, done: true}
```

<br>

> redux-saga는 제너레이터 문법을 기반으로 비동기 작업을 관리해줌 <br>
> 즉, saga는 우리가 디스패치하는 액션을 모니터링해서 그에따라 필요한 작업을 따로 수행할 수 있는 미들웨어
