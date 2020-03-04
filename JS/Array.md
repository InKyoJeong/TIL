### Array.push()

> push() 메서드는 배열의 끝에 하나 이상의 요소를 추가하고, **배열의 새로운 길이**를 반환한다.

```js
const name = ["a", "b", "c"];
const whatisPush = name.push("d");

console.log(name); // (4) ["a", "b", "c", "d"]
console.log(whatisPush); // 4
```

### Array.pop()

> pop() 메서드는 배열에서 마지막 요소를 제거하고 그 **요소**를 반환한다.

```js
const color = ["black", "white"];
const whatIsPop = color.pop();

console.log(color); // ["black"]
console.log(whatIsPop); // white
```

### Array.shift()

> shift() 메서드는 배열에서 첫 번째 요소를 제거하고, **제거된 요소**를 반환한다. 이 메서드는 배열의 길이를 변하게 한다.

```js
const number = ["1", "2", "3"];
const whatisShift = number.shift();

console.log(number); //["2", "3"]
console.log(whatisShift); // 1
```

### Array.forEach()

인수로받은 함수를 배열의 요소별로 한번씩 실행한다. **각각의 아이템에 대해서 어떠한 시행만 하는 것**을 의미한다. 새로운 배열을 `return`하는 `map`과 `filter`와 다르다. user에 저장, 로컬스토리지에 저장, API로 보낸다던가 경고를 보낸다던가 할 수 있다.

```js
let posts = ["Hi", "Hello", "Bye"];

posts.forEach(post => console.log(post));

// Hi
// Hello
// Bye
```

### Array.map()

> array의 각 item에 function을 적용하고 array를 반환한다.

```js
const friends = ["AAA", "BBB", "CCC", "DDD"];

friends;
// ["AAA","BBB","CCC","DDD"]

friends.map(current => {
  return current + "Test"; //["AAATest", "BBBTest", "CCCTest", "DDDTest"]
});

// friends.map(current => current + "Test"); 와 같다.
```

<!-- #### Array.filter() -->
