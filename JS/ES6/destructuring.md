## 비구조화 할당 (Destructuring)

> 비구조화 할당은 배열, 객체, 반복 가능 객체에서 값을 꺼내 그 값을 별도의 변수에 대입하는 문장이다. 객체와 배열로부터 속성이나 요소를 쉽게 꺼낼 수 있다.

```js
var candyMachine = {
  status: {
    name: "jelly",
    count: 4,
  },
  getCandy: function () {
    this.status.count--;
    return this.status.count;
  },
};

var getCandy = candyMachine.getCandy;
var count = candyMachine.status.count;

// count
// 4
// getCandy
// ƒ () {
//     this.status.count--;
//     return this.status.count;
//   }
```

**객체 속성을 같은 이름의 변수에 대입하는 코드**이다. 아래와 같이 바꿀 수 있다.

```js
const candyMachine = {
  status: {
    name: "jelly",
    count: 4,
  },
  getCandy() {
    this.status.count--;
    return this.status.count;
  },
};

const {
  getCandy,
  status: { count },
} = candyMachine;

// count
// 4
// getCandy
// ƒ getCandy() {
//     this.status.count--;
//     return this.status.count;
//   }
```

candyMachine객체 안의 속성을 찾아 변수와 매칭한다. count처럼 여러 단계 안의 속성도 찾을 수 있다.

<br>

### 배열도 비구조화 할 수 있다.

- 예시

```js
const array = [77, 88];
const first = array[0];
const two = array[1];
```

위 코드를 비구조화 할당을 이용해 변경하면 다음과 같다.

```js
const array = [77, 88];
const [first, two] = array;
```

<br>

- 예시2

```js
var array = ["nodejs", {}, 10, true];
var first = array[0];
var second = array[1];
var last = array[3];
```

**_array_** 라는 배열에 첫번째, 두번째, 마지막 요소를 변수에 대입하는 과정이다. 아래와 같이 바꿀 수 있다.

```js
const array = ["nodejs", {}, 10, true];
const [first, second, , last] = array;
```
