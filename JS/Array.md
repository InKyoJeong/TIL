## 배열 메서드

### Array.prototype.push()

> push() 메서드는 배열의 끝에 하나 이상의 요소를 추가하고, **배열의 새로운 길이**를 반환한다.

```js
const name = ["a", "b", "c"];
const whatisPush = name.push("d");

console.log(name); // (4) ["a", "b", "c", "d"]
console.log(whatisPush); // 4
```

### Array.prototype.pop()

> pop() 메서드는 배열에서 마지막 요소를 제거하고 그 **요소**를 반환한다.

```js
const color = ["black", "white"];
const whatIsPop = color.pop();

console.log(color); // ["black"]
console.log(whatIsPop); // white
```

### Array.prototype.shift()

> shift() 메서드는 배열에서 **첫 번째 요소를 제거**하고, **제거된 요소**를 반환한다. 이 메서드는 배열의 길이를 변하게 한다.

```js
const number = ["1", "2", "3"];
const whatisShift = number.shift();

console.log(number); //["2", "3"]
console.log(whatisShift); // 1
```

### Array.prototype.forEach()

인수로받은 함수를 배열의 요소별로 한번씩 실행한다. **각각의 아이템에 대해서 어떠한 시행만 하는 것**을 의미한다. 새로운 배열을 `return`하는 `map`과 `filter`와 다르다. user에 저장, 로컬스토리지에 저장, API로 보낸다던가 경고를 보낸다던가 할 수 있다.

```js
let posts = ["Hi", "Hello", "Bye"];

posts.forEach((post) => console.log(post));

// Hi
// Hello
// Bye
```

### Array.prototype.map()

> array의 각 item에 function을 적용하고 array를 반환한다.

```js
const friends = ["AAA", "BBB", "CCC", "DDD"];

friends;
// ["AAA","BBB","CCC","DDD"]

friends.map((current) => {
  return current + "Test"; //["AAATest", "BBBTest", "CCCTest", "DDDTest"]
});

// friends.map(current => current + "Test"); 와 같다.
```

### Array.prototype.filter()

> filter() 메서드는 주어진 함수의 테스트를 통과하는 모든 요소를 모아 새로운 배열로 반환한다.

```js
const words = ["spray", "limit", "elite", "exuberant", "destruction"];

const result = words.filter((word) => word.length > 6);

console.log(result); // expected output: Array ["exuberant", "destruction"]
```

### Array.prototype.concat()

> concat 메서드는 인자로 주어진 배열이나 값들을 기존 배열에 합쳐서 새 배열을 반환한다.

```js
const x = ["A", "B", "C"];
const y = ["D", "E"];

const z = x.concat(y);

console.log(z); // (5) ["A", "B", "C", "D", "E"]
```

### Array.prototype.join()

> 배열의 모든 요소값을 문자열로 바꾼후에 인수로 받은 문자로 연결해서 반환한다.

```js
const x = ["AA", "BB", "CC"];
x.join("-"); // "AA-BB-CC"
```

### Array.prototype.reduce()

- acc (accmulator) 는 콜백의 반환값을 누적
  - initialValue를 제공한 경우에는 initialValue의 값
- cur (currentValue) 처리할 현재 요소.

```js
const array = [2, 3, 4, 5];

const balance = array.reduce(function (acc, cur, i, arr) {
  console.log(`Iteration ${i}: ${acc}`);
  return acc + cur;
}, 0);

// Iteration 0: 0
// Iteration 1: 2
// Iteration 2: 5
// Iteration 3: 9

console.log(balance); // 14
```

```js
// Maximum value
const movements = [200, 450, -400, 3000, -600, -100, 70, 1300];
const max = movements.reduce((acc, mov) => {
  if (acc > mov) {
    return acc;
  } else {
    return mov;
  }
}, movements[0]);
console.log(max);
```

<br>

```js
arr.reduce(callback[, initialValue])
```

- `callback` : 4가지 인수를 받는다.
  - `accumulator` : 반복될때마다 축적되는 값
  - `currentValue` : 처리할 현재 요소. accumulator와 currentValue 더해진 값이 다시 accumulator 들어가는 반복문이라고 보면 편함
  - `currentIndex` : 처리할 현재 요소의 인덱스. initialValue를 제공한 경우 0, 아니면 1부터 시작
  - `array` : reduce()를 호출한 배열.
- `initialValue` : callback의 최초 호출에서 첫 번째 인수에 제공하는 값. 초기값을 제공하지 않으면 배열의 첫 번째 요소를 사용함

```js
const array1 = [1, 2, 3, 4];
const reducer = (accumulator, currentValue) => accumulator + currentValue;

// 1 + 2 + 3 + 4
console.log(array1.reduce(reducer));
// expected output: 10

// 5 + 1 + 2 + 3 + 4
console.log(array1.reduce(reducer, 5));
// expected output: 15
```

<br>

#### 객체 내의 값 인스턴스 개수 세기

```js
let genres = ["classic", "pop", "classic", "classic", "pop"];

let countGenres = genres.reduce((all, v) => {
  if (v in all) {
    all[v]++;
  } else {
    all[v] = 1;
  }
  return all;
}, {});

console.log(countGenres); // {classic: 3, pop: 2}
```

<br>

### Array.prototype.find()

> find() 메서드는 주어진 판별 함수를 만족하는 **첫 번째 요소의 값을 반환**한다. 그런 요소가 없다면 undefined를 반환한다.

```js
const array = [1, 3, 5, 7, 9];
const found = array.find((e) => e > 5);

console.log(found);
// 7
```

### Array.prototype.findIndex()

> findIndex() 메서드는 주어진 판별 함수를 만족하는 배열의 첫 번째 요소에 대한 **인덱스를 반환**한다. 만족하는 요소가 없으면 -1을 반환한다.

```js
const array = [5, 6, 11, 44, 66];
const found = array.findIndex((e) => e > 9);

console.log(found);
// 2
```

### Array.prototype.splice()

> splice() 메서드는 배열의 기존 요소를 삭제 또는 교체하거나 새 요소를 추가하여 배열의 내용을 변경한다.

```js
array.splice(start[, deleteCount[, item1[, item2[, ...]]]])
```

- `start` : 배열의 변경을 시작할 인덱스. 음수인 경우 배열의 끝에서부터 요소를 센다.
- `deleteCount` : 배열에서 제거할 요소의 수. `0`이하이면 제거하지않는다.
- `item` : 배열에 추가할 요소. 지정하지 않으면 splice()는 요소를 제거하기만 한다.

```js
const words = ["apple", "book", "movie"];
words.splice(1, 0, "add"); //1번 인덱스에서 제거하지않고 "add"추가
console.log(words);
// ["apple", "add", "book", "movie"]

const words2 = ["apple", "book", "movie"];
words2.splice(2, 1); //2번 인덱스에서 1개 제거
console.log(words2);
// ["apple", "book"]
```

### Array.prototype.indexOf()

> indexOf() 메서드는 배열에서 지정된 요소를 찾을 수 있는 첫 번째 인덱스를 반환하고 존재하지 않으면 -1을 반환한다.

```js
arr.indexOf(searchElement[, fromIndex])
```

```js
const item = ["apple", "ms", "samsung"];
console.log(item.indexOf("ms")); //1
```

- 두번째 매개변수를 추가하면 **검색을 시작할 색인**

### Array.prototype.sort()

```js
arr.sort([compareFunction]);
```

- `compareFunction` : 정렬 순서를 결정하는데 사용되는 함수. 이를 생략하면 유니코드 순으로 정렬된다.

  - `compareFunction(a, b)`이 **0보다 작은 경우** a를 b보다 낮은 색인으로 정렬한다. 즉, a가 먼저온다.
  - `compareFunction(a, b)`이 **0보다 큰 경우** b를 a보다 낮은 인덱스로 소트한다.

- 반환 값 : 정렬한 배열. 복사본이 만들어지는게 아니라, **원래 배열이 정렬되는 것**이다.

```js
// 숫자 비교 예시 (오름차순)
const a = [5, 2, 6, 8, 9, 1, 3];
a.sort((a, b) => a - b); //[1, 2, 3, 5, 6, 8, 9]
```

- 문자는 a-b 와같이 할수 없기때문에 부등호로 비교하여 1 or -1을 리턴하는 식으로 사용

```js
// 문자 비교 예시
const items = [
  { name: "Taeyeon", age: 11 },
  { name: "Mary", age: 33 },
  { name: "John", age: 22 },
];
items.sort((a, b) => (a.name > b.name ? 1 : -1));
// {name: "John", age: 22}
// {name: "Mary", age: 33}
// {name: "Taeyeon", age: 11}
```

### Array.prototype.includes()

> 배열이 특정 요소를 포함하고 있는지 판별

```js
const array = ["AA", "BB", "CC"];

console.log(array.includes("BB")); //true
```
