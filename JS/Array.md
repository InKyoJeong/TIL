#### Array.push()

> push() 메서드는 배열의 끝에 하나 이상의 요소를 추가하고, **배열의 새로운 길이**를 반환한다.

```js
const name = ["a", "b", "c"];
const whatisPush = name.push("d");

console.log(name); // (4) ["a", "b", "c", "d"]
console.log(whatisPush); // 4
```

#### Array.pop()

> pop() 메서드는 배열에서 마지막 요소를 제거하고 그 **요소**를 반환한다.

```js
const color = ["black", "white"];
const whatIsPop = color.pop();

console.log(color); // ["black"]
console.log(whatIsPop); // white
```

#### Array.shift()

> shift() 메서드는 배열에서 첫 번째 요소를 제거하고, **제거된 요소**를 반환한다. 이 메서드는 배열의 길이를 변하게 한다.

```js
const number = ["1", "2", "3"];
const whatisShift = number.shift();

console.log(number); //["2", "3"]
console.log(whatisShift); // 1
```
